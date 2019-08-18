import requests
import json
import sys
import os
import poplib
import time
from email import parser
from html.parser import HTMLParser
from time import sleep
sys.path.append("././.")
from config import *

account_Email = sys.argv[1]
account_Password = sys.argv[2]
PROXY = sys.argv[3]
TOKEN = sys.argv[4]
foundLink = False
API_KEY = captchaAPI
site_key = '6Lef5iQTAAAAAKeIvIY-DeexoO3gj7ryl9rLMEnn'

## I'll work on verifier sometime ;) ##
