/*
 * This tag combines position, velocity, and acceleration in one tag.
 */

#ifndef CUSTOM_DATA_TAG_H
#define CUSTOM_DATA_TAG_H

#include "ns3/tag.h"
#include "ns3/vector.h"
#include "ns3/nstime.h"
#include "ns3/ppv-marker-queue-disc.h"

namespace ns3
{
	/** We're creating a custom tag for simulation. A tag can be added to any packet, but you cannot add a tag of the same type twice.
	*/
class CustomDataTag : public Tag {
public:

	//Functions inherited from ns3::Tag that you have to implement. 
	static TypeId GetTypeId(void);
	virtual TypeId GetInstanceTypeId(void) const;
	virtual uint32_t GetSerializedSize(void) const;
	virtual void Serialize (TagBuffer i) const;
	virtual void Deserialize (TagBuffer i);
	virtual void Print (std::ostream & os) const;

	//These are custom accessor & mutator functions
	PpvMarkerQueueDisc* getMarkerNode(void);
	void setMarkerNode(PpvMarkerQueueDisc* mn);

	CustomDataTag();
	CustomDataTag(PpvMarkerQueueDisc* markerN);
	virtual ~CustomDataTag();
private:

	PpvMarkerQueueDisc* markerNode;
};
}

#endif 