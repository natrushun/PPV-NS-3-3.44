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

#ifndef PpovMultiscaleBucketMarkerQueue_H
#define PpovMultiscaleBucketMarkerQueue_H

#include <queue>
#include "ns3/queue.h"
#include "ns3/simulator.h"
#include <vector>
#include "ns3/stats-module.h"
#include "ns3/packet.h"
#include "ns3/token-bucket.h"
#include "ns3/random-variable-stream.h"
#include "ppov-bucket-marker-queue.h"

namespace ns3 {

/**
 * \ingroup queue
 *
 * \brief A FIFO packet queue that drops tail-end packets on overflow
 */
class PpovMultiscaleBucketMarkerQueue : public PpovBucketMarkerQueue
{
public:
  /**
   * \brief Get the type ID.
   * \return the object TypeId
   */
  static TypeId GetTypeId (void);
  /**
   * \brief PpovMultiscaleBucketMarkerQueue Constructor
   *
   * Creates a droptail queue with a maximum size of 100 packets by default
   */
//  void set_id(int id);
  PpovMultiscaleBucketMarkerQueue ();
  std::string markerFunctionPoints;
  bool initialized;
  void InitBucketsFromFile();
  // std::vector<int> ReadMarkerValues();

  virtual ~PpovMultiscaleBucketMarkerQueue();

private:
  float getColor(Ptr<Packet> p);
  float getColor_old(Ptr<Packet> p);
  //std::queue<Ptr<QueueItem> > m_packets; //!< the items in the queue
  std::vector<int> bucketColorValues;
  float bucketLenSec; // token bucket size in sec
             // thr    ppv
  // std::vector< std::pair<float, float> > ppov;
  
  std::vector< std::vector<TokenBucket> > buckets;
  std::vector< std::vector<float> > timescaleThr;
  int getNPvs();
  Ptr<UniformRandomVariable> rnd;



};

} // namespace ns3

#endif /* DROPTAIL_H */
