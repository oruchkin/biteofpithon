f = open("input.txt", "r")
vhod = f.readline()
vhod_list = vhod.split()
a = int(vhod_list[0])
b = int(vhod_list[1])

result = (a + b)


f = open("output.txt", "a")
f.writelines(f"{result}")
f.close()


f = open("output.txt", "r")
print(f.read())
