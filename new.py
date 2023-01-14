def store_data(data): 

x = 0

y = 0

for i in range(len(data)): 
x = x + data[i]
y = y + data[i]

if x != len(data) - 1 or y != len(data) - 1: 
print("Incorrect data")

else: 
print("Data stored in {} squared dimensions.".format(x*x+y*y))