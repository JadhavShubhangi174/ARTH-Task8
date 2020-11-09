import subprocess as sp

print()
print()
print()
print()
print()
print('Hey, Thankyou for clicking me....I will configure Httpd foy you')
print()
print()
print()
print()
print()

op= sp.getoutput
print(op('yum install httpd -y'))
print(op('echo Httpd Configured Edit this file >> /var/www/html/web.html'))
op('systemctl start httpd')
print(op('ifconfig enp0s3'))
print()
print('search In WebBrowser :  <ip>/web.html')
print()
print()
print()
