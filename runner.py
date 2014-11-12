#!/bin/python3
import json
from urllib import request
from pymongo import MongoClient

req = request.urlopen('http://sutd.sns-i2r.org/api/v1/measurements?per_page=1000')
data = json.loads(req.read().decode())
db = MongoClient().sensor
collection = db.data

for node in data['measurements']:
	collection.update({"node_guid": node['node_guid'], "recorded_at": node['recorded_at']}, node, upsert=True)
