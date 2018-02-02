#!/usr/bin/python

from subprocess import call,Popen, PIPE
import sys, os, commands

homedir = os.getcwd()

buildcommand = """yum groupinstall "Development Tools" -y \n
yum install git ant ant-devel java-1.7.0-openjdk java-1.7.0-openjdk-devel mysql mysql-server tomcat6 mkisofs gcc python MySQL-python openssh-clients wget rpm-build ws-commons-util net-snmp net-snmp-devel genisoimage createrepo -y \n
mkdir -p public/download.cloudstack.org/centos/7/4.11 \n
wget http://www.us.apache.org/dist/maven/maven-3/3.5.2/binaries/apache-maven-3.5.2-bin.tar.gz \n
cd /usr/local/ \n
tar -zxvf %s/apache-maven-3.5.2-bin.tar.gz \n
cd %s \n
echo export M2_HOME=/usr/local/apache-maven-3.5.2 >> ~/.bashrc \n
echo export JAVA_HOME=/usr/lib/jvm/java-1.8.0 >> ~/.bashrc \n
echo export PATH=/usr/local/apache-maven-3.5.2/bin:${PATH} >> ~/.bashrc \n
source ~/.bashrc \n
wget http://www-eu.apache.org/dist/cloudstack/releases/4.10.0.0/apache-cloudstack-4.10.0.0-src.tar.bz2 \n
tar -jxvf apache-cloudstack-4.10.0.0-src.tar.bz2 \n
cd apache-cloudstack-4.10.0.0-src/deps \n
./install-non-oss.sh \n
cd ../packaging/centos7 \n
./package.sh
cd %s/apache-cloudstack-4.10.0.0-src/dist/rpmbuild/RPMS/x86_64/ \n
createrepo . \n
cp -rf * %s/public/cloudstack.apt-get.eu/rhel/4.10.0.0 \n
cd %s \n
\n""" % (homedir, homedir, homedir, homedir, homedir)

open('buildrpms.sh', 'w').write(buildcommand)

call(["chmod","a+x", "buildrpms.sh"], shell=False)

call(["./buildrpms.sh"], shell=True)




