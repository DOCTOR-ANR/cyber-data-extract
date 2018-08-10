# Dockerfile to build the cyber-data-extract container for R2

# Based on Debian
FROM debian:jessie

# Configure local DNS and proxy (remove / change for build from another location)
ARG MY_HTTP_PROXY="http://10.222.146.131:80/"
ARG MY_HTTPS_PROXY="http://10.222.146.131:3128/"
ARG MY_NAME_SERVER="10.222.148.2"

RUN export http_proxy="${MY_HTTP_PROXY}"
RUN export https_proxy="${MY_HTTPS_PROXY}"
RUN export HTTP_PROXY="${MY_HTTP_PROXY}"
RUN export HTTPS_PROXY="${MY_HTTPS_PROXY}"
RUN echo "nameserver ${MY_NAME_SERVER}" > /etc/resolv.conf
RUN echo "Acquire::http::proxy \"http://apt.theresis.org:3142\";" >> /etc/apt/apt.conf

# Mode "REST" launch a REST web server waiting for incoming topology
# Mode "FETCH" launch a script fetching topology from an external rest server
ARG MODE="REST"
ENV MODE=${MODE}

# Upgrade / install dependences
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install python python-pip python-yaml python-requests python-flask wget git
#RUN pip install flask
#RUN apt-get -y install vim

# Install git-lfs
RUN mkdir -p /data/build/
WORKDIR /data/build
RUN wget -e https_proxy="${MY_HTTPS_PROXY}" -O git-lfs_2.0.2_amd64.deb https://packagecloud.io/github/git-lfs/packages/debian/jessie/git-lfs_2.0.2_amd64.deb/download
#RUN wget -O git-lfs_2.0.2_amd64.deb https://packagecloud.io/github/git-lfs/packages/debian/jessie/git-lfs_2.0.2_amd64.deb/download
RUN dpkg -i git-lfs_2.0.2_amd64.deb
RUN git lfs install

# Install the software
ADD . /root/cyber-data-extract
WORKDIR /root/cyber-data-extract

RUN mkdir /opt/cybercaptor
RUN cp /root/cyber-data-extract/vulnerability-remediation-database.db /opt/cybercaptor/vulnerability-remediation-database.db
RUN HTTPS_PROXY="${MY_HTTPS_PROXY}" pip install -r requirements.txt

ENV http_proxy ""
ENV HTTP_PROXY ""
#CMD ["/usr/bin/python", "/root/cyber-data-extract/auto-fetcher.py", "--config", "/root/cyber-data-extract/auto-fetcher-config.yaml"]
CMD ["/bin/bash", "/root/cyber-data-extract/run_from_mode.sh"]

