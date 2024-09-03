# Amazon-Recommendation-System
Overview
This project focuses on creating a live product recommendation system tailored to customer preferences, utilizing a vast Amazon product dataset of 128 GB. It leverages big data processing tools like Apache Spark, MongoDB, and Apache Kafka to deliver real-time product recommendations.

Project Goal
The main goal is to develop a highly efficient recommendation system capable of handling large-scale data, analyzing customer reviews, and providing personalized product suggestions through a web interface. The system analyzes customer feedback, trains a recommendation model, and delivers real-time recommendations.

Methodology
Data Loading:

The Amazon dataset is loaded into Apache Spark using a StructType schema to ensure data type safety, minimizing runtime errors.
Schema definition and initial data inspection are performed.
Data Cleaning:

Missing numeric values are replaced with 0, while missing string values are filled with empty strings.
The text is converted to lowercase, and all punctuation marks and URLs are removed.
Data Storage in MongoDB:

The cleaned dataset is efficiently stored in MongoDB for subsequent analysis.
Exploratory Data Analysis (EDA):

Sentiment Analysis of Reviews: Reviews are analyzed based on sentiment derived from ratings.
Result: Most products have a positive sentiment, with an average rating of 5.
Scatter Plot - Reviews vs. Review Length: Visualization of the distribution of review lengths.
Top 10 Most Reviewed Products: Sentiment and profitability analysis of the top 10 most-reviewed products.
Result: Products with the most reviews generally receive good ratings.
Top 10 Least Reviewed Products: Analysis of the sentiment of the least reviewed products.
Result: Products with fewer reviews tend to have poorer ratings.
Model Training:

Initial attempts to train the model on the entire dataset were hampered by memory limitations.
The model was successfully trained on a smaller subset using collaborative filtering techniques (ALS algorithm).
Integration with Kafka and MongoDB:

A web application built using Flask allows users to interact with the recommendation system.
Real-time product recommendations are streamed using Apache Kafka based on user input.
Recommended products are stored in MongoDB and displayed to users via Kafka consumers.
Technologies and Tools
Apache Spark: Efficient data processing and integration with MongoDB.
MongoDB: Storing and managing the cleaned dataset and user preferences.
Pandas and Matplotlib: Performing EDA and creating visualizations.
Flask: Web application framework for user interaction.
Apache Kafka: Real-time streaming and communication between the backend and the user interface.
Machine Learning: Collaborative filtering using the ALS (Alternating Least Squares) algorithm.
Conclusion
This project demonstrates the power of combining big data processing, machine learning, and real-time streaming to build a personalized product recommendation system. Despite the challenges of handling a large dataset, the system effectively processes and analyzes data, providing valuable insights and recommendations. The use of Apache Spark, MongoDB, and Apache Kafka underscores the system's ability to manage large-scale data and offers a scalable solution for real-time product recommendations.
