from time import sleep
print("hello")
while True:
    
    pres = 101.2
    temp = 21.5
    
    f = open("test.txt", "a")
    data = "Pressure: " + str(pres)
    f.write(data)
    f.write('\n')
    print(data)
    f.close()
    sleep(2)