
import os
os.system("tput setaf 3")
print("\t\t<><><><><><><><><><><><><><><><>")
os.system("tput setaf 3")
print("\t\tWelcome To AWS Services")
os.system("tput setaf 3")
print("\t\t<><><><><><><><><><><><><><><><>")

while True:
    os.system("tput setaf 7")
    print("""
    \n
    1 : AWS Configure
    2 : See Launched Instances
    3 : Create key-pair
    4 : Create Security-Group
    5 : Launch ec2 Instance
    6 : Create Volume
    7 : Attach Volume To instance
    8 : start instances
    9 : stop instances
    10 : Terminate instances
    11 : exit
    """)
    ch = input("Enter Your Choice:")

    if int(ch) == 1:
        os.system("aws configure")
    elif int(ch) == 2:
        os.system("aws ec2 describe-instances")
    elif int(ch) == 3:
        print("Enter key name: ", end="")
        key_name = input()
        os.system("aws ec2 create-key-pair --key-name {}".format(key_name))
    elif int(ch) == 4:
        print("Enter Description name: ", end="")
        description = input()
        print("Enter security group name: ", end="")
        gr_name = input()
        print("Enter vpc ID: ", end="")
        vpc_id = input()
        os.system("aws ec2 create-security-group --description {} --group-name {} --vpc-id {}".format(description,gr_name,vpc_id))
    elif int(ch) == 5:
        print("Enter Image ID: ", end="")
        imgid = input()
        print("Enter instance name: ",end="")
        instancetype=input()
        print("Enter count: ",end="")
        count = input()
        print("Enter security group name: ",end="")
        sg = input()
        print("Enter key name: ",end="") 
        keyname = input()
        os.system("aws ec2 run-instances --image-id {} --instance-type {} --count {} --security-group-ids {} --key-name {}".format(imgid,instancetype,count,sg,keyname))
    elif int(ch) == 6:
        print("Enter availability zone to create EBS Volume: ", end="")
        az=input()
        print("Enter size to create EBS Volume: ", end="")
        ebs_size = input()
        os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az , ebs_size) )
    elif int(ch) == 7:
        print("Enetr EBS volume ID to attach EC2 instance: ",end="")
        ebs_vid = input()
        print("Enter EC2 instance ID to attach EBS volume: ",end="")
        ec2_id = input()
        os.system("aws ec2 attach-volume --volume-id {} --instance-id {} --device /dev/sdf".format(ebs_vid,ec2_id))
    elif int(ch) == 8:
        print("Enter instance ID: ", end="")
        instanceid = input()
        os.system("aws ec2 start-instances --instance-ids {}".format(instanceid))
    elif int(ch) == 9:
        print("Enter instance ID: ", end="")
        instanceid = input()
        os.system("aws ec2 stop-instances --instance-ids {}".format(instanceid))
    elif int(ch) == 10:
        print("Enter instance ID: ", end="")
        instanceid = input()
        os.system("aws ec2 Terminate-instances --instance-ids {}".format(instanceid))
    else:
        print("exit")
        break
