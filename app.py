import streamlit as st
from sentence_transformers import SentenceTransformer
import faiss
import pandas as pd

st.title('Semantic Movie Search')
query = st.text_input('Enter movie description')

load_index = faiss.read_index("embeddings/movie_summary_index.faiss")

if st.button('Search') and query is not None:
    query = query.lower().strip()
    
    model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
    query_embedding = model.encode([query]).astype('float32')

    df = pd.read_csv('dataset/preprocessed_data.csv')
    
    D, I = load_index.search(query_embedding, k=3)
    movie_index = I[0]

    st.header('Top 3 Matches:')

    for index in movie_index:
        movie = df.iloc[index]
        st.subheader(movie['name'])
        st.write(movie['summary'])