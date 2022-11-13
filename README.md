# Optimine
![Dark Blue with Space Photos Movie Ticket-2](https://user-images.githubusercontent.com/34663815/201524020-4903a89a-138f-4ab2-be2d-9c92f82a6d1a.jpg)

## Inspiration
EOG provided us with an extensive dataset with drill bit data from 20 extensive asteroid mining expeditions. We were inspired to construct a web app that used data visualization to chart and AI/ML (linear neural network) to analyze the best mining plan on future expeditions. Current engineers at EOG sought to tool to analyze and better visualize previous mining expedition data. We proposed this full stack application, where this application offers a variety of valuable data to the engineers at EOG: delivers metrics to evaluate the performance of prior expeditions, optimizes/suggests better alternative bit drills to use at specific depths, and chart a full course optimized mining plan based on factors like affordability & time.

## What it does
The web app visualizes data from the EOG dataset and depending on user input gives the suggested plan and best drill bit to use at certain intervals. The user input consists of the allowed budget, time, and the length of an interval they want to look at. The user can either get data from each interval or get the overall data. If the user looks at the interval, they will see the best drill bit at that depth. They will also see the cost, time, and a calculated efficiency score of each drill bit at that depth. If the user looks at the overall statistics, they will see our suggested bit for each interval. This plan will also show a comparison to the given budget and time. There will be graphs plotting each past run in the dataset against our suggested plan based on cost per foot of bit depth, time per foot of bit depth, and our calculated score per foot of bit depth.
## How we built it
### UI/UX Design
We used Figma to layout and design our UI to have an idea of what we were coding. By using Figma we were able to structure and layout most of the components to see in hindsight how our final application would appear. For the frontend we used Streamlit to implement most of the custom HTML/CSS components built from scratch.

###Backend Development

####Data Preprocessing

#### Data Computation 
To calculate the time between each subsequent intervals in the dataset, the change in depth was calculated and divided by the rate of penetration by the bit in use.  The cost is calculated through a cost function which is computed by

CostPerRun + ( FT * CostPerFoot ) + ( Hours * CostPerHour )

In order to compute the most efficient possible drilling plan at specific depth intervals, we utilized a efficient score function which is computed by linear neural network model.



#### Data Analysis 

#### Data Visualization 

For the user interface, we used Streamlit to keep our code mainly in python. We used elements of CSS and HTML to help with some styling, but most of the UI is in python. This made it very easy to create and use python models for our backend. For example, our efficiency score was calculated using deep learning with PyTorch to optimize the cost and time functions. Using streamlit made it very easy to use pandas as well to read and modify datasets.
pytorch, python, pandas, numpy, matplotlib, streamlit, sci-kit, figma 
## Challenges we ran into
###Streamlit
The rigidity of streamlit coupled with the difficulty of adding HTML and CSS elements to our code posed a great challenge for us. We were able to overcome this by coming up with creative solutions.
Understanding the problem
Understanding the problem, streamlit, 
## Accomplishments that we're proud of
streamlit, models, 

## What we learned
We already had an existing knowledge of certain _AI/ML algorithms_. Throughout this hackathon we learnt how to use html & css components streamlined with streamlit from scratch. Some of our team members learnt how to use the pandas package to structure the "labeled data" into flexible data structures. 

## What's next for 0ptiMine
Getting more data will improve the accuracy of our model and improve our suggestions. This will also allow us to factor more into our model making it more accurate.
