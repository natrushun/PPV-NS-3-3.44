/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2007 University of Washington
 *
 * This program is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License version 2 as
 * published by the Free Software Foundation;
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program; if not, write to the Free Software
 * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
 */

#include <arpa/inet.h>
#include <iostream>
#include <limits>
#include <math.h>
#include <utility>
#include <vector>
#include <stdexcept>
#include <algorithm>

#include <iostream>
#include <fstream>

#include "ipv4-header.h"
#include "ns3/log.h"
#include "ns3/ppp-header.h"
#include "ns3/string.h"
#include "ns3/ppov-utils.h"
#include "ppov-mts-rm-marker-queue.h"
#include "ns3/ppvlogger.h"
#include "ns3/ppov-rate-measurement.h"


namespace ns3 {
#define MAXPPV (1000000 * 4298662.34708228) // 10^6 * ppovgoldmax  by definition

NS_LOG_COMPONENT_DEFINE ("PpovMtsRmMarkerQueue");

NS_OBJECT_ENSURE_REGISTERED (PpovMtsRmMarkerQueue);

// TODO: when rewriting this for general TVFs all of the should be invertible
// i.e. the algorithm in the MTS-PPV paper only works for invertible TVFs
TypeId PpovMtsRmMarkerQueue::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PpovMtsRmMarkerQueue")
    .SetParent<Queue> ()
    .SetGroupName ("Network")
    .AddConstructor<PpovMtsRmMarkerQueue> ()
    .AddAttribute ("PpovPointsFile",		//maxTS
                   "Filename, that describes a ppov curve point-by-point.",
                   StringValue ("XX.txt"),
                   MakeStringAccessor (&PpovMtsRmMarkerQueue::PpovPointsFile),
                   MakeStringChecker ())
    .AddAttribute ("DClass",
                   "DClass marking",
                   UintegerValue (0),
                   MakeUintegerAccessor (&PpovMtsRmMarkerQueue::dclass),
                   MakeUintegerChecker<uint8_t> ())
    .AddAttribute ("bitRateAvg",
                   "bitRateAvg method id",
                   UintegerValue (1),
                   MakeUintegerAccessor (&PpovMtsRmMarkerQueue::bitRateAvg),
                   MakeUintegerChecker<uint8_t> ())
    .AddAttribute ("ts1",
                   "Timescale1 rate",
                   DoubleValue (0),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::ts1),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("ts2",
                   "Timescale2 rate",
                   DoubleValue (0),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::ts2),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("ts3",
                   "Timescale3 rate",
                   DoubleValue (0),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::ts3),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("ts4",
                   "Timescale4 rate",
                   DoubleValue (0),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::ts4),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("alpha1",
                   "alpha 1",
                   DoubleValue (1),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::alpha1),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("alpha2",
                   "alpha 2",
                   DoubleValue (1),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::alpha2),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("alpha3",
                   "alpha 3",
                   DoubleValue (1),
                   MakeDoubleAccessor (&PpovMtsRmMarkerQueue::alpha3),
                   MakeDoubleChecker<float> ())
    ;
  return tid;
}

PpovMtsRmMarkerQueue::PpovMtsRmMarkerQueue () :
  QueueDisc (QueueDiscSizePolicy::NO_LIMITS)//,
  //m_packets ()
{
  NS_LOG_FUNCTION (this);
  rnd = CreateObject<UniformRandomVariable> ();
  initialized = false;
  
  std::cout << "PpovMtsRmMarkerQueue::PpovMtsRmMarkerQueue ()\n";
  
}

