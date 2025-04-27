from mrjob.job import MRJob


class FireCount(MRJob):
    def mapper(self, _, line):
        # Assume CSV: month,day,temp,wind,area_burned
        fields = line.split(',')
        month = fields[0]
        yield month, 1

    def reducer(self, month, counts):
        yield month, sum(counts)


if __name__ == '__main__':

    # -------------------------------------

    #     CREATE TABLE forest_fires(month STRING, day STRING, temp FLOAT, wind FLOAT, area FLOAT)
    # ROW FORMAT DELIMITED FIELDS TERMINATED BY ','
    # LOAD DATA INPATH 'forestfires.csv' INTO TABLE forest_fires
    # SELECT month, SUM(area) as total_area_burned
    # FROM forest_fires
    # GROUP BY month
    # FireCount.run()
