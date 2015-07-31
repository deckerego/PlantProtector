#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import logging

logging.basicConfig(level=logging.WARN, format='%(levelname)-8s %(message)s')
logger = logging.getLogger()

os.chdir(os.path.dirname(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), ".")))

from config import configuration
from trinket import Sensor
from bottle import Bottle, HTTPResponse, static_file, get, put, request, response, redirect, template
from os import listdir

application = Bottle()
application.install(Sensor())

@application.route('/favicon.ico')
def send_favicon():
	return static_file('favicon.ico', root='views/images')

@application.route('/js/<filename:path>')
def send_js(filename):
	return static_file(filename, root='views/js')

@application.route('/css/<filename:path>')
def send_css(filename):
	return static_file(filename, root='views/css')

@application.get('/')
def editor():
	return template('index')

@application.get('/sensor')
def sensor(sensor):
	return '{ "moisture": %s }' % sensor.readline()
