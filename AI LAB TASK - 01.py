#!/usr/bin/env python
# coding: utf-8

# # THIS IS HEADING

# # This is markdown
This is Raw NBConvert
# In[2]:


print("Hello!")
True + True


# In[4]:


True + True 


# In[5]:


not True


# In[6]:


True and False


# In[7]:


True or True


# In[8]:


False - True


# In[9]:


1<2<3 #and operator


# In[10]:


Name = "Mustafa"


# In[11]:


print(Name)


# In[12]:


"Mustafa" [-1]


# In[14]:


len(Name) #len is use for length


# In[15]:


"Mustafa" #literstring


# In[17]:


f"{Name}"


# In[18]:


Unknow var are not declear 
know var are declear / inlizalize


# In[22]:


studentData = ["Mustafa", 23, True, 4]


# In[24]:


studentData.append(8085)


# In[25]:


studentData


# In[27]:


studentData[1:3] 


# In[28]:


studentData[1::3]


# In[30]:


studentData[::-1] #REVSER ARRAY/LIST


# In[31]:


studentData.insert(1,2)


# In[32]:


studentData


# In[ ]:


# is use for refer


# In[33]:


tup = ("One", 4, 3.9, True)


# In[34]:


tup


# In[35]:


a, b, c = (1,2,4)


# In[36]:


*a, b, c = (1, 2, 3, 4 ,5) #unpad
a


# In[40]:


x = 10
y=16
x, y = y, x #swaping


# In[41]:


x


# In[44]:


myDict = {                             #"Key" : value
    "name" : "Fozia",
    "Age" : 30,
    "isMale" : 4
}


# In[45]:


myDict


# In[48]:


myDict.keys()
myDict.values()


# In[51]:


myDict.get("name")


# In[55]:


for i in range (5, 55, 5):
    print(i)


# In[56]:


#F STRING METHOD
print("{} is way to handsome".format("Mustafa"))


# In[59]:


#enumerate()

for i, value in enumerate(["Cat", "Dog", "Animal"]):
    print(i, value)


# In[60]:


for key, value in myDict.items():
    print(key, value)


# In[101]:


#program to find the lenth of string in first string and save it in secound string

listtwo = []
listone = ["Mustafa", 4, "Raza", 5, "Moiz", 6, True, 4.5] 
for i in listone:
    if(type(i) == str):
        listtwo.append(len(i))

listtwo


# In[100]:


listtwo


# In[ ]:




