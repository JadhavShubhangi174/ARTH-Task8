import os
os.system("tput setaf 6")
menu=input("Where you do you want to run the menu?? (remote/local):\t")
while True:
	os.system("tput setaf 6")
	os.system("clear")
			
			
	print("""\n\n
	Press 1: To open Browser
			
	Press 2: To see date

	Press 3: To see Calendar

	Press 4: To open python interpreter
			
	Press 5: To create a directory
			
	Press 6: To run ifconfig
			
	Press 7: To open Text Editor
			
	Press 8: To reboot 

	Press 9 :To exit
	\n\n""")

	if menu=="local":

		choice=int(input("Enter your choice:\t"))
		if choice==1:
			os.system("firefox")
		
		elif choice==2:
			os.system("date")

		elif choice==3:
			os.system("cal")

		elif choice==4:
			os.system("python3")
		
		elif choice==5:
			d=input("Enter the directory:\t")
			os.system("mkdir {}".format(d))
		
		elif choice==6:
			os.system("ifconfig")

		elif choice==7:
			os.system("gedit")

		elif choice==8:
			os.system("reboot")

		elif choice==9:
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
			os.system("ssh {} firefox".format(ip))
		
		elif choice==2:
			os.system("ssh {} date".format(ip))

		elif choice==3:
			os.system("ssh {} cal".format(ip))

		elif choice==4:
			os.system("ssh {} python3".format(ip))
		
		
		elif choice==5:
			d=input("Enter the directory:\t")
			os.system("ssh {} mkdir {}".format(ip,d))
		
		elif choice==6:
			os.system("ssh {} ifconfig".format(ip))

		elif choice==7:
			os.system("ssh {} gedit".format(ip))

		elif choice==8:
				os.system("ssh {} reboot".format(ip))

		elif choice==9:
			exit()
		

		else:
			print("not supported")
		os.system("tput setaf 3")

		input("press any key to continue....")
	else:
		os.system("tput setaf 3")
		print("Oops!! your choice is not supported..")


