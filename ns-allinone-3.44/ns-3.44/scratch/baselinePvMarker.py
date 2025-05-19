# /*
#  * This program is free software; you can redistribute it and/or modify
#  * it under the terms of the GNU General Public License version 2 as
#  * published by the Free Software Foundation;
#  *
#  * This program is distributed in the hope that it will be useful,
#  * but WITHOUT ANY WARRANTY; without even the implied warranty of
#  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  * GNU General Public License for more details.
#  *
#  * You should have received a copy of the GNU General Public License
#  * along with this program; if not, write to the Free Software
#  * Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#  */


from ns import ns
import configparser
# import netppv


import sys
import os
import glob
import random

# from plotting import plot,createPlotFlows

conf = configparser.ConfigParser()
conf.read("scratch/config.conf")

random.seed(conf['DEFAULT']['rndSeed'])
tcpType = conf['DEFAULT']['tcpFactory']
tcpBufferMulti = int(conf['DEFAULT']['tcpBufferMultiplicator'])
packet_size = int(conf['DEFAULT']['PacketSize'])


# ns.Config.SetDefault("ns3::TcpSocket::SegmentSize", ns.UintegerValue (1460))
ns.Config.SetDefault("ns3::TcpSocket::SegmentSize", ns.UintegerValue (packet_size))
ns.Config.SetDefault("ns3::TcpSocket::SndBufSize", ns.UintegerValue (131072*tcpBufferMulti))
# ns.Config.SetDefault("ns3::TcpSocket::SndBufSize", ns.UintegerValue (1400))
ns.Config.SetDefault("ns3::TcpSocket::RcvBufSize", ns.UintegerValue (131072*tcpBufferMulti))
# ns.Config.SetDefault("ns3::TcpSocket::RcvBufSize", ns.UintegerValue (1400))
# ns.Config.SetDefault("ns3::TcpSocketBase::Sack", ns.BooleanValue (True))
#ns.Config.SetDefault("ns3::TcpL4Protocol::SocketType", ns.StringValue ("ns3::TcpBic"))
# ns.Config.SetDefault ("ns3::TcpL4Protocol::SocketType", ns.TypeIdValue (ns.TcpBic.GetTypeId ()));
#ns.Config.SetDefault ("ns3::TcpL4Protocol::SocketType", ns.TypeIdValue (ns.TcpNewReno.GetTypeId ()));
ns.Config.SetDefault ("ns3::TcpSocket::DelAckCount", ns.UintegerValue (1));
ns.GlobalValue.Bind("ChecksumEnabled", ns.BooleanValue(False))
#GlobalValue::Bind ("ChecksumEnabled", BooleanValue (false));
# ns.Config.SetDefault ("ns3::TcpSocketBase::UseEcn", ns.StringValue ("Off"))


if "newreno" == tcpType:
	print("TCP: NewReno")
	ns.Config.SetDefault ("ns3::TcpL4Protocol::SocketType", ns.TypeIdValue (ns.TcpNewReno.GetTypeId ()))
	ns.Config.SetDefault ("ns3::TcpSocketBase::UseEcn", ns.StringValue ("Off"))
elif "dctcp" == tcpType:
	#https://www.nsnam.org/docs/release/3.31/models/html/tcp.html#data-center-tcp-dctcp
	#The ECN is enabled automatically when DCTCP is used, even if the user has not explicitly enabled it.
	print("TCP: DCTCP")
	ns.Config.SetDefault ("ns3::TcpL4Protocol::SocketType", ns.TypeIdValue (ns.TcpDctcp.GetTypeId ()))
	ns.Config.SetDefault ("ns3::TcpSocketBase::UseEcn", ns.StringValue ("On"))
	ns.Config.SetDefault ("ns3::TcpSocketState::EnablePacing", ns.BooleanValue (True));
else:
	print("UNKOWN TCP TYPE",tcpType)
	X = 1 / 0


try:
	os.mkdir('log')
except:
	pass

files = glob.glob('log/*')
for f in files:
	os.remove(f)
	
def printIpToFile(ip,name):
	mode = 'a' if os.path.exists("log/ips.txt") else 'w'
	with open("log/ips.txt",mode) as f:
		f.write(str(ip)+" "+str(name)+"\n")
		
def printFlows(src_label,client_intf,dst_label,server_intf,tvf_file):
	print(src_label,client_intf,"-->",dst_label,server_intf)
	mode = 'a' if os.path.exists("log/flows.txt") else 'w'
	with open("log/flows.txt",mode) as f:
		f.write(str(client_intf)+"-"+str(server_intf)+" "+tvf_file+"\n")

nodes = ns.NodeContainer()
nodes.Create(4)

'''
  0
	\
		2 -- 3
	/
  1
'''

stack = ns.InternetStackHelper()
stack.Install(nodes)

pointToPoint = ns.PointToPointHelper()
# pointToPoint.SetDeviceAttribute("DataRate", ns.StringValue(conf['DEFAULT']['baseBW']))
pointToPoint.SetDeviceAttribute("DataRate", ns.StringValue(conf['DEFAULT']['baseBW']))
# pointToPoint.SetQueue ("ns3::DropTailQueue", "MaxSize", ns.StringValue ("1000p"));

