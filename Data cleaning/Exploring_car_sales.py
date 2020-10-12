#!/usr/bin/env python
# coding: utf-8

# #In this project we will learn to clean an analyze the included used car listng

# In[1]:


import pandas as pd

autos=pd.read_csv("autos.csv",encoding="Latin-1")


# In[2]:


print(autos.info())
print(autos.head())


# In[3]:


autos.columns


# In[4]:


autos.columns=['date_crawled', 'name', 'seller', 'offer_type', 'price', 'abtest',
       'vehicle_type', 'registration_year', 'gearbox', 'power_ps', 'model',
       'odometer', 'registration_month', 'fuel_type', 'brand',
       'unrepaired_damage', 'ad_created', 'num_photos', 'postal_code',
       'last_seen']
autos.head()


# changed the columns to snake to unify de data names

# In[5]:


autos.describe(include='all')


# Columns where all or nearly all values are the same
# - Seller
# - Offer type
# Check num_photos

# In[6]:


autos['num_photos'].value_counts()


# In[7]:


autos = autos.drop(['num_photos','seller','offer_type'],axis=1)


# In[8]:


autos['price']=(autos['price']
               .str.replace('$','')
               .str.replace(',','')
               .astype(int)
               )
autos['price'].head()


# In[9]:


autos['odometer']=(autos['odometer']
                  .str.replace('km','')
                  .str.replace(',','')
                  .astype(int)
                  )
autos.rename({'odometer':'odometer_km'},axis=1,inplace=True)
autos['odometer_km'].head()


# # Exploring odometer

# In[10]:


autos['odometer_km'].value_counts()


# In[11]:



print(autos["price"].unique().shape)


# there are 2357 unique values 

# In[12]:


print(autos["price"].describe())


# There are prices listed at 0 and at 100,000,000

# In[13]:


autos["price"].value_counts().head(20)


# In[14]:


autos = autos[autos["price"].between(1,351000)]
autos["price"].describe()


# In[15]:


autos[['date_crawled','ad_created','last_seen']][0:5]


# In[16]:


(autos['date_crawled']
    .str[:10]
    .value_counts(normalize=True,dropna=False)
    .sort_index())


# In[17]:


(autos["date_crawled"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_values()
        )


# In[18]:



(autos["last_seen"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[19]:


print(autos["ad_created"].str[:10].unique().shape)
(autos["ad_created"]
        .str[:10]
        .value_counts(normalize=True, dropna=False)
        .sort_index()
        )


# In[21]:


autos['registration_year'].describe()


# error in the in value(1000) and max value(9999)
# min acceptable 1900 
# max acceptable 2016

# In[24]:


(~autos["registration_year"].between(1900,2016)).sum()/autos.shape[0]


# In[25]:


autos = autos[autos["registration_year"].between(1900,2016)]
autos["registration_year"].value_counts(normalize=True).head(10)


# In[26]:


autos["brand"].value_counts(normalize=True)


# In[27]:


brand_counts = autos["brand"].value_counts(normalize=True)
common_brands = brand_counts[brand_counts > .05].index
print(common_brands)


# In[28]:


brand_mean_prices = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_price = brand_only["price"].mean()
    brand_mean_prices[brand] = int(mean_price)

brand_mean_prices


# In[29]:



bmp_series = pd.Series(brand_mean_prices)
pd.DataFrame(bmp_series, columns=["mean_price"])


# In[30]:


brand_mean_mileage = {}

for brand in common_brands:
    brand_only = autos[autos["brand"] == brand]
    mean_mileage = brand_only["odometer_km"].mean()
    brand_mean_mileage[brand] = int(mean_mileage)

mean_mileage = pd.Series(brand_mean_mileage).sort_values(ascending=False)
mean_prices = pd.Series(brand_mean_prices).sort_values(ascending=False)


# In[31]:


brand_info = pd.DataFrame(mean_mileage,columns=['mean_mileage'])
brand_info


# In[32]:


brand_info["mean_price"] = mean_prices
brand_info


# In[ ]:




