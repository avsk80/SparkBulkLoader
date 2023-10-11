import sys

from lib import Utils
from lib.logger import Log4j

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: sbdl {local, qa, prod} {load_date} : Arguments are missing")
        sys.exit(-1)
        
    job_run_env = sys.argv[1].upper()
    load_date = sys.argv[2]
    
    spark = Utils.get_spark_session(job_run_env)
    print(spark)
    logger = Log4j(spark)
    
    print("After Log4j")
    logger.info("Finished creating Spark Session")