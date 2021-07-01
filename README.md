# Minimum Wage Analysis

Full Report: 

https://github.com/ashishvinodkumar/Minimum_Wage_Analysis/blob/main/30_Report/Causal_Inference_Minimum_Wage_Analysis_Report.pdf

Presentation Video: 

https://youtu.be/sedPOnExlcE

# Goal
The aim of this project is to analyze the effects on Unemployment Rate and GDP, caused by increasing minimum wages. Minimum wages are increased from a baseline of $7.25 in our treatment states (South Dakota, West Virginia, Nebraska) compared to our control states (Iowa, Idaho, Kansas) between 2010-2020 in the United States. Our goal is to estimate this causal effect using a Pre-Post Analysis, Difference-in-Difference Analysis, and Regression Analysis with fixed effects. We aim to use the control states as a reference to estimate the effects on the Unemployment Rate and GDP for the treatment states. We also aim to regress the unemployment rate on our treatment (minimum wages pre-2015 and post-2015), to estimate the Average Treatment on the Treated (ATT).

# Background 
Minimum wages have a substantial impact on a state’s economy. For instance, higher minimum wage would mean businesses must give workers higher pay, which could make businesses feel reluctant to hire more workers. While on the other hand, low wages could demotivate workers. The true effect on how to set minimum wage is a controversial topic, and has long been debated by economists and policy makers. This sparked our interest in applying causal inference to study how change in minimum wage would affect a state’s economy. With our hope to quantify the impact of change in minimum wage, we want to help policy makers and economists to make better decisions.

# Project Design
We found our dataset on the United States Census Government website, which contains the quarterly GDP, monthly Unemployment Rate, and annual minimum wage data for every state. We also plan on exploring state demographic information, such as population age sectors and labor forces, in hope to control our study. Some states follow the federal minimum wage and some states have their own wage policies (must be higher than federal minimum wage). We selected states that switched from federal minimum wage policy to their own policies to be in the treatment group and states that continue to adopt federal minimum wage to be in the control group. Our treatment states that deviated from the federal minimum wage were South Dakota, West Virginia and Nebraska, and our control states that continued to adopt the federal minimum wages were Iowa, Idaho, and Kansas. The year 2015 was identified as the ‘change year’ since the treatment states deviated in their minimum wages with respect to the Federal minimum of $7.25, compared to the control states.

# Model Results
By using pre-post and difference-in-difference analysis simultaneously on our treatment states, we can provide a visualization for the impact of key response variables such as unemployment rate and GDP for treatment states that changed their minimum wages in 2015. We also performed regression analysis to further interpret the observed differences.

## Unemployment Rate
<p align="center">
<img src="https://user-images.githubusercontent.com/26104722/124047108-6462d600-d9e1-11eb-9e12-e491d47a6cdc.png" width="600" height="600">
</p>

Through the difference-in-difference plot we observe that the trendline for both treatment and control states are not parallel pre-2015. We also observe that the treatment line has flattened post-2015 and moves from being below the control states line to above the control states line. More importantly, since the trendlines for treatment and control are not parallel pre-2015, we cannot make a reasonable comparison on the effects of increasing minimum wages having a direct impact on unemployment rate.

To better analyze the slight flattening of unemployment rate post-2015, we regressed Unemployment Rate on states that increased their minimum wages (treatment), years after 2015 (post), states that increased their minimum wages after 2015 (interaction between treatment:post), and added a fixed effect for the 6 states (3 control states and 3 treatment states). We observed that the p-values of all features, except Kansas state, is below an alpha of 0.05. More specifically, the interaction term, representing all states that increased their minimum wages post-2015, also corresponds to the observed difference-in-difference change from the plot above. The coefficient of this interaction term is 1.4092 and is statistically significant. As a result, the previous observation where the treatment trendline post-2015 flattens and increases above the control trendline, can be attributed to a difference-in-difference value of 1.4092. We can interpret this result as, for a given treatment state that increased its minimum wages after 2015, the data showcases an increase in unemployment rate.
  
<p align="center">
<img src="https://user-images.githubusercontent.com/26104722/124047254-befc3200-d9e1-11eb-8958-4831d3a382d3.png" width="600" height="400">
</p>

## GDP Analysis
<p align="center">
<img src="https://user-images.githubusercontent.com/26104722/124047104-63ca3f80-d9e1-11eb-9f83-f089815d5f4a.png" width="600" height="600">
</p>

We observe that the treatment and control trendlines are not exactly parallel pre-2015. The control states line has a slightly higher rate of increase in GDP compared to the treatment states line. Due to this, we cannot make a reasonable comparison to directly attribute changes from increasing minimum wages for treatment states.

To better analyze the above observations, we regressed GDP on states that increased their minimum wages (Treatment), years after 2015 (Post), states that increased their minimum wages after 2015 (interaction between Treatment:Post), and added a fixed effect for the 6 states (3 control states and 3 treatment states). We observed that the p-values of all features, except Virginia state, is below an alpha of 0.05. More importantly, the interaction term representing all states that increased their minimum wages post-2015, also corresponds to the observed difference-in-difference change from the plot above. The coefficient of this interaction term is -8,567.285 million dollars and is statistically significant. We can interpret this result as, for a given treatment state that increased its minimum wages after 2015, the data showcases a decrease in GDP.

<p align="center">
<img src="https://user-images.githubusercontent.com/26104722/124047252-befc3200-d9e1-11eb-83e6-a55d92a59aa4.png" width="600" height="400">
</p>

# Conclusion
Utilizing pre-post and differences-in-differences methodology, this article examined the causal effect of raising minimum wage on macro-level indicators such as unemployment rate and GDP, measuring economic prosperity. It took advantage of the year 2015 as a threshold, distinguishing the federal minimum wage policy implementations in different states,  by which we were able to identify the effect of the policy on state economies through quantifying the differences in indicators between the treatment states and the control states.

By visualizing the changes in trend for unemployment rate and GDP before and after the threshold year, the report was trying to reveal the effect of raising the minimum wage on them. However with the difference-in-difference plots, no clear evidence was observed which could support the causal relationship of minimum wages on both unemployment rate and GDP.

Meanwhile, the regression analysis unveiled empirical evidence of causal effects on both unemployment rate and GDP. Specifically, the results showed that there was a statistically significant effect of raising the minimum wage on unemployment rate in terms of differences-in-differences, meaning the minimum wage hike in the treatment states would increase 1.4092 units on average in unemployment rate relative to the control states, controlling for states’ variations. Furthermore, the effect of minimum wage on GDP was also significant from the perspective of differences-in-differences, causing 8567.285 million dollars decrease on average for the treatment states relative to the control states when controlling for states’ variations. 

However, we would admit that the above is just a preliminary study right now. There are various confounding factors that are not included such as population, race, sex and age, but they are definitely exerting impacts on our economic measurements, which could alter the current conclusions. Moreover, our experiment design is not perfect since we were limited to states that concurrently changed their minimum wage legislation. Many states have deviated from the Federal minimum wage by different amounts, but did so at different times - rendering them ineffective for our analysis. A more comprehensive analysis might look at all states that changed their minimum wage, regardless of year. Therefore, further study should be conducted focusing on the improving of experiment design and also considering more influential factors in our models.

