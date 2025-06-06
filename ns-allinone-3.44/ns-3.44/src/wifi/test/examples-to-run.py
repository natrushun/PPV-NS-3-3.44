#! /usr/bin/env python3

# A list of C++ examples to run in order to ensure that they remain
# buildable and runnable over time.  Each tuple in the list contains
#
#     (example_name, do_run, do_valgrind_run).
#
# See test.py for more information.
cpp_examples = [
    ("wifi-phy-configuration --testCase=0", "True", "True"),
    ("wifi-phy-configuration --testCase=1", "True", "False"),
    ("wifi-phy-configuration --testCase=2", "True", "False"),
    ("wifi-phy-configuration --testCase=3", "True", "False"),
    ("wifi-phy-configuration --testCase=4", "True", "False"),
    ("wifi-phy-configuration --testCase=5", "True", "False"),
    ("wifi-phy-configuration --testCase=6", "True", "False"),
    ("wifi-phy-configuration --testCase=7", "True", "False"),
    ("wifi-phy-configuration --testCase=8", "True", "False"),
    ("wifi-phy-configuration --testCase=9", "True", "False"),
    ("wifi-phy-configuration --testCase=10", "True", "False"),
    ("wifi-phy-configuration --testCase=11", "True", "False"),
    ("wifi-phy-configuration --testCase=12", "True", "False"),
    ("wifi-phy-configuration --testCase=13", "True", "False"),
    ("wifi-phy-configuration --testCase=14", "True", "False"),
    ("wifi-phy-configuration --testCase=15", "True", "False"),
    ("wifi-phy-configuration --testCase=16", "True", "False"),
    ("wifi-phy-configuration --testCase=17", "True", "False"),
    ("wifi-phy-configuration --testCase=18", "True", "False"),
    ("wifi-phy-configuration --testCase=19", "True", "False"),
    ("wifi-phy-configuration --testCase=20", "True", "False"),
    ("wifi-manager-example --wifiManager=Aarf --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Aarf --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Aarf --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Aarf --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Aarf --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Aarf --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Aarf --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Aarfcd --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11g --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Aarfcd --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Amrr --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Amrr --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Amrr --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Amrr --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Amrr --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Amrr --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Amrr --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Arf --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Arf --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Arf --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Arf --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Arf --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Arf --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Arf --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Cara --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Cara --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Cara --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Cara --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Cara --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Cara --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Cara --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Onoe --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Onoe --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Onoe --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Onoe --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Onoe --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Onoe --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Onoe --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Rraa --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Rraa --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Rraa --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Rraa --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Rraa --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Rraa --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Rraa --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11a --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11a --rtsThreshold=0 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11a --maxRetryCount=1 --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11g --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Minstrel --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11a --stepTime=0.1",
        "True",
        "True",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11g --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Ideal --standard=802.11a --stepTime=0.1", "True", "True"),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11b --serverChannelWidth=22 --clientChannelWidth=22 --stepTime=0.1",
        "True",
        "False",
    ),
    ("wifi-manager-example --wifiManager=Ideal --standard=802.11g --stepTime=0.1", "True", "False"),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11p-10MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11p-5MHz --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11n-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ac --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=400 --clientShortGuardInterval=400 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=Ideal --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-5GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-2.4GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=1 --clientNss=1 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=2 --clientNss=2 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=3 --clientNss=3 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=20 --clientChannelWidth=20 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=40 --clientChannelWidth=40 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=80 --clientChannelWidth=80 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=800 --clientShortGuardInterval=800 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "False",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=1600 --clientShortGuardInterval=1600 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-manager-example --wifiManager=MinstrelHt --standard=802.11ax-6GHz --serverChannelWidth=160 --clientChannelWidth=160 --serverShortGuardInterval=3200 --clientShortGuardInterval=3200 --serverNss=4 --clientNss=4 --stepTime=0.1",
        "True",
        "False",
    ),
    (
        "wifi-test-interference-helper --enableCapture=0 --txPowerA=5 --txPowerB=15 --delay=10us --txModeA=OfdmRate6Mbps --txModeB=OfdmRate6Mbps --checkResults=1 --expectRxASuccessful=0 --expectRxBSuccessful=0",
        "True",
        "True",
    ),
    (
        "wifi-test-interference-helper --enableCapture=0 --txPowerA=5 --txPowerB=15  --delay=17us --standard=WIFI_PHY_STANDARD_80211ac --preamble=WIFI_PREAMBLE_VHT_SU --txModeA=VhtMcs0 --txModeB=VhtMcs0 --checkResults=1 --expectRxASuccessful=0 --expectRxBSuccessful=0",
        "True",
        "True",
    ),
    (
        "wifi-test-interference-helper --enableCapture=0 --txPowerA=5 --txPowerB=15  --delay=20us --standard=WIFI_PHY_STANDARD_80211ac --preamble=WIFI_PREAMBLE_VHT_SU --txModeA=VhtMcs0 --txModeB=VhtMcs0 --checkResults=1 --expectRxASuccessful=0 --expectRxBSuccessful=0",
        "True",
        "True",
    ),
    (
        "wifi-test-interference-helper --enableCapture=0 --txPowerA=5 --txPowerB=15  --delay=27us --standard=WIFI_PHY_STANDARD_80211ac --preamble=WIFI_PREAMBLE_VHT_SU --txModeA=VhtMcs0 --txModeB=VhtMcs0 --checkResults=1 --expectRxASuccessful=0 --expectRxBSuccessful=0",
        "True",
        "True",
    ),
    (
        "wifi-test-interference-helper --enableCapture=1 --txPowerA=5 --txPowerB=15 --delay=10us --txModeA=OfdmRate6Mbps --txModeB=OfdmRate6Mbps --checkResults=1 --expectRxASuccessful=0 --expectRxBSuccessful=1",
        "True",
        "False",
    ),
    (
        "wifi-bianchi --validate --phyMode=OfdmRate54Mbps --nMinStas=5 --nMaxStas=10 --duration=5",
        "False",
        "False",
    ),  # TODO: run from N=5 to N=50 for 100s (TAKES_FOREVER) when issue #170 is fixed
    (
        "wifi-bianchi --validate --phyMode=OfdmRate6Mbps --nMinStas=5 --nMaxStas=10 --duration=15",
        "True",
        "False",
    ),  # TODO: run from N=5 to N=50 for 400s (TAKES_FOREVER) when issue #170 is fixed
    (
        "wifi-bianchi --validate --phyMode=OfdmRate54Mbps --nMinStas=5 --nMaxStas=10 --duration=5 --infra",
        "False",
        "False",
    ),  # TODO: run from N=5 to N=50 for 100s (TAKES_FOREVER) when issue #170 is fixed
    (
        "wifi-bianchi --validate --phyMode=OfdmRate6Mbps --nMinStas=5 --nMaxStas=10 --duration=20 --infra",
        "False",
        "False",
    ),  # TODO: run from N=5 to N=50 for 600s (TAKES_FOREVER) when issue #170 is fixed
]

# A list of Python examples to run in order to ensure that they remain
# runnable over time.  Each tuple in the list contains
#
#     (example_name, do_run).
#
# See test.py for more information.
python_examples = []
