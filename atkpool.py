#!/usr/bin/python
import os
import bot

bot.dp()
print"""
1: atk6-address6           18: atk6-fake_advertise6   35: atk6-flood_mldrouter6   52: atk6-node_query6
2: atk6-alive6             19: atk6-fake_dhcps6       36: atk6-flood_redir6       53: atk6-parasite6
3: atk6-covert_send6       20: atk6-fake_dns6d        37: atk6-flood_router26     54: atk6-passive_discovery6
4: atk6-covert_send6d      21: atk6-fake_dnsupdate6   38: atk6-flood_router6      55: atk6-randicmp6
5: atk6-denial6            22: atk6-fake_mipv6        39: atk6-flood_rs6          56: atk6-redir6
6: atk6-detect-new-ip6     23: atk6-fake_mld26        40: atk6-flood_solicitate6  57: atk6-redirsniff6
7: atk6-detect_sniffer6    24: atk6-fake_mld6         41: atk6-four2six           58: atk6-rsmurf6
8: atk6-dnsdict6           25: atk6-fake_mldrouter6   42: atk6-fragmentation6     59: atk6-sendpees6
9: atk6-dnsrevenum6        26: atk6-fake_pim6         43: atk6-fuzz_dhcps6        60: atk6-sendpeesmp6
10: atk6-dnssecwalk        27: atk6-fake_router26     44: atk6-fuzz_ip6           61: atk6-smurf6
11: atk6-dos_mld           28: atk6-fake_router6      45: atk6-implementation6    62: atk6-thcping6
12: atk6-dos-new-ip6       29: atk6-fake_solicitate6  46: atk6-implementation6d   63: atk6-thcsyn6
13: atk6-dump_dhcp6        30: atk6-firewall6         47: atk6-inject_alive6      64: atk6-toobig6
14: atk6-dump_router6      31: atk6-flood_advertise6  48: atk6-inverse_lookup6    65: atk6-trace6
15: atk6-exploit6          32: atk6-flood_dhcpc6      49: atk6-kill_router6
16: atk6-extract_hosts6    33: atk6-flood_mld26       50: atk6-ndpexhaust26
17: atk6-extract_networks6 34: atk6-flood_mld6        51: atk6-ndpexhaust6
"""
prog = raw_input("Which Program Would You Like To Use?\n atk6: ")
if prog == "1":
    bot.dp()
    print"""
atk6-address6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax:
	atk6-address6 mac-address [ipv6-prefix]
	atk6-address6 ipv4-address [ipv6-prefix]
	atk6-address6 ipv6-address

Converts a mac or IPv4 address to an IPv6 address (link local if no prefix is
given as 2nd option) or, when given an IPv6 address, prints the mac or IPv4
address. Prints all possible variations. Returns -1 on errors or the number of
variations found
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-address6 $opts")
elif prog == "2":
    bot.dp()
    print"""
atk6-alive6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-alive6 [-CMPSdlpv] [-I srcip6] [-i file] [-o file] [-e opt] [-s port,..] [-a port,..] [-u port,..] [-W TIME] interface [unicast-or-range-or-multicast-address]

Options:
  -i file    check systems from input file
  -o file    write results to output file
  -M         enumerate hardware addresses (MAC) from input addresses (slow!)
  -C         enumerate common address space from input addresses
  -4 ipv4/range    test various IPv4 address encodings per network (1.2.3.4/24)
  -p         send a ping packet for alive check (default)
  -e dst,hop send an errornous packets: destination (default), hop-by-hop
  -s port,port,..  TCP-SYN packet to ports for alive check or "portscan"
  -a port,port,..  TCP-ACK packet to ports for alive check
  -u port,port,..  UDP packet to ports for alive check
  -d         DNS resolve alive IPv6 addresses
  -n number  how often to send each packet (default: local 1, remote 2)
  -W time    time in ms to wait after sending a packet (default: 1)
  -S         slow mode, get best router for each remote target or when proxy-NA
  -I srcip6  use the specified IPv6 address as source
  -l         use link-local address instead of global address
  -P         only print addresses that would be scanned, no scanning
  -v         verbose (twice: detailed, thrice: dumping packets)

