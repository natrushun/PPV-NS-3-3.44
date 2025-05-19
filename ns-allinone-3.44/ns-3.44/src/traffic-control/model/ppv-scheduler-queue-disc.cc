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

#include "ns3/log.h"
#include "ppv-scheduler-queue-disc.h"
#include "ns3/object-factory.h"
#include "ns3/drop-tail-queue.h"
#include <iostream>
#include <fstream>
#include "ns3/inet-socket-address.h"
#include "ns3/tcp-header.h"

#include "ns3/ppv-marker-queue-disc.h"
#include "ns3/ppv-custom-data-tag.h"


namespace ns3 {

NS_LOG_COMPONENT_DEFINE ("PpvSchedulerQueueDisc");

NS_OBJECT_ENSURE_REGISTERED (PpvSchedulerQueueDisc);

TypeId PpvSchedulerQueueDisc::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::PpvSchedulerQueueDisc")
    .SetParent<QueueDisc> ()
    .SetGroupName ("TrafficControl")
    .AddConstructor<PpvSchedulerQueueDisc> ()
    // .AddAttribute ("MaxSize",
                   // "The max queue size",
                   // QueueSizeValue (QueueSize ("1000p")),
                   // MakeQueueSizeAccessor (&QueueDisc::SetMaxSize,
                                          // &QueueDisc::GetMaxSize),
                   // MakeQueueSizeChecker ())
    .AddAttribute ("MaxSizeForLimit",
                   "The max queue size for the real queue",
                   StringValue ("0p"),
                   MakeStringAccessor (&PpvSchedulerQueueDisc::maxSizeForLimit),
                   MakeStringChecker ())
    .AddAttribute ("Name",
                   "Name of the node",
                   StringValue ("Noname"),
                   MakeStringAccessor (&PpvSchedulerQueueDisc::NodeName),
                   MakeStringChecker ())
  ;
  return tid;
}

PpvSchedulerQueueDisc::PpvSchedulerQueueDisc ()
  : QueueDisc (QueueDiscSizePolicy::NO_LIMITS ),
  m_packets ()
{
  NS_LOG_FUNCTION (this);
}

PpvSchedulerQueueDisc::~PpvSchedulerQueueDisc ()
{
  NS_LOG_FUNCTION (this);
}

void PpvSchedulerQueueDisc::checkECN (Ptr<QueueDiscItem> item) {
  Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);
  Ipv4Header ipv4header = ipItem->GetHeader();
  
  NS_ASSERT (ipv4header.GetEcn()==Ipv4Header::ECN_CE);
}

Ptr<QueueDiscItem> PpvSchedulerQueueDisc::setEC (Ptr<QueueDiscItem> item) {
		//red-queue-disc.cc:421
		Mark (item, "Forced Mark");
		  // bool retval = item->Mark ();
 
		// if (!retval)
		// {
			// NS_ASSERT (0 > 1);
		// }
		
		// std::cout<<NodeName<<"ECN"<<std::endl;

		return item;
	
		Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);
		Ptr<Packet> p = item->GetPacket();	
		Ipv4Header ipHeader = ipItem->GetHeader();
		// ipHeader.SetIdentification(65000);
		ipHeader.SetEcn( Ipv4Header::ECN_CE );

		ipHeader.EnableChecksum();

		Ptr<Ipv4QueueDiscItem> newItem = new Ipv4QueueDiscItem(p,item->GetAddress(),item->GetProtocol(),ipHeader);
		
		return newItem;
}

