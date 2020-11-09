import os
os.system("tput setaf 6")
menu=input("Where you do you want to run the menu?? (remote/local):\t")
while True:
	os.system("tput setaf 6")
	os.system("clear")
			
			
	print("""\n\n

	Press 1: To format name node

	Press 2: To start namenode/datanode service
			
	Press 3: To upload a file

	Press 4: to remove a file

	Press 5: To change the  block size
			
	Press 6: To see hadoop report
			
	Press 7: To reboot 

	Press 8 :To exit
	\n\n""")
	if menu=="local":

		choice=int(input("Enter your choice:\t"))
		if choice==1:
			os.system("hadoop namenode -format")
		
		elif choice==2:
			ser=input("Do you want to start datanode or namenode: (D/N)\t")
			if ser=="N":
				os.system("hadoop-deamon.sh start namenode")
			elif ser=="D":
				os.system("hadoop-daemon.sh start datanode")
			else:
				print("Invalid input")

		elif choice==3:
			f=input("Enter the file name:\t")
			os.system("hadoop fs -put {} /".format(f))

		elif choice==4:
			r=input("Enter the file to delete:\t")
			os.system("hadoop fs -rm {} /".format(r))
		
		elif choice==5:
			block=input("Enter the Block size in MB:\t")
			block=block*1024*1024
			os.system("hadoop fs -D dfs.block.size={}".format(block))
		
		elif choice==6:
			os.system("hadoop dfsadmin -report | less")

		elif choice==7:
			os.system("reboot")

		elif choice==8:
			exit()
		

		else:
			print("not supported")
		os.system("tput setaf 3")

		input("press any key to continue....")

	elif menu=="remote":
		ip=input("Enter the ip of the system where do you want to run the menu:\t")
		os.system("tput setaf 6")

		choice=int(input("Enter your choice:\t"))
		if choice==1:
			os.system("ssh {} hadoop namenode -format".format(ip))
		
		elif choice==2:
			ser=input("Do you want to start datanode or namenode: (D/N)\t")
			if ser==N:
				os.system("ssh {} hadoop-deamon.sh start namenode".format(ip))
			elif ser==D:
				os.system("ssh {} hadoop-daemon.sh start datanode".format(ip))
			else:
				print("Invalid input")

		elif choice==3:
			f=input("Enter the file name:\t")
			os.system("ssh {} hadoop fs -put {} /".format(ip,f))

		elif choice==4:
			r=input("Enter the file to delete:\t")
			os.system("ssh {} hadoop fs -rm {} /".format(ip,r))
		
		elif choice==5:
			block=int(input("Enter the Block size in MB:\t"))
			block=block*1024*1024
			os.system("ssh {} hadoop fs -D dfs.block.size={}".format(ip,block))
		
		elif choice==6:
			os.system("ssh {} hadoop dfsadmin -report | less".format(ip))

		elif choice==7:
			os.system("ssh {} reboot".format(ip))

		elif choice==8:
			exit()

		else:
			print("not supported")
		os.system("tput setaf 3")

		input("press any key to continue....")

	else:
		os.system("tput setaf 3")
		print("Oops!! your choice is not supported..")



	
	
		
