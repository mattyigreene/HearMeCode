#This is the beginning of my code to make a PB & J sandwhich

#bread = 4
#jelly = 2
#pb = 2

#if bread >= 2 and jelly >= 1 and pb >= 1:
#	print("yes")
#else:
#	print("nope.")
print('\t')
bread = input('Enter slices of bread\n')
jelly = input('Enter amount of jelly\n')
pb = input('Enter amount of peanutbutter\n')

if bread >= 1 and jelly >= 1 and pb >= 1:
	print("I can make this many:")

	if jelly == pb:
		bread = bread / 2

		if bread < jelly:
			print bread
		else:
			print jelly
	
	else:
		bread = bread / 2

		if pb > jelly:
			
			if jelly <= bread:
				print jelly

			else:
				print bread

		else:
			if pb <= bread:
				print pb

			else:
				print bread

else:
	print("nope.")
