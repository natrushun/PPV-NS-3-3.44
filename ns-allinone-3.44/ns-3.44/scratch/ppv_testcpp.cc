#include "ns3/core-module.h"
#include "ns3/traffic-control-module.h"

using namespace ns3;

NS_LOG_COMPONENT_DEFINE("PpvDistributedMarkerQueueDiscTest");

int main(int argc, char *argv[]) {
    LogComponentEnable("PpvDistributedMarkerQueueDiscTest", LOG_LEVEL_INFO);

    CommandLine cmd;
    cmd.Parse(argc, argv);

    Ptr<PpvDistributedMarkerQueueDisc> marker = CreateObject<PpvDistributedMarkerQueueDisc>();

    marker->SetAttribute("Name", StringValue("TestNode"));

    StringValue nodeName;
    marker->GetAttribute("Name", nodeName);

    NS_LOG_INFO("A node neve: " << nodeName.Get());

    return 0;
}
