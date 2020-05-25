stack = []
op = '+-*/'
def calculate(a):
	ans = 0
	for i in a:
		if i.isdigit():
			stack.append(i)
			#print(stack)
		if i in op:
			y,x = stack.pop(), stack.pop()
			#print(x,y,i)
			ans = _cal(float(x),float(y),i)
			stack.append(str(ans))
	return ans

def _cal(x,y,i):
	if i == '+':
		return x+y
	if i == '-':
		return x-y
	if i == '*':
		return x*y
	if i == '/':
		return x/y

a = ['2','3','*']
print(int(calculate(a)))