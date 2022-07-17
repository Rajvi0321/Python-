n = int (input ("Enter the number:  "))
n1 = 0
n2 = 1
if n <= 0:
    print 👎
elif n == 1:
    print 👎
else:
    count = 0
    while count <= n:
        nth = n1+n2
        print (nth)
        n1 = n2
        n2 = nth
        count = count + 1
