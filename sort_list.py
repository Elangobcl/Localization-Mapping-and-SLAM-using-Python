#a = [10,12,3,6,21,1, 29,50,0]
a = [10,12,3]
for x in range(len(a)):
   for y in range(len(a)):
    if(a[x] > a[y]):
        num1 = a[x]
        num2 = a[y]
        a[x] = num2
        a[y] = num1

print(a)

"""
a =x=y= [10,12,3] sort in descending
=> 1st x Loop
i. x = 0, y = 0
    o/p = 10,12,3
ii. x = 0, y = 1, a = [10,12,3]
    o/p = 10,12,3
iii. x = 0, y = 2, a = [10,12,3]
    o/p = 3,12,10

=> 2nd x Loop
a = [3,12,10]
i. x = 1, y = 0
    o/p = 12,3,10
ii. x = 1, y = 1, a=[12,3,10]
    o/p = 12,3,10
iii. x = 1, y = 2, a=[12,3,10]
    o/p = 12,3,10    

=> 3rd x Loop
a=[12,3,10]
i. x = 2, y = 0
    o/p = 12,3,10
ii. x = 2, y = 1, a=[12,3,10]
    o/p = 12,10,3
iii. x = 2, y = 2, a=[12,10,3]
    o/p = 12,10,3  
"""