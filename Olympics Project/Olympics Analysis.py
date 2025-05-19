import pandas as pd
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import seaborn as sns

username = "root"
password = "your_password"
host = "127.0.0.1"
port = 3306
database = "olympics_db"
engine = create_engine(f"mysql+pymysql://root:Baher05SQL@127.0.0.1:3306/olympics_db")

#Total athletes per sport
query1 = """
SELECT Sport, COUNT(DISTINCT ID) AS total_athletes
FROM athlete_events
GROUP BY Sport
ORDER BY total_athletes DESC;
"""
df1 = pd.read_sql(query1,engine)
print("\nTotal Athletes per Sport:\n", df1.head())

#Number of medals by country
query2 = """
SELECT ae.NOC, nr.Region, COUNT(ae.Medal) AS total_medals
FROM athlete_events ae
JOIN noc_regions nr ON ae.NOC = nr.NOC
WHERE ae.Medal IN ('Gold', 'Silver', 'Bronze')
GROUP BY ae.NOC, nr.Region
ORDER BY total_medals DESC;
"""
df2 = pd.read_sql(query2, engine)
print("\nTotal Medals by Country:\n", df2.head())

#Age distribution of medal winners
query3 = """
SELECT Age, Medal
FROM athlete_events
WHERE Medal IN ('Gold', 'Silver', 'Bronze') AND Age IS NOT NULL;
"""
df3 = pd.read_sql(query3, engine)
print("\nAge Distribution of Medal Winners:\n", df3.describe())

#Gender participation trend over time
query4 = """
SELECT g.Year, ae.Sex, COUNT(DISTINCT ae.ID) AS num_athletes
FROM athlete_events ae
JOIN games g ON ae.GameID = g.GameID
GROUP BY g.Year, ae.Sex
ORDER BY g.Year;
"""
df4 = pd.read_sql(query4, engine)
print("\nGender Participation Over Time:\n", df4.head())

#Which sports have awarded the most medals overall?
query5 = """
SELECT Sport, COUNT(Medal) AS total_medals
FROM athlete_events
WHERE Medal IS NOT NULL
GROUP BY Sport
ORDER BY total_medals DESC;
"""

df5 = pd.read_sql(query5, engine)
print("\nTotal Medals by Sport:\n", df5.head())

#Query1 Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=df1.head(10), x='total_athletes', y='Sport', hue='Sport', palette='viridis', legend=False)
plt.title("Top 10 Sports by Number of Athletes")
plt.xlabel("Number of Athletes")
plt.ylabel("Sport")
plt.tight_layout()
plt.show()

#Query2 Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=df2.head(10), x='total_medals', y='Region', hue='Region', palette='magma', legend=False)
plt.title("Top 10 Countries by Total Medals")
plt.xlabel("Total Medals")
plt.ylabel("Country")
plt.tight_layout()
plt.show()

#Query3 Visualization
plt.figure(figsize=(10, 6))
sns.histplot(data=df3, x='Age', hue='Medal', kde=True, palette='Set2', bins=30)
plt.title("Age Distribution of Medal Winners")
plt.xlabel("Age")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

#Query4 Visualization
plt.figure(figsize=(12, 6))
sns.lineplot(data=df4, x='Year', y='num_athletes', hue='Sex', marker='o')
plt.title("Gender Participation Over Time")
plt.xlabel("Year")
plt.ylabel("Number of Athletes")
plt.tight_layout()
plt.show()

#Query5 Visualization
plt.figure(figsize=(10, 6))
sns.barplot(data=df5.head(10), x='total_medals', y='Sport', hue='Sport', palette='coolwarm', legend=False)
plt.title("Top 10 Sports by Total Medals Awarded")
plt.xlabel("Total Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.show()
