#!/usr/bin/env python
# coding: utf-8

# In[1]:


word=input("enter the word")
reverse_word= ""
index=len(word)-1
while index >=0:
    reverse_word=reverse_word+word[index]
    index=index-1
print("the reverseword is :",reverse_word)


# In[ ]:




