def transpose_array(arr):
    # Use list comprehension to transpose the array
    return [[arr[j][i] for j in range(len(arr))] for i in range(len(arr[0]))]

def merge_arrays(arr1,arr2,row_col_choice):
    if row_col_choice == 1: #merge_by_row
        for i in arr1:
            if i in arr2:
                k1 = arr1.index(i)
                k2 = arr2.index(i)
                print(k1,k2)
                if k1 == len(arr1)-1 and k2 == 0:
                    arr1.extend(arr2[1:])
                    return arr1
                elif k1 == 0 and k2 == len(arr2[1:])-1:
                    arr2.extend(arr1)
                    return arr2
            else:
                print("Cannot be merged")
    elif row_col_choice == 0:
        arr1 = transpose_array(arr1)
        print(arr1)
        arr2 = transpose_array(arr2)
        print(arr2)
        for i in arr1:
            if i in arr2:
                k1 = arr1.index(i)
                k2 = arr2.index(i)
                print(k1,k2)
                if k1 == len(arr1)-1 and k2 == 0:
                    arr1.extend(arr2[1:])
                    return transpose_array(arr1)
                elif k1 == 0 and k2 == len(arr2[1:])-1:
                    arr2.extend(arr1)
                    return transpose_array(arr2)
            else:
                print("Cannot be merged")


arr1 = [[0, 1, 1, 0, 1], [1, 0, 1, 0, 1],[0,0,1,1,0]]
arr2 = [[1, 0, 1, 0, 1], [1, 1, 0, 0, 0], [0, 0, 1, 1, 1]]

for i in range(3):
    print(arr1[i])

print("---------")
for i in range(3):
    print(arr2[i])

    
print(merge_arrays(arr1,arr2,0))
