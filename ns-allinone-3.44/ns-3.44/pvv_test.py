#!/usr/bin/env python3
from ns.traffic_control import PpvDistributedMarkerQueueDisc

def main():
    # Példányosítsuk az osztályt
    marker = PpvDistributedMarkerQueueDisc()
    
    # (Opcionális) Állítsuk be az attribútumokat, például a "Name" attribútumot
    marker.SetAttribute("Name", "TestNode")
    
    # Hívjuk meg a getName() metódust, hogy ellenõrizzük, mûködik-e
    node_name = marker.getName()
    print("A node neve:", node_name)

if __name__ == "__main__":
    main()