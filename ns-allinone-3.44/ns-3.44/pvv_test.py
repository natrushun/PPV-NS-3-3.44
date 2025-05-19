#!/usr/bin/env python3
from ns.traffic_control import PpvDistributedMarkerQueueDisc

def main():
    # P�ld�nyos�tsuk az oszt�lyt
    marker = PpvDistributedMarkerQueueDisc()
    
    # (Opcion�lis) �ll�tsuk be az attrib�tumokat, p�ld�ul a "Name" attrib�tumot
    marker.SetAttribute("Name", "TestNode")
    
    # H�vjuk meg a getName() met�dust, hogy ellen�rizz�k, m�k�dik-e
    node_name = marker.getName()
    print("A node neve:", node_name)

if __name__ == "__main__":
    main()