Target address on command line or in input file can include ranges in the form
of 2001:db8::1-fff or 2001:db8::1-2:0-ffff:0:0-ffff, etc.
Do not use the ranges (from-to) option with -M, -C or -4.
If you specify a remote router, fragmentation+srcroute is performed.
Returns -1 on errors, 0 if a system was found alive or 1 if nothing was found.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-alive6 $opts")
elif prog == "3":
    bot.dp()
    print"""
atk6-covert_send6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-covert_send6 [-m mtu] [-k key] [-s resend] interface target file [port]

Options:
  -m mtu     specifies the maximum MTU (default: interface MTU, min: 1000)
  -k key     encrypt the content with Blowfish-160
  -s resend  send each packet RESEND number of times, default: 1

Sends the content of FILE covertly to the target, And its POC - don't except
too much sophistication - its just put into the destination header.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-covert_send6 $opts")
elif prog == "4":
    bot.dp()
    print"""
atk6-covert_send6d v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-covert_send6d [-k key] interface file

Options:
  -k key     decrypt the content with Blowfish-160

Writes covertly received content to FILE.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-covert_send6d $opts")
elif prog == "5":
    bot.dp()
    print"""
atk6-denial6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-denial6 interface destination test-case-number

Performs various denial of service attacks on a target
If a system is vulnerable, it can crash or be under heavy load, so be careful!
If not test-case-number is supplied, the list of shown.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-denial6 $opts")
elif prog == "6":
    bot.dp()
    print"""
atk6-detect-new-ip6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-detect-new-ip6 interface [script]

This tools detects new IPv6 addresses joining the local network.
If script is supplied, it is executed with the detected IPv6 address as first
and the interface as second command line option.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-detect-new-ip6 $opts")
elif prog == "7":
    bot.dp()
    print"""
atk6-detect_sniffer6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-detect_sniffer6 interface [target6]

Tests if systems on the local LAN are sniffing.
Works against Windows, Linux, OS/X and *BSD
If no target is given, the link-local-all-nodes address is used, which
however not always works.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-detect_sniffer6 $opts")
elif prog == "8":
    bot.dp()
    print"""
atk6-dnsdict6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-dnsdict6 [-d4] [-s|-m|-l|-x|-u] [-t THREADS] [-D] domain [dictionary-file]

Enumerates a domain for DNS entries, it uses a dictionary file if supplied
or a built-in list otherwise. This tool is based on dnsmap by gnucitizen.org.

Options:
 -4      do also dump IPv4 addresses
 -t NO   specify the number of threads to use (default: 8, max: 32).
 -D      dump the selected built-in wordlist, no scanning.
 -d      display IPv6 information on NS and MX DNS domain information.
 -S      perform SRV service name guessing
 -[smlxu] choose the dictionary size by -s(mall=100), -m(edium=1419) (DEFAULT)
           -l(arge=2601), -x(treme=5886) or -u(ber=16724)
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dnsdict6 $opts")
elif prog == "9":
    bot.dp()
    print"""
atk6-dnsrevenum6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-dnsrevenum6 dns-server ipv6address

Performs a fast reverse DNS enumeration and is able to cope with slow servers.
Examples:
  atk6-dnsrevenum6 dns.test.com 2001:db8:42a8::/48
  atk6-dnsrevenum6 dns.test.com 8.a.2.4.8.b.d.0.1.0.0.2.ip6.arpa
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dnsrevenum6 $opts")
elif prog == "10":
    bot.dp()
    print"""
atk6-dnssecwalk v1.2 (c) 2013 by Marc Heuse <mh@mh-sec.de> http://www.mh-sec.de

Syntax: atk6-dnssecwalk [-e46] dns-server domain

Options:
 -e  ensure that the domain is present in found addresses, quit otherwise
 -4  resolve found entries to IPv4 addresses
 -6  resolve found entries to IPv6 addresses

Perform DNSSEC NSEC walking.

Example: atk6-dnssecwalk dns.test.com test.com
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dnssecwalk $opts")
elif prog == "11":
    bot.dp()
    print"""
Syntax: /usr/bin/atk6-dos_mld [-2] interface [target-link-local-address multicast-address]
If specified, the multicast address of the target will be dropped first.
All multicast traffic will cease after a while.
Specify -2 to use MLDv2.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dos_mld $opts")
elif prog == "12":
    bot.dp()
    print"""
atk6-dos-new-ip6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-dos-new-ip6 interface

This tools prevents new IPv6 interfaces to come up, by sending answers to
duplicate ip6 checks (DAD). This results in a DOS for new IPv6 devices.CCC
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dos-new-ip6 $opts")
elif prog == "13":
    bot.dp()
    print"""
atk6-dump_dhcp6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-dump_dhcp6 interface

DHCPv6 information tool. Dumps the available servers and their setup.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dump_dhcp6 $opts")
elif prog == "14":
    bot.dp()
    print"""
