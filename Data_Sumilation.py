#!/usr/bin/env python
# coding: utf-8

# In[46]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df=pd.DataFrame()


# In[5]:


df


# In[6]:


city=['Dhaka','chattragram','Khulna']


# In[7]:


city


# In[8]:


df=pd.DataFrame(city)


# In[9]:


df


# In[10]:


df=pd.DataFrame(city, coloums=['city_'], index=['C1','C2','c3'])


# In[11]:


df=pd.DataFrame(city, columns=['City_Bangladesh'])
df


# In[12]:


df=pd.DataFrame(city, columns=['City_Bangladesh'], index =['c1','c2','c3'])
df


# In[13]:


city2=['Rajshahi', 'Shariatpur','Madaripur']


# In[14]:


df2=pd.DataFrame(zip(city,city2), columns=['city1', 'city2'])
df2


# In[17]:


df2.shape


# In[19]:


city3=[['Dhaka','Shariatpur'],['Chattragram', 'Coxs_Bazar'],['Khulna', 'jossor']]
city3


# In[20]:


df4=pd.DataFrame(city3, columns=['State','City'])


# In[21]:


df4


# In[22]:


dict1={
    'city1':city,
    'city2':city2
}


# In[23]:


dict1


# In[24]:


df5=pd.DataFrame(dict1)


# In[25]:


df5


# In[26]:


type(dict1)


# In[27]:


people_history = [
    ['John Smith', 28, 'New York City', 'New York', 'USA', 'Bachelors', 2018, 'O+'],
    ['Emma Johnson', 34, 'Los Angeles', 'California', 'USA', 'Masters', 2012, 'A+'],
    ['Olivia Williams', 30, 'Chicago', 'Illinois', 'USA', 'PhD', 2015, 'B+'],
    ['Liam Brown', 27, 'Houston', 'Texas', 'USA', 'Bachelors', 2019, 'AB+'],
    ['Sophia Jones', 22, 'Phoenix', 'Arizona', 'USA', 'High School', 2020, 'O-'],
    ['Noah Miller', 31, 'Philadelphia', 'Pennsylvania', 'USA', 'Masters', 2014, 'A-'],
    ['Ava Davis', 29, 'San Antonio', 'Texas', 'USA', 'Bachelors', 2016, 'B-'],
    ['Isabella Wilson', 25, 'San Diego', 'California', 'USA', 'Bachelors', 2017, 'O+'],
    ['Lucas Martinez', 35, 'Dallas', 'Texas', 'USA', 'PhD', 2010, 'A+'],
    ['Mason Anderson', 33, 'San Jose', 'California', 'USA', 'Masters', 2013, 'AB-'],
    ['Harper Thomas', 26, 'Austin', 'Texas', 'USA', 'Bachelors', 2018, 'O-'],
    ['Ethan Jackson', 32, 'Jacksonville', 'Florida', 'USA', 'Masters', 2011, 'B+'],
    ['Ella White', 24, 'Fort Worth', 'Texas', 'USA', 'Bachelors', 2019, 'A-'],
    ['James Harris', 28, 'Columbus', 'Ohio', 'USA', 'Bachelors', 2015, 'O+'],
    ['Alexander Martin', 34, 'Charlotte', 'North Carolina', 'USA', 'PhD', 2012, 'AB+'],
    ['Amelia Thompson', 29, 'San Francisco', 'California', 'USA', 'Masters', 2014, 'B-'],
    ['Benjamin Garcia', 31, 'Indianapolis', 'Indiana', 'USA', 'Bachelors', 2016, 'O+'],
    ['Mia Martinez', 27, 'Seattle', 'Washington', 'USA', 'Bachelors', 2018, 'A+'],
    ['William Rodriguez', 30, 'Denver', 'Colorado', 'USA', 'Masters', 2013, 'AB-'],
    ['Charlotte Clark', 25, 'Washington', 'District of Columbia', 'USA', 'Bachelors', 2017, 'B+'],
    ['Sebastian Lee', 35, 'Boston', 'Massachusetts', 'USA', 'PhD', 2010, 'O-'],
    ['Aiden Walker', 28, 'El Paso', 'Texas', 'USA', 'Masters', 2015, 'A+'],
    ['Chloe Young', 33, 'Detroit', 'Michigan', 'USA', 'Bachelors', 2011, 'B+'],
    ['Henry Allen', 26, 'Nashville', 'Tennessee', 'USA', 'Bachelors', 2019, 'AB+'],
    ['Grace King', 32, 'Memphis', 'Tennessee', 'USA', 'Masters', 2014, 'O-'],
    ['Jackson Wright', 29, 'Portland', 'Oregon', 'USA', 'PhD', 2016, 'B-'],
    ['Isabelle Hill', 24, 'Oklahoma City', 'Oklahoma', 'USA', 'Bachelors', 2018, 'A+'],
    ['Daniel Scott', 31, 'Las Vegas', 'Nevada', 'USA', 'Masters', 2013, 'AB-'],
    ['Emily Green', 27, 'Louisville', 'Kentucky', 'USA', 'Bachelors', 2017, 'O+'],
    ['Jack Adams', 30, 'Baltimore', 'Maryland', 'USA', 'Masters', 2012, 'A-'],
    ['Evelyn Nelson', 28, 'Milwaukee', 'Wisconsin', 'USA', 'Bachelors', 2015, 'B+'],
    ['Owen Carter', 35, 'Albuquerque', 'New Mexico', 'USA', 'PhD', 2009, 'O-'],
    ['Aria Mitchell', 29, 'Tucson', 'Arizona', 'USA', 'Bachelors', 2016, 'A+'],
    ['Matthew Perez', 34, 'Fresno', 'California', 'USA', 'Masters', 2011, 'AB+'],
    ['Lily Roberts', 27, 'Sacramento', 'California', 'USA', 'Bachelors', 2018, 'B-'],
    ['Elijah Turner', 32, 'Kansas City', 'Missouri', 'USA', 'Masters', 2013, 'O+'],
    ['Ella Phillips', 25, 'Mesa', 'Arizona', 'USA', 'Bachelors', 2017, 'A+'],
    ['Logan Campbell', 31, 'Atlanta', 'Georgia', 'USA', 'Masters', 2014, 'AB-'],
    ['Abigail Parker', 28, 'Colorado Springs', 'Colorado', 'USA', 'Bachelors', 2015, 'B+'],
    ['Samuel Evans', 30, 'Miami', 'Florida', 'USA', 'Masters', 2012, 'O-'],
    ['Sofia Edwards', 26, 'Raleigh', 'North Carolina', 'USA', 'Bachelors', 2019, 'A+'],
    ['David Collins', 33, 'Omaha', 'Nebraska', 'USA', 'Masters', 2011, 'AB+'],
    ['Scarlett Stewart', 31, 'Long Beach', 'California', 'USA', 'PhD', 2014, 'B-'],
    ['Joseph Morris', 29, 'Virginia Beach', 'Virginia', 'USA', 'Bachelors', 2017, 'O+'],
    ['Victoria Rogers', 27, 'Oakland', 'California', 'USA', 'Masters', 2018, 'A-'],
    ['James Bell', 34, 'Minneapolis', 'Minnesota', 'USA', 'PhD', 2012, 'B+'],
    ['Avery Murphy', 30, 'Tulsa', 'Oklahoma', 'USA', 'Masters', 2015, 'O-'],
    ['Lucas Rivera', 28, 'Arlington', 'Texas', 'USA', 'Bachelors', 2016, 'A+'],
    ['Mia Cooper', 32, 'New Orleans', 'Louisiana', 'USA', 'Masters', 2013, 'AB+'],
    ['Mason Bailey', 35, 'Wichita', 'Kansas', 'USA', 'PhD', 2010, 'B-'],
    ['Evelyn Barnes', 29, 'Cleveland', 'Ohio', 'USA', 'Bachelors', 2017, 'O+'],
    ['Daniel Brooks', 27, 'Tampa', 'Florida', 'USA', 'Masters', 2018, 'A-'],
    ['Ella Powell', 26, 'Bakersfield', 'California', 'USA', 'Bachelors', 2019, 'B+'],
    ['Oliver Sanchez', 31, 'Aurora', 'Colorado', 'USA', 'PhD', 2014, 'O-'],
    ['Avery Foster', 30, 'Anaheim', 'California', 'USA', 'Masters', 2012, 'A+'],
    ['Liam Simmons', 34, 'Honolulu', 'Hawaii', 'USA', 'Bachelors', 2011, 'AB+'],
    ['Isabella Myers', 25, 'Riverside', 'California', 'USA', 'Bachelors', 2018, 'B-'],
    ['Lucas Long', 28, 'Santa Ana', 'California', 'USA', 'Masters', 2016, 'O+'],
    ['Amelia Richardson', 33, 'Corpus Christi', 'Texas', 'USA', 'PhD', 2012, 'A+'],
    ['Benjamin Ward', 29, 'Lexington', 'Kentucky', 'USA', 'Bachelors', 2015, 'AB-'],
    ['Charlotte Russell', 31, 'Henderson', 'Nevada', 'USA', 'Masters', 2013, 'B+'],
    ['James Barnes', 27, 'Stockton', 'California', 'USA', 'Bachelors', 2019, 'O-'],
    ['Ella Hamilton', 35, 'Saint Paul', 'Minnesota', 'USA', 'PhD', 2011, 'A+'],
    ['William Watson', 30, 'Cincinnati', 'Ohio', 'USA', 'Masters', 2012, 'AB+'],
    ['Sofia Brooks', 32, 'Greensboro', 'North Carolina', 'USA', 'Bachelors', 2014, 'B-'],
    ['Daniel Henderson', 28, 'Plano', 'Texas', 'USA', 'Masters',]]


