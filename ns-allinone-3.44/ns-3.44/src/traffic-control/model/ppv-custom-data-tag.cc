/*
 * cacc-data-tag.cc
 *
 *  Created on: Oct 29, 2019
 *      Author: adil
 */
#include "ppv-custom-data-tag.h"
#include "ns3/log.h"
#include "ns3/simulator.h"

namespace ns3 {

NS_LOG_COMPONENT_DEFINE("CustomDataTag");
NS_OBJECT_ENSURE_REGISTERED (CustomDataTag);

CustomDataTag::CustomDataTag() {
	markerNode = NULL;
}
CustomDataTag::CustomDataTag(PpvMarkerQueueDisc* mn) {
	markerNode = mn;
}

CustomDataTag::~CustomDataTag() {
}

//Almost all custom tags will have similar implementation of GetTypeId and GetInstanceTypeId
TypeId CustomDataTag::GetTypeId (void)
{
  static TypeId tid = TypeId ("ns3::CustomDataTag")
    .SetParent<Tag> ()
    .AddConstructor<CustomDataTag> ();
  return tid;
}
TypeId CustomDataTag::GetInstanceTypeId (void) const
{
  return CustomDataTag::GetTypeId ();
}

uint32_t CustomDataTag::GetSerializedSize (void) const
{
	return sizeof(markerNode); //sizeof(Vector) + sizeof (ns3::Time) + sizeof(uint32_t);
}
/**
 * The order of how you do Serialize() should match the order of Deserialize()
 */
void CustomDataTag::Serialize (TagBuffer i) const
{
	i.Write((uint8_t*)&markerNode, sizeof(markerNode));

}
/** This function reads data from a buffer and store it in class's instance variables.
 */
void CustomDataTag::Deserialize (TagBuffer i)
{
	i.Read((uint8_t*)&markerNode, sizeof(PpvMarkerQueueDisc*));
	// std::cout<<" tag "<<markerNode->getName()<<std::endl;
}
/**
 * This function can be used with ASCII traces if enabled. 
 */
void CustomDataTag::Print (std::ostream &os) const
{
  os << "Custom Data --- Node ";
}

//Your accessor and mutator functions 
PpvMarkerQueueDisc* CustomDataTag::getMarkerNode() {
	return markerNode;
}

void CustomDataTag::setMarkerNode(PpvMarkerQueueDisc* mn) {
	markerNode = mn;
}

} /* namespace ns3 */

