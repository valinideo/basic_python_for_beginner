li=[12,45,85,95,65,45,1,0,51,9,]
# Another way to arrenge li.sort()
new_li = []
while (len(li) > 0):
    min = li[0]
    for i in range(len(li)):
        if li[i] < min:
            min = li[i]
    new_li.append(min)  
    li.remove(min)
print('li=',li)
print('new list is = ',new_li)
