#import xmlrpclib
import xmlrpc.client as xmlrpclib

HOST='localhost'
PORT=8011
DB='uber'
USER='admin'
PASS='a'

root = 'http://%s:%d/xmlrpc/' % (HOST,PORT)

userid=xmlrpclib.ServerProxy(root+'common').login(DB,USER,PASS)
print("Logged in as %s (Userid: %d)" % (USER,userid))

#Create
socket = xmlrpclib.ServerProxy(root + 'object')
args = {
    'name':'DemoAbc',
    'email':'demoabc@gmail.com'
}

#data_id = socket.execute(DB,userid,PASS,'guest.user','create',args)
res = socket.execute(DB,userid,PASS,'guest.user','write',[1],args)
