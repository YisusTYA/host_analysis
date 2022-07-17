
from subprocess import *
import sys
import re
from ipaddress import *

class Host(object):
	"""docstring for Host"""
	def __init__(self, host):
		self.host = ip_address(host)

		process=Popen(["/bin/ping -c 1 %s" %self.host, ""], stdout=PIPE,shell=True)
		(stdout_data,stderr_data)=process.communicate()
		
		try:
			transmited=int(stdout_data.split()[20])
			received=int(stdout_data.split()[23])
			print('Host Connected')
		except ValueError:
			print('Host disconnected ')

	


		
 
#Comprobar que la máquina está en pie
#Comprobar sistema operativos
#Comprobar puertos

#Ejecución por consola
# print("Paso antes del __main__")
if __name__ == '__main__':
	
	host=Host(sys.argv[2])