First I'll give you the **Java MapReduce Code** for this practical — then immediately after that, a **cheatsheet** you can use for your notes or viva.  

---

# 📜 **Java MapReduce Code — Log File User Max Login Time**

**Assumption:**  
The log file format is like:  
```
user1  120
user2  90
user1  60
user3  150
```
*(username followed by session duration in minutes or seconds)*

---

### **1. Mapper Class**

```java
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Mapper;

public class LogMapper extends Mapper<Object, Text, Text, IntWritable> {

    private Text username = new Text();
    private IntWritable sessionDuration = new IntWritable();

    @Override
    protected void map(Object key, Text value, Context context) throws IOException, InterruptedException {
        // Split each line
        String[] parts = value.toString().split("\\s+");
        if (parts.length == 2) {
            username.set(parts[0]);
            sessionDuration.set(Integer.parseInt(parts[1]));
            context.write(username, sessionDuration);
        }
    }
}
```

---

### **2. Reducer Class**

```java
import java.io.IOException;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Reducer;

public class LogReducer extends Reducer<Text, IntWritable, Text, IntWritable> {

    @Override
    protected void reduce(Text key, Iterable<IntWritable> values, Context context) throws IOException, InterruptedException {
        int totalDuration = 0;
        for (IntWritable val : values) {
            totalDuration += val.get();
        }
        context.write(key, new IntWritable(totalDuration));
    }
}
```

---

### **3. Driver Class**

```java
import org.apache.hadoop.conf.Configuration;
import org.apache.hadoop.fs.Path;
import org.apache.hadoop.io.IntWritable;
import org.apache.hadoop.io.Text;
import org.apache.hadoop.mapreduce.Job;
import org.apache.hadoop.mapreduce.lib.input.FileInputFormat;
import org.apache.hadoop.mapreduce.lib.output.FileOutputFormat;

public class LogDriver {
    public static void main(String[] args) throws Exception {
        Configuration conf = new Configuration();
        Job job = Job.getInstance(conf, "User Login Time Calculation");

        job.setJarByClass(LogDriver.class);
        job.setMapperClass(LogMapper.class);
        job.setReducerClass(LogReducer.class);

        job.setOutputKeyClass(Text.class);
        job.setOutputValueClass(IntWritable.class);

        FileInputFormat.addInputPath(job, new Path(args[0]));   // Input file path
        FileOutputFormat.setOutputPath(job, new Path(args[1])); // Output directory path

        System.exit(job.waitForCompletion(true) ? 0 : 1);
    }
}
```

---

# 📋 **Cheatsheet Notes for Viva — MapReduce Log File Application**

---

## 1️⃣ **Problem Statement**
- Analyze a system log file.
- Calculate the **total login time** for each user.
- Identify the **user who spent maximum time** on the system.

---

## 2️⃣ **Input Format**
Each line of the input file contains:
```
<username> <duration>
```
Example:
```
alice 120
bob 60
alice 30
```

---

## 3️⃣ **Architecture Flow**
```
HDFS Input File → Mapper → Shuffle & Sort → Reducer → Output
```
- **Mapper:** Emits (username, session time)
- **Reducer:** Aggregates total session time per user

---

## 4️⃣ **Mapper Logic**
- Read each line of the log file.
- Split line into **username** and **duration**.
- Output: `(username, duration)`

> Example: `(alice, 120)`

---

## 5️⃣ **Reducer Logic**
- Receives all durations for a user.
- Sums all the durations.
- Outputs: `(username, total_duration)`

> Example: `(alice, 150)`

---

## 6️⃣ **Pseudo Distributed Mode Setup**
- Run Hadoop on a **single node**.
- Use local system for both NameNode and DataNode.
- Useful for testing on laptops/desktops.

---

## 7️⃣ **Commands to Run the Job**

```bash
# Put the log file in HDFS
hdfs dfs -put system_log.txt /input

# Run the MapReduce job
hadoop jar LogProcessor.jar LogDriver /input /output

# View the results
hdfs dfs -cat /output/part-00000
```

---

## 8️⃣ **Important Points to Mention in Viva**
- **Key Class Names:**  
  - Mapper: `LogMapper`
  - Reducer: `LogReducer`
  - Driver: `LogDriver`
- **Libraries Used:**  
  - `org.apache.hadoop.io.*`
  - `org.apache.hadoop.mapreduce.*`
- **Partitioning & Combiner:**  
  (Optional) Combiner could be used if there is heavy intermediate data.
- **Fault Tolerance:**  
  Hadoop handles mapper/reducer failures by re-executing tasks.

---

## 9️⃣ **Sample Output**
```
alice 150
bob 60
charlie 90
```
*(Then you can pick user with highest login duration if needed.)*

---

# ✅ **Summary Table**

| **Component** | **Role**                          |
|---------------|------------------------------------|
| **Mapper**    | Emits (user, duration)             |
| **Reducer**   | Sums up durations for each user    |
| **Driver**    | Configures and runs the job        |

---

Would you also like me to give you a **ready-to-use folder structure** for this Java project (so you can compile and run it immediately)? 🚀  
It'll include the `build.xml` if you want to compile using `ant`, too!  
(very useful for practical exam) 📁