labelIdMap={}
edges = []
devices = []

rtt = 5.0
		
pointToPoint.SetChannelAttribute("Delay", ns.StringValue(str(float(rtt/2.0))+"ms"))

for src,dst in [(0,2),(1,2),(2,3)]:
	nc = ns.NodeContainer()
	nc.Add(nodes.Get(src))
	nc.Add(nodes.Get(dst))
	dev = pointToPoint.Install(nc)
	edges.append(nc)
	devices.append(dev)

	
	# forward
	ppvSchedQueueDisc = ns.TrafficControlHelper()
	ppvSchedQueueDisc.SetRootQueueDisc("ns3::PpvSchedulerQueueDisc","Name",ns.StringValue (str(src) +"-"+str(dst)),
	"MaxSizeForLimit",ns.StringValue (conf['DEFAULT']['schedQueueDiscSize']))
	qdiscCont = ppvSchedQueueDisc.Install(dev.Get(0))
	
	# backward
	ppvSchedQueueDisc = ns.TrafficControlHelper()
	ppvSchedQueueDisc.SetRootQueueDisc("ns3::PpvSchedulerQueueDisc", "Name",ns.StringValue (str(dst) +"-"+str(src)),
	"MaxSizeForLimit",ns.StringValue (conf['DEFAULT']['schedQueueDiscSize']))
	qdiscCont = ppvSchedQueueDisc.Install(dev.Get(1))
	

i = 1
interfaces = []


# internet stackhelper utan kell, de az ip kiosztas elott
address = ns.Ipv4AddressHelper()


for d in devices:
	ip1 = str(int(i / 254)+1)
	ip2 = str(int(i % 254)+1)

	address.SetBase(ns.Ipv4Address("10."+ip1+"."+ip2+".0"),
				ns.Ipv4Mask("255.255.255.0"))
	intf = address.Assign(d)
	interfaces.append(intf)
	i += 1
	
#dynamic sceanrio
# U1-U4 id0-3, M1-M3 id4-7, B1-B4 id8-11
#- Dctcp U1-G->U4 (1flow a tobbi 10flow) 10s- U2-S->U3,  20s- B1-G->B2, 30s B3-G->B4, lakpcsolni 40 B1B2, 50 B3B4, 60 U2U3 --70
flowsStatic = [
	{'src':0,'dst':3,'color':'G','start':1.0,'stop':20.0,'flownum':1,'operator':'OP1'},
	{'src':0,'dst':3,'color':'G','start':1.0,'stop':20.0,'flownum':1,'operator':'OP2'},
	{'src':1,'dst':3,'color':'G','start':1.0,'stop':20.0,'flownum':1,'operator':'OP2'},

]
flowsDynamic = [
	#1-1-1-1
	{'src':0,'dst':3,'color':'G','start':1.0,'stop':65.0,'flownum':1,'operator':'OP1'},
	{'src':0,'dst':3,'color':'G','start':1.0,'stop':65.0,'flownum':1,'operator':'OP2'},
	{'src':1,'dst':3,'color':'G','start':1.0,'stop':65.0,'flownum':1,'operator':'OP1'},
	{'src':1,'dst':3,'color':'G','start':1.0,'stop':65.0,'flownum':1,'operator':'OP2'},
	#2-1-1-1 out 50
	{'src':0,'dst':3,'color':'G','start':10.0,'stop':50.0,'flownum':1,'operator':'OP1'},
	#2-1-2-1 out:40
	{'src':1,'dst':3,'color':'G','start':20.0,'stop':40.0,'flownum':1,'operator':'OP1'},
	#2-1-2-4
	{'src':1,'dst':3,'color':'G','start':30.0,'stop':60.0,'flownum':1,'operator':'OP2'},
	{'src':1,'dst':3,'color':'G','start':30.0,'stop':60.0,'flownum':1,'operator':'OP2'},
	{'src':1,'dst':3,'color':'G','start':30.0,'stop':60.0,'flownum':1,'operator':'OP2'},

]

# flows = flowsDynamic
flows = flowsStatic


appInstalledNode = []

