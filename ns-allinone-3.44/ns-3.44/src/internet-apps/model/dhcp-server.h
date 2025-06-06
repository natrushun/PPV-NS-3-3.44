/*
 * Copyright (c) 2011 UPB
 * Copyright (c) 2017 NITK Surathkal
 *
 * SPDX-License-Identifier: GPL-2.0-only
 *
 * Author: Radu Lupu <rlupu@elcom.pub.ro>
 *         Ankit Deepak <adadeepak8@gmail.com>
 *         Deepti Rajagopal <deeptir96@gmail.com>
 *
 */

#ifndef DHCP_SERVER_H
#define DHCP_SERVER_H

#include "dhcp-header.h"

#include "ns3/application.h"
#include "ns3/ipv4-address.h"

#include <map>

namespace ns3
{

class InetSocketAddress;
class Socket;
class Packet;

/**
 * @ingroup dhcp
 *
 * @class DhcpServer
 * @brief Implements the functionality of a DHCP server
 */
class DhcpServer : public Application
{
  public:
    /**
     * @brief Get the type ID.
     * @return the object TypeId
     */
    static TypeId GetTypeId();

    DhcpServer();
    ~DhcpServer() override;

    /**
     * @brief Add a static entry to the pool.
     *
     * @param chaddr The client chaddr.
     * @param addr The address to handle to the client.
     */
    void AddStaticDhcpEntry(Address chaddr, Ipv4Address addr);

  protected:
    void DoDispose() override;

  private:
    void StartApplication() override;
    void StopApplication() override;

    static const int PORT = 67; //!< Port number of DHCP server

    /**
     * @brief Handles incoming packets from the network
     * @param socket Socket bound to port 67 of the DHCP server
     */
    void NetHandler(Ptr<Socket> socket);

    /**
     * @brief Sends DHCP offer after receiving DHCP Discover
     * @param iDev incoming NetDevice
     * @param header DHCP header of the received message
     * @param from Address of the DHCP client
     */
    void SendOffer(Ptr<NetDevice> iDev, DhcpHeader header, InetSocketAddress from);

    /**
     * @brief Sends DHCP ACK (or NACK) after receiving Request
     * @param iDev incoming NetDevice
     * @param header DHCP header of the received message
     * @param from Address of the DHCP client
     */
    void SendAck(Ptr<NetDevice> iDev, DhcpHeader header, InetSocketAddress from);

    /**
     * @brief Modifies the remaining lease time of addresses
     */
    void TimerHandler();

    Ptr<Socket> m_socket;      //!< The socket bound to port 67
    Ipv4Address m_poolAddress; //!< The network address available to the server
    Ipv4Address m_minAddress;  //!< The first address in the address pool
    Ipv4Address m_maxAddress;  //!< The last address in the address pool
    Ipv4Mask m_poolMask;       //!< The network mask of the pool
    Ipv4Address m_gateway;     //!< The gateway address

    /// Leased address container - chaddr + IP addr / lease time
    typedef std::map<Address, std::pair<Ipv4Address, uint32_t>> LeasedAddress;
    /// Leased address iterator - chaddr + IP addr / lease time
    typedef std::map<Address, std::pair<Ipv4Address, uint32_t>>::iterator LeasedAddressIter;
    /// Leased address const iterator - chaddr + IP addr / lease time
    typedef std::map<Address, std::pair<Ipv4Address, uint32_t>>::const_iterator LeasedAddressCIter;

    /// Expired address container - chaddr
    typedef std::list<Address> ExpiredAddress;
    /// Expired address iterator - chaddr
    typedef std::list<Address>::iterator ExpiredAddressIter;
    /// Expired address const iterator - chaddr
    typedef std::list<Address>::const_iterator ExpiredAddressCIter;

    /// Available address container - IP addr
    typedef std::list<Ipv4Address> AvailableAddress;

    LeasedAddress m_leasedAddresses;   //!< Leased address and their status (cache memory)
    ExpiredAddress m_expiredAddresses; //!< Expired addresses to be reused (chaddr of the clients)
    AvailableAddress m_availableAddresses; //!< Available addresses to be used (IP addresses)
    Time m_lease;                          //!< The granted lease time for an address
    Time m_renew;                          //!< The renewal time for an address
    Time m_rebind;                         //!< The rebinding time for an address
    EventId m_expiredEvent;                //!< The Event to trigger TimerHandler
};

} // namespace ns3

#endif /* DHCP_SERVER_H */
