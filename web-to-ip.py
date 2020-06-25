# -*- coding: utf-8 -*-
# Author D4RK5H4D0W5
G0 = "\033[0;32m"
G1 = "\033[1;32m"
C0 = "\033[0;36m"
C1 = "\033[1;36m"
P0 = "\033[0;35m"
P1 = "\033[1;35m"
W0 = "\033[0;37m"
W1 = "\033[1;37m"
B0 = "\033[0;34m"
B1 = "\033[1;34m"
R0 = "\033[0;31m"
R1 = "\033[1;31m"
Y1 = "\033[1;33m"
Y0 = "\033[0;33m"
import socket, os, sys
def ip(site):
	try:
		ip=socket.gethostbyname(site)
		print ('{}[{}•{}] {}'.format(W0,P0,W0,site))
		print ('{}[{}•{}] {}'.format(W0,P0,W0,ip))
		open('results.txt', 'a+').write(ip+'\n')
	except:
		pass
try:
	os.system('clear')
	print ('''%s
   _______  _____         __   __
  /  _/ _ \/ ___/______ _/ /  / /  ___ ____
 _/ // ___/ (_ / __/ _ `/ _ \/ _ \/ -_) __/
/___/_/   \___/_/  \_,_/_.__/_.__/\__/_/

'''%(C1))
	sites=open(sys.argv[1]).read().splitlines()
	for x in sites:
		ip(x)
		print ('')
	print ('{}[{}•{}] Done saved in results.txt'.format(W0,G0,W0))
except IndexError:
	exit('\n{}[{}•{}] Target website without http or https\n{}[{}•{}] Support python3 or python2\n{}[{}•{}] Use : python {} web.txt'.format(W0,R0,W0,W0,R0,W0,W0,R0,W0,sys.argv[0]))
except:
	exit('{}[{}•{}] File does not exist'.format(W0,R0,W0))
