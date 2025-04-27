### 🚀 **Data Science & Big Data Analytics Cheat Sheet** 🚀  
*(For Practical + Viva)*  

---

### 🌐 **Hadoop & MapReduce**

#### **Hadoop Components**
- **Modes:** Local, Pseudo-distributed, Fully-distributed  
- **Core Daemons:**  
  - *HDFS:* NameNode, DataNode  
  - *YARN:* ResourceManager, NodeManager  
  - *Others:* Secondary NameNode

#### **Key Config Files**  
- `core-site.xml` → HDFS URI  
- `hdfs-site.xml` → Replication factor, data directories  
- `mapred-site.xml` → MapReduce framework  
- `yarn-site.xml` → Resource management  

#### **Basic HDFS Commands**  
```bash
hdfs dfs -ls /           # List files
hdfs dfs -mkdir /input   # Create directory
hdfs dfs -put file.txt /input   # Upload file
hdfs dfs -cat /output/part-00000   # View output
hdfs dfs -rm -r /output   # Remove directory
```

#### **MapReduce Flow**  
```
Input → Split → Mapper → Shuffle & Sort → Reducer → Output
```
- **Mapper:** `<key, value>` → `<user, duration>`
- **Reducer:** Aggregate durations, find max.

#### **Combiner:**  
Optional mini-reducer to reduce data transfer between Map & Reduce.

---

### 🗄️ **Hive (Flight Information System)**  

#### **Basic Commands**  
```sql
CREATE DATABASE flight_db;
USE flight_db;

-- Managed Table
CREATE TABLE flights (
  flight_id INT,
  origin STRING,
  dest STRING,
  dep_delay INT
) ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' STORED AS TEXTFILE;

-- External Table
CREATE EXTERNAL TABLE flights_ext (
  flight_id INT,
  origin STRING,
  dest STRING,
  dep_delay INT
)
ROW FORMAT DELIMITED FIELDS TERMINATED BY ',' 
LOCATION '/user/hive/flights/';

-- Alter Table
ALTER TABLE flights ADD COLUMNS (status STRING);
DROP TABLE flights;

-- Load Data
LOAD DATA INPATH '/path/to/data.csv' INTO TABLE flights;

-- Insert/Update
INSERT INTO flights VALUES (1, 'NYC', 'LAX', 10, 'On Time');

-- Joins
SELECT a.flight_id, b.airport_name 
FROM flights a JOIN airport b ON a.origin = b.code;

-- Indexing
CREATE INDEX flight_idx ON TABLE flights (flight_id) AS 'COMPACT';

-- Aggregation (Avg dep delay per day in 2008)
SELECT AVG(dep_delay) AS avg_delay, dep_date 
FROM flights 
WHERE year = 2008 
GROUP BY dep_date;
```

#### **Managed vs External Tables**
- **Managed:** Hive controls data lifecycle.
- **External:** Data stored outside Hive warehouse.

#### **Partitioning vs Bucketing**
- *Partitioning:* Divides data based on column values (e.g., year).  
- *Bucketing:* Hashes data into fixed buckets for faster processing.

---

### 🐍 **Python (pandas & data processing)**  

#### **Data Operations (Facebook Metrics Dataset)**  
```python
import pandas as pd

# Load Data
df = pd.read_csv('facebook_metrics.csv')

# Subset Data
subset = df[['column1', 'column2']]

# Merge DataFrames
merged = pd.merge(df1, df2, on='common_col')

# Sort Data
sorted_df = df.sort_values(by='column', ascending=True)

# Transpose Data
df_transposed = df.T

# Shape & Reshape
df.shape        # (rows, columns)
melted = pd.melt(df, id_vars=['id'], value_vars=['col1', 'col2'])
pivoted = df.pivot(index='id', columns='category', values='value')
```

