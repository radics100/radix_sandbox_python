# nevek1 = ['Józsi','Feri','Jucus','Gizike','Marika',10,23,-4,'János']
# nevek2 = ['Zalán','Márton','Gellért','Fercsi',98]
# for nev in nevek1:
	# print(nev)
# for nev in nevek2:
	# print(nev)
# def kinyomtato(nevek_listaja):
	# for nev in nevek_listaja:
		# if isinstance(nev,str):
			# print(nev.upper())
		# else:
			# print('nem szöveges karakter, hanem: ', str(type(nev)))
# kinyomtato(nevek1)
# kinyomtato(nevek2)
# def osszeadas1(a,b, c=4):
	# return a + b + c
# def osszeadas2(*args):
	# return sum(args)
# d = osszeadas1(34,56)
# print(d)
# print(osszeadas2(44,33,22,11,6,3))
###
# def udvozles(*args):
	# koszones = 'ennyi féle köszönés létezik: '
	# for k in args:
		# koszones += k 
		# koszones += ", "
	# print(koszones)
	# print(koszones[0:len(koszones)-2])
	
# udvozles('szia','hello','mizu','jó reggelt','adjon isten')
###
nevek1 = ['Józsi','Feri','Jucus','Gizike','Marika','János']
    for i,nev in enumerate(nevek1):
	 print(i, nev)
print(list(reversed(nevek1)))
