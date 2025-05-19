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

#ifndef PPV_SCHED_QUEUE_DISC_H
#define PPV_SCHED_QUEUE_DISC_H

#include "ns3/queue-disc.h"

#include <vector>
#include <queue>

#include "ns3/ipv4-queue-disc-item.h"
#include "ns3/string.h"
#include "ns3/simulator.h"


namespace ns3 {

/**
 * \ingroup traffic-control
 *
 * Simple queue disc implementing the FIFO (First-In First-Out) policy.
 *
 */
class PpvSchedulerQueueDisc : public QueueDisc {
	
public:
	struct ctvData {
	  int pv;
	  double time;
	} ;
  /**
   * \brief Get the type ID.
   * \return the object TypeId
   */
  static TypeId GetTypeId (void);
  /**
   * \brief PpvSchedulerQueueDisc constructor
   *
   * Creates a queue with a depth of 1000 packets by default
   */
  PpvSchedulerQueueDisc ();

  virtual ~PpvSchedulerQueueDisc();

  // Reasons for dropping packets
  static constexpr const char* LIMIT_EXCEEDED_DROP = "Queue disc limit exceeded";  //!< Packet dropped due to queue disc limit exceeded

private:
  virtual bool DoEnqueue (Ptr<QueueDiscItem> item);
  virtual Ptr<QueueDiscItem> DoDequeue (void);
  virtual Ptr<const QueueDiscItem> DoPeek (void);
  virtual bool CheckConfig (void);
  virtual void InitializeParams (void);
  
  void SetMarkerCTV(Ptr<QueueDiscItem> _item);

  std::vector<Ptr<QueueDiscItem> > m_packets; //!< the items in the queue
  std::vector<int > m_pstats;
  
  std::string NodeName;
  // std::vector<std::string> statInfos;
  
  uint32_t maxSize = 0;
  uint32_t actSize = 0;		//non ecn marked packet
  uint32_t realSize = 0;	//packet in buffer
  std::string maxSizeForLimit = "0p";
  
  // QueueSize maxSize = QueueSize("0B");
  // QueueSize actSize = QueueSize("0B");
  
  bool RemoveMinPPOV(Ptr<QueueDiscItem>item, int _minppv);
  void addStatInfos(Ptr<QueueDiscItem> item);
  void PPV_Print_Stat (Ptr<Packet> pkt, Ipv4Address from);
  void PPV_Print_DropEcn (Ipv4Header ipHeader);
  
  Ptr<QueueDiscItem> setEC (Ptr<QueueDiscItem> item);
  void checkECN (Ptr<QueueDiscItem> item);
  
  int getCTV();
  uint32_t getBufferSize(bool withoutECN);
  
  double CTVWindowTime = 0.1;
  std::vector<ctvData > CTVDroppedPackets;
  
  bool logExists = false;
  // std::vector<std::string> getStatInfos();
};

} // namespace ns3

#endif /* PPV_SCHED_QUEUE_DISC_H */
