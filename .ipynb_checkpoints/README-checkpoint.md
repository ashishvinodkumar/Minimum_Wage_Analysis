# Minimum Wage Analysis


# Goal
The aim of this project is to analyze the effects on Unemployment Rate and GDP, caused by increasing minimum wages. Minimum wages are increased from a baseline of $7.25 in our treatment states (South Dakota, West Virginia, Nebraska) compared to our control states (Iowa, Idaho, Kansas) between 2010-2020 in the United States. Our goal is to estimate this causal effect using a Pre-Post Analysis, Difference-in-Difference Analysis, and Regression Analysis with fixed effects. We aim to use the control states as a reference to estimate the effects on the Unemployment Rate and GDP for the treatment states. We also aim to regress the unemployment rate on our treatment (minimum wages pre-2015 and post-2015), to estimate the Average Treatment on the Treated (ATT).

# Background 
Minimum wages have a substantial impact on a state’s economy. For instance, higher minimum wage would mean businesses must give workers higher pay, which could make businesses feel reluctant to hire more workers. While on the other hand, low wages could demotivate workers. The true effect on how to set minimum wage is a controversial topic, and has long been debated by economists and policy makers. This sparked our interest in applying causal inference to study how change in minimum wage would affect a state’s economy. With our hope to quantify the impact of change in minimum wage, we want to help policy makers and economists to make better decisions.

# Project Design
We found our dataset on the United States Census Government website, which contains the quarterly GDP, monthly Unemployment Rate, and annual minimum wage data for every state. We also plan on exploring state demographic information, such as population age sectors and labor forces, in hope to control our study. Some states follow the federal minimum wage and some states have their own wage policies (must be higher than federal minimum wage). We selected states that switched from federal minimum wage policy to their own policies to be in the treatment group and states that continue to adopt federal minimum wage to be in the control group. Our treatment states that deviated from the federal minimum wage were South Dakota, West Virginia and Nebraska, and our control states that continued to adopt the federal minimum wages were Iowa, Idaho, and Kansas. The year 2015 was identified as the ‘change year’ since the treatment states deviated in their minimum wages with respect to the Federal minimum of $7.25, compared to the control states.

# Model Results


