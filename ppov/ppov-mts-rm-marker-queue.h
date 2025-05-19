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

#ifndef PpovMtsRmMarkerQueue_H
#define PpovMtsRmMarkerQueue_H

#include <queue>
#include <set>
#include <utility>
#include <vector>

#include "ns3/packet.h"
#include "ns3/queue.h"
#include "ns3/random-variable-stream.h"
#include "ns3/simulator.h"
#include "ns3/stats-module.h"
#include "ns3/token-bucket.h"
#include "ns3/ppov-rate-measurement.h"



namespace ns3 {

/**
 * \ingroup queue
 *
 * \brief A FIFO packet queue that drops tail-end packets on overflow
 */
class PpovMtsRmMarkerQueue : public Queue
{
  public:
    /**
     * \brief Get the type ID.
     * \return the object TypeId
     */
    static TypeId GetTypeId (void);
    /**
     * \brief PpovBucketMarkerQueue Constructor
     *
     * Creates a droptail queue with a maximum size of 100 packets by default
     */
    void set_id(int id);
    PpovMtsRmMarkerQueue ();

    virtual ~PpovMtsRmMarkerQueue();

  protected:
    virtual bool DoEnqueue (Ptr<QueueItem> item);
    virtual Ptr<QueueItem> DoDequeue (void);
    virtual Ptr<const QueueItem> DoPeek (void) const;

    bool ReadPpovFromFile(std::string path);
	
	void setConfig ();
	float getRvesszo(int i,Ptr<Packet> p);
	RateMeasurementAbstract* getRateMeasurementObject(float ts, std::string name);

	float getRateMeasurmentRate (int i, Ptr<Packet> p);
	void updateRateMeasurments (Ptr<Packet> p);
	float delta (int i, Ptr<Packet> p);
	int get_pv(float r,Ptr<Packet> p);


    std::queue<Ptr<QueueItem> > m_packets; //!< the items in the queue

    Ptr<UniformRandomVariable> rnd;

	uint8_t dclass;
	uint8_t bitRateAvg;
	float ts1,ts2,ts3,ts4;
	float alpha1,alpha2,alpha3,alpha4;

    std::string PpovPointsFile; // name of the file containing the ppov curve

    bool initialized;
    //            thr    ppv
    std::vector< std::pair<float, float> > ppov;

    std::vector< RateMeasurementAbstract*> rateMeasurements;
    std::vector< float> alpha;
};

} // namespace ns3

#endif /* PpovMtsRmMarkerQueue_H */
