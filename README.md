# Analysis on Customer Lifetime Value
----------
Vince Pan

-----------------------

# Table of Contents
[1. Background](#Background)<br> 
[2. Methodology](#Methodology)<br> 
>   [2.1. Brief walkthrough](#bw)<br>
>   [2.2. Project setting](#ps)<br>
    
[3. Model](#Model)
> [3.1. Data preprocessing](#Model)<br>
> [3.2. CLTV Model](#cm)<br>
> [3.3. Other Model](#om)<br>

[4. Applications](#Applications)
> [4.1. Who’s VIP](#Applications)<br>
> [4.2. Churn Alarm](#ca)<br>

[5. Summary](#sm)

[6. Appendix](#Appendix)

-----------------------


# Background
<a id="Background"> </a>
## Motivation

In marketing, one question often being asked is what is a **C**ustomer **L**ife**T**ime **V**alue(CLTV or LTV). 

CLTV is a great tool to quantify marketing events, and able to help
* Determine new customer acquisition spend
* Evaluating marketing campaign ROI
* Prioritize customer support resource
* Even for sales prediction

## Definition

By definition

> **Customer lifetime value** is the present value of the future (net) cash flows associated with the customer.

In practice, we usually simplify the question to 

**How much will the customer buy in the future?**

In this study, we define the CLTV of a customer as the future spending(long term of a time range) of the customer from present.

----------

# Methodology
<a id="Methodology"> </a>
The problem of CLTV is a forecasting problem which often could be modelled with supervised machine learning methods in Data Science. However, it would be much more interpretable and straightforward if we modeled in a statistical model. 

Back in 1987, the first probabilistic model able to estimate customer future purchase was made by Schmittlein, Morrison, and Colombo. Then in 1999, Colombo and Jiang developed the gamma-gamma customer spending model which completes the customer lifetime value theory.

## Brief walkthrough
<a id="bw"> </a>
The essential idea of CLTV modelling is to decompose the total spending of a customer

> Total Sales = Number of transactions * Single transaction amount
> = Number of transaction in Unit time * Customer Purchasing Lifetime Length * Single Transaction Amount


Each element is following a common probability distribution.

> * Number of transaction in Unit time ~ Poisson Distribution
> * Customer Purchasing Lifetime Length ~ Exponential Distribution
> * Single Transaction Amount ~ Gamma Distribution

We could utilize the customer purchasing history to estimate the distribution parameters. For detailed derivation, please refer to the papers in the appendix.

## Project setting
<a id="ps"> </a>
We are going to apply the CLTV model to a real-life e-commerce case and compare CLTV model’s performance to traditional supervised learning methods including Random Forest, OLS, etc.


# Model
<a id="Model"> </a>
## Data preprocessing

### Data Source

We use a typical transactional dataset which includes the person, time and amount of the transaction. The dataset describes all transaction records for a UK-based and registered non-store online retail which can also be found in https://www.kaggle.com/carrie1/ecommerce-data.
 
The original dataset was not extracted with the purpose of CLTV study. We truncate the date range into 12 month and keep the purchasing history with below features.
 
Date Range: 2010-12-01 ~ 2011-11-30
Features: 
‘Purchase Date, Customer ID, Purchase Amount’
 
 
### EDA
 
Data points: 406829
Number of Transactions*: 19296
Number of customer: 4372
Average Transaction Amount: 430
 
* Note: One transaction is defined as the aggregation of all purchased records made in the same day.
 
The total sales of the company does not have a clear trend but there is a surge in Winter.
Trend here
 
 
### Train-Test Split
In order to make the data fit into our CLTV, we divided the dataset by time. The first 10 month data were treated as our training data and the last two month as our target or test set.
 
For comparison with supervised methods, we divided the training set into 8:2 in months to set up the predictor and target.
 
Plot here
 



## CLTV Model
<a id="cm"> </a>
### Feature Engineering

In 


### Model Stats

## Other Model
<a id="om"> </a>


# Applications
<a id="Applications"> </a>
## Who’s VIP

## Churn Alarm
<a id="ca"> </a>


# Summary
<a id="sm"> </a>
## Takeaways

* CLTV model reduces bias in customer spending prediction than using the mean.
* CLTV helps identify the most value customer
* Alternative way to predict churn
Integrate with Churn Prediction. Would it be a good way to fill in the cost-benefit matrix? 
Expend the model to include more transactional information, i.e. what they buy.

## What’s next
* Integrate with Churn Prediction. Would it be a good way to fill in the cost-benefit matrix? 
* Expend the model to include more transactional information, i.e. what they buy.

# Appendix

<a id="Appendix"> </a>

## Thanks to
Pareto/NBD “Counting Your Customers” framework proposed by Schmittlein, Morrison, and Colombo (1987) 

The Gamma-Gamma Model of Monetary Value
Peter S. Fader, Bruce G. S. Hardie February 2013
http://brucehardie.com/notes/025/gamma_gamma## Thanks to
Pareto/NBD “Counting Your Customers” framework proposed by Schmittlein, Morrison, and Colombo (1987) 

The Gamma-Gamma Model of Monetary Value
Peter S. Fader, Bruce G. S. Hardie February 2013
http://brucehardie.com/notes/025/gamma_gamma