RateMeasurementAbstract* PpovMtsRmMarkerQueue::getRateMeasurementObject(float ts, std::string name) {
	RateMeasurementAbstract* rm;
	if (bitRateAvg == 1) {
		rm = new RateMeasurementV1(ts, name); 
	} else if (bitRateAvg == 2) {
		rm = new RateFactorBurst(ts, 0.1, 0.0 ,name);		//ts, factor, burst, name
	} else if (bitRateAvg == 3) {
        rm = new TWMA(ts, 10, name);
    } else if (bitRateAvg == 4) {
		if (ts<1.0) {
			rm = new RateFactorBurst(ts, 0.1, 0.0 ,name);
		} else {
            rm = new TWMA(ts, 10, name);
		}
	} else if (bitRateAvg == 5) {
		if (ts<1.0) {
			rm = new PmarkerV4Rate(ts, 5*1500*8, 1000*8, name); //RateFactorBurst(ts, 0.1, 0.0 ,name);
		} else {
			rm = new TWMA(ts, 10, name);
		}
	} else if (bitRateAvg == 6) {
		if (ts<1.0) {
			rm = new RateFactorBurst(ts, 1, 5*1500*8 ,name);
		} else {
            rm = new TWMA(ts, 10, name);
		}
	} else {
		NS_FATAL_ERROR("\n\n--------->>>>>>>>>>>>>>>>> ERROR: Rossz a bitRateAvg parameter a mts-rm-marker-ben!!!! <<<<<<<<<<<<<<<<<<-------------\n\n");
		return 0;
	}
	return rm;
}


void PpovMtsRmMarkerQueue::setConfig () {
	
	std::vector<float> ts_array;
	ts_array.push_back(ts1);
	ts_array.push_back(ts2);
	ts_array.push_back(ts3);
	ts_array.push_back(ts4);
	//tmp alpha array
	std::vector<float> alpha_array;
	alpha_array.push_back(alpha1);
	alpha_array.push_back(alpha2);
	alpha_array.push_back(alpha3);
	alpha_array.push_back(1.0);
	
	for (int i=0; i<(int)ts_array.size();i++) {
		if (ts_array[i] >0) {
			std::stringstream sin;
			sin << ts_array[i];
			std::string val = sin.str();
			RateMeasurementAbstract* rm = getRateMeasurementObject(ts_array[i], "ts"+val);	//param: memory? 
			rateMeasurements.push_back(rm);
			alpha.push_back(alpha_array[i]);
		}
	}

	if(alpha[alpha.size()-1] != 1) {
		NS_FATAL_ERROR("\n\n--------->>>>>>>>>>>>>>>>> ERROR: Rossz parameterezes az mts-rm-marker-ben (az utolso alpha nem 1 )!!!! <<<<<<<<<<<<<<<<<<-------------\n\n");
	}
	if(rateMeasurements.size() == 0) {
		NS_FATAL_ERROR("\n\n--------->>>>>>>>>>>>>>>>> ERROR: Rossz parameterezes az mts-rm-marker-ben (nincs beallitva RateMeasuremant)!!!! <<<<<<<<<<<<<<<<<<-------------\n\n");
	}
}


PpovMtsRmMarkerQueue::~PpovMtsRmMarkerQueue ()
{
  NS_LOG_FUNCTION (this);
}
// new version from python
/*
def delta(k,i, R, alpha):
    R2 = [ max(R[j:]) for j in range(len(R))]
    res = R2[k]*(alpha[i]-1)
    for j in range(i+1, k):
        res += (alpha[i]/alpha[j]-1.0)*(R2[j]-R2[j+1])
	return res
*/

float PpovMtsRmMarkerQueue::delta (int i, Ptr<Packet> p) {
	int k = (int)rateMeasurements.size()-1;	//csak hogy a pythont kovessuk
	//R = rateMeasurements
	//alpha = alpha
	
	//R2 = [ max(R[j:]) for j in range(len(R))]
	std::vector<float> R2;
	for (int j=0; j<=k; j++) {
		float max_R = 0.0;
		for (int x = j; x<(int)rateMeasurements.size(); x++) {
			float tmp_R = getRateMeasurmentRate(x,p);
			if (tmp_R>max_R) {
				max_R = tmp_R;
			}
		}
		R2.push_back(max_R);
	}
    float res = R2[k]*(alpha[i]-1.0);
	for (int j=i+1; j<k; j++) {
		res += (alpha[i]/alpha[j]-1.0)*(R2[j]-R2[j+1]);
	}
	return res;
}

