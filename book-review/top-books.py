import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title='Top 100 Books', page_icon='📚', layout='wide')

df_topTrendingBooks = pd.read_csv('./resources/Top-100 Trending Books.csv')

price_max = df_topTrendingBooks['book price'].max()
price_min = df_topTrendingBooks['book price'].min()

min_price, max_price = st.sidebar.slider('Range de Preço', price_min, price_max, (price_min, price_max))

df_topTrendingBooksFiltered = df_topTrendingBooks[
    (df_topTrendingBooks['book price'] >= min_price) & (df_topTrendingBooks['book price'] <= max_price)]

df_topTrendingBooksFiltered

col1, col2 = st.columns(2)
fig_yearBar = px.bar(df_topTrendingBooksFiltered["year of publication"].value_counts(), title='Books Published by Year',
                     labels={'value': 'Number of Books'})

fig_valueHistogram = px.histogram(df_topTrendingBooksFiltered['book price'])

col1.plotly_chart(fig_yearBar)
col2.plotly_chart(fig_valueHistogram)