group_id =1
for fl_i in flows:
	flownum = fl_i['flownum']
	tvf_file = conf['Source1']['PpovPointsFile'] if fl_i['color'] == 'G' else conf['Source2']['PpovPointsFile']
	send_rate = conf['Source1']['SendingDataRate'] if fl_i['color'] == 'G' else conf['Source2']['SendingDataRate']
	tvf_shortName = tvf_file.split(".")[0].split("/")[-1]
	nTcp = int(conf['DEFAULT']['nTCP'])
	
	if nTcp == 0:
		continue
	
	for i in range(flownum):
		random_src = fl_i['src']
		random_dst = fl_i['dst']
	
		#create sender / receiver
		#sender az elso el elso nodejara bekotve
		# receiver utolso el masodik nodejara
		pointToPoint.SetChannelAttribute("Delay", ns.StringValue("1ms"))
		pointToPoint.SetDeviceAttribute("DataRate", ns.StringValue("100Gbps"))

		nodesSendRecv = ns.NodeContainer()
		nodesSendRecv.Create(2)
		stack.Install(nodesSendRecv)

		senderNc = ns.NodeContainer()
		senderNc.Add(nodesSendRecv.Get(0))
		senderNc.Add(nodes.Get(random_src))	# itt kell meg hogy melyik node kell nekem
		senderDev = pointToPoint.Install(senderNc)

		recvNc = ns.NodeContainer()
		recvNc.Add(nodes.Get(random_dst))
		recvNc.Add(nodesSendRecv.Get(1))
		recvDev = pointToPoint.Install(recvNc)

		ppvMarkerQueueDisc = ns.TrafficControlHelper()
		# ppvMarkerQueueDisc.SetRootQueueDisc("ns3::PpvDistributedMarkerQueueDisc","PpovPointsFile",ns.StringValue (tvf_file), "Name",ns.StringValue (str(random_src)+"-"+str(group_id)+"-"+fl_i['operator']),"Operator",ns.StringValue (fl_i['operator']) )
		
		ppvMarkerQueueDisc.SetRootQueueDisc("ns3::PpvMarkerQueueDisc","PpovPointsFile",ns.StringValue (tvf_file), "Name",ns.StringValue (str(random_src)+"-"+str(group_id)+"-"+fl_i['operator']), "AddTagTime", ns.DoubleValue(65.0) )  #0.005 - fojtas, simTime - nincs fojtas
		
		# itt a routing miatt nem feltetlen arra megy a csomag amerre gondoltuk
		qdiscContainer = ppvMarkerQueueDisc.Install(senderDev.Get(0))

		#sender recv ip assign
		address.SetBase(ns.Ipv4Address("11."+str(int(group_id/254))+"."+str(int(group_id%254))+".0"),
						ns.Ipv4Mask("255.255.255.0"))
		sender_intf = address.Assign(senderDev)

		address.SetBase(ns.Ipv4Address("11."+str(int(group_id/254))+"."+str(int(group_id+1%254))+".0"),
						ns.Ipv4Mask("255.255.255.0"))
		recv_intf = address.Assign(recvDev)


		client = senderNc.Get(0)

		client_intf = sender_intf.GetAddress(0)
		server_intf = recv_intf.GetAddress(1)
		
		# printIpToFile(client_intf,labelIdMap[random_src]) #  conf[group]['srcNodeLabel'])
		# printIpToFile(server_intf,labelIdMap[random_dst]) #conf[group]['dstNodeLabel'])
		# printFlows(labelIdMap[random_src],client_intf,labelIdMap[random_dst],server_intf,tvf_file)
		# http://www.lrc.ic.unicamp.br/ofswitch13/ns-3.25/src/flow-monitor/examples/wifi-olsr-flowmon.py

		port = 9 + group_id
		socketFactory = "ns3::TcpSocketFactory"

		print(server_intf)
		print(type(server_intf))
		
		addr = ns.InetSocketAddress(server_intf, port)
		print(type(addr))
		wrapped = ns.Address(addr)
		sender = ns.OnOffHelper(socketFactory, wrapped)
		sender = ns.OnOffHelper(socketFactory, ns.Address(addr))

		sender.SetConstantRate (ns.DataRate (send_rate), packet_size);
		# sender.SetAttribute("MaxBytes", ns.UintegerValue(0))
		# sender.SetAttribute("DataRate", ns.DataRateValue(ns.DataRate(conf[group]['SendingDataRate'])))
		# sender.SetAttribute("PacketSize", ns.UintegerValue (int(conf[group]['PacketSize'])))
		startTime = 1.0
		for xx in range(nTcp):
			startTime = fl_i['start'] + random.random()

			senderApps = sender.Install(client)
			senderApps.Start(ns.Seconds(startTime))
			senderApps.Stop(ns.Seconds(float(fl_i['stop'])-2.0))


		server = recvNc.Get(1)
		sink = ns.PacketSinkHelper(socketFactory,ns.Address (ns.InetSocketAddress (ns.Ipv4Address.GetAny(), port)))
		# sink.SetAttribute("Name",ns.StringValue(str(client_intf)+"-"+str(server_intf)+"_"+tvf_shortName))  #conf[group]['dstNodeLabel']))
		sink.SetAttribute("Name",ns.StringValue(str(random_src)+"-"+fl_i['operator']))
		sinkApps = sink.Install(server)
		sinkApps.Start(ns.Seconds(startTime-1.0))
		sinkApps.Stop(ns.Seconds(float(fl_i['stop'])-1.0))
		group_id += 2

ns.Ipv4GlobalRoutingHelper.PopulateRoutingTables()

ns.Simulator.Stop(ns.Seconds(float(conf['DEFAULT']['simTime'])))
ns.Simulator.Run()
ns.Simulator.Destroy()

sys.argv = [sys.argv[0]]

#disbale plotting, mert rossz a parameterezes, a sys.argv-t ki kellene kapcsolni!
# if True:
	# createPlotFlows()
	# netppv.run('/log/')
	# plot()