atk6-dump_router6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-dump_router6 interface [target]

Dumps all local routers and their information
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-dump_router6 $opts")
elif prog == "15":
    bot.dp()
    print"""
atk6-exploit6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-exploit6 interface destination [test-case-number]

Performs exploits of various CVE known IPv6 vulnerabilities on the destination
Note that for exploitable overflows only 'AAA...' strings are used.
If a system is vulnerable, it will crash, so be careful!
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-exploit6 $opts")
elif prog == "16":
    bot.dp()
    print"""
/usr/bin/atk6-extract_hosts6 FILE
prints the host parts of IPv6 addresses in FILE
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-extract_hosts6 $opts")
elif prog == "17":
    bot.dp()
    print"""
/usr/bin/atk6-extract_networks6 FILE
prints the networks found in FILE
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-extract_networks6 $opts")
elif prog == "18":
    bot.dp()
    print"""
atk6-fake_advertise6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_advertise6 [-DHF] [-Ors] [-n count] [-w seconds] interface ip-address-advertised [target-address [mac-address-advertised [source-ip-address]]]

Advertise IPv6 address on the network (with own mac if not specified),
sending it to the all-nodes multicast address if no target address is set.
Source ip address is the address advertised if not set.

Sending options:
  -n count    send how many packets (default: forever)
  -w seconds  wait time between the packets sent (default: 5)
Flag options:
  -O  do NOT set the override flag (default: on)
  -r  DO set the router flag (default: off)
  -s  DO set the solicitate flag (default: off)
ND Security evasion options (can be combined):
  -H  add a hop-by-hop header
  -F  add a one shot fragment header (can be specified multiple times)
  -D  add a large destination header which fragments the packet.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_advertise6 $opts")
elif prog == "19":
    bot.dp()
    print"""
atk6-fake_dhcps6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_dhcps6 interface network-address/prefix-length dns-server [dhcp-server-ip-address [mac-address]]

Fake DHCPv6 server. Use to configure an address and set a DNS server
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_dhcps6 $opts")
elif prog == "20":
    bot.dp()
    print"""
atk6-fake_dns6d v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_dns6d interface ipv6-address [fake-ipv6-address [fake-mac]]
Fake DNS server that serves the same IPv6 address to any lookup request
You can use this together with parasite6 if clients have a fixed DNS server
Note: very simple server. Does not honor multiple queries in a packet, norNS, MX, etc. lookups.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_dns6d $opts")
elif prog == "21":
    bot.dp()
    print"""
atk6-fake_dnsupdate6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_dnsupdate6 dns-server full-qualified-host-dns-name ipv6address

Example: atk6-fake_dnsupdate6 dns.test.com myhost.sub.test.com ::1
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_dnsupdate6 $opts")
elif prog == "22":
    bot.dp()
    print"""
atk6-fake_mipv6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_mipv6 interface home-address home-agent-address care-of-address

If the mobile IPv6 home-agent is mis-configured to accept MIPV6 updates without
IPSEC, this will redirect all packets for home-address to care-of-address
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_mipv6 $opts")
elif prog == "23":
    bot.dp()
    print"""
atk6-fake_mld26 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_mld26 [-l] interface add|delete|query [multicast-address [target-address [ttl [own-ip [own-mac-address [destination-mac-address]]]]]]

This uses the MLDv2 protocol. Only a subset of what the protocol is able to
do is possible to implement via a command line. Code it if you need something.
Ad(d)vertise or delete yourself - or anyone you want - in a multicast group of your choice
Query ask on the network who is listening to multicast addresses
Use -l to loop and send (in 5s intervals) until Control-C is pressed.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_mld26 $opts")
elif prog == "24":
    bot.dp()
    print"""
atk6-fake_mld6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_mld6 [-l] interface add|delete|query [multicast-address [target-address [ttl [own-ip [own-mac-address [destination-mac-address]]]]]]

Ad(d)vertise or delete yourself - or anyone you want - in a multicast group of your choice
Query ask on the network who is listening to multicast addresses
Use -l to loop and send (in 5s intervals) until Control-C is pressed.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_mld6 $opts")
elif prog == "25":
    bot.dp()
    print"""
atk6-fake_mldrouter6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_mldrouter6 [-l] interface advertise|solicitate|terminate [own-ip [own-mac-address]]

Announce, delete or soliciated MLD router - sourself or others.
Use -l to loop and send (in 5s intervals) until Control-C is pressed.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_mldrouter6 $opts")
elif prog == "26":
    bot.dp()
    print"""
