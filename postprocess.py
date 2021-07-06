# %%
import sys
import os
import pandas as pd


if __name__ == "__main__":
    ts = pd.Timestamp.now()
    fp_live = sys.argv[1] # outputs e.g: ['./postprocessing.py', 'mmm-parkings-live.csv']
    fp_history = f"mmm-parkings-{ts.year}.csv"

    # %%
    df = pd.read_csv(
        fp_live,
        delimiter=';',
        header=0,
        usecols=[0, 1, 3, 4],
        names=['date', 'parking', 'places_libres', 'total_places'],
        parse_dates=['date'], 
    )


    # %%
    df['places_occupees'] = df['total_places'] - df['places_libres']
    df.drop(columns=['places_libres', 'total_places'], inplace=True)


    # %%
    if os.path.isfile(fp_history):
        df_history = pd.read_csv(
            fp_history
        )

        df = pd.concat([df_history, df], ignore_index=True)
        df.drop_duplicates(inplace=True)


    # %%
    df.to_csv(fp_history, index=False)
