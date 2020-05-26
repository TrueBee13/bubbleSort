import random


def printArray(arr):
	print('sorted Array: ')
	for i in range(len(arr)):
		print(arr[i])

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 
'''
for i in range(0,10000):
 a.append(random.randint(1,1000000))
  
bubbleSort(a)
printArray(a)
print('\n'.join(map(str, a))) 
'''
with open("generateNumbers.txt", "w") as myFile:
	for i in range(1,1000):
    		myFile.write(str(random.randint(0,1000))+'\n')
		#myFile.write('n')

try:
	with open("generateNumbers.txt") as f:
		res=[]
		data=f.read()
		arr=data.split('\n')
		for i in range(len(arr)-1):
			res.append(int(i))
		#print(res)
	bubbleSort(res)
	printArray(res)
except FileNotFoundError:
	data = None
print(data)
  	
