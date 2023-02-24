import streamlit as st 
import pandas as pd
import numpy as np
#interactive visualization
import plotly.express as px 
import plotly.graph_objects as go
years = list(range(1980, 2014)) #list of years from 1980 to 2013

# Loading the data and preprocessing it for the sake of humanity
@st.cache_data
def load_dataset():
    df = pd.read_excel("dapp/canada.xlsx",sheet_name=1, skiprows=20, skipfooter=2)
    df.drop(['AREA', 'REG', 'DEV', 'Type','Coverage'], axis=1, inplace=True)
    df.rename(columns={'OdName':'Country','AreaName':'Continent',
                       'RegName':'Region','DevName':'Status'},inplace=True)
    df.set_index('Country',inplace=True)
    df['Total'] = df[years].sum(axis=1)
    return df
with st.spinner('Loading data..'):
    df  = load_dataset()
    #st.balloons()

countries = df.index.tolist()

sel_country = st.selectbox('Select your country', countries)
st.info(f'Your selected country is {sel_country}')

# KPI 
total_immigrants = df.loc[sel_country,'Total']
avg_immigrants = df.loc[sel_country,years].mean()
st.subheader('KEY PERFORMANCE INDICATORS')
c1,c2, c3 = st.columns(3)

c1.metric("total Immigrant", f'{total_immigrants} people','👪')
c2.metric("average Immigrant", f'{avg_immigrants} people','👪')
c3.metric("Total Immigrant", f'{len(years)} years','📅')

country_df = df.loc[sel_country, years]
fig = px.area(y=country_df, x=country_df.index, title=f'{sel_country} immigrants to canda')
st.plotly_chart(fig)
