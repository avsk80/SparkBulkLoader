from pyspark.sql import *
from pyspark.sql.functions import regexp_extract, substring_index
import os

os.environ['PYSPARK_PYTHON'] = "D:\\anaconda3\envs\pyspark3\python.exe"
os.environ['PYSPARK_DRIVER_PYTHON'] = "D:\\anaconda3\envs\pyspark3\python.exe"

if __name__ == "__main__":
    spark = SparkSession \
        .builder \
        .master("local[3]") \
        .appName("LogFileDemo") \
        .getOrCreate()