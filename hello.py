#from util import my_sum
import util
print(util.my_sum(4,9))
#print(my_sum(4,3))


l=[1,2,3,4]
m=[]
c =0
for item in l:
    
    l[c] = 2*item
    c= c+1
print(l) 


l = [100,200]
a,b, = l
print(a)
print(b)


l = [1,2,3,4]

for item in enumerate(l):
    print(item)


for index,item in enumerate(l):
    print("index Value: " + str(index))
    print("item Value: " + str(item))


print(list(map(lambda x: x*2,l)))
trs = (34,56)

listnew(trs)