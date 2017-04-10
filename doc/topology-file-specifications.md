# CyberCAPTOR Topology XML Input File description

The XML topological file defined here is the main input which is used globally for CyberCAPTOR-Server (it can be uploaded from CyberCAPTOR-Client on the Initialization page).

It unifies all topological data used by CyberCAPTOR-Server to compute the attack graphs and do the risk analysis.

The main goal of the XML topology file is to describe the network topology, all hosts and their network configuration. Each host can have several network interfaces which can be in different VLAN. The routing and filtering information attached to each host allow computing the network topology (packet route in the network, filtered packets, position of firewalls…). This file can be generated automatically thanks to the CyberCAPTOR-Data-Extraction script [https://github.com/fiware-cybercaptor/cybercaptor-data-extraction](https://github.com/fiware-cybercaptor/cybercaptor-data-extraction).


# Description of all fields (xml tags)

## Machine
All next tags defined in the father Machine tag contain all the attributes related to a machine of the topology. Each <machine> tag is related to a specific host. This father machine tag is used by the Remediation. By way, the algorithm is developed, this information is necessary to compute the solutions proposed by Remediation tool.

### Name
- Type : String
- Usage : Contains the name of a host

### Security Requirement (Optional)
- Type : String : NEGLIGEABLE/MINOR/MEDIUM/SEVERE/CATASTROPHIC
- Usage : A value describing a security requirement related to this host.

### Physical host (Optional)
If the machine is a VM or a container, this section contains information related to the physical host it runs on.
Note that VMs / containers can be nested : a container running in a VM running on a physical machine.

#### Hostname
- Type : String
- Usage : The name of the physical host.

#### Hypervisor
- Type : String
- Usage : The name of the hypervisor program running the VM/container.

#### User
- Type : String
- Usage : The name of the user under which the hypervisor runs on the host.

### Interfaces - Interface
These XML tags contain all the attributes related to an interface of a machine. Each <interface> tag is related to a specific network interface.

#### Name
- Type : String
- Usage : Contains the name of this interface

#### VLAN - Name (Optional)
- Type : String
- Usage : Contains the name of the VLAN attached to this interface

#### VLAN – Label (Optional)
- Type : String
- Usage : Contains the label of the VLAN attached to this interface

#### IPaddress
- Type : IP address (string)
- Usage : Contains the IP address of this interface

### Services - Service
The description of the network services or applications running on this machine.

#### Name
- Type : String
- Usage : The name of the service

#### IPaddress (Optional)
- Type : IP address (string)
- Usage : The IP address on which the service is listenning (if applicable).

#### Protocol (Optional)
- Type : TCP/UDP/ICMP/ANY (string)
- Usage : The protocol on which the service is listenning (if applicable).

#### Port (Optional)
- Type : Integer
- Usage : The port on which the service is listenning (if applicable).

#### Vulnerabilities - Vulnerability (Optional)
The vulnerabilities of this service, if applicable.

##### Type
- Type : remoteExploit/localExploit
- Usage : The type of vulnerability (cf CVSS).

##### CVE
- Type : String (CVE-YEAR-1234)
- Usage : The CVE identifier of the vulnerability.

##### Goal
- Type : String
- Usage : The goal of the vulnerability

##### CVSS
- Type : Double
- Usage : The CVSS score of the vulnerability.

### Routes - Route
These XML tags contain the routing table attached to each host. Each <route> tag contains a route of the routing table. Each host needs at least a route containing its default gateway (0.0.0.0/0.0.0.0).

#### Destination
- Type : IP address (string)
- Usage : Contains the destination network address of the route

#### Mask
- Type : IP address (string)
- Usage : Contains the network mask of the destination network

#### Gateway
- Type : String
- Usage : Contains the IP address of the gateway to take for this route (next hop)

#### Interface
- Type : IP address (string)
- Usage : Contains the interface of the host to use for this route

### Input-Firewall
This XML tag contains the input firewall table attached to each host.

#### Default-policy
- Type : ALLOW/DENY
- Usage : Contains the default policy of the input firewall table, selected if no firewall line match.

#### Firewall rule (Optional)
This XML tag contains one line of the input firewall table.

##### Protocol
- Type : String : TCP/UDP/ANY
- Usage : Contains the network flow protocol to match for this firewall line.

##### Source IP
- Type : IP address  (string)
- Usage : Contains the source network address to match for this firewall line

##### Source Mask
- Type : IP address  (string)
- Usage : Contains the source network mask to match for this firewall line

##### Source Port
- Type : integer or ANY
- Usage : Contains the source port to match for this firewall line

##### Destination IP
- Type : IP address  (string)
- Usage : Contains the destination network address to match for this firewall line

##### Destination Mask
- Type : IP address  (string)
- Usage : Contains the destination network mask to match for this firewall line

##### Destination Port
- Type : integer or ANY
- Usage : Contains the destination port to match for this firewall line

##### Action
- Type : ACCEPT / DROP
- Usage : Contains the action to do if a packet match this firewall line

### Output-Firewall
This XML tag contains the output firewall table attached to each host.

#### Default-policy
- Type : ALLOW/DENY
- Usage : Contains the default policy of the output firewall table, selected if no firewall line match.

#### Firewall rule (Optional)
This XML tag contains one line of the output firewall table.

##### Protocol
- Type : String : TCP/UDP/ANY
- Usage : Contains the network flow protocol to match for this firewall line.

##### Source IP
- Type : IP address  (string)
- Usage : Contains the source network address to match for this firewall line

##### Source Mask
- Type : IP address  (string)
- Usage : Contains the source network mask to match for this firewall line

##### Source Port
- Type : integer or ANY
- Usage : Contains the source port to match for this firewall line

##### Destination IP
- Type : IP address  (string)
- Usage : Contains the destination network address to match for this firewall line

##### Destination Mask
- Type : IP address  (string)
- Usage : Contains the destination network mask to match for this firewall line

##### Destination Port
- Type : integer or ANY
- Usage : Contains the destination port to match for this firewall line

##### Action
- Type : ACCEPT / DROP
- Usage : Contains the action to do if a packet match this firewall line

### Flow-matrix - Flow-matrix-line
This contain all the lines of the flow matrix in this network (all authorized accesses)

#### Source - Resource
- Type : String
- Usage : The name of the authorized source resource

#### Source - Type
- Type : VLAN/IP
- Usage : The type of the authorized source resource

#### Destination - Resource
- Type : String
- Usage : The name of the authorized destination resource

#### Destination - Type
- Type : VLAN/IP
- Usage : The type of the authorized destination resource

#### Source Port
- Type : Integer
- Usage : The authorized source port

#### Destination Port
- Type : Integer
- Usage : The authorized destination port

#### Protocol
- Type : TCP/UDP/ICMP/ANY
- Usage : The authorized protocol

### NDN-Links - NDN-Link
This contains all the NDN links of the network.

#### Host-src
- Type : String
- Usage : The source host

#### Face-src
- Type : String
- Usage : The face on the source host

#### Host-dst
- Type : String
- Usage : The destination host

#### Face-dst
- Type : String
- Usage : The face on the destination host

# APPENDIX: Example topology file

```
<topology>
  <machine>
    <name>client</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan1</name>
          <label>vlan1</label>
        </vlan>
        <ipaddress>10.0.1.1</ipaddress>
        <directly-connected>
          <ipaddress>10.0.1.2</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services />
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>10.0.1.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>firewall1</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host1</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth1</name>
        <vlan>
          <name>vlan2</name>
          <label>vlan2</label>
        </vlan>
        <ipaddress>10.0.2.1</ipaddress>
        <directly-connected>
          <ipaddress>10.0.2.2</ipaddress>
        </directly-connected>
      </interface>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan1</name>
          <label>vlan1</label>
        </vlan>
        <ipaddress>10.0.1.2</ipaddress>
        <directly-connected>
          <ipaddress>10.0.1.1</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services />
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>igw</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host1</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan2</name>
          <label>vlan2</label>
        </vlan>
        <ipaddress>10.0.2.2</ipaddress>
        <directly-connected>
          <ipaddress>10.0.2.1</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services>
      <service>
        <name>igw-daemon</name>
        <global_name />
        <ipaddress>10.0.2.2</ipaddress>
        <protocol>TCP</protocol>
        <port>80</port>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>remoteExploit</type>
            <goal>privEscalation</goal>
            <cve>CVE-2013-2249</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>10.0.2.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>egw</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host4</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan3</name>
          <label>vlan3</label>
        </vlan>
        <ipaddress>10.0.3.1</ipaddress>
        <directly-connected>
          <ipaddress>10.0.3.2</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services>
      <service>
        <name>egw-daemon</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>remoteExploit</type>
            <goal>privEscalation</goal>
            <cve>CVE-2013-2249</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>10.0.3.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>firewall2</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host4</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth1</name>
        <vlan>
          <name>vlan4</name>
          <label>vlan4</label>
        </vlan>
        <ipaddress>10.0.4.1</ipaddress>
        <directly-connected>
          <ipaddress>10.0.4.2</ipaddress>
        </directly-connected>
      </interface>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan3</name>
          <label>vlan3</label>
        </vlan>
        <ipaddress>10.0.3.2</ipaddress>
        <directly-connected>
          <ipaddress>10.0.3.1</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services />
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>server</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan4</name>
          <label>vlan4</label>
        </vlan>
        <ipaddress>10.0.4.2</ipaddress>
        <directly-connected>
          <ipaddress>10.0.4.1</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services>
      <service>
        <name>apache2</name>
        <global_name />
        <ipaddress>10.0.4.2</ipaddress>
        <protocol>TCP</protocol>
        <port>80</port>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>remoteExploit</type>
            <goal>privEscalation</goal>
            <cve>CVE-2013-2249</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>10.0.4.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>host1</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan0</name>
          <label>vlan0</label>
        </vlan>
        <ipaddress>192.168.1.1</ipaddress>
        <directly-connected>
          <ipaddress>192.168.1.2</ipaddress>
          <ipaddress>192.168.1.3</ipaddress>
          <ipaddress>192.168.1.4</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services>
      <service>
        <name>kvm</name>
        <global_name>host1_kvm</global_name>
        <ipaddress>192.168.1.1</ipaddress>
        <protocol>ANY</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>localExploit</type>
            <goal>privEscalation</goal>
            <cve>CVE-2011-4622</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>192.168.1.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>host2</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan0</name>
          <label>vlan0</label>
        </vlan>
        <ipaddress>192.168.1.2</ipaddress>
        <directly-connected>
          <ipaddress>192.168.1.1</ipaddress>
          <ipaddress>192.168.1.3</ipaddress>
          <ipaddress>192.168.1.4</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services />
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>192.168.1.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>host3</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan0</name>
          <label>vlan0</label>
        </vlan>
        <ipaddress>192.168.1.3</ipaddress>
        <directly-connected>
          <ipaddress>192.168.1.1</ipaddress>
          <ipaddress>192.168.1.2</ipaddress>
          <ipaddress>192.168.1.4</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services>
      <service>
        <name>kvm</name>
        <global_name>host3_kvm</global_name>
        <ipaddress>192.168.1.3</ipaddress>
        <protocol>ANY</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>localExploit</type>
            <goal>privEscalation</goal>
            <cve>CVE-2011-4622</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>192.168.1.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>host4</name>
    <cpe>cpe:/</cpe>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces>
      <interface>
        <name>eth0</name>
        <vlan>
          <name>vlan0</name>
          <label>vlan0</label>
        </vlan>
        <ipaddress>192.168.1.4</ipaddress>
        <directly-connected>
          <ipaddress>192.168.1.1</ipaddress>
          <ipaddress>192.168.1.2</ipaddress>
          <ipaddress>192.168.1.3</ipaddress>
        </directly-connected>
      </interface>
    </interfaces>
    <services />
    <routes>
      <route>
        <destination>0.0.0.0</destination>
        <mask>0.0.0.0</mask>
        <gateway>192.168.1.254</gateway>
        <interface>eth0</interface>
      </route>
    </routes>
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn1</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host2</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>localExploit</type>
            <goal>privEscalation</goal>
            <cve>NDN-2017-0002</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn2</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host3</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>localExploit</type>
            <goal>privEscalation</goal>
            <cve>NDN-2017-0002</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn3</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host2</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>signatureExploit</type>
            <goal>cachedPoisonned</goal>
            <cve>NDN-2017-0001</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn4</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host3</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>signatureExploit</type>
            <goal>cachedPoisonned</goal>
            <cve>NDN-2017-0001</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn5</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host3</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <machine>
    <name>ndn6</name>
    <cpe>cpe:/</cpe>
    <physical_host>
      <hostname>host3</hostname>
      <hypervisor>kvm</hypervisor>
      <user>root</user>
    </physical_host>
    <controllers>
      <controller>orchestrateur_global</controller>
    </controllers>
    <interfaces />
    <services>
      <service>
        <name>NFD</name>
        <global_name />
        <protocol>NDN</protocol>
        <CPE>cpe:/</CPE>
        <vulnerabilities>
          <vulnerability>
            <type>localExploit</type>
            <goal>privEscalation</goal>
            <cve>NDN-2017-0002</cve>
          </vulnerability>
        </vulnerabilities>
      </service>
    </services>
    <routes />
    <input-firewall>
      <default-policy>ACCEPT</default-policy>
    </input-firewall>
    <output-firewall>
      <default-policy>ACCEPT</default-policy>
    </output-firewall>
  </machine>
  <flow-matrix>
    <flow-matrix-line>
      <source type="VLAN" resource="vlan1" />
      <destination type="VLAN" resource="vlan2" />
      <source_port>any</source_port>
      <destination_port>80</destination_port>
      <protocol>TCP</protocol>
    </flow-matrix-line>
    <flow-matrix-line>
      <source type="VLAN" resource="vlan2" />
      <destination type="VLAN" resource="vlan1" />
      <source_port>80</source_port>
      <destination_port>any</destination_port>
      <protocol>TCP</protocol>
    </flow-matrix-line>
    <flow-matrix-line>
      <source type="VLAN" resource="vlan3" />
      <destination type="VLAN" resource="vlan4" />
      <source_port>any</source_port>
      <destination_port>80</destination_port>
      <protocol>TCP</protocol>
    </flow-matrix-line>
    <flow-matrix-line>
      <source type="VLAN" resource="vlan4" />
      <destination type="VLAN" resource="vlan3" />
      <source_port>80</source_port>
      <destination_port>any</destination_port>
      <protocol>TCP</protocol>
    </flow-matrix-line>
  </flow-matrix>
  <ndn-links>
    <ndn-link>
      <host-src>ndn1</host-src>
      <face-src>igw</face-src>
      <host-dst>igw</host-dst>
      <face-dst>r1</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn1</host-src>
      <face-src>r2</face-src>
      <host-dst>ndn2</host-dst>
      <face-dst>r1</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn1</host-src>
      <face-src>r3</face-src>
      <host-dst>ndn3</host-dst>
      <face-dst>r1</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn2</host-src>
      <face-src>r4</face-src>
      <host-dst>ndn4</host-dst>
      <face-dst>r2</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn3</host-src>
      <face-src>r4</face-src>
      <host-dst>ndn4</host-dst>
      <face-dst>r3</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn4</host-src>
      <face-src>r5</face-src>
      <host-dst>ndn5</host-dst>
      <face-dst>r4</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn4</host-src>
      <face-src>r6</face-src>
      <host-dst>ndn6</host-dst>
      <face-dst>r4</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn5</host-src>
      <face-src>r6</face-src>
      <host-dst>ndn6</host-dst>
      <face-dst>r5</face-dst>
    </ndn-link>
    <ndn-link>
      <host-src>ndn6</host-src>
      <face-src>egw</face-src>
      <host-dst>egw</host-dst>
      <face-dst>r6</face-dst>
    </ndn-link>
  </ndn-links>
</topology>
```
