#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Determine a host's IP address given its MAC address and an IP address
range to scan for it.

I created this to discover a WLAN printer (which dynamically gets an IP
address assigned via DHCP) on the local network.

Calls Nmap_ to ping hosts and return their MAC addresses (requires root
privileges).

Requires Python_ 2.7+ or 3.3+.

.. _Nmap: http://nmap.org/
.. _Python: http://python.org/

:Copyright: 2014-2016 `Jochen Kupperschmidt
:Date: 27-Mar-2016 (original release: 25-Jan-2014)
:License: MIT
:Website: http://homework.nwsnet.de/releases/9577/#find-ip-address-for-mac-address
"""
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtCore import pyqtSlot
from PyQt4 import QtGui, QtCore
import subprocess
import xml.etree.ElementTree as ET
"""
print "Relaunching with root permissions"
applescript = ('do shell script "/Users/namikerdogan/nenra/dist/espressif.app/Contents/MacOS/espressif" '
                   'with administrator privileges')
exit_code = subprocess.call(['osascript', '-e', applescript])
sys.exit(exit_code)
"""


def main():
    app = QtGui.QApplication(sys.argv)

    w = QtGui.QMainWindow()
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle(ip_address)
    btn1 = QtGui.QPushButton(" AC KAPAT",w)
    btn1.resize(150,50)
    btn1.move(50,50)





    btn1.clicked.connect(buttonClicked)


    w.show()
    w.raise_()

    sys.exit(app.exec_())


def buttonClicked(self):
    global onof
    onof=onof+1
    import httplib
    h1 = httplib.HTTPConnection(ip_address)
    if  (divmod(onof,2))[1]:
        h1.request("GET", "/LED=OFF")

    else:
        h1.request("GET", "/LED=ON")


    h2 = h1.getresponse()
    print h2.read()
    print onof,(divmod(onof,2))[1]


def scan_for_hosts(ip_range):
    """Scan the given IP address range using Nmap and return the result
    in XML format.
    """
    nmap_args = ['nmap', '-n', '-sP', '-oX', '-', ip_range]
    return subprocess.check_output(nmap_args)


def find_ip_address_for_mac_address(xml, mac_address):
    """Parse Nmap's XML output, find the host element with the given
    MAC address, and return that host's IP address (or `None` if no
    match was found).
    """
    host_elems = ET.fromstring(xml).iter('host')
    host_elem = find_host_with_mac_address(host_elems, mac_address)
    if host_elem is not None:
        return find_ip_address(host_elem)


def find_host_with_mac_address(host_elems, mac_address):
    """Return the first host element that contains the MAC address."""
    for host_elem in host_elems:
        if host_has_mac_address(host_elem, mac_address):
            return host_elem


def host_has_mac_address(host_elem, wanted_mac_address):
    """Return true if the host has the given MAC address."""
    found_mac_address = find_mac_address(host_elem)
    return (
        found_mac_address is not None and
        found_mac_address.lower() == wanted_mac_address.lower()
    )


def find_mac_address(host_elem):
    """Return the host's MAC address."""
    return find_address_of_type(host_elem, 'mac')


def find_ip_address(host_elem):
    """Return the host's IP address."""
    return find_address_of_type(host_elem, 'ipv4')


def find_address_of_type(host_elem, type_):
    """Return the host's address of the given type, or `None` if there
    is no address element of that type.
    """
    address_elem = host_elem.find('./address[@addrtype="{}"]'.format(type_))
    if address_elem is not None:
        return address_elem.get('addr')


if __name__ == '__main__':
    mac_address = '18:FE:34:D5:21:16'
    ip_range = '192.168.1.1-255'
    onof = 0

    xml = scan_for_hosts(ip_range)
    print xml
    ip_address = find_ip_address_for_mac_address(xml, mac_address)
    main()

    if ip_address:
        print('Found IP address {} for MAC address {} in IP address range {}.'
              .format(ip_address, mac_address, ip_range))
    else:
        print('No IP address found for MAC address {} in IP address range {}.'
              .format(mac_address, ip_range))