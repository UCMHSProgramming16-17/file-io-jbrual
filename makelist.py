# open file
file = open('mylist.txt', 'w')

# TODO: add items to file
for n in range(10):
    file.write(str(n + 1) + input("Item! ") + '\n')

# close file
file.close()