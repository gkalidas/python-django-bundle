# write to the file

f = open('test.txt', 'w')
content = "Writing file now has been changed."
f.write(content)
f.close()

# read from the file
f = open('test.txt', 'r')
content = f.read()
print("file content.\n", content)
