import os
import subprocess

def ossystemstring(input):
	cmd = [input]
	fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	fd_popen.close()
	return data
def logdata():
	cmd = ['wc','-l','/var/log/apache2/access.log']
	fd_popen = subprocess.Popen(cmd,stdout=subprocess.PIPE).stdout
	data = fd_popen.read().strip()
	fd_popen.close()
	return data
strsys = ossystemstring("date")
try :
#	if (strsys[11:13]=="15"):
#		os.system("sudo rm /var/log/apache2/access.log")
#		fw=open("/var/log/apache2/access.log", 'a')
#		os.system("sudo service apache2 restart")
#		os.system("sudo chmod 777 /var/log/apache2/access.log")


	num =logdata()
	if (num[2]=='/'):
		num = "00" + num[0]
	elif(num[2]==' '):
		num = "0" + num[0:2]
	elif(num[0]!='0'):
		num = num[0:3]

	bar = "barcode000000000"

	barcode = "scanner/"+bar + num + ".jpg"
	
	print barcode
except:
	os.system("sudo rm /var/log/apache2/access.log")
	fw=open("/var/log/apache2/access.log",'a')
	os.system("sudo service apache2 restart")
	os.system("sudo chmod 777 /var/log/apache2/access.log")
