### Task2

1. DNSMASQ server option:
    * /etc/dnsmasq.conf
        * setting ip range: 192.168.1.10-192.168.1.20
        * interface = eth1
    
    * /etc/network/interfaces
        * setting ip address 192.168.1.1
        * setting netmask 255.255.255.0 
        
    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task2/Screenshots/Screenshot-2022-07-18-114243.png" width=70% height=70%>

2. ISC-DHSPSERVER server option:
    * /etc/network/interfaces
        * setting ip address 192.168.1.1
        * setting netmask 255.255.255.0
        
    * /etc/dhcp/dhcpd.conf - provide ip range for clients and lease time
        * 
        ```
            subnet 192.168.1.0 netmask 255.255.255.0 {
            range 192.168.1.10 192.168.1.20;
            default-lease-time 600;
            max-lease-time 7200;
            }
        ```
    * /etc/default/isc-dhcp-server - set up default interface to *eth1*
    * Restart server - **sudo /etc/init.d/isc-dhcp-server restart**

    <img src="https://github.com/kofesenko/ITA-Kh-077-DevOps/blob/main/SoftServeITA/Networking/Task2/Screenshots/Screenshot-2022-07-18-133049.png" width=70% height=70%>

3. To configure DNS we can do the following:
    * /etc/dhcp/dhcpd.conf
        * option domain-name-servers 8.8.8.8; 
    * Restart server - **sudo /etc/init.d/isc-dhcp-server restart**

4. Make the following iptables rules:
        **iptables -t nat -A POSTROUTING --out-interface eth0 -j MASQUERADE**
        **iptables -A FORWARD --in-interface eth1 --out-interface eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT**
        **iptables -t -A FORWARD --in-interface eth1 --out-interface eth0 -j ACCEPT**
        
    * Allow port forwarding by editing **/etc/sysctl.conf** file. We need to uncomment **net.ipv4.ip_forward=1** line.

    * To keep iptables rules persistent we can install **iptables-persistent** utility