#### **Data Cleaning & Transformation (Air Quality/Heart Disease)**  
```python
# Check missing values
df.isnull().sum()

# Handle missing data
df.dropna(inplace=True)
df.fillna(0, inplace=True)

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['encoded_col'] = le.fit_transform(df['categorical_col'])

# Normalization & Standardization
from sklearn.preprocessing import MinMaxScaler, StandardScaler
scaler = MinMaxScaler()
df[['col1', 'col2']] = scaler.fit_transform(df[['col1', 'col2']])

# Outlier detection
import seaborn as sns
sns.boxplot(x=df['col'])
```

#### **Python + Hadoop (PyHadoop)**  
- Running Python MapReduce scripts with Hadoop streaming:
```bash
hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming*.jar \
  -input /input/logs.txt \
  -output /output/result \
  -mapper mapper.py \
  -reducer reducer.py
```
- **Mapper (mapper.py):**
```python
import sys
for line in sys.stdin:
    user, duration = line.strip().split(',')
    print(f"{user}\t{duration}")
```
- **Reducer (reducer.py):**
```python
import sys
from collections import defaultdict
user_durations = defaultdict(int)

for line in sys.stdin:
    user, duration = line.strip().split('\t')
    user_durations[user] += int(duration)

max_user = max(user_durations, key=user_durations.get)
print(max_user, user_durations[max_user])
```

---

### 📊 **Data Visualization**

#### **Matplotlib / Seaborn**
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Line Plot
plt.plot(df['x'], df['y'])
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot')
plt.show()

# Bar Plot
sns.barplot(x='category', y='value', data=df)

# Scatter Plot
plt.scatter(df['x'], df['y'])

# Heatmap
sns.heatmap(df.corr(), annot=True)

# Pairplot
sns.pairplot(df)
```

#### **Types of Visualization (Tableau)**  
- **1D:** Bar chart, Histogram  
- **2D:** Scatter plot, Line chart  
- **3D:** 3D scatter, Surface plots  
- **Temporal:** Time series (line chart with dates)  
- **Multidimensional:** Heatmaps, Bubble charts  
- **Hierarchical:** TreeMap, Sunburst  
- **Network:** Network diagrams (nodes/edges)  

---

### ⚙️ **Key Differences & Concepts**

| **Concept**          | **Explanation**                          |
|----------------------|-------------------------------------------|
| **HDFS vs HBase**     | HDFS: File storage; HBase: NoSQL database |
| **MapReduce vs Spark**| Spark is faster (in-memory processing)    |
| **Managed vs External (Hive)** | Data ownership differences       |
| **Combiner**          | Optional mini-reducer to reduce data shuffle|
| **Normalization**     | Scale between 0-1 (MinMaxScaler)         |
| **Standardization**   | Mean = 0, Std Dev = 1 (StandardScaler)   |

---

### 💡 **Common Viva Q&A**

- **Explain HDFS architecture.**
- **What is the role of NameNode?**
- **Why use Hive over SQL?**
- **Difference between inner and outer joins in Hive.**
- **How do you handle missing values in Python?**
- **What are different types of data visualization?**
- **How does MapReduce achieve fault tolerance?**
- **Difference between Pandas `merge` and `concat`.**
- **What is PyHadoop?**
- **How does partitioning improve Hive performance?**

---

### 🔑 **Quick Commands Recap**

| **Task**       | **Command**                           |
|----------------|----------------------------------------|
| Start Hadoop   | `start-dfs.sh`, `start-yarn.sh`        |
| List HDFS files| `hdfs dfs -ls /`                      |
| Upload data    | `hdfs dfs -put localfile /input`        |
| Run MR job     | `hadoop jar <jarfile> <input> <output>`|
| Open Hive shell| `hive`                                 |
| View tables    | `SHOW TABLES;`                         |

---

### ✅ **Final Tips**
- Revise **basic SQL** and **pandas commands**.
- Be clear on **Hadoop architecture** and **MapReduce flow**.
- Understand the **differences between tools** (Hadoop vs Spark, Hive vs RDBMS).
- Brush up on **data cleaning techniques** and **visualization types**.

You got this! 🔥  
Need clarification on anything? 💬
