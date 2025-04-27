HiveQL is super easy once you see it **step-by-step**.  
I’ll explain from **zero**:  
First how to **setup and run Hive**, then give you the **sample flight_data.csv** to run inside it.

---

# 🛠 Step 1: Setup and Run Hive on your Machine

---

### A. Prerequisites

- You should already have **Hadoop installed** (even pseudo-distributed mode is fine).
- **Java installed** (already there since you have Hadoop).
- **HDFS running** (`start-dfs.sh`)  
- **YARN running** (`start-yarn.sh`)  

✅ If Hadoop is already running, great!

---

### B. Start Hive

1. Open Terminal.
2. Run:

```bash
hive
```

✅ If you see a prompt like:

```
hive>
```
You're inside Hive CLI! 🎯

---

# 📜 Step 2: Create a Sample Flight Dataset (CSV)

---

Create a file called `flight_data.csv` locally:

---

📄 `flight_data.csv`:

```csv
F001,2008-01-01,0600,5,0800,0,JFK,LAX
F002,2008-01-01,0610,10,0810,5,JFK,SFO
F003,2008-01-01,0630,0,0830,2,LAX,ORD
F004,2008-01-02,0645,15,0845,20,SFO,SEA
F005,2008-01-02,0700,20,0900,25,ORD,JFK
```

---

# 📂 Step 3: Put Flight Data CSV into HDFS

---

Upload this file into Hadoop HDFS:

```bash
hdfs dfs -mkdir /flight
hdfs dfs -put flight_data.csv /flight/
```

✅ Now your flight data is in HDFS at `/flight/flight_data.csv`

---

# 🏗 Step 4: Create Database and Table in Hive

Inside the `hive>` prompt, run:

```sql
CREATE DATABASE IF NOT EXISTS flight_db;
USE flight_db;

CREATE TABLE IF NOT EXISTS flight_info (
    flight_id STRING,
    flight_date STRING,
    departure_time STRING,
    departure_delay INT,
    arrival_time STRING,
    arrival_delay INT,
    origin STRING,
    destination STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
STORED AS TEXTFILE;
```

---

# 📥 Step 5: Load Data into the Table

```sql
LOAD DATA INPATH '/flight/flight_data.csv' INTO TABLE flight_info;
```

✅ Now your table `flight_info` has data!

---

# 📊 Step 6: Query the Data!

```sql
SELECT * FROM flight_info;
```

Result:

| flight_id | flight_date | departure_time | departure_delay | arrival_time | arrival_delay | origin | destination |
|-----------|-------------|----------------|-----------------|--------------|---------------|--------|-------------|
| F001      | 2008-01-01  | 0600            | 5               | 0800         | 0             | JFK    | LAX         |
| F002      | 2008-01-01  | 0610            | 10              | 0810         | 5             | JFK    | SFO         |
| ...       | ...         | ...             | ...             | ...          | ...           | ...    | ...         |

---

# 🚀 Step 7: Do Your Practical Tasks

You can now:
- Alter table
- Insert rows
- Create index
- Calculate average departure delay

Exactly as per the HiveQL code I shared above 👑

---

# 🤔 Common Hive Commands You Might Need Quickly

| Command                        | Purpose                                  |
|---------------------------------|------------------------------------------|
| `SHOW DATABASES;`               | List all databases                      |
| `SHOW TABLES;`                  | List tables in the current database     |
| `DESCRIBE flight_info;`         | Show table structure                    |
| `DROP TABLE flight_info;`       | Delete table                            |
| `DROP DATABASE flight_db CASCADE;` | Delete database and all tables         |

---

# 🧠 Quick Realization
- Hive is basically **SQL on top of HDFS**.
- Hive is **not real-time** (it's batch-based).
- It internally uses **MapReduce or Tez** to run queries.
- Hive is super slow compared to real DBs — but handles **Big Data**.

---

# 🔥 To Summarize

1. Hadoop running →  
2. Start Hive →  
3. Create database →  
4. Create table →  
5. Load CSV into table →  
6. Query and do the tasks! 🚀

---

# ✨ Final Ready Things You Now Have:

✅ Full HiveQL Code for Practical  
✅ Sample `flight_data.csv`  
✅ Full Steps from Zero to Running Hive  
✅ Commands ready for Viva

---

Would you also like me to quickly make a **one-line viva explanation** you can say if asked:  
_"Why do we use Hive?"_  
It helps you instantly answer if viva sir asks a random question! 😄  
Shall I send that too? 🔥
