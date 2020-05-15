# Analysis on Customer Lifetime Value
----------

# Background

In data science, one of the hottest topics is Churn Analysis.

**Churn Analysis** is a technique to predict whether a current customer will leave or stay in the near future base on information at present. It is crucial to many B2C businesses because the cost of retaining an existing customer is generally less than acquiring a new one. The marketer assigns a cost-benefit matrix based on the expected revenue for each group of customers.

## Motivation

Such a business decision was made based on there are only two types of customers, churn and not churn. However, it is not the most optimizing way to manage customer relationships by only two labels. In marketing, customers were dividing into several small groups that are similar demographics or spending habits, indicating the marketer should treat different segments separately. Similarly, the marketer could assign different customer value based on the expected revenue for customer segments.

Moreover, unlike some special cases like credit card or subscription membership, in more general business cases, customers will not notify the business when they want to leave, which is also called non-contractual. Customers don’t show up during a certain time still possible to come back in the future which would cause misclassification. To overcome the misclassification, a probabilistic model based on the customer purchase behaviors will be introduced in this article.

---------

# Theory

There is a trend that tranditional companies are hiring more and more data scientist to support their business decision making. The Churn analysis is a classical application example by predicting whether a customer will churn or not. 

However, the decision maker cannot making decision only based on the predicted probablities or predicted classification. They need to transform the classification into predicted revenue or cost which is commonly done by averaging the revenue from customer of past certain time. 

This method is often critized in two ways, one is lack of complexity by dividing customers into only two group, and other is averaging the revenue from customer indicates every customers spends the same.

There are existing theorical solutions in marketing for these two problems, Customer Segmentation and Customer Lifetime Value. We will introduce the brief theory and implementation in Python.

First, let's review on Churn analysis. 

## Churn

**Churn Analysis** is a technique to predict whether a current customer will leave or stay in the near future base on information at present. It is crucial to many B2C businesses because the cost of retaining an existing customer is generally less than acquiring a new one. In order to prevent customer churn, companies often provide retention offer to customers were predicted churned.

* **Churn**: Whether a current customer will continue purchasing during a particular period of time

Target Type: Binary

Common Algorithm: K-nearest neighbors, Naive Bayes Classification, Logister Regression, Ramdon Forest, Support Vector Machines, etc

Decision making base: Predict revenue by calculate 2X2 cost-benefit matrix mutiply by the confusion matrix.


## RFM Segmentation

The most common method to segmentize customers is using RFM to differiate customer purchasing behavior. RFM is representing Recency, Frequency and Monetary.

* **Recency**: How much time has passed since a customer’s last purchase? 

* **Frequency**: How often has a customer bought with the brand during a particular period of time? 

* **Monetary**: How much a customer has spent with the brand during a particular period of time?

from https://www.optimove.com/resources/learning-center/rfm-segmentation

To conduct RFM analysis, we sorted Recency, Frequency, Monetary value for all customers and ranked with 1~5. Each rank is a group so that we will have 5X5X5 = 125 groups.

Target Type: Categorical

Common Algorithm: K-nearest neighbors, Naive Bayes Classification, Support Vector Machines, etc

Decision making base: Predict revenue by calculate n X n cost-benefit matrix mutiply by a  n X n confusion matrix.


## CLTV
> In marketing, customer lifetime value (CLV or often CLTV), lifetime customer value (LCV), or lifetime value (LTV) is a prediction of the net profit attributed to the entire future relationship with a customer. By Wikipedia

### Defining “customer value”

One of the powers of CLV is that it is flexible enough to be applied across a range of business types, including retailer, direct sales, or subscription business.

In most B2C business, customer value could be defined as many ways, such as

* Gross Revenue
* Net Gross Margin
* Either one in a future certain time

Here, the customer lifetime value is defined as **Total Sales Maded from a Customer for a Period**, where
**Total Sales = Number of transactions * Single transaction amount = Number of transaction in Unit time * customer lifetime length * Single transaction amount**

To be less theorotical, 
Number of transaction in Unit time ~ Poission Distribution
Customer lifetime length ~ Expontial Distribution
Single transaction amount - Gamma Distribution

The combined model built is call Pareto/NBD Gamma Gamma model.

$$RMSE = \sqrt{\frac{\sum (\hat{y_i} - y_i)^{2}}{n}}$$

https://github.com/dataandcaffeine/pydata-seattle-2017/tree/master/lifetime-value
-------

# ML

## Data

We use anonymized transactional data from Kaggle which contains almost 350 million rows from over 300,000 customers. It is a good general data example of a B2C business.

* Date Range: 

`2012-03-02 to 2013-07-28`

After a quick EDA on the raw data, we only keep first 12 month of raw data and cut the data at 2012-12-01(at the end on 9th month) and makes the data before that time be our predictors and the data from 2012-12-02 to 2013-03-01 (10th to 12th month) to be the response.

* Features:

`customer_id, store_id, purchase_date, item_brand, item_department, item quantity and amount` 

To simplify all the models, we excluded any item inforation, such as brand, department etc, then transformed the raw transaction data into
`customer_id, store_id, first_purchase_date, last_purchase_date, average_purchase_amount, number_of_transactions, last_3_months_spend, next_3_months_spend`

where `last_3_months_spend` is total transaction amount from 2012-09-02 to 2012-12-01 and `next_4_months_spend` is total transaction amount. Other helper features will be introduced on specific model.

### Train test split

The train-test set is split on 80:20 randomly.

## EDA

## Churn

New feature as response:
`Churn`: Value 1 when customer have at least one purchase during 2012-12-02 to 2013-03-01, else 0.

ML Algorithm: Crossvalidate based on F1 score for following models:

K-nearest neighbors, Naive Bayes Classification, Logister Regression, Ramdon Forest.

Decision making base: Predict revenue by calculate 2X2 cost-benefit matrix mutiply by the confusion matrix.

## RFM

New feature as response:
`RFM Class`: a string `a - b - c` abc represents the RFM ranking.

ML Algorithm: Crossvalidate based on F1 score for following models:

K-nearest neighbors, Naive Bayes Classification, Logister Regression, Ramdon Forest.

Decision making base: Predict revenue by calculate 2X2 cost-benefit matrix mutiply by the confusion matrix.

## CLTV

Pareto/NBD Model a hierarchical Bayesian model. 
Gamma-Gamma

## Comparision

---------
# Summary

## Takeaways

## What's next?

## Thanks to
Pareto/NBD “Counting Your Customers” framework proposed by Schmittlein, Morrison, and Colombo (1987) 

The Gamma-Gamma Model of Monetary Value Peter S. Fader, Bruce G. S. Hardie† February 2013

RFM and CLV: Using Iso-value Curves for Customer Base Analysis Peter S. Fader, Bruce G. S. Hardie, Ka Lok Lee


