import pandas as pd

df_plot = pd.read_csv('../dataset/MovieSummaries/plot_summaries.txt', sep = '\t', header = None)
df_movie = pd.read_csv('../dataset/MovieSummaries/movie.metadata.tsv', sep = '\t', header = None)

movie = pd.merge(df_plot, df_movie, on=0, how='inner')

df = movie[['1_x', 2]]
df = df.rename(columns={'1_x':'summary', 2:'name'})

df['cleaned_summary'] = df['summary'].apply(lambda x: x.lower().strip())

df.to_csv('../dataset/preprocessed_data.csv', index=False)