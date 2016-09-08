import time

f = open('1.txt', 'r')

while True:

    line = f.readline()

    if not line:
        time.sleep(1)
        print ('Nothing New')
    else:
        print ('Call Function: ', line)