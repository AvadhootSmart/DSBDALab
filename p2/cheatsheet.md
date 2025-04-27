Perfect! 🔥 Here's your **Viva Cheatsheet** for this practical — fast to read, powerful for tomorrow:

---

# 🎯 Viva Cheatsheet — Log File Processing using Hadoop MapReduce

---

## Q1. What is the purpose of this practical?

> ➔ **We process a system log file using Hadoop MapReduce to find users who logged in for the maximum period.**

---

## Q2. What does the Mapper do?

> ➔ **Mapper reads each line of the log file.**  
> ➔ **Splits the line into username and session time.**  
> ➔ **Emits (username, session_duration) as key-value pairs.**

Example:  
Input Line ➔ `alice 120`  
Mapper Output ➔ `(alice, 120)`

---

## Q3. What does the Reducer do?

> ➔ **Reducer takes all session times for each user.**  
> ➔ **Sums them up to find the total login duration per user.**

Example:  
Input ➔ `(alice, [120, 60])`  
Reducer Output ➔ `(alice, 180)`

---

## Q4. Why did we use Hadoop?

> ➔ **Hadoop can process large files in a distributed and fault-tolerant manner.**  
> ➔ **It splits the job into chunks and processes faster on multiple nodes (even in pseudo mode).**

---

## Q5. What is pseudo-distributed mode?

> ➔ **Hadoop runs all daemons (NameNode, DataNode, ResourceManager, NodeManager) on a single machine but treats them like different nodes.**  
> ➔ **Useful for development and testing.**

---

## Q6. What is HDFS?

> ➔ **HDFS (Hadoop Distributed File System) is used to store large files across multiple machines.**  
> ➔ **It breaks files into blocks and replicates them to ensure fault tolerance.**

---

## Q7. What happens if a Mapper or Reducer fails?

> ➔ **Hadoop automatically retries the task on another node to ensure the job completes successfully.**  
> ➔ **This makes Hadoop fault-tolerant.**

---

# ⚡ Bonus: Keywords to quickly use during viva

- **Key-Value Pairs**  
- **Splitting Phase (Map)**  
- **Aggregation Phase (Reduce)**  
- **Distributed Computing**  
- **Fault Tolerance**  
- **Scalability**

---

# 🧠 Pro-Tip for tomorrow:
In any viva, if you get confused — **use the word "distributed" and "fault-tolerant"** somewhere — examiner will get impressed!  
😂🎯

---

# ✅ You’re 100% ready for this practical!

If you want, I can also quickly make a **one-liner overview** you can tell at the start of viva when they ask:  
_"Tell me what you have done in this practical."_  
Want that too? (It's just 2-3 lines!) 🚀
