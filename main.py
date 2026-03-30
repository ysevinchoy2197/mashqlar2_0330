#5-misol
hisob = 0

def qo_shish(n):
    global hisob
    hisob += n

qo_shish(5)
qo_shish(3)
qo_shish(2)
print(hisob)


#6-misol
x = 10

def chop_et():
    print(x)

chop_et()


#7-misol
x = 5

def birinchi():
    global x
    x = 10

def ikkinchi():
    print(x)

birinchi()
ikkinchi()


#8-misol
counter = 0

def ortir():
    global counter
    counter += 1

def kamayt():
    global counter
    counter -= 1

ortir()
ortir()
ortir()
kamayt()
print(counter)


#9-misol
def yangi_qiymat():
    global z
    z = 99

print(z)
yangi_qiymat()
print(z)