atk6-fake_pim6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax:
  atk6-fake_pim6 [-t ttl] [-s src6] [-d dst6] interface hello [dr_priority]
  atk6-fake_pim6 [-t ttl] [-s src6] [-d dst6] interface join|prune neighbor6 multicast6 target6

The hello command takes optionally the DR priority (default: 0).
The join and prune commands need the multicast group to modify, the target
address that joins or leavs and the neighbor PIM router
Use -s to spoof the source ip6, -d to send to another address than ff02::d,
and -t to set a different TTL (default: 1)
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_pim6 $opts")
elif prog == "27":
    bot.dp()
    print"""
atk6-fake_router26 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_router26 [-E type] [-A network/prefix] [-R network/prefix] [-D dns-server] [-s sourceip] [-S sourcemac] [-ardl seconds] [-Tt ms] [-n no] [-i interval] interface [target]

Options:
 -A network/prefix  add autoconfiguration network (up to 16 times)
 -a seconds         valid lifetime of prefix -A (defaults to 99999)
 -R network/prefix  add a route entry (up to 16 times)
 -r seconds         route entry lifetime of -R (defaults to 4096)
 -D dns-server      specify a DNS server (up to 16 times)
 -L searchlist      specify the DNS domain search list, separate entries with ,
 -d seconds         dns entry lifetime of -D (defaults to 4096
 -M mtu             the MTU to send, defaults to the interface setting
 -s sourceip        the source ip of the router, defaults to your link local
 -S sourcemac       the source mac of the router, defaults to your interface
 -l seconds         router lifetime (defaults to 2048)
 -T ms              reachable timer (defaults to 0)
 -t ms              retrans timer (defaults to 0)
 -p priority        priority "low", "medium", "high" (default), "reserved"
 -F flags           Set one or more of the following flags: managed, other,
                   homeagent, proxy, reserved; separate by comma
 -E type            Router Advertisement Guard Evasion option. Types: 
     H             simple hop-by-hop header
     1             simple one-shot fragmentation header (can add multiple)
     D             insert a large destination header so that it fragments
     O             overlapping fragments for keep-first targets (Win, BSD, Mac)
     o             overlapping fragments for keep-last targets (Linux, Solaris)
                    Examples: -E H111, -E D
 -m mac-address    if only one machine should receive the RAs (not with -E DoO)
 -i interval       time between RA packets (default: 5)
 -n number         number of RAs to send (default: unlimited)

Announce yourself as a router and try to become the default router.
If a non-existing link-local or mac address is supplied, this results in a DOS.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_router26 $opts")
elif prog == "28":
    bot.dp()
    print"""
atk6-fake_router6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_router6 [-HFD] interface network-address/prefix-length [dns-server [router-ip-link-local [mtu [mac-address]]]]

Announce yourself as a router and try to become the default router.
If a non-existing link-local or mac address is supplied, this results in a DOS.
Option -H adds hop-by-hop, -F fragmentation header and -D dst header.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_router6 $opts")
elif prog == "29":
    bot.dp()
    print"""
atk6-fake_solicitate6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fake_solicitate6 [-DHF] interface ip-address-solicitated [target-address [mac-address-solicitated [source-ip-address]]]

Solicate IPv6 address on the network, sending it to the all-nodes multicast address
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fake_solicitate6 $opts")
elif prog == "30":
    bot.dp()
    print"""
atk6-firewall6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-firewall6 [-Hu] interface destination port [test-case-no]

Performs various ACL bypass attempts to check implementations.
Defaults to TCP ports, option -u switches to UDP.
Option -H prints the hop count.
For all test cases to work, ICMPv6 ping to the destination must be allowed.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-firewall6 $opts")
elif prog == "31":
    bot.dp()
    print"""
atk6-flood_advertise6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_advertise6 interface [target]

Flood the local network with neighbor advertisements.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_advertise6 $opts")
elif prog == "32":
    bot.dp()
    print"""
atk6-flood_dhcpc6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_dhcpc6 [-n|-N] [-1] [-d domain-name] interface [dhcpserver]

DHCP client flooder. Use to deplete the IP address pool a DHCP6 server is
offering. Note: if the pool is very large, this is rather senseless. :-)

