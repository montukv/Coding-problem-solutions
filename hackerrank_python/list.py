'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.

Input Format

The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.

Constraints

The elements added to the list must be integers.
Output Format

For each command of type print, print the list on a new line.

Sample Input 0

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]'''
l = []

def action(c):
	if c[0] == 'insert' :
		i = int(c[1])
		e = int(c[2])
		l.insert(i,e)
	if c[0] == 'print' :
		print(l)
	if c[0] == 'remove' :
		l.remove(int(c[1]))
	if c[0] == 'append' :
		l.append(int(c[1]))
	if c[0] == 'sort' :
		l.sort()
	if c[0] == 'pop' :
		l.pop()
	if c[0] == 'reverse' :
		l.reverse()


n = int(input())

for _ in range(n):
	command = input().split()
	action(command)
	command = []
