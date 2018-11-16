#!/usr/bin/env python
# coding: utf-8

# In[14]:


import csv
f = open('guns.csv', 'r')
data = list(csv.reader(f))
print(data[:4])



# In[15]:


headers = data[0]
data = data[1:]
print(headers)
print(data[:4])


# In[3]:


years = [each[1] for each in data]
year_counts = {}
for each in years:
    if each in year_counts:
        year_counts[each] += 1
    else:
        year_counts[each] = 1
print(year_counts)


# In[10]:


import datetime
dates = [datetime.datetime(year = int(each[1]), month = int(each[2]), day = 1) for each in data]
print(dates[:4])


# In[12]:


date_counts = {}
for each in dates:
    if str(each) in date_counts:
        date_counts[str(each)] += 1
    else:
        date_counts[str(each)] = 1
print(date_counts)


# In[18]:


sex_counts = {}
race_counts = {}
for each in data:
    if each[5] in sex_counts:
        sex_counts[each[5]] += 1
    else:
        sex_counts[each[5]] = 1
    if each[7] in race_counts:
        race_counts[each[7]] += 1
    else:
        race_counts[each[7]] = 1
print(sex_counts)
print(race_counts)


# So far we have learned gender and race breakdowns of gun related deaths. Intent, whether or not police were involved, education, and the place the deaths occurred can be examined.

# In[19]:


f = open('census.csv', 'r')
census = list(csv.reader(f))
print(census)


# In[20]:


mapping = {'Asian/Pacific Islander':15834141, 'Black':44618105, 'Native American/Native Alaskan':40250635, 'Hispanic':197318956,'White':308745538}
race_per_hundredk = {}
for each in race_counts:
    race_per_hundredk[each] = race_counts[each]/mapping[each] * 100000
print(race_per_hundredk)


# In[ ]:


intents = [each[3] for each in data]
races = [each[7] for each in data]
homicide_race_counts = {}
for i, race in enumerate(races):
    if intents[i] == 'Homicide':
        if race not in homicide_race_counts:
            homicide_race_counts[race] = 1
        else:
            homicide_race_counts += 1
for each in homicide_race_counts:
    homicide_race_counts[each] = homicide_race_counts[each]/mapping[each]
    

