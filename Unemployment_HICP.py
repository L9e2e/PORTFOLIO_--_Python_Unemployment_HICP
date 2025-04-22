# -*- coding: utf-8 -*-


#Quick analisys and data preperation for further analisys
#Data: Unemployment/HICP (Harmonised Index of Consumer Prices)
#Data for years 2020 to 2024. All EU Countries
#Source: Eurostat


# %%
#Identifying data, creating variable lists from unemployment file

import csv
unemployment_country = []
unemployment_yearmonth = []
unemployment_indicator = []

with open('Unemployment.csv') as unemployment_file:
    csv_reader_unemployment = csv.reader(unemployment_file)
    for line in csv_reader_unemployment:
        print(line[6])
        unemployment_country.append(line[6])
        print(line[7])
        unemployment_yearmonth.append(line[7])
        print(line[8])
        unemployment_indicator.append(line[8])
    unemployment_country[0] = 'Country'
    unemployment_yearmonth[0] = 'Year_month'
    unemployment_indicator[0] = 'Indicator_Unemployment'


# %%
#Identifying data, creating variable lists from HICP file

import csv
hicp_country = []
hicp_yearmonth = []
hicp_hicp = []

with open('HICP.csv') as hicp_file:
    csv_reader_hicp = csv.reader(hicp_file)
    for line in csv_reader_hicp:
        print(line[5])
        hicp_country.append(line[5])
        print(line[6])
        hicp_yearmonth.append(line[6])
        print(line[7])
        hicp_hicp.append(line[7])
    hicp_country[0] = 'Country'
    hicp_yearmonth[0] = 'Year_month'
    hicp_hicp[0] = 'Indicator_HICP'


# %%
#Creating table for unemployment
import pandas as pd
import datetime
pd.set_option('display.max_rows', 10)

data_unemployment = {unemployment_country[0]: unemployment_country[1:],
                     unemployment_yearmonth[0]: unemployment_yearmonth[1:],
                     unemployment_indicator[0]: unemployment_indicator[1:]}

df_unemployment = pd.DataFrame(data_unemployment)

print(df_unemployment)

df_unemployment['Country'] = df_unemployment['Country'].astype('str')
df_unemployment['Year_month'] = df_unemployment['Year_month'].astype('str')
df_unemployment['Indicator_Unemployment'] = (df_unemployment
                                             ['Indicator_Unemployment']
                                             .astype('float'))
print(df_unemployment.dtypes)


# %%
#Printing highest and lowest indicators for unemployment
df_unemployment = df_unemployment.sort_values(by = ['Indicator_Unemployment'], 
                                              inplace = False, 
                                              ascending = False)
print(df_unemployment[0:10])

df_unemployment = df_unemployment.sort_values(by = ['Indicator_Unemployment'], 
                                              inplace = False, 
                                              ascending = True)
print(df_unemployment[0:10])


# %%
#Creating table for HICP
import pandas as pd
import datetime
pd.set_option('display.max_rows', 10)

data_hicp = {hicp_country[0]: hicp_country[1:],
                     hicp_yearmonth[0]: hicp_yearmonth[1:],
                     hicp_hicp[0]: hicp_hicp[1:]}

df_hicp = pd.DataFrame(data_hicp)

print(df_hicp)

df_hicp['Country'] = df_hicp['Country'].astype('str')
df_hicp['Year_month'] = df_hicp['Year_month'].astype('str')
df_hicp['Indicator_HICP'] = df_hicp['Indicator_HICP'].astype('float')
print(df_hicp.dtypes)


# %%
#Printing highest and lowest indicators for HICP
df_hicp = df_hicp.sort_values(by = ['Indicator_HICP'], 
                                              inplace = False, 
                                              ascending = False)
print(df_hicp[0:10])

df_hicp = df_hicp.sort_values(by = ['Indicator_HICP'], 
                                              inplace = False, 
                                              ascending = True)
print(df_hicp[0:10])


# %%
#Joining tables of unemployment and HICP
frames = [df_unemployment, df_hicp['Indicator_HICP']]
full_table = pd.concat((frames), axis=1)
print(full_table)


# %%
#Printing specific data from joined table
i = full_table[(full_table.Country == 'Austria')].index
print(i)

austria_full_table = full_table.loc[i]
print(austria_full_table)


# %%
#Testing correlations between unemployment and HICP in different variants. 
#Dropping indicators for EU averages

all_territory = full_table['Country'].unique()
print(all_territory)

drop_1 = full_table[(full_table.Country == 'Euro area â€“ 20 countries '
                     '(from 2023)')].index
drop_2 = full_table[(full_table.Country == 'European Union - 27 countries '
                     '(from 2020)')].index

only_countries = full_table.drop(drop_1).drop(drop_2)

print(only_countries.corr())


# %%
#Testing correlation between unemployment and HICP for Poland
poland_i = full_table[(full_table.Country == 'Poland')].index
poland_full_table = full_table.loc[poland_i]
print(poland_full_table)
print(poland_full_table.corr())


# %%
#Saveing data to CSV for further analisys
full_table.to_csv('Full_table.csv', index = False)