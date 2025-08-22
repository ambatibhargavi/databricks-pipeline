import dlt



customers_rules = {
    "rule_1" : "customer_id IS NOT NULL",
    "rule_2" : "customer_name IS NOT NULL"
}

@dlt.table(
    name="customers_stag"
)
@dlt.expect_all(customers_rules)
def products_stag():
    df = spark.readStream.table("dltbharru.source.customer ")
    return df