By default the link-local IP MAC address is random, however this won't work
in some circumstances. -n will use the real MAC, -N the real MAC and
link-local address. -1 will only solicate an address but not request it.
If -N is not used, you should run parasite6 in parallel.
Use -d to force DNS updates, you must specify a domain name.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_dhcpc6 $opts")
elif prog == "33":
    bot.dp()
    print"""
atk6-flood_mld26 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_mld26 interface [target]

Flood the local network with MLDv2 reports.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_mld26 $opts")
elif prog == "34":
    bot.dp()
    print"""
atk6-flood_mld6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_mld6 interface [target]

Flood the local network with MLD reports.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_mld6 $opts")
elif prog == "35":
    bot.dp()
    print"""
atk6-flood_mldrouter6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_mldrouter6 interface [target]

Flood the local network with MLD router advertisements.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_mldrouter6 $opts")
elif prog == "36":
    bot.dp()
    print"""
atk6-flood_redir6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_redir6 [-HFD] interface [target] [oldrouter [newrouter]]

Flood the local network with ICMPv6 redirect packets.
-F/-D/-H add fragment/destination/hopbyhop header to bypass simple filters
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_redir6 $opts")
elif prog == "37":
    bot.dp()
    print"""
atk6-flood_router26 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_router26 [-HFD] [-sSG] [-RPA] interface [target]

Flood the local network with router advertisements.
Each packet contains ~25 prefix and route enries
Modes:
  default  sends both routing entries and prefix information
  -R       does only send routing entries, no prefix information
  -P       does only send prefix information, no routing entries
  -A       an attack to disable privacy extensions
Options:
  -H       add a hopbyhop header to bypass RA guard security
  -F       add an atomic fragment header to bypass RA guard security
  -D       add a large destination header to bypass RA guard security
  -s       use small lifetimes, resulting in a more devasting impact
  -S       performs a slow start, which can increases the impact
  -G       gigantic packet of 64kb of prefix/route entries
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_router26 $opts")
elif prog == "38":
    bot.dp()
    print"""
atk6-flood_router6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_router6 [-HFD] interface

Flood the local network with router advertisements.
-F/-D/-H add fragment/destination/hopbyhop header to bypass RA guard security.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_router6 $opts")
elif prog == "39":
    bot.dp()
    print"""
atk6-flood_rs6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_rs6 [-sS] interface [target]

Flood the local network with ICMPv6 Router Soliciation packets.
Option -s uses random source IPv6 addresses. Option -S also randomizes the MAC.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_rs6 $opts")
elif prog == "40":
    bot.dp()
    print"""
atk6-flood_solicitate6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-flood_solicitate6 interface [target]

Flood the network with neighbor solicitations.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-flood_solicitate6 $opts")
elif prog == "41":
    bot.dp()
    print"""
atk6-four2six v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-four2six [-FHD] [-s src6] interface ipv6-to-ipv4-gateway ipv4-src ipv4-dst [port]

Options:
  -F       insert atomic fragment header (can be set multiple times)
  -H       insert and empty hop-by-hop header
  -D       insert a large destination header that fragments the packet
  -s src6  set a specific IPv6 source address

Send an IPv4 packet to an IPv6 4to6 gateway. If a port is specified, a UDP packet is sent, otherwise an ICMPv4 ping.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-four2six $opts")
elif prog == "42":
    bot.dp()
    print"""
atk6-fragmentation6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fragmentation6 [-fp] [-n number] interface destination [test-case-no]

-f activates flooding mode, no pauses between sends; -p disables first and
final pings, -n number specifies how often each test is performed

Performs fragment firewall and implementation checks, incl. denial-of-service.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fragmentation6 $opts")
elif prog == "43":
    bot.dp()
    print"""
atk6-fuzz_dhcps6 v2.5 (c) 2013 by Brandon Hutcheson and Graeme Neilson www.thc.org

Syntax: atk6-fuzz_dhcps6 [-t number | -T number] [-e number | -T number] [-p number] [-md] [-1|-2|-3|-4|-5|-6|-7|-8] interface [domain-name]

Fuzzes an DHCPv6 packet
Options:
 -1         fuzz DHCPv6 Solicit (default)
 -2         fuzz DHCPv6 Request
 -3         fuzz DHCPv6 Confirm
 -4         fuzz DHCPv6 Renew
 -5         fuzz DHCPv6 Rebind
 -6         fuzz DHCPv6 Release
 -7         fuzz DHCPv6 Decline
 -8         fuzz DHCPv6 Information Request
 -m         fuzz the message type as well
 -t number  continue from test no. number
 -e number  continue to test no. number
 -T number  only performs test no. number
 -n number  how many times to send each packet (default: 1)
 -f         spoof mac
 -F         spoof link address
 -p number  perform an alive check every number of tests (default: none)
 -d         Use -d to force DNS updates, you can specify a domain name on the commandline.
You can only define one of -0 ... -4, defaults to -1.
Returns -1 on error, 0 on tests done and targt alive or 1 on target crash.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fuzz_dhcps6 $opts")
elif prog == "44":
    bot.dp()
    print"""
