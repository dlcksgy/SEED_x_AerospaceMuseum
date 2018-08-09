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
	if (strsys[11:13]=="15"):#midnight initalize
		os.system("sudo rm /var/log/apache2/access.log")
		fw=open("/var/log/apache2/access.log", 'a')
		os.system("sudo service apache2 restart")
		os.system("sudo chmod 777 /var/log/apache2/access.log")


	num =logdata()

	if (num[2]=='/'):
		num = "00" + num[0]
	elif(num[2]==' '):
		num = "0" + num[0:2]
	elif(num[0]!='0'):
		num = num[0:3]

#	intnum = int(num)
#	if(intnum%2==1):#odd
#		num = str((intnum+1)/2)
#	if(intnum%2==0):#even
#		num = str(intnum/2)
#
#	if(len(num)==1):
#		num = "00" + num
#	if(len(num)==2):
#		num = "0" + num
#	if(len(num)==3):
#		num = num

	bar = "barcode000000000"

	barcode = "scanner/"+bar + num + ".jpg"
	fw=open(barcode,'r')

	print barcode
except:

#	If you wanna clear at err
#	os.system("sudo rm /var/log/apache2/access.log")
#	fw=open("/var/log/apache2/access.log",'a')
#	os.system("sudo service apache2 restart")
#	os.system("sudo chmod 777 /var/log/apache2/access.log")


#	If you wanna inform expire coin today
	print ("scanner/expire.jpg")
