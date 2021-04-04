sym = 0
pol = 0
otr = 0
zero = 0
print ("input seven digitals")
for i in range (7):
    digitale =int (input ())
    if digitale > 0:
        pol += 1
    if digitale < 0:
        otr += 1
    if digitale == 0:
        zero += 1
    sym += digitale
print ("сумма =",sym)
print ("положительных чисел было",pol)
print ("отрицательных чисел было",otr)
print ("нулей было",zero)
