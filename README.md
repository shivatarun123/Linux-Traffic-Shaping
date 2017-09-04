# Linux-Traffic-Shaping

Features of Linux Traffic Shaping Tool 
                                                                                                                             
Autostarts once deployed on nodes                                                                                     
Survives reboot                                                                                                       
Auto discovery of interfaces                                                                                          
performs Packet delay on interface using REST API                                                                     
performs Packet duplication on interface using REST API                                                               
performs Packet reordering using REST API                                                                             
performs delete settings using REST API                                                                               
Checks history using REST API                                                                                         
Checks whether log catches if settings performed on shaper from console                                               
Updates the key of controller node                                                                                    
Updates the key of shaper node                                                                                        
Tracks the settings done and by which shaper ,from controller node     

# AFTER INSTALLING PACKAGES MENTIONED IN INSTALL.txt

1. Deploy the following files On shaper nodes:                                                                         
		- make directory “project” like below                                                                          
		/home/ats/project                                                                                               
			-shaper.py                                                                                             
			-shaperd.sh                                                                                            
			-his.txt                                                                                               
			-key.txt                                                                                               
Enable read and write privileges on text files using                                                                   
		$sudo Chmod 777 filename                                                                                       
	- ​ The config files should be in                                                                                       
		/etc/supervisor/conf.d/                                                                                        
		-​ shaper.conf                                                                                                   
		-shaperd.conf                                                                                                  
2. Restart the supervisor using                                                                                        
		--sudo service supervisor restart                                                                              
                                                                                                                             
# THIS ENDS DEPLOYING ON NODES
# ON CONTROLLER NODE
                                                                                                                             
	Deploy ctrl.py,crtl.conf file on controller node and enable autostart using supervisor similar to shaper nodes         
		$cd /project                                                                                                   
			-ctrl.py                                                                                               
		$cd /etc/supervisor/conf.d/                                                                                    
			-ctrl.conf                                                                                             
		Supervisor restart                                                                                             
                                                                                                                              
	Database creation and grant of privileges:                                                                             
		create user 'newuser'@'localhost' identified by 'password​ ';                                                   
	grant all privileges ON * . * to 'user'@'ip_address'’                                                                  
		Create tables on database using script tables.py                                                               
			$ python tables.py                                                                                     
# THIS ENDS DEPLOYING ON CONTROLLER

1. Ping the destination from source through the shaper to notice changes or settings .
2. User will have the access to control node using a key provided.
	key:admin
3. Now from the control node, user can control and interact with the tool using curl commands.

 

