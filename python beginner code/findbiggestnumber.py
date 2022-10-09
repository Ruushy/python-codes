def finbiggestNumber(sample):
    biggest = sample[0]
    for i in range(1 , len(sample)):
        if sample[i] < biggest:
            biggest = sample[i]
    print(biggest , "this is the smallest number ")


finbiggestNumber([2,3,4,5,6,7,8,9 , 99, 121 , 111 , 1209])
