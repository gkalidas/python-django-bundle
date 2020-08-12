import json

num = [1, 2, 3, 4, 5]

file_name = 'num.json'

with open(file_name, 'w') as file:
    json.dump(num, file)
    file.close()
print("Data has been save to ", file_name)

with open(file_name) as file:
    numbers = json.load(file)
    print("Data retrieved from the file")
    print(numbers)
