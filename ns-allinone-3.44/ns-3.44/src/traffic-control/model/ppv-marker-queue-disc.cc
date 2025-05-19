/* -*- Mode:C++; c-file-style:"gnu"; indent-tabs-mode:nil; -*- */
/*
 * Copyright (c) 2017 Universita' degli Studi di Napoli Federico II
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
 *
 * Authors:  Stefano Avallone <stavallo@unina.it>
 */
 
/*
Copyfrom p-marker-v5
*/

#include "ns3/log.h"
#include "ppv-marker-queue-disc.h"
#include "ns3/object-factory.h"
#include "ns3/drop-tail-queue.h"
#include "ns3/ppv-custom-data-tag.h"


namespace ns3 {
#define MAXPPV (1000000 * 4298662.34708228) // 10^6 * ppovgoldmax  by definition

NS_LOG_COMPONENT_DEFINE ("PpvMarkerQueueDisc");

NS_OBJECT_ENSURE_REGISTERED (PpvMarkerQueueDisc);

TypeId PpvMarkerQueueDisc::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PpvMarkerQueueDisc")
    .SetParent<QueueDisc> ()
    .SetGroupName ("TrafficControl")
    .AddConstructor<PpvMarkerQueueDisc> ()
	.AddAttribute ("PpovPointsFile",
                   "Filename, that describes a ppov curve point-by-point.",
                   StringValue ("XX.txt"),
                   MakeStringAccessor (&PpvMarkerQueueDisc::PpovPointsFile),
                   MakeStringChecker ())
    .AddAttribute ("MarkerMode",
                   "Mode defines how long the selective ppov range is applied.",
                   UintegerValue (1),
                   MakeUintegerAccessor (&PpvMarkerQueueDisc::mode),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("TbTime",
                   "Lenght of the Token Bucket in seconds.",
                   DoubleValue (0.04),
                   MakeDoubleAccessor (&PpvMarkerQueueDisc::tb_time),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("TbTarget",
                   "Lenght of the Token Bucket in bytes.",
                   UintegerValue (5*1500),
                   MakeUintegerAccessor (&PpvMarkerQueueDisc::tb_target),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("DClass",
                   "DClass marking",
                   UintegerValue (0),
                   MakeUintegerAccessor (&PpvMarkerQueueDisc::dclass),
                   MakeUintegerChecker<uint8_t> ())
    .AddAttribute ("Beta",
                   "Beta paramter for update",
                   UintegerValue (1000),
                   MakeUintegerAccessor (&PpvMarkerQueueDisc::tb_d_extra),
                   MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("AddTagTime",
                   "Time for tagging a packet",
                   DoubleValue (0.005),
                   MakeDoubleAccessor (&PpvMarkerQueueDisc::t_tagtime),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("Name",
                   "Name of the node",
                   StringValue ("Noname"),
                   MakeStringAccessor (&PpvMarkerQueueDisc::NodeName),
                   MakeStringChecker ())
   ;
  return tid;
}

PpvMarkerQueueDisc::PpvMarkerQueueDisc ()
  : QueueDisc (QueueDiscSizePolicy::NO_LIMITS ) //,
  // m_packets ()
{
  NS_LOG_FUNCTION (this);
  
  R = 0.0; //10000000.0/8.0; // 10 Mbps
  R_old = R;
  tb_time = 0.040; // 40 ms 
  tb_dmax = 1500;//tb_time * R;
  tb_d = 0;//tb_dmax/2;
  alpha = 0.9;
  tlast = 0.0;
  mode = 1;
  tb_target = 5*1500; //byte
  dclass = 0;
  rnd = CreateObject<UniformRandomVariable> ();
  initialized = false;
  lastTagtime = 0.0;
  // updateCTVTime = 0.005;
  updateCTVTime = 0.03;
  lastUpdateCTV = 0.0;
  ctv = 1;
  
  lower_percentile = 0.9;
  upper_percentile = 0.8;
  
  //ReadPpovFromFile(PpovPointsFile);
}

PpvMarkerQueueDisc::~PpvMarkerQueueDisc ()
{
  NS_LOG_FUNCTION (this);
  std::cout << "DESTROY PpvMarkerQueueDisc::PpvMarkerQueueDisc ()\n";
	
}

bool
PpvMarkerQueueDisc::DoEnqueue (Ptr<QueueDiscItem> item)
{
	// https://stackoverflow.com/questions/59040124/how-to-extract-ip-address-from-queuediscitem-in-ns3
 
	NS_LOG_FUNCTION (this << item);
    // NS_ASSERT (m_packets.size () == GetNPackets ());

    NS_LOG_LOGIC ("PPV-MARKER Npackets" << GetNPackets());
	
	Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);
		
    Ptr<Packet> p = item->GetPacket();

	//ide kell hogy ha eltelt x ido, akkor ne rakjuk be a sorba
	updateCTV();

    int markerColor = calcCodedPacketValueFromRateBps(getColor(p)); // TODO: Rename getRndRate
	
	// std::cout<<ctv<<"  "<<markerColor<<std::endl;
	if (ctv > markerColor) {
		DropBeforeEnqueue (item, LIMIT_EXCEEDED_DROP);
		return false;
	}
	
		//rakjunk ra taget
	Ipv4Header ipHeader = ipItem->GetHeader();
	
	float tnow = Simulator::Now ().GetSeconds ();
	
	if (tnow - lastTagtime > t_tagtime) {
		// todo: tvf-1 tomb feltoltese
		
		// double RforTag = R;
		// if (R > TVFinverz[ctv])
			// RforTag = TVFinverz[ctv];
		
		
		// float lower_ctv = convertToLogScale(calcPacketValue(RforTag-(RforTag*lower_percentile)));
		// float upper_ctv = convertToLogScale(calcPacketValue(RforTag-(RforTag*upper_percentile)));
		
		double r_lower = lower_percentile*R;
		if (r_lower > TVFinverz[ctv]) {
			r_lower = TVFinverz[ctv];
		}
		float lower_ctv = convertToLogScale(calcPacketValue(r_lower ));
		float upper_ctv = convertToLogScale(calcPacketValue(r_lower*upper_percentile ));

		// if (NodeName == "A0") 
			// std::cout<<" Add tag: "<< lastTagtime <<" vs "<<tnow<<" "<<  tnow - lastTagtime << " "<< t_tagtime << " "<< lower_ctv<< " "<< markerColor<< " "<< upper_ctv<<std::endl;
		// TODO: kikapcsolva
		if (false || (lower_ctv <= markerColor && upper_ctv >= markerColor)) {
			//mark packet
			CustomDataTag tag;
			tag.setMarkerNode ( this );
			p->AddPacketTag (tag);
			// std::cout<<" Add tag: "<< lastTagtime <<" vs "<<tnow<<" "<<  tnow - lastTagtime << " "<< t_tagtime <<std::endl;
			lastTagtime = tnow;
			LogMarkerCTV(tnow,R, markerColor);
		}
	}
	
	
	
    NS_LOG_LOGIC ("PPV-MARKER-COLOR " << markerColor);
    // std::cout<<"PPV-MARKER-COLOR " << markerColor<<std::endl;

    ipHeader.SetIdentification(markerColor);
	if (lastTagtime != tnow) 
		LogMarkerCTV(tnow,R, markerColor);
	// ipHeader.SetTos(1);
	ipHeader.SetDscp(Ipv4Header::DSCP_CS1);	
	
    ipHeader.EnableChecksum();

	Ptr<Ipv4QueueDiscItem> newItem = new Ipv4QueueDiscItem(p,item->GetAddress(),item->GetProtocol(),ipHeader);
	


	//feleseleges queue tarolas, de kell a statisztikajaba
	bool retval = GetInternalQueue (0)->Enqueue (newItem);

	return retval;

}

std::string 
PpvMarkerQueueDisc::getName() {
	return NodeName;
}

void 
PpvMarkerQueueDisc::setCTV(int _ctv) {
	// std::cout<<" setCTV "<<_ctv<<std::endl;
	if (_ctv > ctv) {
		lastUpdateCTV = Simulator::Now ().GetSeconds ();
		ctv = _ctv;
	}
}

void 
PpvMarkerQueueDisc::updateCTV() {
	//eltelt idovel csokkenteni a CTV-t
	float tnow = Simulator::Now ().GetSeconds ();
	int multiple = (tnow - lastUpdateCTV) / updateCTVTime;
	if (multiple > 0) {
		lastUpdateCTV = tnow;
		ctv -= multiple*64;
		if (0 > ctv) ctv = 0;
	}
}

Ptr<QueueDiscItem>
PpvMarkerQueueDisc::DoDequeue (void)
{
	NS_LOG_FUNCTION (this);
    // NS_ASSERT (m_packets.size () == GetNPackets ());
	
    // std::cout << "DoDequeue Marker Size " << GetInternalQueue(0)->GetNPackets() << std::endl;
	if (GetInternalQueue(0)->GetNPackets() == 0) {
		return 0;
	}

    // NS_LOG_LOGIC ("DoDequeue Size " << GetInternalQueue(0)->GetNPackets());
    // std::cout << "DoDequeue Size " << GetInternalQueue(0)->GetNPackets() << std::endl;

	//feleseleges queue tarolas, de kell a statisztikajaba
	Ptr<QueueDiscItem> item = GetInternalQueue (0)->Dequeue ();
	
	

	
	// Ptr<Ipv4QueueDiscItem> newItem = new Ipv4QueueDiscItem(p,item->GetAddress(),item->GetProtocol(),ipHeader);

    return item;
}

Ptr<const QueueDiscItem>
PpvMarkerQueueDisc::DoPeek (void)
{
  NS_LOG_FUNCTION (this);
  // NS_ASSERT (m_packets.size () == GetNPackets ());
  
  Ptr<const QueueDiscItem> item = GetInternalQueue (0)->Peek ();

  if (!item)
    {
      NS_LOG_LOGIC ("Queue empty");
      return 0;
    }

  return item;
}

bool
PpvMarkerQueueDisc::CheckConfig (void)
{
  NS_LOG_FUNCTION (this);
  if (GetNQueueDiscClasses () > 0)
    {
      NS_LOG_ERROR ("PpvMarkerQueueDisc cannot have classes");
      return false;
    }

  if (GetNPacketFilters () > 0)
    {
      NS_LOG_ERROR ("PpvMarkerQueueDisc needs no packet filter");
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
      NS_LOG_ERROR ("PpvMarkerQueueDisc needs 1 internal queue");
      return false;
    }

  return true;
}

void
PpvMarkerQueueDisc::InitializeParams (void)
{
  NS_LOG_FUNCTION (this);
}

float PpvMarkerQueueDisc::getColor(Ptr<Packet> p) {
  // NS_LOG_LOGIC ("Ppv-marker getColor npackets" << GetNPackets());


  if(!initialized){
      ReadPpovFromFile(PpovPointsFile);
      // std::cout << std::endl;
	  
	  double rate = 10e3;
	  int pv = calcCodedPacketValueFromRateBps(rate);
	  // TVFinverz.push_back(0);
	  // TVFinverz[pv] = rate;
		for (int i = 0; i<=65535; i++) {
			TVFinverz.push_back(0);
		}
	  
	  double rateStep = 1e3;
	  //TODO kisebb pvket is kitolteni
		for (int i = 65535; i>=pv; i--) {
			TVFinverz[i] = rate;
		}
	  while (rate < 1e9) {
		  rate += rateStep;
		  int pv_new = calcCodedPacketValueFromRateBps(rate);
		  if (pv_new < pv) {
			for (int i = pv-1; i>=pv_new; i--) {
				TVFinverz[i] = rate;
			}
			pv = pv_new;
		  }
	  }
		for (int i = pv-1; i>=0; i--) {
			TVFinverz[i] = rate;
		}
		// for (int i = 0; i<=65535; i++) {
			 // std::cout <<std::fixed<<"TVFxx "<< i << " " <<TVFinverz[i]<< std::endl;
		 // }

      initialized = true;
      // std::cout << "---### tb_time: " << tb_time
                // << " tb_target: " << tb_target
                // << " file: " << PpovPointsFile
                // << " mode: " << mode << " ###---\n";
  }

  //  std::cout << "#### TB DATA: "<< tb_time << ", "<< tb_target << "," << tb_d_extra<< std::endl;
  float color = 0.0; 
  int packetsize = p->GetSize();
  float tnow = Simulator::Now ().GetSeconds ();
  float dt = tnow - tlast;

  tlast = tnow;

  // Update token bucket
  tb_d += R*dt;

  //FIXME: no upper limit now. 
  // tb_time is still used, but only as an averaging interval
  //if (tb_d>tb_dmax) tb_d = tb_dmax;

  long tb_d_new= tb_d - packetsize;

  if (tb_d_new < 0) { // not enough tokens: 
    // - increase rate
    // - get uniform random rate between old rate and new rate
    R_old = R;
	//long tb_d_extra = 1000; //tb_target/2;
	tb_d_new -= tb_d_extra;
    R += -tb_d_new/tb_time;
    tb_d = tb_d_extra;
    //std::cout << "TB_DMAX: " << tb_dmax << std::endl;
    tb_dmax = tb_time * R;
    color = (float)rnd->GetValue((double)R_old, (double)R);
	//color = (float)rnd->GetValue(0.0,(double)R);
  } else if (tb_d_new > tb_target) { // too many tokens:
    // -decrease rate to reach target 
    // -set new buket size to taget
    // FIXME - handling of too large buffer is missing - in that case tb_d is probably zero. (no packets for tb_time)
    //R =  max( R - (tb_d_new - tb_target)/tb_time , packetsize/tb_time);
    R -= (tb_d_new - tb_target)/tb_time;
    if (R < packetsize/tb_time) {
      R = packetsize/tb_time;
      tb_d = 0;
    } else {
      tb_d = tb_target;
    }

    color = (float)rnd->GetValue(0.0,(double)R);
  } else { // just remove token and get a random between 0 and R
    tb_d = tb_d_new;
    color = (float)rnd->GetValue(0.0,(double)R);
  }
  //kikommentezve hogy kevesebb log legyen
  PPV_Print_Stat(tnow,tb_d_new,R_old,R);
  
  return color;
}

 int PpvMarkerQueueDisc::calcCodedPacketValueFromRateBps(double rateBps) {
     return convertToLogScale(calcPacketValue(rateBps));
 }

int PpvMarkerQueueDisc::convertToLogScale(double color) {
    if(color < 1 || color > MAXPPV)
        throw "Error! Cannot convert color to a log scale - input is out of range.";
    double b = log10(color) / log10(MAXPPV);
    return (int)((b * 65535) +1);
}

// any unnecessary write to the stdout will probably mess up the post processing
double PpvMarkerQueueDisc::calcPacketValue(double throughput) {

  throughput =  throughput * 8 / 1000; // byte p s -> kbps conversion

  if ( throughput > ppov.back().first) {
    throw "Error! This packet's color is greater than the highest defined - would have ppv: 0 - Aborting!";
    return 0; // unreachable
  } else if (throughput < ppov.front().first) {
    return ppov.front().second;
  }

  int section = -1; // watch for indexing!!
  for(std::vector< std::pair<float, float> >::iterator it = ppov.begin(); it != ppov.end(); ++it)
    if ((*it).first < throughput)
      ++section;

  if(-1 == section && throughput == ppov.front().first)
    section = 0;

  double pow = ( std::log10( ppov[section +1].second / ppov[section].second ) ) /
               ( std::log10( ppov[section +1].first  / ppov[section].first  ) );

  double res = ppov[section].second * (std::pow( ( throughput / ppov[section].first ), pow));
  // std::cout << "   POW: " << pow << "  RES: " << res  << "   " << std::flush;

  if (std::isnan(res))
    throw "Error! Calculated pv is nan!";
  if (std::isinf(res))
    throw "Error! Owerflow during calcPacketValue!";

  return res;
}


// needs to be called
bool PpvMarkerQueueDisc::ReadPpovFromFile(std::string path) {
  NS_LOG_LOGIC ("ppovfilename ::: " << PpovPointsFile );
  std::cout << "ppovfilename ::: " << PpovPointsFile << std::endl;
  float thr, ppv;
  std::ifstream infile (PpovPointsFile.c_str());
  if (infile.is_open())
  {
    while ( infile >> thr, infile >> ppv ) {
      if (ppv > MAXPPV)
        throw "Error! Too high PV defined in the input file!";
      ppov.push_back(std::make_pair(thr, ppv));
      NS_LOG_LOGIC ("ppvpoint ::: t: " << thr << "  ppv: " << ppv);
    }
    if (ppov.size() < 2) {
      throw "Error! The ppov.txt file does not contain enugh points!";
    }
    return true;
  } else {
    std::cout << "Unable to open file";
    throw "Error! The input ppov.txt file could not be opened!\n"
          "Please check the scratch folder!";
    return false; // unreachable
  }
}

void PpvMarkerQueueDisc::PPV_Print_Stat (float tnow, long tb_d_new, float R_old, float R)
{
  NS_LOG_FUNCTION (this);
 	std::ofstream myfile;
	std::stringstream ss;
	ss << "log/marker"<<"_"<<NodeName<<".txt";
	
	myfile.open (ss.str(),std::ios::app);
  
  myfile<<tnow<<";"<<tb_d_new<<";"<<R_old<<";"<<R<<";"<<ctv<<"\n";

  myfile.close();

}

void PpvMarkerQueueDisc::LogMarkerCTV (float tnow, float R, float pv)
{
  NS_LOG_FUNCTION (this);
 	std::ofstream myfile;
	std::stringstream ss;
	ss << "log/markerPV"<<"_"<<NodeName<<".txt";
	
	myfile.open (ss.str(),std::ios::app);
  
  myfile<<tnow<<";"<<(R*8.0)<<";"<<pv<<"\n";

  myfile.close();

}

} // namespace ns3
