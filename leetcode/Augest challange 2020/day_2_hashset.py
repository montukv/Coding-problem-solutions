'''
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet. 
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.

Example:

MyHashSet hashSet = new MyHashSet();
hashSet.add(1);         
hashSet.add(2);         
hashSet.contains(1);    // returns true
hashSet.contains(3);    // returns false (not found)
hashSet.add(2);          
hashSet.contains(2);    // returns true
hashSet.remove(2);          
hashSet.contains(2);    // returns false (already removed)

Note:

All values will be in the range of [0, 1000000].
The number of operations will be in the range of [1, 10000].
Please do not use the built-in HashSet library.
'''



class MyHashSet:
    def eval_hash(self, key):
        return ((key*1031237) & (1<<20) - 1)>>5

    def __init__(self):
        self.a = [[] for _ in range(1<<15)]        

    def add(self, key: int) -> None:
        pos = self.eval_hash(key)     #calling function foa a key to generate a position using hash formula 
        if key not in self.a[pos]:
            self.a[pos].append(key)
        

    def remove(self, key: int) -> None:
        pos = self.eval_hash(key)
        if key in self.a[pos]:
            self.a[pos].remove(key)
        

    def contains(self, key: int) -> bool:
        
        pos = self.eval_hash(key)
        print(pos,self.a[pos])
        if key in self.a[pos]:
            return True
        return False
        
'''
The idea is to have hash function in the following form.
image

Here we use the following notations:

K is our number (key), we want to hash.
a is some big odd number (sometimes good idea to use prime number) I choose a = 1031237 without any special reason, it is just random odd number.
m is length in bits of output we wan to have. We are given, that we have no more than 10000 operations overall, so we can choose such m, so that 2^m > 10000. I chose m = 15, so in this case we have less collistions.
if you go to wikipedia, you can read that w is size of machine word. Here we do not really matter, what is this size, we can choose any w > m. I chose m = 20.
So, everything is ready for function eval_hash(key): ((key*1031237) & (1<<20) - 1)>>5. Here I also used trick for fast bit operation modulo 2^t: for any s: s % (2^t) = s & (1<<t) - 1.'''