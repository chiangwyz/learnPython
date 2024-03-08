import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views['author_id'] == views['viewer_id']]

    df.drop_duplicates(subset=['author_id'], inplace=True)
    df.sort_values(by=['author_id'], inplace=True)
    df.rename(columns={'author_id':'id'}, inplace=True)

    df = df[['id']]

    return df
