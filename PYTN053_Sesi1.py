#!/usr/bin/env python
# coding: utf-8

# Ini adalah markdown. Ini adalah  **bold**.

# In[1]:


100


# In[2]:


get_ipython().system('python --version')


# In[3]:


print(999)
#print menampilkan sesuatu - build in function , keyword


# In[4]:


type(999)
#menunjukkan type data


# In[5]:


type(3.14)


# In[6]:


type(1.0)


# In[7]:


type(1)


# In[10]:


print(1.)
type(1.)
print(.3)
type(.3)
#ga perlu nulis 0


# In[11]:


print(12345)
#ga ada tulisan OUT, dengan menulis print bentuk tampilan 12345, print ga nampilin output tp nampilin display


# In[12]:


1234
#dia ga nampilin tetapi cuma menghasilkan output


# In[13]:


print("hacktiv8")#double codes
print('hacktiv8') #single codes


# In[18]:


print("""hacktiv8""")#triple codes = untuk multiple lines
print('''hacktiv8''')
print("ha'tiv")
print("\"I am attending ha'tiv8\", he said")
print('\"I am attending ha\'tiv8", he said')
print("""
I ama ha'tiv.
I am attending hacktiv8
""")
#campsulation codes
#print('ha'tiv')= bakal error makanya meminimalisirkan 


# In[19]:


print(12345*10)


# In[20]:


type(print("hacktiv8")),type(None) #print cuma display saja maka tidak ada type data
#output itu ada nilai


# In[21]:


type(100), type(100.),type('100')


# In[22]:


100, 100., '100'


# In[23]:


type(-10), type(-10.)


# In[24]:


type(True), type(False)


# In[29]:


int(10.01), float(10), str(19), bool(1),bool(1000),bool(1.34),bool(-10) 
#convert type data
#primitive data type


# In[28]:


bool(0), bool(None),bool("") # ga ada datanya makanya false


# In[30]:


#Variable
n = 300
print(n)


# In[32]:


a=b=c=300
print(a,b,c)


# In[36]:


print(n, type(n))


# In[39]:


n = 1000
a = b = c = 500
x = y = 3.14
print(n, type(n))
print(a,b,c, type(a), type(b), type(c))
print(x,y, type(x), type(y))


# In[37]:


s = "Hacktivate"
n = str(n)
print(s, type(s))
print(n, type(n))


# In[ ]:


#klo di restart atau shut down perlu define lagi variable nya
# run all aja atau restart & run all
#has_laptops => slip case
# ga boleh diawali dengan angka 
# konstan = valuenya ga bisa diubah


# In[38]:


username ="syahrulhamdani"
num_students = 14
#ns = 14 bisa aja tp enakan readible
COUNT = 5
print(username, num_students, COUNT)
COUNT = 10
print(COUNT) #biasanya capital udh dianggap tidak akan berubah


# In[45]:


#print(a**b) = pangkat
print(a + b, type(a*b))
print(a * b, type(a / b))
print(a / b)
print(a // b, type( a // b))
print(5 // 2, type( 5 // 2))
print(5 / 2, type( 5 / 2))
print(4 / 2)
print(a - x, type(a - x))
print(a ** 2)
print(x ** 2)
print(n % 501)


# In[46]:


5 % 2


# In[48]:


#$5/2 = (2 * 2) + 1$


# In[55]:


print(s * 3)
print(s + s + s)


# In[58]:


print(s+ str(3)) 
print("hacktiv" + " " + "8")
print("hacktiv" + " " + "8", "hacktiv" + "8", "hacktiv" + str(8))


# In[62]:


print(s *-1)
print((s*3) *-1)
print("ackack" * -1)
type(print("ackack" * 0))


# In[63]:


book_title = "monty's python"
bootcamp_name = "hacktiv8"
password = "mY9nAmEIS"

print(book_title)
print(bootcamp_name)
print(book_title.title())
print(bootcamp_name.upper())
print(password.swapcase()) #built in method
print(password.lower()) #built in method of string
#' funtuation


# In[ ]:




