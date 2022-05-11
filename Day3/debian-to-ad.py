#!/usr/bin/python

# Author: n4t5ru
# Email: hello@nasru.me
# Script: Debian to Active Directory

#required imports for the script to run
import socket
from subprocess import check_call

#installing the required packages
check_call(['apt','install','-y','realmd','libnss-sss','libpam-sss','sssd','sssd-tools','adcli','samba-common-bin','oddjob','oddjob-mkhomedir','packagekit','zsh'])

#User inputs
hostname = input('Enter Hostname: ')
domainName = input('Enter Domain Name: ')
domainAdmin = input('Enter Domain Admin: ')

#set hostname of the machine/system
hostDomainName = hostname + '.' + domainName
check_call(['hostnamectl', 'set-hostname', hostDomainName])

#Join Domain and restart service
check_call(['realm', 'join', '-v', '-U', domainAdmin, domainName])
check_call(['systemctl', 'restart', 'sssd'])

#check to see if everything is updated
print('Updated Hostname: ' + socket.getfqdn())