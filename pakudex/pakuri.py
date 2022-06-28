
from hashlib import md5
from math import floor, sqrt

class Pakuri:
	
	def __init__(self, name, species, level):
		self.__name = name
		self.__species = species
		self.__level = level
	
	# Properties
	@property
	def name(self):
		return self.__name
	
	@property
	def species(self):
		return self.__species
	
	@property
	def hp(self):
		species_hash_int = int.from_bytes(md5(self.__species.encode()).digest(), byteorder='little')
		name_hash_int = int.from_bytes(md5(self.__name.encode()).digest(), byteorder='little')
		
		stamina = (species_hash_int + 11) % 16 + (name_hash_int + 11) % 16
		
		return floor(stamina * self.__level / 6)
	
	@property
	def cp(self):
		species_hash_int = int.from_bytes(md5(self.__species.encode()).digest(), byteorder='little')
		name_hash_int = int.from_bytes(md5(self.__name.encode()).digest(), byteorder='little')
		
		attack = species_hash_int % 16 + name_hash_int % 16
		defense = (species_hash_int + 5) % 16 + (name_hash_int + 5) % 16
		stamina = (species_hash_int + 11) % 16 + (name_hash_int + 11) % 16
		
		return floor(attack * sqrt(defense) * sqrt(stamina) * self.__level * 0.08)
	
	@property
	def level(self):
		return self.__level
	
	@level.setter
	def level(self, level):
		self.__level = level
	
	# Comparators
	def __lt__(self, pakuri2):
		return self.name < pakuri2
	
	def __le__(self, pakuri2):
		return self.name <= pakuri2
	
	def __gt__(self, pakuri2):
		return self.name > pakuri2
	
	def __ge__(self, pakuri2):
		return self.name >= pakuri2
	
	def __eq__(self, pakuri2):
		return self.name == pakuri2
	
	