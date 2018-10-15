n = int(input())
arr = [int(x) for x in input().strip().split()]

def quick_sort(arg_arr):
    
    if(arg_arr == []):
        return []
    
    left = []
    right = []
    equal = [arg_arr[0]]
    p = arg_arr[0]
    for x in range(1,len(arg_arr)):
        if(arg_arr[x] > p):
            right.append(arg_arr[x])
        elif(arg_arr[x] < p ):
            left.append(arg_arr[x])
    
    if(len(arg_arr) == 1):
        return(left + equal + right)
    else: 
        result = quick_sort(left) + equal + quick_sort(right)
        print(''.join(str(e)+' ' for e in result))
        return(result)
    
quick_sort(arr)
