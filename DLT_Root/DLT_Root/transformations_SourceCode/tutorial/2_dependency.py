#from pyspark.sql.functions import *



# Staging area

#@dlt.table(
   # name = "staging_orders"
#)

#def staging_orders():

    # df = spark.readStream.table("dltbharru.source.orders")
     #return df
 

 # Creating Transformed area

#@dlt.view(
    #name = "transformed_orders"
#)

#def transformed_orders():

     #df = spark.readStream.table("staging_orders")
     #df = df.withColumn("order_status", lower(col("order_status")))
     #return df