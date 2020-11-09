import importlib
import os 
import getpass

os.system("tput setaf 3")
print("\t\t\t\t-----------------------------------------WELCOME-----------------------------------------")
os.system("tput setaf 6")

n=3
i=1
while i<=n:
	
	os.system("tput setaf 6")
	p=getpass.getpass("Enter the password:\t")
	if p!="Arth10_16":
		os.system("tput setaf 3")
		if i<3:
			
			print("Incorrect password....Try again")
		elif i==3:
			print("Sorry!")
		i=i+1
	
	else:
		os.system("tput setaf 6")
		while True:
			os.system("tput setaf 6")
			os.system("clear")
			
			
			print("""\n\n
			Press 1: To use LINUX 
			
			Press 2: To use AWS SERVICE

			Press 3: To use HADOOP

			Press 4: To use APACHE HTTPD SERVICE
			
			Press 5: To reboot 

			Press 6:To exit
			\n\n""")

			choice=int(input("Enter your choice:\t"))
			if choice==1:
					importlib.import_module("linux")
		
			elif choice==2:
					importlib.import_module("awscli")

			elif choice==3:
					importlib.import_module("hadoop")

			elif choice==4:
					importlib.import_module("httpd")
		
			elif choice==5:
					os.system("reboot")

			elif choice==6:
					exit()

			else:
				print("not supported")
			os.system("tput setaf 3")
			input("press any key to continue....")

			



