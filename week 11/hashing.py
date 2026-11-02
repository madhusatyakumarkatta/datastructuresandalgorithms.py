# CSE25118 K MADHU SATYA KUMAR
# AV.SC.U4CSE25118

size = 10 
chain = [[] for i in range(size)] 
 
def separate_chaining(key): 
    index = key % size 
    chain[index].append(key) 
 
linear = [None] * size 
 
def linear_probing(key): 
    index = key % size 
    i = 0
    while linear[index] is not None and i < size: 
        index = (index + 1) % size 
        i += 1
    if i == size:
        print("Hash table is full")
        return
    linear[index] = key 
 
quadratic = [None] * size 
 
def quadratic_probing(key): 
    index = key % size 
    i = 0 
    while i < size: 
        new_index = (index + i * i) % size 
        if quadratic[new_index] is None: 
            quadratic[new_index] = key 
            return 
        i += 1 
    print("Hash table is full") 

print("CSE25118, K Madhu Satya Kumar") 
n = int(input("Enter number of elements: ")) 
keys = [] 
 
for i in range(n): 
    key = int(input("Enter key: ")) 
    keys.append(key) 
    separate_chaining(key) 
    linear_probing(key) 
    quadratic_probing(key) 
 
print("\nSeparate Chaining:") 
for i in range(size):  
    print(i, ":", chain[i]) 
print("\nLinear Probing:") 
print(linear) 
print("\nQuadratic Probing:") 
print(quadratic)
