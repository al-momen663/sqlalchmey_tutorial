with open('data.txt', 'r') as file:
    content = file.read()  # this function is used to read file

print(content)

with open('results.txt', 'w') as file:
    file.write("Processed Data\nAccuracy: 95%")  # write into file using write() function