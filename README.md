# 🏅 Olympics Data Analysis Project

## 📊 Overview

This project focuses on analyzing historical Olympic Games data to uncover trends and insights about athletes, countries, sports, and performances. Using SQL for querying and Python with libraries like `pandas`, `matplotlib`, and `seaborn` for data processing and visualization, this project demonstrates end-to-end handling of raw datasets and transformation into meaningful insights.

---

## 🛠 Tools & Technologies Used

- **Python**
- **Pandas** – data cleaning, manipulation, transformation
- **Matplotlib** – static visualizations
- **Seaborn** – advanced and aesthetic plotting
- **MySQL** – relational database for data storage and querying
- **SQLAlchemy** – Python SQL toolkit for database connection
- **MySQL Connector** – to populate the database from pandas DataFrames

---

## 📁 Dataset Sources

- `athlete_events.csv` – Olympic athletes' performances and attributes.
- `noc_regions.csv` – Mapping between NOC (National Olympic Committee) codes and regions.

---

## 🧹 Data Cleaning & Preprocessing

The following steps were performed to clean and prepare the data:

1. **Missing Values Handling**
   - Dropped rows with missing `Name` and `Event`.
   - Replaced missing values in:
     - `Age`, `Height`, `Weight` with `-1` and cast to `int`.
     - `Medal` with `"None"`.

2. **Creating Game IDs**
   - Extracted unique pairs of `Year` and `Season` and generated unique `GameID`s.

3. **Table Normalization**
   - Separated cleaned data into three DataFrames:
     - `athlete_events_df`
     - `games_df`
     - `noc_regions`

4. **Data Merging**
   - Merged `GameID` back into the main DataFrame using `Year` and `Season`.

---

## 🗄️ Database Design & Insertion

The MySQL database `olympics_db` includes the following tables:

- `athlete_events`
- `noc_regions`
- `games`

Data was inserted using `mysql.connector` with `INSERT IGNORE` to avoid duplicates.

---

## 🧠 Analytical Questions & SQL Queries

Five main analytical questions were explored using SQL:

1. **Which sports have the most athletes?**
   - Counted distinct athletes (`ID`) per sport.
   
2. **Which countries have won the most medals?**
   - Joined `athlete_events` and `noc_regions` to aggregate medals per NOC and region.

3. **What is the age distribution of medal winners?**
   - Filtered only rows where `Medal` is not `None` and `Age` is valid.

4. **How has gender participation evolved over the years?**
   - Grouped athletes by `Year` and `Sex` to track trends.

5. **Which sports awarded the most medals?**
   - Counted total medals per sport.

---

## 📈 Data Visualization

Visualizations were created for each query using **Matplotlib** and **Seaborn**:

1. **Top 10 Sports by Number of Athletes**
   - Bar chart (`sns.barplot`) with count of athletes.

2. **Top 10 Countries by Total Medals**
   - Bar chart showing medal count by country (`Region`).

3. **Age Distribution of Medal Winners**
   - Histogram with KDE overlays for each medal type (`Gold`, `Silver`, `Bronze`).

4. **Gender Participation Over Time**
   - Line plot showing number of male and female athletes by year.

5. **Top 10 Sports by Total Medals Awarded**
   - Bar chart showing sports with the highest number of total medals.

---

## 📌 Project Highlights

- Full ETL (Extract, Transform, Load) pipeline from raw CSV to a normalized SQL database.
- Descriptive and comparative analysis via SQL and visual storytelling.
- Use of good data practices like null handling, deduplication, and database normalization.
- Clean, professional visualizations for insight delivery.

---

## 📎 How to Run

1. Ensure MySQL is running and a database `olympics_db` is created.
2. Adjust credentials in the script to match your local MySQL setup.
3. Run the **data insertion script** to populate the database.
4. Execute the **analysis and visualization script** to generate charts and output.

---

## 📂 Project Structure

Olympics-Analysis/
│
├── Olympics DB.py # Main Python script to connect cleaned data with the database
├── Olympics Analysis.py # Python script with SQL queries, data processing, and visualizations
├── Olympics_db # SQL database file (created from raw CSVs or provided)
├── Plots # All visualized charts
├── Presentation # A presentation file to document the project
└── README.md # Project documentation
