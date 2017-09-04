# Linux-Traffic-Shaping

###############################################################################################################################
#                                                                                                                             #
#							MANUAL                                                                # #                                                                                                                             #
###############################################################################################################################


########################### Features of Linux Traffic Shaping Tool ############################################################
#                                                                                                                             #
# 	Autostarts once deployed on nodes                                                                                     #
# 	Survives reboot                                                                                                       #
# 	Auto discovery of interfaces                                                                                          #
# 	performs Packet delay on interface using REST API                                                                     #
# 	performs Packet duplication on interface using REST API                                                               #
# 	performs Packet reordering using REST API                                                                             #
# 	performs delete settings using REST API                                                                               #
# 	Checks history using REST API                                                                                         #
# 	Checks whether log catches if settings performed on shaper from console                                               #
# 	Updates the key of controller node                                                                                    #
# 	Updates the key of shaper node                                                                                        #
# 	Tracks the settings done and by which shaper ,from controller node                                                    #
#                                                                                                                             #
###############################################################################################################################


################ AFTER INSTALLING PACKAGES MENTIONED IN INSTALL.txt ############################################################
#                                                                                                                              #
#	1. Deploy the following files On shaper nodes:                                                                         #
#		- make directory “project” like below                                                                          #
#		/home/ats/project                                                                                              # 
#			-shaper.py                                                                                             #
#			-shaperd.sh                                                                                            #
#			-his.txt                                                                                               #
#			-key.txt                                                                                               # 
#	Enable read and write privileges on text files using                                                                   #
#		$sudo Chmod 777 filename                                                                                       #
#	- ​ The config files should be in                                                                                       #
#		/etc/supervisor/conf.d/                                                                                        #
#		-​ shaper.conf                                                                                                  # 
#		-shaperd.conf                                                                                                  #
#	2. Restart the supervisor using                                                                                        #
#		--sudo service supervisor restart                                                                              #
#                                                                                                                              #
###########################THIS ENDS DEPLOYING ON NODES#########################################################################

#####################################ON CONTROLLER NODE#########################################################################
#                                                                                                                              #
#	Deploy ctrl.py,crtl.conf file on controller node and enable autostart using supervisor similar to shaper nodes         #
#		$cd /project                                                                                                   #
#			-ctrl.py                                                                                               #
#		$cd /etc/supervisor/conf.d/                                                                                    #
#			-ctrl.conf                                                                                             #
#		Supervisor restart                                                                                             #
#                                                                                                                              #
#	Database creation and grant of privileges:                                                                             #
#		create user 'newuser'@'localhost' identified by 'password​ ';                                                   #
#	grant all privileges ON * . * to 'user'@'ip_address'’                                                                  #
#		Create tables on database using script tables.py                                                               #
#			$ python tables.py                                                                                     #
##############################THIS ENDS DEPLOYING ON CONTROLLER#################################################################

################################################################################################################################



	1. Ping the destination from source through the shaper to notice changes or settings .
	2.. User will have the access to control node using a key provided.
		key:admin
	3. Now from the control node, user can control and interact with the tool using curl commands.

####################### TO SEE LIST OF INTERFACES ON THE DEVICE ################################################################
#	                                                                                                                       #
#	4. User can check the available interfaces for shaping:                                                                #
#                                                                                                                              #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/interfaces"                                                        #
#                                                                                                                              #
#	 This displays available interfaces on the device in the JSON format                                                   #
#			Example:                                                                                               #
#                             {                                                                                                #
# 			                                                                                                       #
#                               "interfaces on this device:"[                                                                  #
#					"lo",                                                                                  #
#					"br0",                                                                                 #
#					"eth0",                                                                                #
#					"eth1",                                                                                #
#					"eth2"                                                                                 #
#					]                                                                                      #
#					                                                                                       #
#				}                                                                                              #
################################################################################################################################

################################################################################################################################
#                                                                                                                              #
#	UserWill be able to apply settings to the traffic between source and destination1                                      #
#                                                                                                                              #
################################################################################################################################

#############################DELETE SETTINGS ON THE INTERFACE###################################################################
#                                                                                                                              #
#	7. -to delete settings on interface                                                                                    #
#                                                                                                                              #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/pkt_delay_del/interface="eth1""                                    #
#       The above command will delete all the settings on the interface                                                        #
#                                                                                                                              #
#	                                                                                                                       #
#			Example:                                                                                               #
#				{                                                                                              #
#                                      "message1": "delay removed successfully"                                                #
#				}                                                                                              #
#                                                                                                                              #
#                                                                                                                              #
################################################################################################################################	
	

