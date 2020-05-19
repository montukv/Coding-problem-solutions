a = int(input()) 	#for single interger input
m,n=input().split()  	#know number of input for different variable
l=list(map(int,input().split()))

for i in l:			# for output in same line space seprated for list 
   print(i,end=' ') 


#long integer declaration
x = 1L #L or  l in suffix for long integer 


#dictionary input output
d={}
n = 3
d = [ map(str,raw_input().split()) for x in range(n)]
print(d) #display all
print(d["key"]) #display a perticular value

''' 
INPUT
A1023 CRT
A1029 Regulator
A1030 Therm

Desired Output:

{'A1023': 'CRT', 'A1029': 'Regulator', 'A1030': 'Therm'}
'''