/*
def get_pv(r, R, alpha):
    ts_idx = 0
    for i in sorted(range(len(R)), reverse=True):
        if r<=R[i]:
            ts_idx=i
            break
    return tvf_base((r + delta(len(R)-1, ts_idx, R, alpha))/alpha[ts_idx])
*/

int PpovMtsRmMarkerQueue::get_pv(float r,Ptr<Packet> p) {
	int ts_idx = 0;
	
	for (int i=(int)rateMeasurements.size()-1; i>=0; i--) {
		if (r<=getRateMeasurmentRate(i,p)) {
			ts_idx = i;
			break;
		}
	}
	return calcCodedPacketValueFromRateBps(  (r+delta(ts_idx,p) )/alpha[ts_idx]/8, MAXPPV, ppov  );
}


bool
  PpovMtsRmMarkerQueue::DoEnqueue (Ptr<QueueDiscItem> item)
  {
    NS_LOG_FUNCTION (this << item);
    //NS_ASSERT (m_packets.size () == GetNPackets ());

    NS_LOG_LOGIC ("P-MARKER-V6 " << GetNPackets());
	
    Ipv4Header ipv4header;
    PppHeader pppHeader;

    //Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);
		

    Ptr<Packet> p = item->GetPacket();

	if(!initialized){
		initialized = true;
		ReadPpovFromFile(PpovPointsFile);
		printSourceAndPort(p);
		std::cout << std::endl;
		setConfig();
	}
	//update all rate
	updateRateMeasurments(p);
	float r = (float)rnd->GetValue(0.0,getRateMeasurmentRate(0,p));
	int markerColor = get_pv(r,p);

    p->RemoveHeader(pppHeader);
    p->RemoveHeader(ipv4header);

    NS_LOG_LOGIC ("P-MARKER-V4-COLOR " << markerColor);

    ipv4header.SetIdentification(markerColor);
    uint8_t tmptos = ipv4header.GetTos();
    tmptos &= 0x3;
    tmptos |= (dclass << 2);

	ipv4header.SetTos(tmptos);
    ipv4header.EnableChecksum();	
    p->AddHeader(ipv4header);
    p->AddHeader(pppHeader);

	float ps = p->GetSize();
	
	value_pairs value;
	value.add("ps",ps);
	PPVLogger* Logger = PPVLogger::getInstance();
	Logger->log("MarkerQueue",  "getColor", makeID(this), getSourceAndPortDCEcn(p), value);
	Logger->logEtvf("MarkerQueue", "getColor", makeID(this), getSourceAndPortDCEcn(p), markerColor, ps);

	
    //m_packets.push (item);
    
     Ptr<Ipv4QueueDiscItem> newItem = new Ipv4QueueDiscItem(p, item->GetAddress(), item->GetProtocol(), ipv4header);

    bool retval = GetInternalQueue(0)->Enqueue(newItem);

    return retval;
    
    //return true;
  }

