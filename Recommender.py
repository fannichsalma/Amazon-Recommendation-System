from flask import Flask, render_template, request
import warnings
from flask import redirect
from pymongo import MongoClient, collection

import numpy as np
from kafka import KafkaProducer
from kafka import KafkaConsumer

warnings.simplefilter("ignore", UserWarning)
warnings.filterwarnings('ignore')
import pyspark
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, BooleanType, LongType, IntegerType
from pyspark.sql.functions import col, sum
from pyspark.sql.functions import mean, min, max
from pyspark.sql.functions import from_unixtime
import numpy
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType
import pyspark.sql.functions as F
from pyspark.ml.feature import StringIndexer
import os
import sys

os.environ['PYSPARK_PYTHON'] = sys.executable
os.environ['PYSPARK_DRIVER_PYTHON'] = sys.executable

# spark = SparkSession.builder.appName("Amazon Reviews").getOrCreate()
# https://img.freepik.com/free-vector/musical-pentagram-sound-waves-notes-background_1017-33911.jpg?w=2000
spark = SparkSession.builder.appName("Amazon Reviews") \
    .config("spark.driver.memory", "4g") \
    .config("spark.executor.memory", "4g") \
    .config("spark.executor.heartbeatInterval", "5000s") \
    .config("spark.network.timeout", "10000s") \
    .getOrCreate()

mongo_client = MongoClient('mongodb://localhost:27017')
db = mongo_client['RECOMMENDATIONS']
collection = db['User_Recommendation']
app = Flask(__name__)

recommendations = []


@app.route('/', methods=['GET'])
def home():
    return render_template('review.html')


@app.route('/', methods=['POST'])
def index():
    from pyspark.ml.recommendation import ALS, ALSModel
    models = ALSModel.load("E:\\AmazonResc")
    user_id = request.form['review']

    user_data = spark.createDataFrame([(user_id,)], ["Revindexed"])

    userRecs = models.recommendForUserSubset(user_data, numItems=5)  # Specify the number of recommendations
    rec = userRecs.collect()
    producer = KafkaProducer(bootstrap_servers=['localhost:9092'])


    recommendations.append(str(rec[0][1][1][0]))
    recommendations.append(str(rec[0][1][2][0]))
    recommendations.append(str(rec[0][1][3][0]))
    recommendations.append(str(rec[0][1][4][0]))

    document = {
        'user_id': user_id,
        'recommendations': recommendations
    }
#insert document in mongodb
    collection.insert_one(document)
    recommendations.append(user_id)


    for recommendation in recommendations:
        producer.send('Rec', value=recommendation.encode())

    return redirect('/result')


@app.route('/result')
def display_result():
    consumer = KafkaConsumer(
        'Rec',
        bootstrap_servers='localhost:9092',
        auto_offset_reset='earliest',
        group_id='i23'
    )
    i = 0
    rec = []
    # Poll for new messages
    for message in consumer:
        value = message.value.decode()
        rec.append(value)
        consumer.commit_async()
        i += 1
        if i == 4:
            break

    return render_template("outputRec.html", a=rec[0], b=rec[1], c=rec[2], d=rec[3])


if __name__ == '__main__':
    app.run(debug=True)
