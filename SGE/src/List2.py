# D. Given a list of numbers, return a list where
# all adjacent == elements have been reduced to a single element,
# so [1, 2, 2, 3] returns [1, 2, 3]. You may create a new list or
# modify the passed in list.

def remove_adjacent(nums):
    
    
    if len(nums) > 1:
        
        index = 1
        
        while(index < len(nums)):
            
            if nums[index] == nums[index-1]:
            
                del nums[index]
                
                index-=1
                    
            index+=1        

    print "Resultado" ,nums    
        
    return nums
    
    


# E. Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists.


def linear_merge(list1, list2):
    
    print sorted(list1 + list2)
    
    return sorted(list1 + list2)
    
    