bool
PpvSchedulerQueueDisc::DoEnqueue (Ptr<QueueDiscItem> item)
{
  NS_LOG_FUNCTION (this << item);

  // std::cout<<NodeName<<" "<<actSize << "/" << maxSize << std::endl;
  if (maxSize == 0) {  //QueueSize("0B")
	QueueSize q = QueueSize(maxSizeForLimit);
	maxSize = q.GetValue();
	// SetMaxSize(QueueSize ("100000000p"));
	std::cout<<"maxsize"<<maxSize<<std::endl;
	actSize = 0; // QueueSize("0B");
	realSize = 0;
  }
  // uint32_t old_actSize = actSize;
  // uint32_t old_realSize = realSize;

  Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);

  Ipv4Header ipv4header = ipItem->GetHeader();
  
  // TcpHeader tcpHdr;
  // Ptr<Packet> pkt = ipItem->GetPacket ();
  // pkt->PeekHeader (tcpHdr);
  // uint8_t flags = tcpHdr.GetFlags ();
  // std::string flags_s = tcpHdr.FlagsToString(flags);

  int ppv = ipv4header.GetIdentification();
  //mar markolva volt a csomag mire ideert
  if (ipv4header.GetEcn()==Ipv4Header::ECN_CE) ppv = 65535;
  
  // std::cout<<"PPV "<<ppv<<std::endl; 
  
  // if (flags_s.find("ACK") !=std::string::npos ) {
  if (item->GetSize() < 500 ) {
		ppv = 65534;
  }
  
  NS_LOG_LOGIC ("PpvSchedulerQueueDisc::DoEnqueue ppv:" << ppv);
  // if (GetCurrentSize () + item < GetMaxSize ()) {
  if (ipv4header.GetEcn()==Ipv4Header::ECN_CE || actSize + item->GetSize() <= maxSize) {
		//nop
  } else {
	if ( ! RemoveMinPPOV(item, ppv ) ) {
		// kikommentezve hogy kevesebb log legyen
		PPV_Print_DropEcn(ipv4header);
		if (ipv4header.GetEcn()!=Ipv4Header::ECN_NotECT  && 
          ipv4header.GetProtocol() != 17) // FIXME hacking: UDP is assumed non-ECT, even when UDP header says ECT
		{ 
			// item = 
			setEC(item);
			ppv = 65535;	// csak a statisztikaba lesz felveve
			checkECN(item);
		} else {
			ctvData x;
			x.time = Simulator::Now ().GetSeconds ();
			x.pv = ppv;
			CTVDroppedPackets.push_back(x);

			DropBeforeEnqueue (item, LIMIT_EXCEEDED_DROP);
			return false;
		}
	}
	// Ptr<QueueDiscItem> _item = GetInternalQueue (0)->Dequeue ();
  }

  GetInternalQueue (0)->Enqueue (item);
  m_packets.push_back (item);
  m_pstats.push_back ( ppv );
  if (ppv != 65535 && ipv4header.GetEcn() != Ipv4Header::ECN_CE) {
	actSize = actSize + item->GetSize();
  }
  realSize = realSize + item->GetSize();

  NS_ASSERT (actSize <= realSize);
  NS_ASSERT (actSize == getBufferSize(true));
  return true;
}

Ptr<QueueDiscItem>
PpvSchedulerQueueDisc::DoDequeue (void)
{
  NS_LOG_FUNCTION (this);
	if (m_packets.size() == 0) {
		// std::cout<<"-----EMPTY-----"<<std::endl;
		return 0;
	}
 
  Ptr<QueueDiscItem> item =  m_packets.front ();
  
  Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);

  Ipv4Header ipv4header = ipItem->GetHeader();
  
  if (item->GetSize()>=realSize) {
	realSize=0;
  } else {
	realSize=realSize - item->GetSize();
  }
  
  if (ipv4header.GetEcn() != Ipv4Header::ECN_CE) // FIXME hacking: UDP is assumed non-ECT, even when UDP header says ECT
		{
	if (item->GetSize()>=actSize) {
		actSize = 0;
	} else {
		actSize= actSize - item->GetSize();
	}
  } else {checkECN(item);}
  
  
	m_packets.erase( m_packets.begin ());
	m_pstats.erase( m_pstats.begin ());
	addStatInfos(item);

	NS_ASSERT (actSize <= realSize);
	NS_ASSERT (actSize == getBufferSize(true));

	//ez csak azert hogy uruljon a sor es a statisztika
	// Ptr<QueueDiscItem> tmp_item = GetInternalQueue (0)->Dequeue ();
	
	//csunya de mukodik, hogy kiuritem a sort
	GetInternalQueue (0)->Flush ();
	
	return item;

}

Ptr<const QueueDiscItem>
PpvSchedulerQueueDisc::DoPeek (void)
{
  NS_LOG_FUNCTION (this);
  return m_packets.front ();
  }
  
int
PpvSchedulerQueueDisc::getCTV() {
	double actTime = Simulator::Now ().GetSeconds ();
	

	// while (CTVDroppedPackets.size() > 0 && actTime - CTVDroppedPackets[0].time > CTVWindowTime ) {
	while (CTVDroppedPackets.size() > 0 && actTime - CTVDroppedPackets.begin()->time > CTVWindowTime ) {
		CTVDroppedPackets.erase( CTVDroppedPackets.begin ());
	}				
	
	int CTV = 1;
	for (unsigned int i = 0; i<CTVDroppedPackets.size(); i++ ) {
		if (CTV < CTVDroppedPackets[i].pv) {
			CTV = CTVDroppedPackets[i].pv;
		}
	}
	
	return CTV;
}

