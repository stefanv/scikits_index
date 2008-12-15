from itertools import *
from net import *
from utils import *

import cgi
import datetime
import wsgiref.handlers

import re
import os.path

#~ import xml.etree.ElementTree as ET

# set up locations
ROOT = os.path.dirname(__file__)

ON_DEV_SERVER = os.environ.get("SERVER_SOFTWARE", "dev").lower().startswith("dev")

REPO_PATH = "http://svn.scipy.org/svn/scikits/trunk"

#~ import rdfxml
#~ class Sink(object):
	#~ def __init__(self):
		#~ self.result = []
	#~ def triple(self, s, p, o):
		#~ self.result.append((s, p, o))
#~ def rdfToPython(s, base=None):
	#~ sink = Sink()
	#~ return rdfxml.parseRDF(s, base=None, sink=sink).result

#~ text = file("/home/janto/download/scikits.ann-0.2.dev-r803(4).xml").read()
#~ print rdfxml.parseRDF(text).result
#~ print rdfToPython(text)

#~ import PyRSS2Gen as RSS2

import time

# set up logging system
import logging
log_format = "%(levelname)s:%(module)s.%(name)s@%(asctime)s : %(message)s"
logging.basicConfig(
	level=logging.DEBUG,
	datefmt="%H:%M",
	format=log_format,
	)
logger = logging.getLogger("")
