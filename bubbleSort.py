import random

def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n): 
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
                arr[j], arr[j+1] = arr[j+1], arr[j] 

with open("generateNumbers.txt", "w") as myFile:
	for i in range(1,1000):
    		myFile.write(str(random.randint(0,1000))+'\n')
		#myFile.write('n')

try:
	with open("generateNumbers.txt") as f:
		res=[]
		data=f.read()
		arr=data.split('\n')
		for i in arr:
			try: 		
				res.append(int(i))
			except ValueError:
				pass
		
	bubbleSort(res)
except FileNotFoundError:
	data = None
print("Sorted Arrey: ")
print(str(res))
  	