void 
PpvSchedulerQueueDisc::addStatInfos(Ptr<QueueDiscItem> item) {
	//print statistical information
	//nodeId/schedulerId, source, pkt_size, ppv-t, ctv-t(a limit a schedulerben)
	Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(item);
	Ptr<Packet> p = item->GetPacket();

	Ipv4Header ipHeader = ipItem->GetHeader();

	// if (ipHeader.GetTos() != 1) {
		// return;
	// }
	
	if (ipHeader.GetDscp() != Ipv4Header::DSCP_CS1) {
		return;
	}

	std::ofstream myfile;
	myfile.open ("log/sched_"+NodeName+".txt",std::ios::app);

    if (!logExists) {
		// print header
		myfile << "nodename;src;dst;time;pktSize;pv;ctv;qlenReal;qlenAct;calcqlenReal;calcqlenAct\n";
		logExists = true;
	}

	
	myfile << NodeName << ";";
	ipHeader.GetSource().Print(myfile);
	myfile << ";";
	ipHeader.GetDestination().Print(myfile);
	myfile << ";";
	myfile << Simulator::Now ().GetSeconds () << ";";
	myfile << p->GetSize() << ";";
	myfile << ipHeader.GetIdentification() << ";";
	myfile << getCTV() << ";";
	myfile << realSize << ";";
	myfile << actSize;
	// TODO: Ez csak teszt miatt van kiiratva
	myfile << ";"<<getBufferSize(false) ;
	myfile << ";"<<getBufferSize(true) ;
	myfile << "\n";
	myfile.close();

	// statInfos.push_back(os.str());
}


bool
PpvSchedulerQueueDisc::CheckConfig (void)
{
  NS_LOG_FUNCTION (this);
  // return true;
  if (GetNQueueDiscClasses () > 0)
    {
      NS_LOG_ERROR ("PpvSchedulerQueueDisc cannot have classes");
      return false;
    }

  if (GetNPacketFilters () > 0)
    {
      NS_LOG_ERROR ("PpvSchedulerQueueDisc needs no packet filter");
      return false;
    }

  if (GetNInternalQueues () == 0)
    {
      // add a DropTail queue
      // AddInternalQueue (CreateObjectWithAttributes<DropTailQueue<QueueDiscItem> >
                          // ("MaxSize", QueueSizeValue (GetMaxSize ())));
                          // ("MaxSize", QueueSizeValue ( QueueSize(maxSizeForLimit))));		//ez a sor csak a queuediscnek kell, nincs lenyegeben haszalva, ezert nagy a queusize
      AddInternalQueue (CreateObjectWithAttributes<DropTailQueue<QueueDiscItem> >
                          ("MaxSize", StringValue ("10000000p")));
    }

  if (GetNInternalQueues () != 1)
    {
      NS_LOG_ERROR ("PpvSchedulerQueueDisc needs 1 internal queue");
      return false;
    }

  return true;
}

void
PpvSchedulerQueueDisc::InitializeParams (void)
{
  NS_LOG_FUNCTION (this);
}

void
PpvSchedulerQueueDisc::SetMarkerCTV(Ptr<QueueDiscItem> _item) {
	Ptr<Packet> packet = _item->GetPacket();	
		
	CustomDataTag tag;
    if (packet->PeekPacketTag (tag))
    {
		PpvMarkerQueueDisc* markerNode = tag.getMarkerNode ( );
        // NS_LOG_INFO ("\tFrom Node Id: " << markerNode->getName());
		Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(_item);
		Ipv4Header ipv4header = ipItem->GetHeader();
		int ppv = ipv4header.GetIdentification();
     	markerNode->setCTV(ppv);
     	// markerNode->setCTV(getCTV());
        // std::cout<< "Set CTV on Node: "<< markerNode->getName()<<" "<<getCTV()<<std::endl;
    }
}


