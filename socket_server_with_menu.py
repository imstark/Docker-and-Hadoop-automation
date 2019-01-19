#!/usr/bin/python36

import os
import subprocess
import subprocess as sp
import getpass
import trainmodel

if(trainmodel.confidence>80):
print("Welcome to my Tools ")
print("\t\t\t_ _ _ _ _ _ _ _ _ _ _ _ _ _")
import socket
s=socket.socket()
ip="192.168.43.240"
port = 1211
s.bind((ip,port))
s.listen(5) 
conn , addr = s.accept()


actual_pass = "redhat"
#var = ("""Enter your menu unique password ....""")
#print(var)
#s.send(var.encode())
password = conn.recv(100)
password = password.decode()
if password != actual_pass:
	var = ("you are not authrized to open this tool .....!")

else:
	
	var = ("Where you want to execute your tool (local/Remote) :")
conn.send(var.encode())	


platform = conn.recv(100)
platform = platform.decode()


while True:
	
	if platform == "local":

		os.system("clear")
	
		var = ("""
		Welcome ....
		
		press 1:To create Hadoop-HDFS-Cluster
		press 2:To create Hadoop-Map_reduce-cluster
		press 3:To create user
		press 4:To create file
		press 5:To exit


		Enter your choice .....
		""")

		conn.send(var.encode())
		ch = conn.recv(100)

		if int(ch) == 1:
			
			var = ("""welcome to hadoop-HDFS-cluster)
				==============================

				What you want to configure ...
				1:master
				2:slave 
				3:clent""")
			print(var)
			conn.send(var.encode())
			choice = conn.recv(100)

			var1 = ("enter the ip of the master")
			print(var1)
			conn.send(var1.encode())
			ch1 = conn.recv(100)

			if choice ==1:
				f= open("hdfs-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>dfs.name.dir</name>
			<value>/name</value>
			</property>
			</configuration>
			""")
				f.close()
				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()

				os.system("mkdir /name")
				os.system("hadoop namenode -format -y")
				os.system("hadoop-daemon.sh start namenode")
				os.system("hadoop dfsadmin -report")
			elif choice==2:
				f= open("hdfs-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>dfs.data.dir</name>
			<value>/data</value>
			</property>
			</configuration>
			""")
				f.close()

				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()
				os.system("hadoop-daemon.sh start datanode")
	
			elif choice==3:

				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()

		elif int(ch) == 2:
			
			print("welcome to hadoop-Map_Reduce-cluster:::\n")
			print("============================\n")

			print("What you want to configure ...\n 1:Job-Tracker  \n 2:Task-Tracker \n 3:clent")
			choice = int(input())

			print("enter the ip of the Job-Tracker")
			job_tracker_ip = input()

			print("Enter the ip of the Namenode")
			namenode_ip = input()
			if int(choice) == 1:
				f= open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>

			</configuration>
			""".format(namenode_ip))
				ff.close()
				os.system("hadoop-daemon.sh start jobtracker")
	
			if int(choice) == 2:
				f=open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				os.system("hadoop-daemon.sh start tasktracker")

			elif int(choice) ==3:
					
				f=open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				


		elif int(ch) == 3:
			print("Enter User Name :")
			user_name = input()
			user_create_output = subprocess.getstatusoutput("useradd {} ".format(user_name))
			if user_create_output[0] == 0:
				print("User_created....")
			else:
				print("User not created : {}".format(user_create_output[1]))
		elif int(ch) == 4:
			print("Enter File/directory name :")
			file_name = input()
			print("Enter directory path , which u want :")
			file_path = input()
			file_create_output = subprocess.getstatusoutput("mkdir {}/{} ".format(file_path , file_name))
			if file_create_output[0] == 0:
				print("File/Directory successfully created ....!")
			else:
				print("File/Directory not created : {} ".format(file_create_output[1])) 
			
	
		elif int(ch) == 5:
			exit()

		input("Enter to continue .....")

	elif platform == "remote":
		os.system("clear")

		print("Enter remote host IP : " , end='')
		remote_ip=input()

		print ("enter the passwd")
		passwd = input()


		print ("""
		press 1:To create Hadoop-HDFS-Cluster
		press 2:To create Hadoop-Map_reduce-cluster
		press 3:To create user
		press 4:To create file
		press 5:To click user_photo
		press 6:To user live_streaming
		press 7:To exit
		""")

		print("Enter your choice : ")

		ch = input()

		if int(ch) == 1:
			print("welcome to hadoop-HDFS-cluster:::\n")
			print("============================\n")

			print("What you want to configure ...\n 1:master::  \n 2:slave \n 3:clent")
			choice = int(input())

			print("enter the ip of the master")
			master_ip = input()

			if choice ==1:
				f= open("hdfs-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>dfs.name.dir</name>
			<value>/name</value>
			</property>
			</configuration>
			""")
				f.close()
				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()


				os.system("scp hdfs-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("ssh {} mkdir /name".format(remote_ip))
				os.system("scp core-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("ssh {} hadoop namenode -format -y".format(remote_ip))
				os.system("ssh {} hadoop-daemon.sh start namenode".format(remote_ip))
				os.system("ssh {} hadoop dfsadmin -report".format(remote_ip))
			elif choice==2:
				f= open("hdfs-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>dfs.data.dir</name>
			<value>/data</value>
			</property>
			</configuration>
			""")
				f.close()

				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()


				os.system("scp hdfs-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("scp core-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("ssh {} hadoop-daemon.sh start datanode".format(remote_ip))
	
			elif choice==3:

				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>
			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>
			</configuration>
			""".format(master_ip))
				ff.close()
				os.system("scp core-site.xml {}:/etc/hadoop".format(remote_ip))	





		elif int(ch) == 2:

			print("welcome to hadoop-Map_Reduce-cluster:::\n")
			print("============================\n")

			print("What you want to configure ...\n 1:Job-Tracker::  \n 2:Task-Tracker \n 3:clent")
			choice = int(input())

			print("enter the ip of the Job-Tracker")
			job_tracker_ip = input()

			print("Enter the ip of the Namenode")
			namenode_ip = input()
			if int(choice) == 1:
				f= open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				ff= open("core-site.xml" , "w")
				ff.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>fs.default.name</name>
			<value>hdfs://{}:9001</value>
			</property>

			</configuration>
			""".format(namenode_ip))
				ff.close()
				os.system("scp mapred-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("scp core-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("ssh {} hadoop-daemon.sh start jobtracker".format(remote_ip))
	
			if int(choice) == 2:
				f=open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				os.system("scp mapred-site.xml {}:/etc/hadoop".format(remote_ip))
				os.system("ssh {} hadoop-daemon.sh start tasktracker".format(remote_ip))
			if int(choice) == 3:
				f=open("mapred-site.xml" , "w")
				f.write("""
			<?xml version="1.0"?>
			<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>

			<!-- Put site-specific property overrides in this file. -->

			<configuration>

			<property>
			<name>mapred.job.tracker</name>
			<value>{}:9002</value>
			</property>

			</configuration>
			""".format(job_tracker_ip))
				f.close()
				os.system("scp mapred-site.xml {}:/etc/hadoop".format(remote_ip))

		elif int(ch) == 3:
			print("Enter User Name :")
			user_name = input()
			user_create_output = subprocess.getstatusoutput("ssh {} useradd {} ".format(remote_ip,user_name))
			if user_create_output[0] == 0:
				print("User_created....")
			else:
				print("User not created : {}".format(user_create_output[1]))
		elif int(ch) == 4:
			print("Enter File/directory name :")
			file_name = input()
			print("Enter directory path , which u want :")
			file_path = input()
			file_create_output = subprocess.getstatusoutput("ssh {} mkdir {}/{} ".format(remote_ip ,file_path , file_name))
			if file_create_output[0] == 0:
				print("File/Directory successfully created ....!")
			else:
				print("File/Directory not created : {} ".format(file_create_output[1])) 
	
		elif int(ch) == 5:
			c1 = "scp /root/Desktop/python_code/click_photo_file.py {}:/root/Desktop/click_photo_file.py".format(remote_ip)
			c2 = "ssh -X {} python36 /root/Desktop/click_photo_file.py".format(remote_ip)
			c3 = "scp {}:/root/Desktop/click.png  /root/Desktop/click.png".format(remote_ip)

			sp.getoutput(c1)
			sp.getoutput(c2)
			sp.getoutput(c3)

		elif int(ch) == 6:
			c1 = "scp /root/Desktop/python_code/video_capture.py {}:/root/Desktop/video_capture.py".format(remote_ip)
			c2 = "ssh -X {} python36 /root/Desktop/video_capture.py".format(remote_ip)
		
			sp.getoutput(c1)
			sp.getoutput(c2)

		elif int(ch) == 7:
			exit()
		
		input("Enter to continue .....")
	

	else:
		print("Platform Does not supported")	

