import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

df = pd.read_csv('../dataset/preprocessed_data.csv')

summaries = df['cleaned_summary'].tolist()

summary_embeddings = model.encode(summaries)

embeddings = np.array(summary_embeddings).astype('float32')

index = faiss.IndexFlatL2(embeddings.shape[1])

index.add(embeddings)

faiss.write_index(index, "../embeddings/movie_summary_index.faiss")