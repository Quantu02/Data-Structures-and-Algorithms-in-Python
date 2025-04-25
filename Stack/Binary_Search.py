def binary_search(data,target,low,high):
    if low>high:
        return False
    else:
        mid=(low+high)//2
        if target ==data[mid]:
            return True,mid
        elif target<data[mid]:
            return binary_search(data,target,low,mid-1)
        elif target>data[mid]:
            return binary_search(data,target,low,mid+1)
data=[i for i in range(100) ]
if binary_search(data,int(input("enter target:")),0,len(data)-1):
    print("element in list")
    