atk6-fuzz_ip6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-fuzz_ip6 [-x] [-t number | -T number] [-p number] [-IFSDHRJ] [-X|-1|-2|-3|-4|-5|-6|-7|-8|-9|-0 port] interface unicast-or-multicast-address [address-in-data-pkt]

Fuzzes an icmp6 packet
Options:
 -X         do not add any ICMP/TCP header (transport layer)
 -1         fuzz ICMP6 echo request (default)
 -2         fuzz ICMP6 neighbor solicitation
 -3         fuzz ICMP6 neighbor advertisement
 -4         fuzz ICMP6 router advertisement
 -5         fuzz multicast listener report packet
 -6         fuzz multicast listener done packet
 -7         fuzz multicast listener query packet
 -8         fuzz multicast listener v2 report packet
 -9         fuzz multicast listener v2 query packet
 -0         fuzz node query packet
 -s port    fuzz TCP-SYN packet against port
 -x         tries all 256 values for flag and byte types
 -t number  continue from test no. number
 -T number  only performs test no. number
 -p number  perform an alive check every number of tests (default: none)
 -a         do not perform initial and final alive test
 -n number  how many times to send each packet (default: 1)
 -I         fuzz the IP header too
 -F         add one-shot fragmentation, and fuzz it too (for 1)
 -S         add source-routing, and fuzz it too (for 1)
 -D         add destination header, and fuzz it too (for 1)
 -H         add hop-by-hop header, and fuzz it too (for 1 and 5-9)
 -R         add router alert header, and fuzz it too (for 5-9 and all)
 -J         add jumbo packet header, and fuzz it too (for 1)
You can only define one of -0 ... -9 and -s, defaults to -1.
Returns -1 on error, 0 on tests done and targt alive or 1 on target crash.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-fuzz_ip6 $opts")
elif prog == "45":
    bot.dp()
    print"""
atk6-implementation6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-implementation6 [-p] [-s sourceip6] interface destination [test-case-number]

Options:
  -s sourceip6  use the specified source IPv6 address
  -p            do not perform an alive check at the beginning and end

Performs some IPv6 implementation checks, can be used to test some
firewall features too. Takes approx. 2 minutes to complete.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-implementation6 $opts")
elif prog == "46":
    bot.dp()
    print"""
atk6-implementation6d v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-implementation6d interface

Identifies test packets by the implementation6 tool, useful to check what
packets passed a firewall
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-implementation6d $opts")
elif prog == "47":
    bot.dp()
    print"""
atk6-inject_alive6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-inject_alive6 [-ap] interface

This tool answers to keep-alive requests on PPPoE and 6in4 tunnels; for PPPoE
it also sends keep-alive requests.
Note that the appropriate environment variable THC_IPV6_{PPPOE|6IN4} must be set
Option -a will actively send alive requests every 15 seconds.
Option -p will not send replies to alive requests.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-inject_alive6 $opts")
elif prog == "48":
    bot.dp()
    print"""
atk6-inverse_lookup6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-inverse_lookup6 interface mac-address

Performs an inverse address query, to get the IPv6 addresses that are assigned
to a MAC address. Note that only few systems support this yet.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-inverse_lookup6 $opts")
elif prog == "49":
    bot.dp()
    print"""
atk6-kill_router6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-kill_router6 [-HFD] interface router-address [srcmac [dstmac]]

Announce that a target a router going down to delete it from the routing tables.
If you supply a '*' as router-address, this tool will sniff the network for any
RA packet and immediately send the kill packet.
Option -H adds hop-by-hop, -F fragmentation header and -D dst header.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-kill_router6 $opts")
elif prog == "50":
    bot.dp()
    print"""
atk6-ndpexhaust26 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-ndpexhaust26 [-acpPTUrR] [-s sourceip6] interface target-network

