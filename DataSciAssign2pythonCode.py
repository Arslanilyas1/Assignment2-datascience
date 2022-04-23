#!/usr/bin/env python
# coding: utf-8

# In[2]:


# essential libraries 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb


# In[3]:



# function on pandas to read the file of extension .csv 

dataFrame = pd.read_csv("data2.csv")


# In[4]:



# part 1 make dataframe for countries 

country_df = dataFrame["Country Name"]


# In[ ]:





# In[6]:



# countires name repeated for each indicator so, we use this function to get only countries name 
country = list()
country.append(country_df[1])
for i in country_df:

    if i not in country:
    
        country.append(i)

    
        


# In[7]:



# now we extract dataframe for years. 
years_df = dataFrame.iloc[:,4:-1]


# In[ ]:





# In[12]:





# In[30]:


# data frame of years to list

years = list()
for i in years_df:
    val = int(i)
    years.append(val)


# In[32]:


# calculating urban population of aruba 

def urban_pop_aruba():
#     builtin function of pandas to make data frame of indicator
    df = dataFrame.loc[(dataFrame['Country Name'] == "Aruba") & (dataFrame['Indicator Name'] == "Urban population (% of total population)")]
    data = df.iloc[:,4:-1].values
    data=data[np.logical_not(np.isnan(data))]
    up_data = list(data)
    
    
#     plotting
    plt.figure(figsize=(8,6))
    plt.plot(years,up_data,color="r")
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 2.5
    plt.title("Aruba urban population from 1960 to 2019")
    plt.xlabel("years")
    plt.ylabel("population")
    plt.show()
urban_pop_aruba()


# In[118]:





# In[ ]:





# In[34]:


def urban_pop_australia():
#     dataset of indicator by using builtin function of pandas
    df_Australia = dataFrame.loc[(dataFrame['Country Name'] == "Australia") & (dataFrame['Indicator Name'] == "Urban population (% of total population)")]
    data = df_Australia.iloc[:,4:-1].values
    data=data[np.logical_not(np.isnan(data))]
    dataList_australia = list(data)
    
    
#     ploting
    plt.figure(figsize=(8,6))
    plt.plot(years,dataList_australia,color="b")
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 2.5
    plt.title("Australia urban population from 1960 to 2019")
    plt.xlabel("years")
    plt.ylabel("population")
    plt.show()
urban_pop_australia()


# In[ ]:





# In[35]:


def urban_pop_Belgium():
    
#     data frame of indicator
    df= dataFrame.loc[(dataFrame['Country Name'] == "Belgium") & (dataFrame['Indicator Name'] == "Urban population (% of total population)")]
    
#     array
    data = df.iloc[:,4:-1].values
    
#     removing null spaces 
    data=data[np.logical_not(np.isnan(data))]
    
#     to list
    dataList = list(data)
    
    plt.figure(figsize=(8,6))
    plt.plot(years,dataList,color="g")
    plt.rcParams["figure.autolayout"] = True
    plt.rcParams["axes.edgecolor"] = "black"
    plt.rcParams["axes.linewidth"] = 2.5
    plt.title("Belgium urban population from 1960 to 2019")
    plt.xlabel("years")
    plt.ylabel("population")
    plt.show()
urban_pop_Belgium()


# In[ ]:





# In[ ]:





# In[ ]:





# In[23]:


# comparison of all
def indicatorComparison():
#     1 INDICATOR
    df_co2_gas = dataFrame.loc[(dataFrame['Country Name'] == "Belgium") & (dataFrame['Indicator Name'] == "CO2 emissions from gaseous fuel consumption (% of total)")]
    df_bel_co2_gas_data = df_co2_gas.iloc[:,5:-1].values  
    df_bel_co2_gas_data=df_bel_co2_gas_data[np.logical_not(np.isnan(df_bel_co2_gas_data))] 
    mydata1 = list(df_bel_co2_gas_data)
    
#     2 INDICATOR
    df_co2 = dataFrame.loc[(dataFrame['Country Name'] == "Belgium") & (dataFrame['Indicator Name'] == "CO2 emissions (metric tons per capita)")]
    df_co2_data = df_co2.iloc[:,5:-1].values
    df_co2_data=df_co2_data[np.logical_not(np.isnan(df_co2_data))] 
    mydata2 = list(df_co2_data)

    
                                #setting of graphs or figure using matplotlib
    plt.figure(figsize=(10,8))
    plt.ylabel("increase in electircity production")
    plt.title("ELECTRICITY PRODUCTION FROM COAL & HYDRO IN FRANCE")
    tick = np.arange(10,55,5)
    plt.yticks(tick)

                                #plotting on distplot
    sb.distplot(mydata1, bins=20, kde = True,color='r')
    sb.distplot(mydata2,bins=8, kde = True)
indicatorComparison()


# In[ ]:




