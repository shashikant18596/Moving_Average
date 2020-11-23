#!/usr/bin/env python
# coding: utf-8

# In[1]:


def Moving_Average(n,w):
    i = 0
    moving_avg_result = []
    while i < len(n)-w+1:
        number = numbers[i : i + w]
        m_a = sum(number)/w
        moving_avg_result.append(m_a)
        i += 1
        print(moving_avg_result)

numbers = [3, 5, 7, 2, 8, 10, 11, 65, 72, 81, 99, 100, 150]
Moving_Average(numbers,3)


# In[ ]:




