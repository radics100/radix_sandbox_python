class Allat:
	def __init__(self, tipus, nev, hang):
		self._tipus = tipus
		self._nev = nev
		self._hang = hang
		
	def tipus(self):
		return self._tipus
		
	def nev(self):
		return self._nev
		
	def hang(self):
		return self._hang
		
def print_animal(o):
	if not isinstance(o, Allat):
		#raise TypeError('print_animal(): requires an Animal')
		print('Az állat neve és a hang ', o.formatio.type(), o.nev(), o.hang())
				
def main():
	a1 = Allat('macska', 'Garfield', 'halk')
	a2 = Allat('kacsa', 'Donald', 'kvak')
	print_animal(a1)
	print_animal(a2)
		
main()	

		