bool
PpvSchedulerQueueDisc::RemoveMinPPOV(Ptr<QueueDiscItem>_item, int arrive_ppv)
{
  NS_LOG_FUNCTION (this);

  int minppv = arrive_ppv;
  int minidx = -1;

  while (actSize + _item->GetSize() > maxSize ) {
    minppv = arrive_ppv;
    minidx = -1;
	for (unsigned int i=0;i<m_packets.size();++i)
	{
		int act_ppv = m_pstats.at(i);
		if (act_ppv<minppv) {
			minppv = act_ppv;
			minidx = i;
		}
	}
	ctvData x;
	x.time = Simulator::Now ().GetSeconds ();
	if (minidx != -1)
	{
		//TODO: ITT EZ NEM JO!!! NEM AZ ITEM KELLENE, HANEM m_packets.at(minidx)
		Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(m_packets.at(minidx));
		Ipv4Header ipHeader = ipItem->GetHeader();
		
		// kikommentezve,hogy kevesebb log legyen
		PPV_Print_DropEcn(ipHeader);
		if (ipHeader.GetEcn()!=Ipv4Header::ECN_NotECT  && 
          ipHeader.GetProtocol() != 17) // FIXME hacking: UDP is assumed non-ECT, even when UDP header says ECT
		{
			Ptr<QueueDiscItem> item = m_packets.at(minidx);
			setEC(item);
			// m_packets.at(minidx) = item;
			int ppv = 65535;	// csak a statisztikaba lesz felveve
			m_pstats.at(minidx) = ppv;
			if (m_packets.at(minidx)->GetSize()>= actSize) {
				actSize = 0;
			} else {
				actSize = actSize - m_packets.at(minidx)->GetSize();
			}
			checkECN(item);

		} else {
			if (m_packets.at(minidx)->GetSize()>= actSize) {
				actSize = 0;
				realSize = 0;
			} else {
				actSize = actSize - m_packets.at(minidx)->GetSize();
				realSize = realSize - m_packets.at(minidx)->GetSize();
			}
			SetMarkerCTV(m_packets.at(minidx));
			m_packets.erase( m_packets.begin() + minidx);
			m_pstats.erase( m_pstats.begin() + minidx);
			// Ptr<QueueDiscItem> _item = GetInternalQueue (0)->Dequeue ();
		}
		x.pv = minppv;
		CTVDroppedPackets.push_back(x);
		// std::cout<<"PPV  "<<x.pv<<std::endl;
	} else {
		x.pv = arrive_ppv;
		CTVDroppedPackets.push_back(x);
		SetMarkerCTV(_item);
		Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(_item);
		Ipv4Header ipHeader = ipItem->GetHeader();
		PPV_Print_DropEcn(ipHeader);
		// std::cout<<"PPV2  "<<x.pv<<" "<<arrive_ppv<<std::endl;
		break;
	}
  }  
  return minidx!=-1;
}

uint32_t
PpvSchedulerQueueDisc::getBufferSize(bool withoutECN) {
	uint32_t size = 0;
	//1tol induljon mert az elso el fogjuk dobni
	for (unsigned int i=0;i<m_packets.size();++i)
	{
	  if (withoutECN) {
		Ptr<const Ipv4QueueDiscItem> ipItem = DynamicCast<const Ipv4QueueDiscItem>(m_packets.at(i));
		Ipv4Header ipv4header = ipItem->GetHeader();
		if (ipv4header.GetEcn()!=Ipv4Header::ECN_CE) size += m_packets.at(i)->GetSize();
	  } else {
		 size += m_packets.at(i)->GetSize();
	  }
	}
	return size;
}


void PpvSchedulerQueueDisc::PPV_Print_Stat (Ptr<Packet> pkt, Ipv4Address from)
{
  NS_LOG_FUNCTION (this);
 	std::ofstream myfile;
	std::stringstream ss;
	ss << "log/trace_sched"<<"_"<<NodeName<<".txt";
	

	
	myfile.open (ss.str(),std::ios::app);

	// if (!logExists) {
		// print header
		// myfile << "time;pktSize;src\n";
		// logExists = true;
	// }
  
  myfile<<Simulator::Now ().GetSeconds ()<<";"<<pkt->GetSize()<<";"<<from<<"\n";

  myfile.close();

}

void PpvSchedulerQueueDisc::PPV_Print_DropEcn (Ipv4Header ipHeader)
{
	NS_LOG_FUNCTION (this);

 	std::ofstream myfile;
	std::stringstream ss;
	ss << "log/dropEcn"<<"_"<<NodeName<<".txt";

	myfile.open (ss.str(),std::ios::app);
		
	if (ipHeader.GetEcn()!=Ipv4Header::ECN_NotECT  && 
	  ipHeader.GetProtocol() != 17) // FIXME hacking: UDP is assumed non-ECT, even when UDP header says ECT
	{
		myfile<<Simulator::Now ().GetSeconds ()<<";ecn";
	} else {
		myfile<<Simulator::Now ().GetSeconds ()<<";drop";
	}
  
  	myfile << ";";
	ipHeader.GetSource().Print(myfile);
	myfile << ";";
	ipHeader.GetDestination().Print(myfile);
	myfile << "\n";

  myfile.close();

}


} // namespace ns3
