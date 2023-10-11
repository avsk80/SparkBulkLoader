spark-submit --master yarn \
--deploy-mode cluster \
--py-files sbdl_lib.zip \
--files conf/spark.conf, conf/sbdl.conf, log4j.properties \
main.py qa 2022-08-02
