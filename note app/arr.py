def rev(arr1):
    arr2=[]
    for ele in arr1[::-1]:
        arr1.append(ele)
    print(arr2)


arr=[4,2,7,8,5]
print(arr)
rev(arr)
print(arr)