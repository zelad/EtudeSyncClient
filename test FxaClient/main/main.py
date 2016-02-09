#!/usr/bin/python
# -*- coding:Utf-8 -*-
'''
Created on 4 f�vr. 2016

@author: Kiki
'''
# from hashlib import sha256
# from binascii import hexlify
# import json
# import six
# import sys
# 
# import requests
# from requests_hawk import HawkAuth
# from fxa.core import Client as FxAClient

from client import SyncClient, get_browserid_assertion
from pprint import pprint

TOKENSERVER_URL = "https://token.services.mozilla.com/"
FXA_SERVER_URL = "https://api.accounts.firefox.com"

# def get_browserid_assertion(login, password, fxa_server_url=FXA_SERVER_URL,
#                             tokenserver_url=TOKENSERVER_URL):
#     """Trade a user and password for a BrowserID assertion and the client
#     state.
#     """
#     client = FxAClient(server_url=fxa_server_url)
#     session = client.login(login, password, keys=True)
#     bid_assertion = session.get_identity_assertion(tokenserver_url)
#     _, keyB = session.fetch_keys()
#     if isinstance(keyB, six.text_type):  # pragma: no cover
#         keyB = keyB.encode('utf-8')
#     return bid_assertion, hexlify(sha256(keyB).digest()[0:16])
#     return session

if __name__ == '__main__':
    bid_assertion_args = get_browserid_assertion("rbeck@assystem.com", "comptePourDev")
    client = SyncClient(*bid_assertion_args)
    
    pprint(client)
#     pprint(getattr(client, args.action)(*extra))
    