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

#include "ns3/log.h"
#include "ppov-multiscale-bucket-marker-queue.h"
#include "ipv4-header.h"
#include "ns3/ppp-header.h"
#include <vector>
#include <arpa/inet.h>
#include <iostream>
#include <utility>
#include <limits>
#include <math.h>
#include <string>
#include "ns3/string.h"
#include "ns3/ppov-utils.h"
#include "ns3/ppvlogger.h"


namespace ns3 {
#define MAXPPV (1000000 * 4298662.34708228) // 10^6 * ppovgoldmax  by definition from p-maker-v5

NS_LOG_COMPONENT_DEFINE ("PpovMultiscaleBucketMarkerQueue");

NS_OBJECT_ENSURE_REGISTERED (PpovMultiscaleBucketMarkerQueue);

TypeId PpovMultiscaleBucketMarkerQueue::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PpovMultiscaleBucketMarkerQueue")
    .SetParent<Queue> ()
    .SetGroupName ("Network")
    .AddConstructor<PpovMultiscaleBucketMarkerQueue> ()
    .AddAttribute ("Limit",
        "Constant limit parameter of the packet value calculation.",
        UintegerValue (-1),
        MakeUintegerAccessor (&PpovMultiscaleBucketMarkerQueue::limit),
        MakeUintegerChecker<uint32_t> ())
    .AddAttribute ("MarkerFunctionPoints",
        "Filename, that contains the 150 numeric values for the marker function.",
        StringValue ("XX.txt"),
        MakeStringAccessor (&PpovMultiscaleBucketMarkerQueue::markerFunctionPoints),
        MakeStringChecker ())
    .AddAttribute ("TbTime",
                   "Lenght of the Token Bucket in seconds.",
                   DoubleValue (0.04),
                   MakeDoubleAccessor (&PpovMultiscaleBucketMarkerQueue::bucketLenSec),
                   MakeDoubleChecker<float> ())
    .AddAttribute ("DClass",
                    "DClass marking",
                    UintegerValue (0),
                    MakeUintegerAccessor (&PpovMultiscaleBucketMarkerQueue::dclass),
                    MakeUintegerChecker<uint8_t> ())

   ;
  return tid;
}

PpovMultiscaleBucketMarkerQueue::PpovMultiscaleBucketMarkerQueue ()
{
  NS_LOG_FUNCTION (this);
  limit = 0;
  rnd = CreateObject<UniformRandomVariable> ();
  initialized = false;
}

void PpovMultiscaleBucketMarkerQueue::InitBucketsFromFile()
{
  //float bucketLenSec = 0.1;	//FIXME - make it an NS parameter, was 100 ms in article. 40 ms might be a better value, but keep default to 100 ms
  buckets.clear();
//  bucketColorValues = ReadMarkerValues();
  //	for (uint16_t i=0xffff;i>1;i /= 2 ) {
//  for (uint16_t i=0;i<150;i++ ) {
  NS_LOG_LOGIC ("markerfilename ::: " << markerFunctionPoints );
  std::cout << "markerfilename ::: " << markerFunctionPoints << std::endl;
  std::vector<int> ret;
  float thr, ppv, bsize;
  std::string line;
  std::ifstream infile (markerFunctionPoints.c_str());
  //File row example
  //38788 1333.5222992134745 1666 666.7611496067373 83345 333.38057480336863 208362 166.69028740168432 208362
  //coded_pv th1_kbps mbs1_byte ... thn_kbps mbsn_byte 
  if (infile.is_open())
  {
	while (std::getline(infile, line))
	{
	  std::istringstream iss(line);
	  std::vector<TokenBucket> tbForOnePv;
	  std::vector<float> _tsThr;
	  
	  
	  iss >> ppv;

	  while (iss >> thr, iss >> bsize)
	  {
		TokenBucket tb = TokenBucket();
		tb.setBucketFlowRate(thr*1000.0);
		tb.setBucketSize(bsize);		//(thr*1000.0/8.0)*bucketLenSec
		tb.setColor(ppv);
		  
		tbForOnePv.push_back(tb);
		
		float _thr = 0.0;
		int j = tbForOnePv.size()-1;
		for (int iPv=0; iPv < (int)buckets.size(); iPv++ ) {
			_thr += buckets[iPv][j].getRate();
		}
		_tsThr.push_back(_thr);
	  }

	  buckets.push_back(tbForOnePv);
	  timescaleThr.push_back(_tsThr);
	}


	// while ( infile >> thr, infile >> ppv, infile >> bsize ) {
		// if (ppv > MAXPPV)
			// throw "Error! Too high PV defined in the input file!";
		
		// TokenBucket tb = TokenBucket();
		// tb.setBucketFlowRate(thr*1000.0);
		// tb.setBucketSize(bsize);		//(thr*1000.0/8.0)*bucketLenSec
		// tb.setColor(ppv);
		// buckets.push_back(tb);
		// ppov.push_back(std::make_pair(thr, ppv));
    // }
  }
}

PpovMultiscaleBucketMarkerQueue::~PpovMultiscaleBucketMarkerQueue ()
{
  NS_LOG_FUNCTION (this);
}

