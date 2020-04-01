n = int(input())

d = {
	'ht' : "I hate that ",
	'lt' : "I love that ",
	'h' : "I hate it",
	'l' : "I love it"
}
out = ''

for i in range(1,n):
	if i == 0:
		print('')
		break
	elif n == 1:
		out+=d['h']
	elif i == 1:
		out += d['ht']
	elif i%2 == 0:
		out+=d['lt']
	else :
		out+=d['ht']
if n%2 == 0:
	out+=d['l']
else :
	out+=d['h']

print(out)
