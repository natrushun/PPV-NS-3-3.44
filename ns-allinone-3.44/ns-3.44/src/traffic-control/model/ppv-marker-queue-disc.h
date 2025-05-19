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

#ifndef PPV_MARKER_QUEUE_DISC_H
#define PPV_MARKER_QUEUE_DISC_H

#include <queue>
#include <set>
#include <utility>
#include <vector>
#include <fstream>
#include "ns3/random-variable-stream.h"
#include "ns3/simulator.h"
#include "ns3/string.h"

#include "ns3/ipv4-header.h"
#include "ns3/ppp-header.h"
#include "ns3/ipv4-queue-disc-item.h"

#include "ns3/queue-disc.h"


namespace ns3 {

/**
 * \ingroup traffic-control
 *
 * Simple queue disc implementing the FIFO (First-In First-Out) policy.
 *
 */
class PpvMarkerQueueDisc : public QueueDisc {
public:
  /**
   * \brief Get the type ID.
   * \return the object TypeId
   */
  static TypeId GetTypeId (void);
  /**
   * \brief PpvMarkerQueueDisc constructor
   *
   * Creates a queue with a depth of 1000 packets by default
   */
  PpvMarkerQueueDisc ();

  virtual ~PpvMarkerQueueDisc();

  // Reasons for dropping packets
  static constexpr const char* LIMIT_EXCEEDED_DROP = "Queue disc limit exceeded";  //!< Packet dropped due to queue disc limit exceeded

  void set_id(int id);
	std::string getName();
	void setCTV (int ctv);

private:
  virtual bool DoEnqueue (Ptr<QueueDiscItem> item);
  virtual Ptr<QueueDiscItem> DoDequeue (void);
  virtual Ptr<const QueueDiscItem> DoPeek (void);
  virtual bool CheckConfig (void);
  virtual void InitializeParams (void);
  
    virtual float getColor(Ptr<Packet> p);
    double calcPacketValue(double throughput);
    bool ReadPpovFromFile(std::string path);
    int convertToLogScale(double color);
    int calcCodedPacketValueFromRateBps(double rateBps);
	void PPV_Print_Stat (float tnow, long tb_d_new, float R_old, float R);
	void LogMarkerCTV (float tnow, float R, float ctv);
	void updateCTV ();
	

    // std::queue<Ptr<QueueDiscItem> > m_packets; //!< the items in the queue

    Ptr<UniformRandomVariable> rnd;
    //int packetSize;
    
	std::string NodeName;
  
    float R; // bytes/sec
    float R_old; // bytes/sec
    float tb_time; // token bucket size in sec
    long tb_d; // bytes in token bucket
    long tb_dmax; // max bytes in token bucket 
    float alpha;
    uint32_t mode; // 1 - apply selective PPOV once; else - selective PPOV session for tb_time
    float tlast; // time in sec
    uint32_t tb_target; // target token packet level in bytes
	uint8_t dclass;
	uint32_t tb_d_extra;		//beta parameter in update
	float t_tagtime;
	float lastTagtime;
	int ctv;
	float lastUpdateCTV;
	float updateCTVTime;
	float lower_percentile;
	float upper_percentile;
	
    std::string PpovPointsFile; // name of the file containing the ppov curve

    bool initialized;
    //            thr    ppv
    std::vector< std::pair<float, float> > ppov;
	
	std::vector<float> TVFinverz;
  
  
};

} // namespace ns3

#endif /* PPV_MARKER_QUEUE_DISC_H */
