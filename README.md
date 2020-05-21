# Analysis on Customer Lifetime Value
----------

# Background

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

> how much will the customer buy in the future?

In this study, we define the CLTV of a customer as the future spending(long term of a time range) of the customer from present.

----------

# Methodology

The problem of CLTV is a forecasting problem which often could be modelled with supervised machine learning methods in Data Science. However, it would be much more interpretable and straightforward if we modeled in a statistical model. 

Back in 1987, the first probabilistic model able to estimate customer future purchase was made by Schmittlein, Morrison, and Colombo. Then in 1999, Colombo and Jiang developed the gamma-gamma customer spending model which completes the customer lifetime value theory.

## Brief walkthrough

The essential idea of CLTV modelling is to decompose the total spending of a customer

> Total Sales = Number of transactions * Single transaction amount
> = Number of transaction in Unit time 
> * Customer Purchasing Lifetime Length 
> * Single Transaction Amount

Each element is following a common probability distribution.

> Number of transaction in Unit time ~ Poisson Distribution
> Customer Purchasing Lifetime Length ~ Exponential Distribution
> Single Transaction Amount ~ Gamma Distribution

We could utilize the customer purchasing history to estimate the distribution parameters. For detail derivation, please refer to the papers in appendix.

## Project setting

We are going to apply the CLTV model to a real-life e-commerce case and compare its performance to traditional machine learning methods.

# Model

## Data

## CLTV Model

## Other Model

# Applications

## Who’s VIP

## Survival Probability

# Summary

## Takeaways

* CLTV model reduces bias in customer spending prediction than using the mean.
* CLTV helps identify the most value customer
* Alternative way to predict churn
Integrate with Churn Prediction. Would it be a good way to fill in the cost-benefit matrix? 
Expend the model to include more transactional information, i.e. what they buy.

## What’s next
* Integrate with Churn Prediction. Would it be a good way to fill in the cost-benefit matrix? 
* Expend the model to include more transactional information, i.e. what they buy.

## Thanks to
Pareto/NBD “Counting Your Customers” framework proposed by Schmittlein, Morrison, and Colombo (1987) 

The Gamma-Gamma Model of Monetary Value
Peter S. Fader, Bruce G. S. Hardie February 2013
http://brucehardie.com/notes/025/gamma_gamma## Thanks to
Pareto/NBD “Counting Your Customers” framework proposed by Schmittlein, Morrison, and Colombo (1987) 

The Gamma-Gamma Model of Monetary Value
Peter S. Fader, Bruce G. S. Hardie February 2013
http://brucehardie.com/notes/025/gamma_gamma