#######################################################TO ADD DELAY##############################################################
#                                                                                                                               #
#                                                                                                                               #
#                                                                                                                               #
#	8. To add delay​ .                                                                                                       #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/pkt_delay?interface="eth1"&time=100"                                #
#          The above curl request will add delay to the selected interface.                                                     #
#		                                                                                                                #
#		Example:                                                                                                        #
#			{                                                                                                       #
#				"message1": "delay added successfully"                                                          #
#				"message1": "delay 100ms"                                                                       #
#			}                                                                                                       #
#                                                                                                                               #
#                                                                                                                               #
#################################################################################################################################

#############################################TO CHANGE DELAY ON THE INTERFACE#####################################################
#                                                                                                                                #
#        9. -to delay change                                                                                                     #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/pkt_delay_change?interface="eth1"&time=100"                          #
#	     The above curl requst will change the already existing delay to the new delay                                       #
#			Example:                                                                                                 #
#			{                                                                                                        #
#				"message1": "delay changes were successfull"                                                     # 
#				"message1": "delay changed to 100ms"                                                             #      
#			}                                                                                                        #
#                                                                                                                                #
#                                                                                                                                #
#                                                                                                                                #
##################################################################################################################################

############################### TO DO PACKET LOSS ################################################################################
#                                                                                                                                #
#                                                                                                                                #
#                                                                                                                                #
#                                                                                                                                #
#	10. -to apply packet loss                                                                                                #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/pkt_loss?interface="eth1"&loss%=16"                                  #
#           The above curl requst will drop the packets and displays the following message on the screen                         #
#                                                                                                                                #
#			{                                                                                                        #
#				"message1": "loss added successfully"                                                            # 
#				"message1": "loss added 16%"                                                                     #      
#			}                                                                                                        #
#                                                                                                                                #
##################################################################################################################################

##################################### TO REORDER PACKETS #########################################################################
#                                                                                                                                #
#	11. -for packet reordering                                                                                               #
#		~$ curl -u key:"1""<shaperip>:5000/shaper/pkt_reorder?interface="eth1"&delay="100"&reorder%="50"&corl%="25""     #
#		The above curl requst will reorder the packets as specified in the in request and displays the following message.#
#                                                                                                                                #
#                  {                                                                                                             #
#                      "message": "Packets reordered successfully"			                                         #
#		    }                                                                                                            #  
#                                                                                                                                #
##################################################################################################################################

######################################### TO DISPLAY HISTORY #####################################################################
#	12. -for history log                                                                                                     #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/history/interface="eth1""                                            #
#	    The above curl request will show the changes that were made on the given interface with timestamp                    #
#                                                                                                                                #
##################################################################################################################################

#################################### TO DUPLICATE PACKETS ########################################################################
#                                                                                                                                #
#	13. - for packet duplication                                                                                             #
#		~$ curl -u key:"1" "<shaper ip>:5000/shaper/pkt_dup?interface="eth1"&dup%="16""                                  #  
#            The above curl request will dulpicate the packets and displays the following message                                #
#                                                                                                                                #
#                  {                                                                                                             #
#                    "message1": "duplicated successfully"                                                                       #
#                    "message1": "duplication 16%"                                                                               #
#                  }                                                                                                             #
#                                                                                                                                #
##################################################################################################################################
	
################################### KEY UPDATE FOR CONTROLLER ###################################################################
#		                                                                                                                #
#       14. Key update:                                                                                                         #
#		User can also update the key in order to access the information from the controller node by giving
                the current key and specifying the new key ,he wants to change as below only through restapi.

                $ curl -u key:"admin"  "<controller ip>:5000/shaper/key_update/"new key""

                                                                                              #
#                                                                                                                               #
#                                                                                                                               #
##################################################CONTROLLER USER INTERFACE ###############################################
-Type the following URL on your browser:
     http://(ip):5000/controller
     (Here,ip refers to the controller node ip from which you want to have the control or access information about shapers)
-This shall open a user interface as shown in the attached controller_UI.png file
-Find the available shaper nodes by clicking on the button "shaper nodes"
-User can check the interfaces of a particular shaper node by giving its ip address and then click on the button "find interfaces"
-User can check the settings applied by the latest or any shaper node by giving its ip address and interface,then click on the button "find settings"(latest shaper can be found from history )
-User can check the history,that is which all acted as shapers previously,at what time and what are the settings applied on them  and ip addresses of the users who has done shaping, by giving a number(here "number" is the number of shapers and its changes user wants to see).And then click on the button "history",a list of shapers and there settings will be displayed in a list in json format in web browser,the first shaper in the list is the latest one.
-User can delete the settings done by the  shaper by giving its ip address and interface ,then click on the button "delete settings"    



