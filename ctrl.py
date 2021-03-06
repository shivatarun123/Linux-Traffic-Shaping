#!flask/bin/python
from flask_httpauth import HTTPBasicAuth
from flask import Flask, jsonify
from flask import request
from flask import make_response
from flask import abort
#from flask.ext.httpauth import HTTPBasicAuth	

import MySQLdb
global  r
r=[]

auth = HTTPBasicAuth()
app = Flask(__name__)
conn = MySQLdb.connect("localhost","root","123","task" )
c = conn.cursor()
# Print the contents of the database.
c.execute("SELECT * FROM ipkeys")

@app.route('/key_update=<string:m>', methods=['GET'])
@auth.login_required
def kem(m):
	global r
	c.execute("UPDATE ipkeys SET keyval=%s WHERE sno='1'",m)
	conn.commit()
	return jsonify({'message':"key updated succcessfully"})

@auth.get_password
def get_password(username):
    global r
    c.execute("SELECT * FROM ipkeys WHERE sno='1'")
    [(r[0], r[1]) for r in c.fetchall()]
    if username == 'key':
	return r[1]
    return None

###########################################################################################

@app.route('/shaper/settings/<string:ip>/<string:interface>', methods=['GET'])
def his3(ip,interface):
    c.execute("SELECT * FROM hislog WHERE shaper='%s' AND interfaces='%s' ORDER BY sno DESC LIMIT 0,1"%(ip,interface))
    return jsonify(list=[j  for j in c.fetchall()])
	
########################################HellloME#####################################
@app.route('/shaper/history/<string:n>', methods=['GET'])
def his1(n):
    c.execute("SELECT * FROM hislog ORDER BY sno DESC LIMIT 0,%s",n)
    return jsonify(list=[j  for j in c.fetchall()])
	

	
#####################################################################################

@app.route('/shaper/active/', methods=['GET'])
def his2():
    c.execute("SELECT * FROM ip_addr ORDER BY sno DESC LIMIT 0,100")
    return jsonify(list=[j  for j in c.fetchall()])
	

##############################################################################################################
@app.route('/controller',methods=['GET'])
def ctrl():
    return '''
<html>
<head>
  
    <title>controller</title>
    
<style>

input[value="Shaper nodes"] {
    width: 10%;
    background-color: #DB7093;
    color: white;
    padding: 14px 20px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[value="find interfaces"] {
    width: 10%;
    background-color: #00BFFF;
    color: white;
    padding: 4px 10px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
input[value="find settings"] {
    width: 10%;
    background-color:   #F08080;
    color: white;
    padding: 4px 10px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
input[value="history"] {
    width: 10%;
    background-color:   red;
    color: white;
    padding: 4px 10px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}

input[value="delete settings"] {
    width: 10%;
    background-color:   #9ACD32;
    color: white;
    padding: 4px 10px;
    margin: 8px 0;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
 body{
    background-color: white;
}
table {
    width:50%;
}
table, th, td {
    border: 1px solid black;
    border-collapse: collapse;
}
th, td {
    padding: 5px;
    text-align: left;
}
table#t01 tr:nth-child(even) {
    background-color: #eee;
}
table#t01 tr:nth-child(odd) {
   background-color:#fff;
}
table#t01 th {
    background-color: black;
    color: white;
}
</style>

</head>
<body>
<h1>Controller USER INTERFACE</h1>
<h4>Click to find  Available Shaper nodes</h4>
<script>
function shapernodes()
{
var url="http://localhost:5000/shaper/active/"
location.href=url;
return false;
}
</script>
<form onSubmit="return shapernodes();">
<input type="submit" value="Shaper nodes">
</form>


       <br/>

<script>       
function findinterfaces()
{
var url="http://"+document.getElementById("fi").value+":5000"+"/shaper/interfaces"
location.href=url;
return false;
}
</script>
            <form method="GET"  onSubmit="return findinterfaces();">
                
                        <h4>Interfaces on shaper Node</h4>
                        <label for="ip">Enter IP of Shaper Node :</label>
  
                        <input type="text" name="ip" id="fi" size="20">
                    
                <input type="submit" value="find interfaces">
         </form>
<script>             
function findsettings()
{
var url2="http://localhost:5000/shaper/settings/"+document.getElementById("shaperip").value+"/"+document.getElementById("shaperint").value
location.href=url2;
return false;
}
</script>
                 <form method="GET"  onSubmit="return findsettings();">
                
                        <h4>Settings on interfaces</h4>
                        <label for="ip">Enter IP of Shaper Node :</label>
                        <input type="text" name="ip" id="shaperip" size="20">
                        <label for="interface">Interface :</label>
                        <input type="text" name="interface" id="shaperint" size="20">
                    
                <input type="submit" value="find settings">
            </form>
            



<script>
function history()
{
var url3="http://localhost:5000/shaper/history/"+document.getElementById("num").value
location.href=url3;
return false;
}
</script>

            <form method="GET"  onSubmit="return history();">
                        <h4>History of shaper nodes</h4>
                        <label for="interface"> last no. of changes:</label>
                        <input type="text" name="number" id="num" size="20">
                    
                <input type="submit" value="history">
            </form>
            
<script>
function deletesettings()
{
var url5="http://"+ document.getElementById("ship1").value+":5000/shaper/pkt_delay_del/interface="+document.getElementById("shipint1").value
location.href=url5;
return false;
}
</script>           
            
            
            <form method="GET"  onSubmit="return deletesettings();">
                
                        <h4>Delete Settings on interfaces</h4>
                        <label for="ip">Enter IP of Shaper Node :</label>
                        <input type="text" name="ip" id="ship1" size="20">
                        <label for="interface">Interface :</label>
                        <input type="text" name="interface"  id="shipint1" size="20">
                    
                <input type="submit" value="delete settings">

             </form>
</body>
</html>
'''
	
########################################################################################################


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'Bad request'}), 400)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

