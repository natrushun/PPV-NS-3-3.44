from ns import ns

def main():

    ppvMarkerQueueDisc = ns.TrafficControlHelper()
    ppvMarkerQueueDisc.SetRootQueueDisc(
    "ns3::PpvMarkerQueueDisc",
    "PpovPointsFile",ns.StringValue ("testfile"), 
    "Name",ns.StringValue ("testName"),
    "AddTagTime", ns.DoubleValue(12) )
    
    #node_name = ns.StringValue()
    #devices = ns.NetDeviceContainer()  
    #queueDiscs = ppvMarkerQueueDisc.Install(devices)
  
    #queueDisc = queueDiscs.Get(0)
    
    #queueName = queueDisc.GetAttribute("Name")
    #print("Queue Disc Name:", queueName)
    
    #print("A node neve:", node_name)

if __name__ == "__main__":
    main()
