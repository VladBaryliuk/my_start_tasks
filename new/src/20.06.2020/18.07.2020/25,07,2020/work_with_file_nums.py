new_file = open('nums. txt', 'r')
help = 0
for i in new_file:
    help += int(i)
new_file.close()
print(help)
