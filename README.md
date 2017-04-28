CyberCAPTOR-Data-Extraction
==============

## Table of Contents

- [CyberCAPTOR-Data-Extraction](#cybercaptor-data-extraction)
	- [Prerequisite](#prerequisite)
	- [Build](#build)
	- [Use the script](#use-the-script)
	- [Docker build for GCI integration](#Docker-build-for-CGI-integration)

## Prerequisite

- Python >= 2.7
- pip
- git-lfs

## Build

1) Get sources from Github

```
git clone https://github.com/DOCTOR-ANR/cyber-data-extract.git
cd cyber-data-extract
```

2) Use pip to download dependencies

```
pip install -r requirements.txt
```

## Use the script

Now you can use the script to generate a XML topology file (for CyberCAPTOR-Server), from several topological files (.CSV files and .XML vulnerability scan).

Here is a typical use of the script to generate the .XML topology file :

```
/usr/bin/python3 main.py --hosts-interfaces-file ./inputs/hosts-interfaces.csv --vlans-file ./inputs/vlan.csv --flow-matrix-file ./inputs/flow-matrix.csv --vulnerability-scan ./inputs/scan.nessus --routing-file ./inputs/routing.csv --to-fiware-xml-topology ./output/topology-generated.xml
```

This execution of the script parse the following inputs files:
  - `./inputs/hosts-interfaces.csv`: The CSV file describing the hosts and their network interfaces.
  - `./inputs/vlan.csv`: The CSV file describing the vlans and their default gateway.
  - `./inputs/flow-matrix.csv`: The CSV file describing the flow matrix inside the information system.
  - `./inputs/scan.nessus`: The XML file output of the Nessus scanner.
  - `./inputs/scan-generic.json`: The JSON file containing services/vulnerabilities in a generic format.
  - `./inputs/routing.csv`: The CSV file describing the routes of the routers.
  - `./inputs/hosts-vms.csv`: The CSV file describing placement of VMs on physical hosts.
  - `./inputs/controllers-hosts.csv`: The CSV file describing placement of machines (physical and virtual) in orchestration domains.
  - `./inputs/ndn-topo.csv`: The CSV file describing NDN links, in the case of a hybrid IP/NDN network.
  - `./inputs/input-gci.xml`: The entire topology from Generic Collector Interface (XML file). If this file is provided, no other is needed or read.
  
The complete description of the inputs files can be found in [./doc/inputs-file-specifications.md](./doc/inputs-file-specifications.md).

It produces two output files:
  - `topology-generated.xml`: The XML file containing the description of the whole network topology.
	The exhaustive description of this XML file is provided in [./doc/topology-file-specifications.md](./doc/topology-file-specifications.md).
  - `mulval-output-file.P`: The mulval Datalog input file for this topology.

Here is the complete script manual:

```
usage: main.py [-h] --hosts-interfaces-file HOSTS_INTERFACES_FILE 
	--vlans-file VLANS_FILE 
	[--vulnerability-scan VULNERABILITY_SCAN [VULNERABILITY_SCAN ...]]
	[--openvas-scan OPENVAS_VULNERABILITY_SCAN [OPENVAS_VULNERABILITY_SCAN ...]] 
	[--generic-scan GENERIC_VULNERABILITY_SCAN [GENERIC_VULNERABILITY_SCAN ...]]
	[--flow-matrix-file FLOW_MATRIX_FILE] 
	[--routing-file ROUTING_FILE] 
	[--vm-mapping-file HOST_VM_FILE [HOST_VM_FILE ...]]
	[--controllers-file HOST_CONTROLLER_FILE [HOST_CONTROLLER_FILE ...]]
	[--gci-file GCI_INPUT_FILE]
	[--ndn-topology-file NDN_TOPOLOGY_FILE]
	[--mulval-output-file MULVAL_OUTPUT_FILE] 
	[--to-fiware-xml-topology TO_FIWARE_XML_TOPOLOGY] 
	[--display-infos] 
	[-v] [-vv]

Generates attack graph input files from topological files.

optional arguments:
  -h, --help            show this help message and exit
  --hosts-interfaces-file HOSTS_INTERFACES_FILE
                        The CSV file containing the hosts and the interfaces.
  --vlans-file VLANS_FILE
                        The CSV file containing the VLANS.
  --vulnerability-scan VULNERABILITY_SCAN [VULNERABILITY_SCAN ...]
                        The Nessus scanner report file(s).
  --openvas-scan OPENVAS_VULNERABILITY_SCAN [OPENVAS_VULNERABILITY_SCAN ...]
                        The OpenVAS scanner report file(s).
  --generic-scan GENERIC_VULNERABILITY_SCAN [GENERIC_VULNERABILITY_SCAN ...]
                        The generic services/vulnerabilities file(s).
  --flow-matrix-file FLOW_MATRIX_FILE
                        The CSV file containing the flow matrix
  --routing-file ROUTING_FILE
                        The CSV file containing the routing informations
  --vm-mapping-file HOST_VM_FILE [HOST_VM_FILE ...]
                        The CSV file describing placement of VMs on physical hosts.
  --controllers-file HOST_CONTROLLER_FILE [HOST_CONTROLLER_FILE ...]
                        The CSV file describing placement of machines (physical
                        and virtual) in orchestration domains.
  --gci-file GCI_INPUT_FILE
                        The XML file provided by the Generic Collector Interface :
                        It contains all the topology and should be used with no
                        other input file.
  --ndn-topology-file NDN_TOPOLOGY_FILE
                        The CSV file containing NDN links, in the case of a
                        hybrid IP/NDN network.
  --mulval-output-file MULVAL_OUTPUT_FILE
                        The output path where the mulval input file will be
                        stored.
  --to-fiware-xml-topology TO_FIWARE_XML_TOPOLOGY
                        The path where the XML topology file should be stored.
  --display-infos       Display information and statistics about the topology.
  -v                    Set log printing level to INFO
  -vv                   Set log printing level to DEBUG
```

## Docker build for CGI integration

Input generation from GCI XML file can be automated using the `gci-fetcher.py` file, and packaged in a standalone Docker container.

1) Copy and edit the config file

```
cp gci-fetcher-config.yaml.sample gci-fetcher-config.yaml
```

2) Build the container

```
docker build -t cyber-data-extract .
```

3) Start the container

```
docker run -ti cyber-data-extract
```
