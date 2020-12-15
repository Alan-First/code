class Solution():
#    def __init__(self):
        #self.fastSort2 = fastSort2()
    
    def fastSort2(self,start,end,array):
        if start>=end:return
        key = array[start]
        low = start
        high = end
        while low<high:
            while low<high and array[high]>=key:
                high-=1
            if low<high:
                array[low] = array[high]
            while low<high and array[low]<key:
                low+=1
            if low < high:
                array[high] = array[low]
        array[low] = key
        self.fastSort2(start,low,array)
        self.fastSort2(low+1,end,array)
        return
    
 
test = Solution()
array = [1,7,13,5,8,26,2,11,3,6]
test.fastSort2(0,len(array)-1,array)
print(array)
