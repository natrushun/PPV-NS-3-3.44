/*
 * Copyright (c) 2020 Universita' di Firenze, Italy
 *
 * SPDX-License-Identifier: GPL-2.0-only
 *
 * Author: Tommaso Pecorella <tommaso.pecorella@unifi.it>
 */

#include "bit-deserializer.h"

#include "ns3/abort.h"
#include "ns3/log.h"

#include <iostream>

namespace ns3
{

NS_LOG_COMPONENT_DEFINE("BitDeserializer");

BitDeserializer::BitDeserializer()
{
    NS_LOG_FUNCTION(this);
    m_deserializing = false;
}

void
BitDeserializer::PushBytes(std::vector<uint8_t> bytes)
{
    NS_LOG_FUNCTION(this << bytes);
    NS_ABORT_MSG_IF(m_deserializing, "Can't add bytes after deserialization started");
    m_bytesBlob.insert(m_bytesBlob.end(), bytes.begin(), bytes.end());
}

void
BitDeserializer::PushBytes(uint8_t* bytes, uint32_t size)
{
    NS_LOG_FUNCTION(this << bytes << size);
    NS_ABORT_MSG_IF(m_deserializing, "Can't add bytes after deserialization started");
    for (uint32_t index = 0; index < size; index++)
    {
        m_bytesBlob.push_back(bytes[index]);
    }
}

void
BitDeserializer::PushByte(uint8_t byte)
{
    NS_LOG_FUNCTION(this << +byte);
    NS_ABORT_MSG_IF(m_deserializing, "Can't add bytes after deserialization started");
    m_bytesBlob.push_back(byte);
}

uint64_t
BitDeserializer::GetBits(uint8_t size)
{
    NS_LOG_FUNCTION(this << +size);
    uint8_t result = 0;
    PrepareDeserialization();

    NS_ABORT_MSG_IF(size > 64, "Number of requested bits exceeds 64");
    NS_ABORT_MSG_IF(size > m_blob.size(), "Number of requested bits exceeds blob size");

    for (uint8_t i = 0; i < size; i++)
    {
        result <<= 1;
        result |= m_blob.front();
        m_blob.pop_front();
    }
    return result;
}

void
BitDeserializer::PrepareDeserialization()
{
    NS_LOG_FUNCTION(this);
    if (!m_deserializing)
    {
        m_deserializing = true;
        for (auto index = m_bytesBlob.begin(); index != m_bytesBlob.end(); index++)
        {
            m_blob.push_back(*index & 0x80);
            m_blob.push_back(*index & 0x40);
            m_blob.push_back(*index & 0x20);
            m_blob.push_back(*index & 0x10);
            m_blob.push_back(*index & 0x8);
            m_blob.push_back(*index & 0x4);
            m_blob.push_back(*index & 0x2);
            m_blob.push_back(*index & 0x1);
        }
    }
}

} // namespace ns3
