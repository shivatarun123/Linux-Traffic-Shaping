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

AFTER INSTALLING PACKAGES MENTIONED IN INSTALL.txt

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
                                                                                                                             
THIS ENDS DEPLOYING ON NODES

 

