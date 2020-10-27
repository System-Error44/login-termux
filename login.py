#!/usr/bin/python
# coding=utf-8
from getpass import getpass
import time,os

w = "\033[1;0m"
r = "\033[1;31m"
g = '\033[1;32m'
y = '\033[1;33m'
b = '\033[1;34m'
s = '\033[1;36m'

logo = '''       _        _______  _______ _________ _    
      ( \      (  ___  )(  ____ \\__   ____/ \    /|  
      | (      | (   ) || (    \/   ) (   |  \  / |   
      | |      | |   | || |         | |   |   \ | |  
      | |      | |   | || | ____    | |   | /\ \/ | 
      | |      | |   | || | \_  )   | |   | | \   |  
      | (____/\| (___) || (___) |___) (___| /  \  |  
      (_______/(_______)(_______)\_______/|/    \_/ 
                                                      
   _______  _______  _______ _________ _______ _________
  (  ____ \(  ____ \(  ____ )\__   __/(  ____ )\__   __/
  | (    \/| (    \/| (    )|   ) (   | (    )|   ) (   
  | (_____ | |      | (____)|   | |   | (____)|   | |   
  (_____  )| |      |     __)   | |   |  _____)   | |   
        ) || |      | (\ (      | |   | (         | |   
  /\____) || (____/\| ) \ \_____) (___| )         | |   
  \_______)(_______/|/   \__/\_______/|/          )_(   '''
d = "  #====================================================#"
def menu():
	while True:
		try:
			os.system("clear")
			print(g+logo+w)
			print(y+"                                       System Error"+w)
			print("")
			print (d)
			print("")
			u = raw_input(y+"               username       :       "+s)
			print(w+"  #                                                    #")
			p = getpass(y+"               password       :       "+w)
			print("")
			print(w+d)
			if u=="user"  and p=="pass":
				print("")
				print(g+"                       Access Granted"+w)
				time.sleep(2)
				os.system("clear")
				print("")
				os.system("figlet -f ASCII-Shadow.flf !! BOSS !! | lolcat")
				print ("")
				print (d)
				print("")
				print (y+"             【W】【E】【L】【C】【O】【M】【E】")
				print("")
				print (s+"                         【T】【O】")
				print ("")
				print (y+"                【T】【E】【R】【M】【U】【X】"+w)
				print("")
				print (d)
				time.sleep(2.5)
				os.system("clear")
				print("")
				os.system("figlet -f ASCII-Shadow.flf TERMUX | lolcat")
				print("-----------------------------------------------------------")
				break
			else:
				print("")
				print(r+"                       Access Denied"+w)
				time.sleep(2)
				os.system("clear")
				print(g+logo+w)
				print ("  ======================================================")
				print ("")
				print (r+"                You Can't Login To My Termux"+w)
				print ("")
				print ("  ======================================================")
				time.sleep(2)
		except Exception:
			print ("")
			print(r+"                       Access Denied"+w)
			time.sleep(2)
		except KeyboardInterrupt:
			os.system("clear")
			print(g+logo+w)
			print (w+"  ======================================================")
			print ("")
			print (r+"                You Can't Login To My Termux"+w)
			print ("")
			print ("  ======================================================")
			time.sleep(2)
menu()
