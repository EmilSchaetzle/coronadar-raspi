#!/usr/bin/python

from scapy.all import *
from threading import Timer
from Buffer import Buffer
from Poster import post


NAME = 'WIFI Device Reporter'
DESCRIPTION = "a tool for counting devices in the area and submitting to coronadar"

def build_packet_callback():
    def packet_callback(packet):
        if not packet.haslayer(Dot11) and not packet.haslayer(Dot11FCS):
            return
        # we are looking for management frames with a probe subtype
        # if neither match we are done here
        if packet.type != 0 or packet.subtype != 0x04:
            return

        global macs
        macs.add(packet.addr2)

    return packet_callback
    
def begin_update(lon, lat):
    global macs
    def update():
        while True:
            post(lon, lat, len(macs.request(62)))
            macs.clear(300)
            time.sleep(60)
    timer = Timer(60, update)
    timer.daemon = True
    timer.start()
    
def main():
    global macs
    lat = 48.001677434323233432424
    lon = 10.001677434323233432424
    macs = Buffer()
    built_packet_cb = build_packet_callback()
    begin_update(lon, lat)
    sniff(iface="wlan0mon", prn=built_packet_cb, store=0)    
    

if __name__ == '__main__':
    main()
