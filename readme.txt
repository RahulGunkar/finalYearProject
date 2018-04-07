
Precision farming refers to increasing the crop production by closely observing the environment conditions and taking the required steps.
This project is devided into two parts i)software part consist of a web app whose frontend consist of options for image stitching,ndvi generation etc..
In the hardware side..two ROS nodes are made using Raspberry Pi and Robots are given introduction according to the data generated from the wep app..



*********FOLLOW THE BELOW STEPS TO SETUP THE ENVIRONMENT*************************
1)Install docker...u can search the steps on internet or visit the following link
	"https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-16-04"

2)Down the zip file or clone the repository in a perticular folder..
Open the terminal and browse the path inside to that directory and run the following command
	$python setup.py

	-It will first run the requirements.txt file which will install the dependencies and then install ODM

3)You need to change the paths in the following files according to the location of the files in your pc
	-In the file "get_coord.py" change the path from  /home/rahulgunkar/Precision_farming-master/app/odm_orthophoto.tif

	to /your home/where folder exist/Precision_farming-master/app/odm_orthophoto.tif


	
