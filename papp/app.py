import pandas as pd
import streamlit as st
import plotly.express as px

#page config

st.set_page_config(
    page_title='Pokemon App',
    page_icon='🦖',
    layout='wide'
)

st.sidebar.title('🦖🦕 👻 Pokemon App')
st.image('papp/pokemon.jpg',use_column_width=True)
#load data
@st.cache_data
def load_pokemon():
    data = pd.read_csv('papp/Pokemon.csv',index_col=0)
    return data
with st.spinner('Loading pokemon data...'):
    pokemon = load_pokemon()
    st.sidebar.success('Pokemon loaded successfully')
    
#sidebar
show_data = st.sidebar.checkbox('show the data set')
if show_data:
    st.subheader('pokemon data')
    st.dataframe(pokemon)
    st.dataframe(pokemon, use_container_width=True)
    
type1 = st.sidebar.selectbox('Select pokemon type',pokemon['Type 1'].unique())
#type2 = st.sidebar.selectbox('Select the legendary status',pokemon['Legendary'].unique())
subset = pokemon[pokemon['Type 1']== type1]#filter

tabs = st.tabs(['Data','Univariate analysis','Bivariate analysis','trivarial analysis',])

#attck
ss =subset.sort_values(by='Attack')
fig1 = px.histogram(subset,x='Attack',nbins=20)
fig2 = px.funnel(subset,x='Name',y='Attack')
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('Attack')
tabs[1].plotly_chart(fig1,use_container_width=True)
tabs[1].plotly_chart(fig2,use_container_width=True)


#Univariate analysis tab

#defense
ss =subset.sort_values(by='Defense')
fig1 = px.histogram(subset,x='Attack',nbins=20)
fig2 = px.funnel(subset,x='Name',y='Defense')
tabs[1].subheader(f'{type1} stats')
tabs[1].subheader('Defence')
tabs[1].plotly_chart(fig1,use_container_width=True)
tabs[1].plotly_chart(fig2,use_container_width=True)

#do the dame for hp,sp,atck,sp,def,spped
#Bivariate analysis tab
x = tabs[2].selectbox('Select X',pokemon.select_dtypes('number').columns)
y = tabs[2].selectbox('Select Y',pokemon.select_dtypes(exclude='number').columns)
c = tabs[2].selectbox('Select color',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter(subset, x=x,y=y,color=c,hover_data=['Name'],size=x,size_max=60)
tabs[2].subheader(f'{type1}: {x} vs {y} by {c}')
tabs[2].plotly_chart(fig, use_container_width=True)



#trivariate analysis
x = tabs[2].selectbox('Select X data',pokemon.select_dtypes('number').columns)
y = tabs[2].selectbox('Select Y data',pokemon.select_dtypes(exclude='number').columns)
z = tabs[2].selectbox('Select z data',pokemon.select_dtypes(exclude='number').columns)
c = tabs[2].selectbox('Select color type',pokemon.select_dtypes(exclude='number').columns)
fig = px.scatter_3d(subset, x=x,y=y,z=z,color=c,hover_data=['Name'],size=x,size_max=60)
tabs[3].subheader(f'{type1}: {x} vs {y} vs {z} by {c}')
tabs[3].plotly_chart(fig, use_container_width=True)