Options:
 -a      add a hop-by-hop header with router alert
 -c      do not calculate the checksum to save time
 -p      send ICMPv6 Echo Requests
 -P      send ICMPv6 Echo Reply
 -T      send ICMPv6 Time-to-live-exeeded
 -U      send ICMPv6 Unreachable (no route)
 -r      randomize the source from your /64 prefix
 -R      randomize the source fully
 -s sourceip6  use this as source IPv6 address

Flood the target /64 network with ICMPv6 TooBig error messages.
This tool version is manyfold more effective than ndpexhaust6.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-ndpexhaust26 $opts")
elif prog == "51":
    bot.dp()
    print"""
!
! Please note: ndpexhaust6 is deprecated, please use ndpexhaust26!
!

atk6-ndpexhaust6 by mario fleischmann <mario.fleischmann@1und1.de>

Syntax: atk6-ndpexhaust6 interface destination-network [sourceip]

Randomly pings IPs in target network
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-ndpexhaust6 $opts")
elif prog == "52":
    bot.dp()
    print"""
atk6-node_query6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-node_query6 interface target

Sends an ICMPv6 node query request to the target and dumps the replies.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-node_query6 $opts")
elif prog == "53":
    bot.dp()
    print"""
atk6-parasite6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-parasite6 [-lRFHD] interface [fake-mac]

This is an "ARP spoofer" for IPv6, redirecting all local traffic to your own
system (or nirvana if fake-mac does not exist) by answering falsely to
Neighbor Solitication requests
Option -l loops and resends the packets per target every 5 seconds.
Option -R will also try to inject the destination of the solicitation
NS security bypass: -F fragment, -H hop-by-hop and -D large destination header
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-parasite6 $opts")
elif prog == "54":
    bot.dp()
    print"""
atk6-passive_discovery6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-passive_discovery6 [-Ds] [-m maxhop] [-R prefix] interface [script]

Options:
 -D          do also dump destination addresses (does not work with -m)
 -s          do only print the addresses, no other output
 -m maxhop   the maximum number of hops a target which is dumped may be away.
             0 means local only, the maximum amount to make sense is usually 5
 -R prefix   exchange the defined prefix with the link local prefix

Passivly sniffs the network and dump all client's IPv6 addresses detected.
Note that in a switched environment you get better results when additionally
starting parasite6, however this will impact the network.
If a script name is specified after the interface, it is called with the
detected ipv6 address as first and the interface as second option.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-passive_discovery6 $opts")
elif prog == "55":
    bot.dp()
    print"""
Syntax: atk6-randicmp6 [-p] [-s sourceip] interface destination [type [code]]

Sends all ICMPv6 type and code combinations to destination.
Option -s  sets the source IPv6 address.
Option -p  will not print answers received.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-randicmp6 $opts")
elif prog == "56":
    bot.dp()
    print"""
atk6-redir6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-redir6 interface victim-ip target-ip original-router new-router [new-router-mac] [hop-limit]

Implant a route into victim-ip, which redirects all traffic to target-ip to
new-ip. You must know the router which would handle the route.
If the new-router-mac does not exist, this results in a DOS.
If the TTL of the target is not 64, then specify this is the last option.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-redir6 $opts")
elif prog == "57":
    bot.dp()
    print"""
atk6-redirsniff6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-redirsniff6 interface victim-ip destination-ip original-router [new-router [new-router-mac]]

Implant a route into victim-ip, which redirects all traffic to destination-ip to
new-router. This is done on all traffic that flows by that matches
victim->target. You must know the router which would handle the route.
If the new-router/-mac does not exist, this results in a DOS.
You can supply a wildcard ('*') for victim-ip and/or destination-ip.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-redirsniff6 $opts")
elif prog == "58":
    bot.dp()
    print"""
atk6-rsmurf6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-rsmurf6 interface victim-ip

Smurfs the local network of the victim. Note: this depends on an
implementation error, currently only verified on Linux.
Evil: "ff02::1" as victim will DOS your local LAN completely
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-rsmurf6 $opts")
elif prog == "59":
    bot.dp()
    print"""
sendpees6 by willdamn <willdamn@gmail.com>

Syntax: atk6-sendpees6 interface key_length prefix victim

Send SEND neighbor solicitation messages and make target to verify a lota CGA and RSA signatures
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-sendpees6 $opts")
elif prog == "60":
    bot.dp()
    print"""
