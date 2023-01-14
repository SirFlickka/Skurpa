def storeData(data):

quantums = []

for i in range(len(data)):

quantums.append(data[i])

json = "{}".format(quantums)

fileName = "quantum_stored_data.json"

with open(fileName, "w") as f:

f.write(json)