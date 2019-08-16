import json
import random
import urllib.request
# import urllib.request as urllib
import urllib3

HOST = 'localhost'
PORT = 8011
DB = 'uber'
USER = 'admin'
PASS = 'a'

def json_rpc(url,method,params):
    data = {
        "jsonrpc" : "2.0",
        "method" : method,
        "params" : params,
        "id" : random.randint(0,1000),
    }

    req = urllib.Request(url=url,data=json.dumps(data),
                         headers={"Content-Type":"application/json",
                                  })
    reply = json.load(urllib.urlopen(req))
    if reply.get("error"):
        raise Exception(reply["error"])
        return reply["result"]

def call(url,service,method,*args):
    return json_rpc(url,"call",{"service":service,"method":method,"args":args})

#Log in the given database
url = "http://%s:%s/jsonrpc" % (HOST,PORT)
userid = call(url,"common","login",DB,USER,PASS)

#Edir record
args = {
    'name' : 'NONAME',
}
data_id = call(url,"object","execute",DB,userid,PASS,'guest.user','write',[2],args)