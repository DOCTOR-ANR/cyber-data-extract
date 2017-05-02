# Dockerfile to build the cyber-data-extract container for R2

# Based on Debian
FROM debian:jessie

# Configure local DNS and proxy (remove / change for build from another location)
ENV http_proxy http://10.222.146.131:80/
ENV https_proxy http://10.222.146.131:3128/
ENV HTTP_PROXY http://10.222.146.131:80/
ENV HTTPS_PROXY http://10.222.146.131:3128/
RUN echo "nameserver 10.222.148.2" > /etc/resolv.conf
RUN echo "Acquire::http::proxy \"http://apt.theresis.org:3142\";" >> /etc/apt/apt.conf

# Upgrade / install dependences
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python python-pip python-yaml python-requests wget git

# Install git-lfs
RUN mkdir -p /data/build/
WORKDIR /data/build
RUN wget -O git-lfs_2.0.2_amd64.deb https://packagecloud.io/github/git-lfs/packages/debian/jessie/git-lfs_2.0.2_amd64.deb/download
RUN dpkg -i git-lfs_2.0.2_amd64.deb
RUN git lfs install

# Install the software
ADD . /root/cyber-data-extract
WORKDIR /root/cyber-data-extract

RUN mkdir /opt/cybercaptor
RUN cp /root/cyber-data-extract/vulnerability-remediation-database.db /opt/cybercaptor/vulnerability-remediation-database.db
RUN pip install -r requirements.txt

ENV http_proxy ""
ENV HTTP_PROXY ""
CMD ["/usr/bin/python", "/root/cyber-data-extract/auto-fetcher.py", "--config", "/root/cyber-data-extract/auto-fetcher-config.yaml"]
