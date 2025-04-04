#!/usr/bin/env python
# coding: utf-8

# In[4]:


movie = 'Mega Blockbuster'

print(movie)


# In[6]:


movie = 'It\'s a Mega Blockbuster'

print(movie)


# In[8]:


movie = "It's a Mega Blockbuster"

print(movie)


# In[10]:


movie = '"Mega" Blockbuster'

print(movie)


# In[12]:


movie = '''It's a "Mega" Blockbuster'''

print(movie)


# In[16]:


movie = '''It's a "Mega" Blockbuster was a very good 
movie and I want to 
see it again so bad '''

print(movie)


# In[22]:


movie = 'Mega Blockbuster'
review = 'Was very good'

print(movie + ' ' + review.lower())


# In[24]:


movie * 4


# In[26]:


(movie + ' ') * 4


# In[29]:


sentence = "Let's go to the"
location = 'park'

print(sentence + ' ' + location)


# In[37]:


movie = '''It's a "Mega" Blockbuster'''

movie[0]


# In[39]:


movie[3]


# In[41]:


movie[-1]


# In[ ]:





# ## Assignment 1

# In[45]:


text1 = '          Your friend Mark'
text2 = 'was'
text3 = 'having'
text4 = 'a great day'
text5 = 'on the mountain'


# In[53]:


# Your code goes here - combine the letters in to a word and assign to the variable 'maven'
maven = text1[-4] + text2[1] + text3[2] + text4[4] + text5[-1]

print('The secret password is ' + maven)


# In[ ]:





# ### String clicing

# In[59]:


movie = "It's a Mega Blockbuster"


# In[61]:


movie[:4]


# In[63]:


movie[4:]


# In[65]:


movie[5:]


# In[67]:


movie[::2]


# In[69]:


movie[::-1]


# In[74]:


movie[-6:]


# In[ ]:





# In[77]:


a = "Let's go to the park"

a[-4:]


# In[ ]:





# ## Assignment 2

# In[81]:


testimonial = '''I love skiing. It's my favorite hobby.
Some people say, "It's not a hobby, it's life."
'''


# In[109]:


#First Draft
short_testimonial = testimonial[0:23] + testimonial[-7:-2]
print(short_testimonial)


# In[121]:


#Second Draft
happy_customer = short_testimonial[:7] + short_testimonial[-8:-1] + '!' 
print(happy_customer)


# In[ ]:





# ## Assignment 3 String Length

# In[125]:


alphabet = 'abcdefghijklmnopqrstuvwxyz'
message1 = 'Hello World!'
message2 = ''
message3 = 'It snowed a lot today'
message4 = 'eeee'
message5 = 'I love snow!!'


# In[139]:


password = alphabet[len(message1)] + alphabet[len(message2)] + alphabet[len(message3)] + alphabet[len(message4)] + alphabet[len(message5)]
password


# In[ ]:





# ### String Methods

# In[147]:


movie = "It's a Mega Blockbuster!"


# In[149]:


movie.upper()


# In[151]:


movie.lower()


# In[153]:


movie.strip('!')


# In[155]:


movie.rstrip('!')


# In[157]:


movie.lstrip('!')


# In[159]:


movie.replace('!', '.')


# In[161]:


movie.split()


# In[165]:


movie.split("'")


# In[169]:


word_list = movie.split()

word_list


# In[171]:


' '.join(word_list)


# In[185]:


movie.lower().replace("'", '').rstrip('!')


# In[187]:


text1 = '          Your friend Mark'
text2 = 'was'
text3 = 'having'
text4 = 'a great day'
text5 = 'on the mountain'


# In[197]:


full_text = ' '.join([text1, text2, text3, text4, text5])

full_text


# In[199]:


fixed_text = full_text.lower().strip()

fixed_text


# In[201]:


new_text = fixed_text.replace('on the mountain', 'at the ski shop')

new_text


# In[211]:


word_count = len(new_text.split())

word_count


# In[ ]:





# ## f-string

# In[214]:


movie = 'A Mega Blockbuster II'


# In[218]:


print(f'My favorite movie is: {movie.upper()}!')


# In[ ]:





# ## Assignment 3

# In[228]:


price = 499.99
product = 'snowboard'

# your print statement here
print(f'The {product} costs ${price}.')


# In[230]:


price = 19.99
product = 'scarf'

# exact copy of print statement in first cell 
print(f'The {product} costs ${price}.')


# In[ ]:




