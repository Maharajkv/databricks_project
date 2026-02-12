from pyspark import pipelines as dp

@dp.table(
    name="customer_data",
    comment="Cleaned customer information",
    partition_cols=["country"]
)
def get_customer_data():
    return spark.read.format("csv").option("header", "true").load("dbfs:/mnt/your_mount/customer_data.csv")