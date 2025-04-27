import pandas as pd
import sys
import os
from pyhive import hive

# Part a: Data Analysis using MapReduce in PyHadoop (using Hadoop Streaming)
# Example: Count fires by month using MapReduce

# Mapper script (mapper.py)
mapper_code = """
#!/usr/bin/env python
import sys

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    # Skip header
    if line.startswith('X,Y,month'):
        continue
    # Split CSV line
    fields = line.split(',')
    if len(fields) >= 3:
        month = fields[2]  # Month is the third column
        # Emit month and count
        print(f'{month}\t1')
"""

# Reducer script (reducer.py)
reducer_code = """
#!/usr/bin/env python
import sys

current_month = None
current_count = 0

# Read input from standard input
for line in sys.stdin:
    line = line.strip()
    month, count = line.split('\t')
    count = int(count)
    
    # If same month, increment count
    if current_month == month:
        current_count += count
    else:
        # Output previous month count
        if current_month:
            print(f'{current_month}\t{current_count}')
        current_month = month
        current_count = count

# Output the last month
if current_month:
    print(f'{current_month}\t{current_count}')
"""

# Save mapper and reducer scripts
with open('mapper.py', 'w') as f:
    f.write(mapper_code)
with open('reducer.py', 'w') as f:
    f.write(reducer_code)

# Make scripts executable
os.system('chmod +x mapper.py reducer.py')

# Run Hadoop Streaming job
hadoop_cmd = """
hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming.jar \
    -input /user/forestfires/forestfires.csv \
    -output /user/forestfires/output \
    -mapper mapper.py \
    -reducer reducer.py \
    -file mapper.py \
    -file reducer.py
"""

print("Running MapReduce job...")
os.system(hadoop_cmd)

# Display results from HDFS
print("MapReduce Results (Fires by Month):")
os.system('hdfs dfs -cat /user/forestfires/output/part-*')

# Part b: Data Mining in Hive
# Connect to Hive and perform queries

# Establish Hive connection
conn = hive.connect(host='localhost', port=10000, database='default')
cursor = conn.cursor()

# Create a Hive table for the Forest Fire dataset
create_table_query = """
CREATE TABLE IF NOT EXISTS forest_fires (
    X INT,
    Y INT,
    month STRING,
    day STRING,
    FFMC FLOAT,
    DMC FLOAT,
    DC FLOAT,
    ISI FLOAT,
    temp FLOAT,
    RH FLOAT,
    wind FLOAT,
    rain FLOAT,
    area FLOAT
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
TBLPROPERTIES ('skip.header.line.count'='1')
"""

cursor.execute(create_table_query)

# Load data from HDFS into Hive table
load_data_query = """
LOAD DATA INPATH '/user/forestfires/forestfires.csv' 
OVERWRITE INTO TABLE forest_fires
"""

cursor.execute(load_data_query)

# Data Mining Query 1: Average area burned by month
query1 = """
SELECT month, AVG(area) as avg_area_burned
FROM forest_fires
GROUP BY month
"""

cursor.execute(query1)
results = cursor.fetchall()
print("\nHive Query 1: Average Area Burned by Month")
for row in results:
    print(row)

# Data Mining Query 2: Top 5 conditions with highest fire area
query2 = """
SELECT temp, wind, area
FROM forest_fires
WHERE area > 0
ORDER BY area DESC
LIMIT 5
"""

cursor.execute(query2)
results = cursor.fetchall()
print("\nHive Query 2: Top 5 Conditions with Highest Fire Area")
for row in results:
    print(row)

# Close Hive connection
cursor.close()
conn.close()
