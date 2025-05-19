import pandas as pd
import mysql.connector

df = pd.read_csv(r"C:\Users\Baher\Downloads\Compressed\athlete_events.csv")
df_noc = pd.read_csv(r"C:\Users\Baher\Downloads\Compressed\noc_regions.csv")

df = df.dropna(subset=['Name', 'Event'])
df['Age'] = df['Age'].fillna(-1).astype(int)
df['Height'] = df['Height'].fillna(-1).astype(int)
df['Weight'] = df['Weight'].fillna(-1).astype(int)
df['Medal'] = df['Medal'].fillna("None")

games_df = df[['Year', 'Season']].drop_duplicates().reset_index(drop=True)
games_df['GameID'] = games_df.index + 1
df = df.merge(games_df, on=['Year', 'Season'], how='left')

athlete_events_df = df[[
    'ID', 'Name', 'Sex', 'Age', 'Height', 'Weight',
    'Team', 'NOC', 'GameID', 'City', 'Sport', 'Event', 'Medal'
]].drop_duplicates()

df_noc = df_noc.rename(columns={'region': 'Region', 'notes': 'Notes'})
df_noc = df_noc[['NOC', 'Region', 'Notes']].drop_duplicates()
df_noc = df_noc.where(pd.notnull(df_noc), None)

df = df.fillna(0)

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Baher05SQL",
    database="olympics_db",
    port=3306
)
cursor = conn.cursor()

for _, row in df_noc.iterrows():
    cursor.execute(
        "INSERT IGNORE INTO noc_regions (NOC, Region, Notes) VALUES (%s, %s, %s)",
        (row['NOC'], row['Region'], row['Notes'])
    )

for _, row in games_df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO games (GameID, Year, Season)
        VALUES (%s, %s, %s)
    """, (row['GameID'], row['Year'], row['Season']))

for _, row in athlete_events_df.iterrows():
    cursor.execute("""
        INSERT IGNORE INTO athlete_events (
            ID, Name, Sex, Age, Height, Weight,
            Team, NOC, GameID, City, Sport, Event, Medal
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        row['ID'], row['Name'], row['Sex'], int(row['Age']), int(row['Height']), int(row['Weight']),
        row['Team'], row['NOC'], int(row['GameID']), row['City'], row['Sport'], row['Event'], row['Medal']
    ))

conn.commit()
cursor.close()
conn.close()
print("Data inserted successfully.")