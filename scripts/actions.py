#!/usr/bin/python3

import sys
import requests
import json
import re
from datetime import datetime


st = 0
en = ''

if len(sys.argv) > 1:

  if sys.argv[1] == 'help':
    print("\n  actions [start_idx] [end_date]\n")
    sys.exit(0)

  st = int(sys.argv[1])

  if len(sys.argv) > 2:
    en = sys.argv[2]

url='https://api.fxhash.xyz/graphql'
headers = {'content-type':'application/json', 'Accept-Charset':'UTF-8'}

data_template="""
{"query":"query
  Q($skip: Int, $take: Int, $sort: ActionsSortInput) {
    actions(skip: $skip, take: $take, sort: $sort) {
      id type metadata numericValue createdAt opHash
      issuer { id name }
      target { id name }
      token { id slug flag }
      objkt { id name slug }
    }
  }",
 "variables":{
   "skip":<START>,
   "take":50,
   "sort":{"createdAt":"DESC"}
  }
}
"""

filt_tm  = datetime.now()
if en != '':
  filt_tm = datetime.strptime(en, "%Y-%m-%dT%H:%M:%S.%fZ")

last_en = '...'
while last_en != en:
  data = re.sub('\n', ' ', re.sub('<START>', str(st), data_template))

  r = requests.post(url, data=data, headers=headers)
  if not r.ok:
    print("## ERROR")
    break

  json_data = r.json();
  if ("data" in json_data) and ("actions" in json_data["data"]):
    for a in json_data["data"]["actions"]:
      print(json.dumps(a))

  #print(json.dumps(r.json(), indent=2))

  resp = r.json()
  actions = resp["data"]["actions"]
  for a in actions:
    #print(a["id"], a["createdAt"])

    # ex: 2022-05-18T11:44:44.000Z
    #
    tm = datetime.strptime(a["createdAt"], "%Y-%m-%dT%H:%M:%S.%fZ")

    last_en = a["createdAt"]


  if last_en != '...':
    last_tm = datetime.strptime(last_en, "%Y-%m-%dT%H:%M:%S.%fZ")
    if last_tm < filt_tm:
      #print("ending...")
      break

  st += 50


