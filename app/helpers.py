import json
from datetime import datetime as dt, timedelta

st = {"status": "true"}
sf = {"status": "false"}

def clean(objts):
    res = []
    for obj in objts:
        data = json.loads(obj.to_json())
    	d = {}
    	for k,v in data.items():
	    if k=="_id": pass
	    elif k=="time_stamp": d[k] = (dt.fromtimestamp(v["$date"]/1000) - timedelta(hours=5, minutes=30)).strftime('%Y-%m-%d %H:%M:%S')
	    else: d[k] = v
	res.append(d)
    return res
