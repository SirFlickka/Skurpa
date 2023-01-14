def store_data(self, data):

self.data_id = data.id

self.data = [[0, 0], [0, 1], [1, 0], [1, 1]]

for row in data:

self.data[row] = self.data[row] + (1 * data[row][0])

def main():

print("Initializing store data")

store_data()

main()