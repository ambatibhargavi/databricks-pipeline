import dlt


products_rules = {
    "rule_1" : "product_id IS NOT NULL",
    "rule_2" : "price >= 0"
}




@dlt.table(
    name="products_stag"
)
@dlt.expect_all(products_rules)
def products_stag():
    df = spark.readStream.table("dltbharru.source.product")
    return df