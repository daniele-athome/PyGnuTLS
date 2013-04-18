#!/usr/bin/env python

"""Cryptographic examples using python-gnutls"""

import sys, os

from gnutls.crypto import *
from gnutls.constants import OPENPGP_FMT_RAW, OPENPGP_FMT_BASE64

script_path = os.path.realpath(os.path.dirname(sys.argv[0]))
certs_path = os.path.join(script_path, 'certs')

pkey = OpenPGPPrivateKey(open(certs_path + '/valid-pgp.key').read(), OPENPGP_FMT_BASE64)
print pkey

crt = OpenPGPCertificate(open(certs_path + '/valid-pgp.pub').read(), OPENPGP_FMT_BASE64)
print crt
uid = crt.uid()
print '\nU:'.join((uid, uid.name, uid.comment, uid.email))
