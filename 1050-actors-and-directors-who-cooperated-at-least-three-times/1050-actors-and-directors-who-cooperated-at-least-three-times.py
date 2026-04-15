import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    stats = actor_director.groupby(['actor_id', 'director_id'], as_index=False).count()
    stats= stats[stats['timestamp'] >=3]

    return stats[['actor_id', 'director_id']]