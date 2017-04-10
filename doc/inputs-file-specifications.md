# Topological inputs file specifications

CyberCAPTOR-Data-Extraction can take several types of inputs to generate the XML topology file.

We describe in this documentation file the format of the inputs that are currently taken by the script. CyberCAPTOR-Data-Extraction may be extended to take into account new types of inputs.

Note that all CSV files use a semi-colon `;` as separator, as it is done by default with Microsoft Excel.

## Topological files

### Host-interfaces file

This CSV file describes the hosts of the topology, with their network interface. 

#### Columns explanations

Hostname  | Interface Name | IP address | Connected to WAN | Metric
--------- | -------------- | ---------- | ---------------- | ------
The name of the host (without spaces) | The name of the interface | The IP address of the interface | Whether or not this network interface is connected to WAN (Internet) | A Metric describing the importance of the services running on this IP address.


#### Example

```
Hostname;Interface Name;IP address;Connected to WAN;Metric
linux-user-1;eth0;192.168.1.111;false;7
linux-user-2;eth0;192.168.1.112;false;30
Dmz-1;eth0;10.15.10.11;false;0.8
Dmz-2;eth0;10.15.10.14;false;0.7
router;eth0;192.168.1.1;false;0.1
router;eth1;10.15.10.1;false;0.1
router;eth2;1.1.2.2;true
```

### Vlans file

This CSV file describes the subnetworks/VLANS of the network topology.

#### Columns explanations

VLAN Name | VLAN Address | VLAN Netmask | VLAN default Gateway 
--------- | ------------ | ------------ | --------------------
The name of the VLAN | The IP address of the network | The subnet mask CIDR | The IP address of the VLAN default gateway

#### Example

```
name;address;netmask;gateway
user-lan;192.168.1.0;24;192.168.1.1
dmz;10.15.10.0;24;10.15.10.1

```

### Flow Matrix File 

This CSV file describes the authorized accesses in the network topology. Note that all accesses that are not specified are supposed unauthorized.

#### Columns explanations

Source | Destination | Source port | Destination port | Protocol
------ | ----------- | ----------- | ---------------- | -------
The source network (`IP/mask`) or internet | The destination network (`IP/mask`) or internet | The source port or `any` | the destination portor `any` | the protocol or `any`.

Each line describes an authorized access.

#### Example

```
"source";"destination";"source_port";"destination_port";"protocol"
"10.15.10.0/24";"192.168.1.0/24";"any";80;"TCP"
"192.168.1.0/24";"10.15.10.0/24";"any";"any";"any"
"internet";"10.15.10.0/24";"any";"any";"any"
"internet";"10.15.10.0/24";"any";443;"TCP"
"192.168.1.0/24";"internet";"any";"any";"any"
"10.15.10.0/24";"internet";"any";"any";"any"
10.15.10.11;192.168.1.112;any;5353;TCP
```

### Routing file

This file describes the routes of the hosts that have routes, others than the default gateways of the interfaces' VLAN.

#### Columns explanations

Host | Destination | Mask | Gateway | Interface
---- | ----------- | ---- | ------- | ---------
The name of the host for which this route is specified | The destination network of this route | the network mask of this route | The gateway IP address for this route | The outgoing interface of the route.

#### Example

```
host;destination;mask;gateway;interface
router;10.15.10.1;255.255.255.0;10.15.10.1;eth1
router;192.168.1.1;255.255.255.0;192.168.1.1;eth0
router;0.0.0.0;0.0.0.0;1.1.1.1;eth2
```

## Vulnerability scanner files 

Currently, two vulnerability scanners can be used: Nessus and OpenVAS.

### Nessus scanner files

The outputs of the vulnerability scanner Nessus are stored in a .nessus file, which is an XML file.

The only outputs that are used in this file are:
```
<Report>
<ReportHost name="host ip address or hostname">
<ReportItem port="service port" svc_name="service name" protocol="service protocol">
<cve>CVE-2015-1234</cve>
<cve>CVE-2015-2345</cve>
</ReportItem>
<ReportItem>
...
</ReportItem>
```

### OpenVAS files

The outputs of the vulnerability scanner OpenVAS are stored in an XML file.

### Generic scan file

This file describes service placement (network interface, transport protocol / port, version) and vulnerabilities.

#### Example

```
{
        "date" : "2016-08-09 11:02:00",
        "hosts" : [
                {
                        "name" : "machine1",
                        "services" : [
                                {
                                        "serviceName" : "apache2",
                                        "serviceVersion" : "2.2.4-rc10",
                                        "serviceProto" : "TCP",
                                        "servicePort" : 443,
                                        "vulnerabilities" : [
                                                {
                                                        "name" : "CVE-2013-2249"
                                                }
                                        ]
                                }
                        ]
                }
        ]
}

```

### Host-VM mapping file

This file describes placement of VMs on physical hosts

#### Columns explanations

VM | Host | Software | User
-- | ---- | -------- | ----
The name of the VM | The name of the physical host | The hypervisor software on which runs the VM | The user under which the hypervisor software runs on the host.

#### Example

```
vm;host;software;user
firewall1;host1;kvm;root
firewall2;host2;kvm;root
machine1;host1;kvm;root
machine2;host2;kvm;root
machine3;host2;kvm;root
machine4;host2;kvm;root
machine5;host3;kvm;root
```

### Host-controller mapping file

This file describes orchestration dependancies between hosts and domains. Each line corresponds to the membership of a host to a domain.

#### Columns explanations

Host | Controller_global_name
---- | ----------------------
The name of the machine (physical or VM) | The name of the orchestration domain the machine depends on.

#### Example

```
host;controller_global_name
machine1;orchestrator1
machine2;orchestrator2
machine3;orchestrator2
firewall1;orchestrator1
firewall2;orchestrator1
```

### GCI input file

This file contains the whole topology, as provided by the Generic Collector Interface. It must be used with no other input file

### NDN topoogy file

This file describes the NDN links in a hybrid IP/NDN network. Each link is composed of a source and destination machine and their associated NDN faces.

#### Columns explanations

source | face_src | dest | face_dst
------ | -------- | ---- | --------
The name of the source machine | The name of the NDN face on the source machine | The name of the destination machine | The name of the NDN face on the destination macgine

#### Example

```
source;face_src;dest;face_dst
ndn1;igw;igw;r1
ndn1;r2;ndn2;r1
ndn1;r3;ndn3;r1
ndn2;r4;ndn4;r2
ndn3;r4;ndn4;r3
ndn4;r5;ndn5;r4
ndn4;r6;ndn6;r4
ndn5;r6;ndn6;r5
ndn6;egw;egw;r6
```
