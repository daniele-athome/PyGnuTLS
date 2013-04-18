#!/usr/bin/env python

"""Synchronous client using python-gnutls"""

import sys
import os
import socket

from gnutls.crypto import *
from gnutls.connection import *

script_path = os.path.realpath(os.path.dirname(sys.argv[0]))
certs_path = os.path.join(script_path, 'certs')

cert = OpenPGPCertificate(open(certs_path + '/valid-pgp.pub').read())
key = OpenPGPPrivateKey(open(certs_path + '/valid-pgp.key').read())
cred = OpenPGPCredentials(cert, key)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
session = ClientSession(sock, cred)

session.connect(('localhost', 10000))
session.handshake()
session.send("test\r\n")
buf = session.recv(1024)
print 'Received: ', buf.rstrip()
session.bye()
session.close()

