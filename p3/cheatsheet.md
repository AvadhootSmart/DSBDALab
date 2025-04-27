# 🎯 **HiveQL Viva Cheatsheet**


## 1. What is Hive?

> Hive is a **data warehouse tool** on top of Hadoop.  
> It lets you **query large datasets** using a language called **HiveQL**, similar to SQL.

---

## 2. What is the difference between Internal and External tables?

| Internal Table  | External Table        |
|-----------------|------------------------|
| Managed by Hive | Managed externally     |
| Deleting table **deletes data** too | Deleting table **does not delete** data |

---

## 3. How to load data into a Hive table?

> Using the `LOAD DATA INPATH` command.  
> Example:  
> ```sql
> LOAD DATA INPATH '/path/to/file.csv' INTO TABLE table_name;
> ```

---

## 4. Why create an index in Hive?

> Indexing **speeds up** queries by allowing faster **lookup** and **retrieval** of data on specific columns.

---

## 5. What is the default file format in Hive?

> **TEXTFILE** is the default.  
> (Others include ORC, PARQUET for optimization.)

---

## 6. Why do we use External Tables?

> To **protect data** in HDFS even if the table is dropped.  
> External tables point to existing **HDFS paths**.

---

## 7. How is Hive different from RDBMS like MySQL?

| Hive           | RDBMS (MySQL, etc.)     |
|----------------|--------------------------|
| Works on **huge datasets** (TBs) | Works on **small/medium datasets** |
| Based on **MapReduce/Tez** | Based on traditional **DB engines** |
| **Batch processing** (slow) | **Real-time queries** (fast) |

---

## 8. How to calculate average departure delay per day in Hive?

```sql
SELECT flight_date, AVG(departure_delay)
FROM flight_info
GROUP BY flight_date;
```

---

## 9. How to create and use a database in Hive?

```sql
CREATE DATABASE dbname;
USE dbname;
```

---

## 10. What happens when you `DROP` a table?

- If **Internal table** → data + table **both deleted**.
- If **External table** → only **table is deleted**, **data stays**.

---

# 📌 Final Line if Sir Asks "Explain your Practical"

_"Sir, in this practical, I created a database and flight information tables using HiveQL, loaded flight data from HDFS, performed insertion, alteration, joining operations, created indexes for optimization, and finally analyzed departure delays for the year 2008."_

---

✅ With this cheatsheet, you’ll **answer ANYTHING** about Hive in your viva confidently.  
✅ Plus you have **full code + setup ready**.

---

# ⚡ Wrap up:

✅ Hadoop installed  
✅ Hive running  
✅ `flight_data.csv` uploaded  
✅ Full HiveQL queries written  
✅ Viva questions prepared

---

**Next move** ➔  
Tell me the next practical you want to prepare! 💥 (We can blitz it the same way!)  

What’s the next one? 🔥  
(You can just say: "Next: Facebook metrics Python" or whichever it is.)  
Ready when you are! 🚀
