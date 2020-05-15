import pyspark as ps    # for the pyspark suite
spark = (ps.sql.SparkSession
         .builder
         .master('local[4]')
         .appName('lecture')
         .getOrCreate()
        )
sc = spark.sparkContext

df = spark.read.csv('transactions.csv',
                    header=True,       # use headers or not
                    quote='"',         # char for quotes
                    sep=",",           # char for separation
                    inferSchema=True)  # do we infer schema or not ?


df.createOrReplaceTempView('trans')

# for EDA
query = """SELECT distinct chain, 
                count(distinct id) as total_customer,
                sum(purchaseamount) as total_sales
                FROM trans
                GROUP BY chain
             """
sdf = spark.sql(query)
sdf.show()
pdf = sdf.toPandas()
pdf.to_csv("chain_sales.csv")

query = """SELECT distinct dept, 
                count(distinct id) as total_customer,
                sum(purchaseamount) as total_sales
                FROM trans
                GROUP BY dept
             """
sdf = spark.sql(query)
sdf.show()
pdf = sdf.toPandas()
pdf.to_csv("dept_sales.csv")

query = """SELECT distinct category, 
                count(distinct id) as total_customer,
                sum(purchaseamount) as total_sales
                FROM trans
                GROUP BY category
             """
sdf = spark.sql(query)
sdf.show()
pdf = sdf.toPandas()
pdf.to_csv("category_sales.csv")

query = """SELECT distinct brand, 
                count(distinct id) as total_customer,
                sum(purchaseamount) as total_sales
                FROM trans
                GROUP BY brand
             """
sdf = spark.sql(query)
sdf.show()
pdf = sdf.toPandas()
pdf.to_csv("brand_sales.csv")

query = """SELECT distinct MONTH(date) as month, 
                count(distinct id) as total_customer,
                sum(purchaseamount) as total_sales
                FROM trans
                GROUP BY month
             """
sdf = spark.sql(query)
# sdf.show()
pdf = sdf.toPandas()
pdf.to_csv("month_sales.csv")

# For model

query = """SELECT distinct id, 
                min(date) as first_purchase_date,
                max(date) as last_purchase_date,
                count(distinct date) as total_purchases,
                sum(purchasequantity) as total_purchase_quantity,
                sum(purchaseamount) as total_purchase_amount,
                SUM(CASE WHEN date >= '2012-11-02' THEN purchaseamount ELSE 0 END) AS last_4_months_spend
                FROM trans
                WHERE date <= '2013-03-01'
                GROUP BY id
             """
sdf = spark.sql(query)
# sdf.show()

rdf = sdf.toPandas()
rdf.to_csv("ndb1.csv")

query = """SELECT distinct id, 
                min(date) as first_purchase_date,
                max(date) as last_purchase_date,
                count(distinct date) as total_purchases,
                sum(purchasequantity) as total_purchase_quantity,
                sum(purchaseamount) as total_purchase_amount
                FROM trans
                WHERE date between '2013-03-02' and '2013-07-01'
                GROUP BY id
             """
sdf = spark.sql(query)
# sdf.show()

# Datebase for Churn prediction
fdf = pd.merge(rdf, pdf[["id","total_purchases"]], how="left", left_on="id", right_on="id")
fdf.rename({"total_purchases_y":"next_4_months_spend"}, axis=1, inplace=True)
fdf["churn"] = fdf["next_4_months_spend"].apply(lambda x:0 if x>0 else 1)

fdf.to_csv("fdb_churn.csv")

# Datebase for RFM prediction
pdf["recency"] = pd.to_datetime("2013-07-02") - pdf["last_purchase_date"]
pdf["recency"] = pdf["recency"].apply(lambda x:x.days)
pdf.rename({"total_purchases" : "frequency", "total_purchase_amount" : "monetery"},
           axis = 1,
          inplace = True)

# --Calculate R and F groups--
# Create labels for Recency and Frequency
r_labels = range(4, 0, -1); f_labels = range(1, 5)
# Assign these labels to 4 equal percentile groups 
r_groups = pd.qcut(pdf['recency'], q=4, labels=r_labels)
# Assign these labels to 4 equal percentile groups 
f_groups = pd.qcut(pdf['frequency'], q=4, labels=f_labels)
# Create new columns R and F 
pdf = pdf.assign(R = r_groups.values, F = f_groups.values)
pdf.head()

# Create labels for MonetaryValue
m_labels = range(1, 5)
# Assign these labels to three equal percentile groups 
m_groups = pd.qcut(pdf['monetery'], q=4, labels=m_labels)
# Create new column M
pdf = pdf.assign(M = m_groups.values)

pdf["RFM"] = pdf["R"].astype(str) + "-"  + pdf["F"].astype(str) + "-" + pdf["M"].astype(str)

# Datebase for RFM prediction
fdf = pd.merge(rdf, pdf[["id","RFM", "monetery"]], how="left", left_on="id", right_on="id")
fdf.rename({"monetery":"next_4_months_spend"}, axis=1, inplace=True)
fdf["churn"] = fdf["next_4_months_spend"].apply(lambda x:0 if x>0 else 1)


