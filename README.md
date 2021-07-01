# Goal
We aim to analyze the effects on the unemployment rate caused by an increase in minimum wages, from a baseline of $7.25, in our treatment states (South Dakota, West Virginia, Nebraska) compared to our control states (Iowa, Idaho, Kansas) between 2010-2020 in the United States. Our goal is to estimate this causal effect using a Difference in Difference analysis where we aim to use the control states as a reference to estimate the effects on the unemployment rate for treatment states. We also aim to regress the unemployment rate on our treatment (minimum wages pre-2015 and post-2015), to estimate the Average Treatment on the Treated (ATT).

# Background 
Minimum wages have a substantial impact on a state’s economy. For instance, higher minimum wage would mean businesses must give workers higher pay and could make businesses feel reluctant to hire more workers. While on the other hand, low wages could demotivate workers. The true effect on how to set minimum wage is a controversial topic, and has long been debated by economists and policy makers. This sparked our interest in applying causal inference to study how change in minimum wage would affect a state’s economy. With our hope to quantify the impact of change in minimum wage, we want to help policy makers and economists to make better decisions.

# Project Design
We found our dataset on the United States Census Government website, which contains the quarterly GDP , monthly unemployment rate, and annual minimum wage data for every state. We also plan on finding state demographic information, such as population age sectors and labor forces, in hope to control our study. Some states follow the federal minimum wage and some states have their own wage policies (must be higher than federal minimum wage). We selected states that switched from federal minimum wage policy to their own policies to be in the treatment group and states that continue to adopt federal minimum wage to be in the control group. We plan to design a difference-in-difference analysis to quantify the effect of changing minimum wage on the effect on the unemployment rate.

# Model Results
We aim to plot a difference in difference graph that outlines both the treatment and control pre 2015 and post 2015. The year 2015 was identified as the ‘change year’ since the treatment states deviated in their minimum wages with respect to the Federal minimum of $7.25, compared to the control states. Below is an example of a diff-in-diff plot that allows us to measure the unemployment rate between treatment and control states.

![Sample_Diff_in_Diff](https://user-images.githubusercontent.com/26104722/113231777-f7b52f80-9269-11eb-95e0-894e25218a5c.png)

![ATT_Table](https://user-images.githubusercontent.com/26104722/113231958-419e1580-926a-11eb-9a34-6a87431e5823.png)


# Final Variables
In order to complete this analysis we will need:
> A set of control states that follow the minimum wage ($7.25) from 2010 - 2020 (Iowa, Idaho, Kansas)
> A set of treatment states that have similar increases above the Federal minimum wage beginning in 2015 (South Dakota, West Virginia, Nebraska)
> The unemployment rates for each state in our control and treatment groups
> The GDP for the states in our control and treatment groups
> Other demographic data for the states in our control and treatment groups (i.e. labor force, age, sex) 