original sendpees by willdamn <willdamn@gmail.com>
modified sendpeesMP by Marcin Pohl <marcinpohl@gmail.com>
Code based on thc-ipv6

Syntax: atk6-sendpeesmp6 interface key_length prefix victim

Send SEND neighbor solicitation messages and make target to verify a lota CGA and RSA signatures
Example: atk6-sendpeesmp6 eth0 2048 fe80:: fe80::1
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-sendpeesmp6 $opts")
elif prog == "61":
    bot.dp()
    print"""
atk6-smurf6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-smurf6 interface victim-ip [multicast-network-address]

Smurf the target with icmp echo replies. Target of echo request is the
local all-nodes multicast address if not specified
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-smurf6 $opts")
elif prog == "62":
    bot.dp()
    print"""
atk6-thcping6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-thcping6 [-af] [-H t:l:v] [-D t:l:v] [-F dst] [-t ttl] [-c class] [-l label] [-d size] [-S port|-U port|-T type -C code] interface src6 dst6 [srcmac [dstmac [data]]]

Options:
  -a              add a hop-by-hop header with router alert option.
  -q              add a hop-by-hop header with quickstart option.
  -E              send as ethertype IPv4
  -H t:l:v        add a hop-by-hop header with special content
  -D t:l:v        add a destination header with special content
  -D "xxx"        add a large destination header which fragments the packet
  -f              add a one-shot fragementation header
  -F ipv6address  use source routing to this final destination
  -t ttl          specify TTL (default: 255)
  -c class        specify a class (0-4095)
  -l label        specify a label (0-1048575)
  -d data_size    define the size of the ping data buffer
  -T number       ICMPv6 type to send (default: 128 = ping)
  -C number       ICMPv6 code to send (default: 0)
  -S port         use a TCP SYN packet on the defined port instead of ping
  -U port         use a UDP packet on the defined port instead of ping
  -n count        how often to send the packet (default: 1)
t:l:v syntax: type:length:value, value is in hex, e.g. 1:2:0eab
You can put an "x" into src6, srcmac and dstmac for an automatic value.

Craft a ICMPv6/TCP/UDP packet with special IPv6 or EH header options.
Returns -1 on error or no reply, 0 on normal reply or 1 on error reply.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-thcping6 $opts")
elif prog == "63":
    bot.dp()
    print"""
atk6-thcsyn6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-thcsyn6 [-AcDrRS] [-p port] [-s sourceip6] interface target port

Options:
 -A      send TCP-ACK packets
 -S      send TCP-SYN-ACK packets
 -r      randomize the source from your /64 prefix
 -R      randomize the source fully
 -s sourceip6  use this as source IPv6 address
 -D      randomize the destination (treat as /64)
 -p port       use fixed source port

Flood the target port with TCP-SYN packets. If you supply "x" as port, it
is randomized.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-thcsyn6 $opts")
elif prog == "64":
    bot.dp()
    print"""
atk6-toobig6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-toobig6 [-u] interface target-ip existing-ip mtu [hop-limit]

Implants the specified mtu on the target.
If the TTL of the target is not 64, then specify this as the last option.
Option -u will send the TooBig without the spoofed ping6 from existing-ip.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-toobig6 $opts")
elif prog == "65":
    bot.dp()
    print"""
atk6-trace6 v2.5 (c) 2013 by van Hauser / THC <vh@thc.org> www.thc.org

Syntax: atk6-trace6 [-abdtu] [-s src6] interface targetaddress [port]

Options:
  -a       insert a hop-by-hop header with router alert option.
  -D       insert a destination extension header
  -E       insert a destination extension header with an invalid option
  -F       insert a one-shot fragmentation header
  -b       instead of an ICMP6 Ping, use TooBig (you will not see the target)
  -B       instead of an ICMP6 Ping, use PingReply (you will not see the target)
  -d       resolves the IPv6 addresses to DNS.
  -t       enables tunnel detection
  -u       use UDP instead of TCP if a port is supplied
  -s src6  specifies the source IPv6 address
Maximum hop reach: 31

A basic but very fast traceroute6 program.
If no port is specified, ICMP6 Ping requests are used, otherwise TCP SYN
packets to the specified port. Options D, E and F can be use multiple times.
"""
    os.system("read -p 'Enter Options: ' opts ; /usr/bin/atk6-trace6 $opts")
else:
    print("ERROR: [\"" + prog + "\"]  INVALID INPUT!\n   YOU MUST INPUT NUMBER [1-65] ")
    quit()
