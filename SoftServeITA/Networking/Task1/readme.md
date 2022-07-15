### Task1

1. Two VMs were created using VirtualBox: 
    * VM1 - with NAT (eth0) and internal interfaces
    * VM2 - with internal interface only

2. Curent state:
    * VM1 - has access to the internet
    * VM2 - doesn't have internet access 
3. VM1 config:
    * Change **/etc/network/interfaces** file as follow:

    ```
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    # The loopback network interface
    auto lo
    iface lo inet loopback

    # The primary network interface
    auto eth0
    iface eth0 inet dhcp

    #Internal interface to connect to vm2
    auto eth1
    iface eth1 inet static
        address 192.168.1.1
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255
    ```
    Now we have configured internal interface (eth1)

    * Make the following iptables rules:
        **iptables -t nat -A POSTROUTING --out-interface eth0 -j ACCEPT**
        **iptables -A FORWARD --in-interface eth1 -j ACCEPT**
    * Allow port forwarding by editing **/etc/sysctl.conf** file. We need to uncomment **net.ipv4.ip_forward=1** line.

    * To keep iptables rules persistent we can install **iptables-persistent** utility

4. VM2 config
    * Change **/etc/network/interfaces** file as follow:

    ```
    # This file describes the network interfaces available on your system
    # and how to activate them. For more information, see interfaces(5).

    # The loopback network interface
    auto lo
    iface lo inet loopback

    #Internal interface to connect to vm2
    auto eth0
    iface eth0 inet static
        address 192.168.1.11
        netmask 255.255.255.0
        network 192.168.1.0
        gateway 192.168.1.1
        broadcast 192.168.1.255
        dns-nameservers 8.8.8.8 8.8.4.4
    ```
    Now we have configured internal interface (eth0)

5. Routing table on VM2:
    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task1/Screenshots/VirtualBox_UbuntuVM2_15_07_2022_21_08_18.png" width=100% height=100%>
6. Checking connection:
    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task1/Screenshots/VirtualBox_UbuntuVM2_15_07_2022_20_53_44.png" width=100% height=100%>
7. To determine wich resource has an IP address 8.8.8.8 we can use **nslookup 8.8.8.8** or **host 8.8.8.8** commands.
    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task1/Screenshots/VirtualBox_UbuntuVM2_15_07_2022_20_58_45.png" width=100% height=100%>
8. To check, wich IP address belongs to epam.com we can use **nslookup epam.com**, **dig epam.com** or **host epam.com** commands. 
    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task1/Screenshots/VirtualBox_UbuntuVM2_15_07_2022_20_59_45.png" width=100% height=100%>
9. On Windows machine which is host we can check default gateway using command **ipconfig /all**. To see routing tables we can use **arp -a** or **route PRINT** commands. 

10. After execution traceroute command:
 * VM1 - we got information about first hop, the rest marked as ***.
 * VM2 - we got information about first and second hops, the rest marked as ***.
 * Host - we got full information. 
    ```
    traceroute to google.com (142.250.203.142), 30 hops max, 60 byte packets
        1  DESKTOP-ARI96VB.mshome.net (172.26.16.1)  0.271 ms  0.252 ms  0.244 ms
        2  192.168.0.1 (192.168.0.1)  3.825 ms  3.284 ms  3.810 ms
        3  10.0.13.1 (10.0.13.1)  3.789 ms  3.922 ms  3.914 ms
        4  192.168.44.1 (192.168.44.1)  3.769 ms  3.250 ms  3.896 ms
        5  google2-ix.giganet.ua (185.1.63.152)  3.899 ms  3.845 ms  4.267 ms
        6  108.170.248.139 (108.170.248.139)  4.153 ms 108.170.248.154 (108.170.248.154)  3.724 ms 108.170.248.139 (108.170.248.139)  9.822 ms
        7  142.251.242.37 (142.251.242.37)  18.493 ms 142.251.242.41 (142.251.242.41)  16.630 ms  28.401 ms
        8  142.250.37.209 (142.250.37.209)  17.539 ms  17.521 ms 142.250.37.193 (142.250.37.193)  16.635 ms
        9  209.85.253.225 (209.85.253.225)  16.624 ms 72.14.237.17 (72.14.237.17)  17.284 ms  17.558 ms
        10  waw07s06-in-f14.1e100.net (142.250.203.142)  16.755 ms  17.039 ms  17.193 ms
    ```