#!flask/bin/python
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort
import subprocess
from subprocess import Popen, PIPE, STDOUT
import os

import MySQLdb
global name, names
global d
global e, r
global t,i
t = "RTNETLINK answers:" 
i=os.listdir("/sys/class/net")
r=[]
e=[]
d=1

cmd=('hostname','-I')
name = subprocess.Popen (cmd,stdout=subprocess.PIPE).communicate()[0]
name=name.rstrip()
name,sep,tail = name.partition(' ')

auth = HTTPBasicAuth()
app = Flask(__name__)

@auth.get_password
def get_password(username):
     if username =='key':
       with open("/home/ats/project/key.txt") as f:
         k = f.readlines()
         w=k[0].strip("\n")
       return w
     return None

conn = MySQLdb.connect("192.168.150.37","st","123","linux_traffic_shaping" )
c = conn.cursor()
# Print the contents of the database.
c.execute("SELECT * FROM ipkeys")
##############key update#############################################################
@app.route('/shaper/key_update=<string:m>', methods=['GET'])
@auth.login_required
def kem(m):
    tefile = open('/home/ats/project/key.txt','w')
    with open('/home/ats/project/key.txt','wb') as f:
         f.write("%s"%(m))

    return jsonify({'message':"key updated succcessfully"})
######################get password######################################################
###################################historylog######################################
 
@app.route('/shaper/history/interface=<string:x>',methods=['GET'])
@auth.login_required
def his(x):
    c=[]
    with open("/home/ats/project/his.txt") as f:
       lines = f.readlines()
       for line in lines:
              if(x in line and ("delay" in line or "loss" in line or "duplicate" in line or "reorder" in line)):
                m=[]
                l=[]
                line=line.strip('\n')
                y=line.split()
                m.append(y[10])
                l=y[0:4]+m+y[16:]
                n=" ".join(l) 
                c.append(n)
              if(x in line and ("pfifo_fast" in line and "bands" in line and "priomap" in line)):
                m=[]
                l=[]
                a=[]
                line=line.strip('\n')
                y=line.split()
                a.append("settings deleted")
                m.append(y[10])
                l=y[0:4]+m+a
                n=" ".join(l) 
                c.append(n)
    c=c[::-1] 
    return jsonify({'history': c })

@app.route('/shaper/history/interface=<string:x>/<int:s>',methods=['GET'])
@auth.login_required
def his1(x,s):
    c=[]
    with open("/home/ats/project/his.txt") as f:
       lines = f.readlines()
       for line in lines:
              if(x in line and ("delay" in line or "loss" in line or "duplicate" in line or "reorder" in line)):
                m=[]
                l=[]
                line=line.strip('\n')
                y=line.split()
                m.append(y[10])
                l=y[0:4]+m+y[16:]
                n=" ".join(l) 
                c.append(n)
              if(x in line and ("pfifo_fast" in line and "bands" in line and "priomap" in line)):
                m=[]
                l=[]
                a=[]
                line=line.strip('\n')
                y=line.split()
                a.append("settings deleted")
                m.append(y[10])
                l=y[0:4]+m+a
                n=" ".join(l) 
                c.append(n)
    c=c[::-1]
    return jsonify({'history': c[:s] })            
                     
    

########################################################################################

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
################################discovery of interfaces########################################################
@app.route('/shaper/interfaces', methods=['GET'])
@auth.login_required
def get_interfaces():
    ip=request.remote_addr
    i=os.listdir("/sys/class/net")
    return jsonify({'interfaces on this device':i})

##############################delay############################################
#for adding delay

@app.route('/shaper/pkt_delay', methods=['GET'])
@auth.login_required
def task_ad():
    m=request.args.get('interface')
    n=request.args.get('time')
    global i
    global t, names
    if(m in i):
     n=str(n)
     m=str(m)
     cmd = ' echo "atslabb00" |  sudo -S sudo tc qdisc add dev %s root netem delay %sms '%(m,n)
     p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     p.stdin.write('atslabb00')
     output=p.stdout.read()
     if(t in output): 
      return jsonify({'message':"Delay already exists on this interface."})  
     else:
      if(output=="Illegal \"latency\"\n"):
       return jsonify({'message':"add a valid latency or check the request"})        
      else:
       global name
       act="delay "+n+"ms"
       ip=request.remote_addr
       ip=str(ip)
       c.execute("INSERT INTO hislog (shaper, interfaces, action, IPadd) VALUES (%s, %s, %s, %s)",(names[0] , m, act, ip))
       conn.commit()
       return jsonify({'message1':"delay added succcessfully",'message2' : act}) 
    else: 
      return jsonify({'message':"not a valid interface or check the request"}) 
#########################################change delay########################################################

@app.route('/shaper/pkt_delay_change', methods=['GET'])
@auth.login_required
def task_chd():
    m=request.args.get('interface')
    n=request.args.get('time')
    global i
    global t, names
    if(m in i):
     m=str(m)
     cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc del dev %s root '%(m)
     p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     output1=p.stdout.read()
     if(t in output1):
       return jsonify({'message':"please add delay before changing it"})     
     else: 
      cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc add dev %s root netem delay %sms '%(m,n)
      p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
      output2=p.stdout.read()
      if(output2=="Illegal \"latency\"\n"):
       act="delay deleted"
       ip=request.remote_addr
       ip=str(ip)
       c.execute("INSERT INTO hislog (shaper, interfaces, action, IPadd) VALUES (%s, %s, %s, %s)",(names[0], m, act, ip))
       return jsonify({'message1':"Delay Change Failed because of invalid latency or request", 'message2':"The previous delay is deleted. "})  
      else:
       global name
       act="delay changed to "+n+"ms"
       ip=request.remote_addr
       ip=str(ip)
       c.execute("INSERT INTO hislog (shaper, interfaces, action, IPadd) VALUES (%s, %s, %s, %s)",(names[0], m, act, ip))
       conn.commit()
       return jsonify({'message1':"delay changes were successful",'message2' : act})   
    else: 
      return jsonify({'message':"not a valid interface or check the request"})

