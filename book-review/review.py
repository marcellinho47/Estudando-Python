import pandas as pd
import streamlit as st

st.set_page_config(page_title='Book Review', page_icon='📚', layout='wide')

df_customerReview = pd.read_csv('./resources/customer reviews.csv')
df_topTrendingBooks = pd.read_csv('./resources/Top-100 Trending Books.csv')

books = df_topTrendingBooks["book title"].unique()

book_title = st.sidebar.selectbox('Selecione o Livro', books)

df_topTrendingBooksFiltered = df_topTrendingBooks[df_topTrendingBooks['book title'] == book_title]
df_customerReviewFiltered = df_customerReview[df_customerReview['book name'] == book_title]

book_name = df_topTrendingBooksFiltered['book title'].iloc[0]
book_author = df_topTrendingBooksFiltered['author'].iloc[0]
book_price = df_topTrendingBooksFiltered['book price'].iloc[0]
book_year = df_topTrendingBooksFiltered['year of publication'].iloc[0]
book_genre = df_topTrendingBooksFiltered['genre'].iloc[0]
book_rating = df_topTrendingBooksFiltered['rating'].iloc[0]

st.title(book_name)
st.header(book_genre)
st.subheader(book_author)

col1, col2, col3 = st.columns(3)
col1.metric('Preço', f'$ {book_price:.2f}')
col2.metric('Avaliação', book_rating)
col3.metric('Ano de Publicação', book_year)

st.divider()

df_customerReviewFiltered

for index, row in df_customerReviewFiltered.iterrows():
    st.subheader(f'{row["review title"]}')
    st.write(f'{row["review description"]}')
    st.divider()
