
# Buble_sort
n = 6
mas = [5,7,4,3,8,2]
count = 0
for run in range(n-1):
    for i in range (n-1-run):
        print(f'сейчас сравниваем {mas[i]} с {mas[i+1]}')
        if mas[i]>mas[i+1]:
            count += 1
            mas[i],mas[i+1] = mas [i+1],mas[i]
    print(mas)
print(count)





def binarysearch(mylist, search, start, stop):
    if start > stop:
        return False
    else:
        mid = (start + stop) //2
        if search == mylist[mid]:
           return  mid
        elif search <  mylist[mid]:
            return binarysearch(mylist, search, start, mid - 1)
        else:
            return binarysearch(mylist, search, mid +1, stop)

mylist = [10, 12, 13, 15, 20, 24, 27, 33, 42, 51, 57, 68, 70, 77, 79, 81]
search = 20
start = 0
stop = len(mylist)

x = binarysearch(mylist, search, start, stop)

if x == False:
    print("Item", search, "Not Found")

else:
    print("Item", search, "Found at Index", x)