####################################DELETE#############################################
@app.route('/shaper/pkt_delay_del/interface=<string:k>', methods=['GET'])
@auth.login_required
def task_rd(k):
    ip=request.remote_addr
    global t
    global i, names
    if(k in i):
     cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc del dev %s root '%(k)
     p=Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     output=p.stdout.read()
     if(t in output):
      return jsonify({'message':"Please add delay to the interface before deleting it."})  
     else:
      global name
      act="delay deleted"
      ip=request.remote_addr
      ip=str(ip)
      c.execute("INSERT INTO hislog (shaper, interfaces, action, IPadd) VALUES (%s, %s, %s, %s)",(names[0],k, act, ip))
      conn.commit()
      return jsonify({'message':"delay removed succcessfully"})
    else: 
     return jsonify({'message':"not a valid interface or check the request"}) 

######################## end of delay ################################################################


############################ packet loss ##y#############################################################
#for changing packet loss 

@app.route('/shaper/pkt_loss', methods=['GET'])
@auth.login_required
def taskc_pl():
    ip=request.remote_addr
    m1=request.args.get('interface')
    n1=request.args.get('loss%')
    m1=str(m1)
    n1=str(n1)
    global i, names
    global t
    if(m1 in i):
     cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc change dev %s root netem loss %s '%(m1,n1)
     p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     output=p.stdout.read()
     if(t in output):
       return jsonify({'message':"you might first add delay to interface for packet loss "})  
     else:
      if (output=="Illegal \"loss percent\"\n" or output == "Unknown loss parameter: None\n"):
       return jsonify({'message':"please enter an interger for loss % or check the request"}) 
      else:
       global name
       act="loss added "+n1+"%"
       ip=request.remote_addr
       ip=str(ip)
       c.execute("INSERT INTO hislog (shaper,interfaces, action, IPadd) VALUES (%s,%s, %s, %s)",(names[0],m1, act, ip))
       conn.commit()
       return jsonify({'message1':"loss added succcessfully",'message2': act})      
    else: 
      return jsonify({'message':"not a valid interface or check the request"})
   

#####################################end of packet loss###################################################################
####
######################## packet duplication ###############################################################
#for changing packet duplication

@app.route('/shaper/pkt_dup', methods=['GET'])
@auth.login_required
def taskc_pd():
    ip=request.remote_addr
    m6=request.args.get('interface')
    n6=request.args.get('dup%')
    global t, names
    m6=str(m6)
    n6=str(n6)
    if(m6 in i):
     cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc change dev %s root netem duplicate %s '%(m6,n6)
     p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     output=p.stdout.read()
     if(t in output):
       return jsonify({'message':"you might first add delay to interface for packet duplication"})  
     elif (output=="Illegal \"duplicate\"\n"):
       return jsonify({'message':"please enter an interger for dup % or check the request"})
     global name
     act="duplication "+n6+"%"
     ip=request.remote_addr
     ip=str(ip)
     c.execute("INSERT INTO hislog (shaper,interfaces, action, IPadd) VALUES (%s,%s, %s, %s)",(names[0],m6, act, ip))
     conn.commit()
     return jsonify({'message1':"duplicated succcessfully",'message2': act})       
    else: 
      return jsonify({'message':"not a valid interface or check the request"}) 

#####################################end of packet duplication ###################################################################




#############################################packet reordering###################################################
@app.route('/shaper/pkt_reorder', methods=['GET'])
@auth.login_required
def taskc_pckt_ro():
    ip=request.remote_addr
    m2=request.args.get('interface')
    n2=request.args.get('delay')
    n3=request.args.get('reorder%')
    n4=request.args.get('corl%')
    global t, names
    if(m2 in i):
     n3=str(n3)
     n2=str(n2)
     n4=str(n4)
     cmd = ' echo "atslabb00" | sudo -S sudo tc qdisc change dev %s root netem delay %sms reorder %s %s '%(m2,n2,n3,n4)
     p = Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE, stderr=STDOUT, close_fds=True)
     output=p.stdout.read()
     if(t in output):
      return jsonify({'message':"you might first add delay to interface for packet reordering"})
     elif(output=="Illegal \"latency\"\n"):
      return jsonify({'message':"add a valid latency or check the request"})    
     elif (output=="Illegal \"reorder\"\n"):
      return jsonify({'message':"please enter an interger for reorder % or check the request"})
     elif ("What is" in output):
      return jsonify({'message':" invalid request"}) 
     else:
      global name
      act="packet reordering with delay "+n2+"with reorder"+n3+"%"+"correlation"+n4+"%"
      ip=request.remote_addr
      ip=str(ip)
      c.execute("INSERT INTO hislog (shaper,interfaces, action, IPadd) VALUES (%s,%s, %s, %s)",( names[0], m2, act, ip))
      conn.commit()
      return jsonify({'message':"packets reordered succcessfully"})    
    else: 
     return jsonify({'message':"not a valid interface or check the request"})

##############################################################################################################
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

