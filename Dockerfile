# Dockerfile to build the cyber-data-extract container for R2

# Based on Debian
FROM debian:jessie

# Configure local DNS and proxy
RUN echo "Acquire::http::proxy \"http://apt.theresis.org:3142\";" >> /etc/apt/apt.conf

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python python-pip python-yaml python-requests

# install the software
ADD . /root/cyber-data-extract
WORKDIR /root/cyber-data-extract

RUN mkdir /opt/cybercaptor
RUN cp /root/cyber-data-extract/vulnerability-remediation-database.db /opt/cybercaptor/vulnerability-remediation-database.db
RUN HTTPS_PROXY=http://10.222.146.131:3128/ pip install -r requirements.txt

CMD ["/usr/bin/python", "/root/cyber-data-extract/gci-fetcher.py", "--config", "/root/cyber-data-extract/gci-fetcher-config.yaml"]