void PpovMtsRmMarkerQueue::updateRateMeasurments (Ptr<Packet> p) {
	float ps = p->GetSize();
	for (int j = 0; j<(int)rateMeasurements.size(); j++) {
		rateMeasurements[j]->new_sample(Simulator::Now ().GetSeconds (), ps*8);
	}
}

  
float PpovMtsRmMarkerQueue::getRateMeasurmentRate (int i, Ptr<Packet> p) {
	std::string sourceInfo = getSourceAndPort(p);
	
	if (i>= (int)rateMeasurements.size()) {
		std::cout<<"rateMeasurement out of index: "<<i<<std::endl;
		exit(1);
	}
	return rateMeasurements[i]->get_rate(Simulator::Now ().GetSeconds (),sourceInfo);
}
 
  
Ptr<QueueDiscItem>
  PpovMtsRmMarkerQueue::DoDequeue (void)
  {
    NS_LOG_FUNCTION (this);
    //NS_ASSERT (m_packets.size () == GetNPackets ());
    if (GetInternalQueue(0)->GetNPackets() == 0) {
		return 0;
	}
    //Ptr<QueueItem> item = m_packets.front ();
    //m_packets.pop ();

    Ptr<QueueDiscItem> item = GetInternalQueue (0)->Dequeue ();
    NS_LOG_LOGIC ("Popped " << item);

    return item;
  }

Ptr<const QueueDiscItem>
  PpovMtsRmMarkerQueue::DoPeek (void) const
  {
    NS_LOG_FUNCTION (this);
    //NS_ASSERT (m_packets.size () == GetNPackets ());
    Ptr<const QueueDiscItem> item = GetInternalQueue (0)->Peek ();

  if (!item)
    {
      NS_LOG_LOGIC ("Queue empty");
      return 0;
    }

  return item;
  }

//TODO CheckConfig implementálása
bool
PpovMtsRmMarkerQueue::CheckConfig (void)
{
    
    NS_LOG_FUNCTION (this);
    NS_LOG_ERROR ("PpovMtsRmMarkerQueue CheckConfig metódusa még nincs implementálva ");
      return false;
  /*if (GetNQueueDiscClasses () > 0)
    {
      NS_LOG_ERROR ("PpovMtsRmMarkerQueue cannot have classes");
      return false;
    }

  if (GetNPacketFilters () > 0)
    {
      NS_LOG_ERROR ("PpovMtsRmMarkerQueue needs no packet filter");
      return false;
    }

  if (GetNInternalQueues () == 0)
    {
      // add a DropTail queue
      // AddInternalQueue (CreateObjectWithAttributes<DropTailQueue<QueueDiscItem> >
                          // ("MaxSize", QueueSizeValue (GetMaxSize ())));
      AddInternalQueue (CreateObjectWithAttributes<DropTailQueue<QueueDiscItem> >
                          ("MaxSize", StringValue ("100000p")));
    }

  if (GetNInternalQueues () != 1)
    {
      NS_LOG_ERROR ("PpovMtsRmMarkerQueue needs 1 internal queue");
      return false;
    }*/

  //return true;
}
void
PpovMtsRmMarkerQueue::InitializeParams (void)
{
  NS_LOG_FUNCTION (this);
}

bool PpovMtsRmMarkerQueue::ReadPpovFromFile(std::string path) {
  NS_LOG_LOGIC ("ppovfilename ::: " << PpovPointsFile );
  float thr, ppv;
  std::ifstream infile (PpovPointsFile.c_str());
  if (infile.is_open())
  {
    while ( infile >> thr, infile >> ppv ) {
      if (ppv > MAXPPV)
        throw std::invalid_argument("Error! Too high PV defined in the input file!");
      ppov.push_back(std::make_pair(thr, ppv));
	  // std::cout << "ppvpoint ::: t: " << thr << "  ppv: " << ppv << std::endl;
      NS_LOG_LOGIC ("ppvpoint ::: t: " << thr << "  ppv: " << ppv);
    }
    if (ppov.size() < 2) {
      throw std::invalid_argument("Error! The ppov.txt file does not contain enugh points!");
    }
    std::cout << "PpovMtsRmMarkerQueue::ReadPpovFromFile type: PpovMtsRmMarkerQueue ppovfilename: " << PpovPointsFile << " object: " << this << " ";

    return true;
  } else {
    std::cout << "Unable to open file";
    throw std::invalid_argument("Error! The input ppov.txt file could not be opened!\nPlease check the scratch folder!");
  }
}

} // namespace ns3