# In[28]:


people_history


# In[29]:


df5=pd.DataFrame(people_history, columns=['Name','Age','Location','State', 'Country','Education','Passing_Year','Blood_Group'])


# In[30]:


df5


# In[31]:


type(df5)


# In[32]:


df5.head(10)


# In[34]:


df5['Education'].sort_values()


# In[35]:


df5.sort_values('Age')


# In[36]:


df5.describe()


# In[37]:


df5.corr()


# In[42]:


sns.heatmap(df5.corr(Age,Passing_Year), annot=True)


# In[43]:


df5[['Age', 'Passing_Year']].corr()


# In[44]:


sns.heatmap(correlation_matrix, annot=True)


# In[48]:


df5 = pd.DataFrame(people_history)


# In[49]:


correlation_matrix = df5[['Age', 'Passing_Year']].corr()


# In[50]:


sns.heatmap(correlation_matrix, annot=True)


# In[51]:


df5.head()


# In[52]:


df5=pd.DataFrame(people_history, columns=['Name','Age','Location','State', 'Country','Education','Passing_Year','Blood_Group'])


# In[53]:


df5.head()


# In[55]:


#subsudding rows:
df5[df5['Age']>20]


# In[56]:


df5[df5['Education'] == 'Bachelors']


# In[58]:


df5[(df5['Education'] == 'Bachelors') | (df5['Education']== 'PhD')]


# In[59]:


df5["Education"].isin(['Bachelors','PhD'])


# In[60]:


df5[df5["Education"].isin(['Bachelors','PhD'])]


# In[ ]:




