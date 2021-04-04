file1 = open(r'D:\Программирование\Влада программирование\interesting\file.txt', 'r', encoding='utf-8')
file = file1.read()
file1.close()
def unchipher(file):
    for i in file:
        help = ord(i)
        if not i.isalpha():
            file = file.replace(i, '')
        if help % 5 == 0:
            file = file.replace(i, '')
        if file.count(i) >= 33:
            file = file.replace(i, '')
    return file


print(unchipher(file))