int PpovMultiscaleBucketMarkerQueue::getNPvs() {
	return buckets.size();
}

float PpovMultiscaleBucketMarkerQueue::getColor(Ptr<Packet> p) {
  NS_LOG_LOGIC ("HIER Bucket getColor " << GetNPackets());
  if (!initialized) {
    NS_LOG_LOGIC ("Buckets initialization.");
    InitBucketsFromFile();
    initialized = true;
    std::cout << "PpovMultiscaleBucketMarkerQueue::INIT type: PpovMultiscaleBucketMarkerQueue ppovfilename: " << markerFunctionPoints << " object: " << this <<  " ";
    printSourceAndPort(p);
    std::cout << std::endl;
  }

	//buckets[iPv][iTs] first index is PVs second is TimeScales
	float color = buckets[0][0].getColor(); //the smallest PV
	int iPv = 0;
	int packetsize = p->GetSize();
	int breakIts = 0;
	
	for (iPv=0; iPv < getNPvs(); iPv++) {
		int iTs = 0;
		
		//check whether packetsize buckets are available on all timescales
		for (iTs=0; iTs<(int)buckets[iPv].size(); iTs++) {
			buckets[iPv][iTs].update();
			if (buckets[iPv][iTs].getAvailableBucketSize() < packetsize) {
				breakIts = iTs;
				break; //iTS for
			}
		}

		// for else of the iTs for (break was not called)
		// this part only runs if all buckets had at least packetsize tokens for thie PV
		// we decrease those buckets with packetsize, and return with this pv
		if (iTs==(int)buckets[iPv].size()) {
			for (int k=0; k<(int)buckets[iPv].size(); k++) {
				buckets[iPv][k].decreaseAvailableBucketSize(packetsize);
			}
			color = buckets[iPv][0].getColor();
			//TODO call logMTSstate here
			break; //iPv for 
		}
	}
	
	
	// LOG	

        for (iPv=0; iPv < getNPvs(); iPv++) {
                int iTs = 0;
                std::cout << this << " --PV: " << iPv << " TS " << Simulator::Now().GetSeconds();
                for (iTs=0; iTs<(int)buckets[iPv].size(); iTs++) {
			buckets[iPv][iTs].update();
                        std::cout << " " << buckets[iPv][iTs].getAvailableBucketSize() << " Bytes";
		}
                std::cout << std::endl;
        }

	// std::cout << "PpovMultiscaleBucketMarkerQueue::getColor object: " << this << " t: " << Simulator::Now().GetSeconds();
	// std::cout << std::fixed << " color: " << color << " packetsize: " << packetsize ;
	// printSourceAndPort(p);
	//TODO: Ennek itt semmi ertelme, kell ez nekunk????? lehet ki lehet venni, ha senki nem hasznalja
	// std::cout << " bucketnum: "<< i << " bucketsize: " << buckets[i][0].getAvailableBucketSize() << std::endl;
	// std::cout << std::endl;

	value_pairs value;
	value.add("ps",packetsize);


	PPVLogger* Logger = PPVLogger::getInstance();
	//std::stringstream address;
	//address<<static_cast<void*>(this);
	//Logger->log("MarkerQueue",  "getColor", makeID(this), getSourceAndPortDC(p), value);
	Logger->log("MarkerQueue",  "getColor", makeID(this), getSourceAndPortDCEcn(p), value);
	// Logger->logEtvf("MarkerQueue", "getColor", makeID(this), getSourceAndPortDC(p), calcCodedPacketValueFromRateBps(color, MAXPPV, ppov), packetsize);
	// Logger->logEtvf("MarkerQueue", "getColor", makeID(this), getSourceAndPortDC(p), color, packetsize);
	Logger->logEtvf("MarkerQueue", "getColor", makeID(this), getSourceAndPortDCEcn(p), color, packetsize);


	// logMTState
	if (color != buckets[0][0].getColor()) {
		int i=0;
		for (i=0; i<(int)buckets[iPv-1].size(); i++) {
			value_pairs TSLogvalue;
			TSLogvalue.add("ppv",color);
			float v = 0.0;
			if (i == breakIts) {
				v = timescaleThr[iPv-1][breakIts];
			}
			std::ostringstream ss;
			ss << "TS"<<i;
			// TSLogvalue.add("TS",ss.str());
			TSLogvalue.add("thr",v);
			Logger->log("MarkerQueue","TSThr",ss.str(),getSourceAndPortDCEcn(p),TSLogvalue);	//ss.str()
		}
	}
	
	//FIXME - eszinda, hack to get it working with ECN scheduler
	//color += (int) rnd->GetValue(0,100);
	
	return color;
}


/*LogMTS State
az egyyel kisebb indexu ppv reszen nezzuk meg melyik TS limitalt eloszor.
per ts legyen ezeket pl. 100 ms-enkent lehetne logolni
-codedpv amit kapott (az adott ts miatt), ha az adott ts sose limital, akkor ez a iPv=0-hoz tartozo pv
-throughput ami ehhez tartozott

-minPV
-maxTh

*/

} // namespace ns3
