Awesome! Here’s a **simple `system_log.txt`** you can use immediately:

---

# 📄 `system_log.txt`

```
alice 120
bob 90
charlie 45
alice 60
david 30
bob 30
charlie 75
eve 50
david 120
eve 60
```

---

✅ **Explanation**:  
- `alice` has two sessions: 120 + 60 = **180**
- `bob` has two sessions: 90 + 30 = **120**
- `charlie` has two sessions: 45 + 75 = **120**
- `david` has two sessions: 30 + 120 = **150**
- `eve` has two sessions: 50 + 60 = **110**

---

# 🧠 Expected Output (after running MapReduce)

```
alice   180
bob     120
charlie 120
david   150
eve     110
```

*(Depending on Hadoop output format, there might be tab space.)*

---

# 📌 How to use this in your exam tomorrow:

1. Save this as `system_log.txt`
2. Upload to HDFS:

```bash
hdfs dfs -mkdir /input
hdfs dfs -put system_log.txt /input/
```

3. Then run your MapReduce job like we discussed:

```bash
hadoop jar dist/LogProcessor.jar LogDriver /input /output
```

4. See the results:

```bash
hdfs dfs -cat /output/part-00000
```

---

Would you also want a **VERY SHORT viva answer sheet** for this practical like:
- "What is Mapper doing?"
- "What is Reducer doing?"
- "Why Hadoop?"
(you can glance at it right before viva starts)? 📄👀  
Takes 2 mins to read! 🚀  
Should I prepare it?
