#!/usr/bin/bash

import os
import socket
from subprocess import STDOUT, check_call

#installing the required packages
check_call(['apt','install','-y','realmd','libnss-sss','libpam-sss','sssd','sssd-tools','adcli','samba-common-bin','oddjob','oddjob-mkhomedir','packagekit','zsh'], 
    STDOUT=open(os.devnull, 'wb'), stderr=STDOUT)

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