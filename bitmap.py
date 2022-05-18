#coding:utf-8
import os


class BitMap():
    def __init__(self,maxvalue=9999):
        #for 0~31 int
        self.step = 31
        self.size = ( maxvalue + self.step - 1 ) // self.step
        self.arr = [0 for _ in range(self.size)]

    def getindex(self,num):
        index = num // self.step
        step = num % self.step
        return index,step
    
    def set(self,num):
        index,step = self.getindex(num)
        self.arr[index] = self.arr[index] | (1<<step)

    def find(self,num):
        index,step = self.getindex(num)
        now = self.arr[index] & (1<<step)
        if now != 0 :
            return True
        return False

    def count(self):
        cnt = 0
        for item in self.arr:
            for i in range(self.step):
                if item & (1<<i):
                    cnt +=1
        return cnt


'''
cnt = 0
while n !=0 :
    n = n & (n -1) #去除最后一位1
    cnt += 1
'''
        

def main():
    array_list = [123,4323,132,123,4,53,6456,868,242,654,23,42,53,12]
    bitmap = BitMap(max(array_list))

    for item in array_list:
        bitmap.set(item)

    ans = []
    for item in range(max(array_list)+1):
        result = bitmap.find(item)
        if result:
            ans.append(item)
            #break
    print(bitmap.count())
    print(ans,"|",len(ans))
    print(array_list)
if __name__ == "__main__":
    main()