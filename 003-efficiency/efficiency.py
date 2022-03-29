#!/usr/bin/env python
# coding: utf-8

# # Big O Notation

# One of the main goals of this lesson is to help you develop your ability to look at some code and identify its time complexity—and then describe this time complexity using Big O notation.
# 
# We will use this graph as a referece and reminder of the importance of the run time of an algorithm. We have the number of inputs (n) on the X axis and the the number of operations required (N) on the Y axis.
# 
# <img src="./assets/bigo.svg" alt="Drawing" style="width: 400px;"/>
# 
# ["Comparison of computational complexity"](https://commons.wikimedia.org/wiki/File:Comparison_computational_complexity.svg) by Cmglee. Used under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.en).

# #### Quadratic Example

# In[ ]:


# O(n^2)

def Quad_Example(our_list):
    for first_loop_item in our_list:
        for second_loop_item in our_list:
            print ("Items: {}, {}".format(first_loop_item,second_loop_item))
            
            
Quad_Example([1,2,3,4])

get_ipython().run_line_magic('time', '')


# #### Log Linear Example 

# In[ ]:


# O(nlogn)

# Don't worry about how this algorithm works, we will cover it later in the course!

def Log_Linear_Example(our_list):
    
    if len(our_list) < 2:
        return our_list
    
    else:
        mid = len(our_list)//2
        left = our_list[:mid]
        right = our_list[mid:]

        Log_Linear_Example(left)
        Log_Linear_Example(right)

        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                our_list[k]=left[i]
                i+=1
            else:
                our_list[k]=right[j]
                j+=1
            k+=1

        while i < len(left):
            our_list[k]=left[i]
            i+=1
            k+=1

        while j < len(right):
            our_list[k]=right[j]
            j+=1
            k+=1
        
        return our_list

Log_Linear_Example([56,23,11,90,65,4,35,65,84,12,4,0])

get_ipython().run_line_magic('time', '')


# #### Linear Example

# In[ ]:


# O(n)

def Linear_Example(our_list):
    for item in our_list:
        print ("Item: {}".format(item))

Linear_Example([1,2,3,4])

get_ipython().run_line_magic('time', '')


# #### Logarithmic Example

# In[ ]:


# O(logn)

def Logarithmic_Example(number):
    if number == 0: 
        return 0
    
    elif number == 1: 
        return 1
    
    else: 
        return Logarithmic_Example(number-1)+Logarithmic_Example(number-2)

    
Logarithmic_Example(29)

get_ipython().run_line_magic('time', '')


# #### Constant Example

# In[ ]:


# O(1)

def Constant_Example(our_list):
    return our_list.pop()

Constant_Example([1,2,3,4])

get_ipython().run_line_magic('time', '')

