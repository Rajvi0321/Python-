# Fibonacci Numbers.

# Taking input for length of series.
FS_len = int(input("Enter Length of the series you want : "))

# Defining first two number in list.
FS = [0, 1]

if FS_len<=len(FS) and FS_len>0:
    print(FS[:FS_len])
elif FS_len>0:
    while FS_len > len(FS):
        ele = FS[-1] + FS[-2]
        FS.append(ele)
    print(FS)
else:
    print("Invalid Length of Series.")