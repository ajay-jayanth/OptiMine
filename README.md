![Dark Blue with Space Photos Movie Ticket-2](https://user-images.githubusercontent.com/34663815/201524020-4903a89a-138f-4ab2-be2d-9c92f82a6d1a.jpg)

## Inspiration
EOG provided us with an extensive dataset with drill bit data from 20 extensive asteroid mining expeditions. We were inspired to construct a web app that used data visualization to chart and AI/ML (linear neural network) to analyze the best mining plan on future expeditions. Current engineers at EOG sought to tool to analyze and better visualize previous mining expedition data. We proposed this full stack application, which offers a variety of valuable data to the engineers at EOG. Such examples include delivering metrics to evaluate the performance of prior expeditions, suggesting better alternative bit drills to use at specific depths, and charting a full course optimized mining plan based on factors like affordability & time.

## What it does
The web app visualizes data from the EOG dataset and depending on user input gives the suggested plan and best drill bit to use at certain intervals. The user input consists of the allowed budget, time, and the length of an interval they want to look at. The user can either get data from each interval or get the overall data. If the user looks at the interval, they will see the best drill bit at that depth. They will also see the cost, time, and a calculated efficiency score of each drill bit at that depth. If the user looks at the overall statistics, they will see our suggested bit for each interval. This plan will also show a comparison to the given budget and time. There will be graphs plotting each past run in the dataset against our suggested plan based on cost per foot of bit depth, time per foot of bit depth, and our calculated score per foot of bit depth.
## How we built it
### UI/UX Design
We used Figma to layout and design our UI to have an idea of what we were coding. By using Figma we were able to structure and layout most of the components to see in hindsight how our final application would appear. For the frontend, we used Streamlit for the most part. Streamlit is a python package that enables interaction with data manipulation, visualization, and analysis tools in Python such as Pandas, Matplotlib, and Scikit-learn respectively. It also enables relatively easy coordination with scripting languages such as HTML and CSS, which we used for certain elements of our web app, giving users a wide variety of features they can add to their applications.

### Backend Development

#### Data Preprocessing
Using the Pandas framework, we identified and purged the missing data and outliers in the provided dataset. As a result, we were able to organize and build upon a robust dataset using cutting-edge data preprocessing such as extrapolation. Further, by utilizing a dynamic data-frame that we grouped into numerous configurations based on drill-bit combinations and depth intervals. This consequently provided variable depth intervals for scalable analysis and deployment.

#### Data Computation 
To calculate the time between each subsequent intervals in the dataset, the change in depth was calculated and divided by the rate of penetration by the bit in use.  The cost is calculated through a cost function which is computed by a given cost function provided by EOG-resources. In order to compute the most efficient possible drilling plan at specific depth intervals, we utilized an efficient score function which is computed by linear neural network model. Each specific score value for each drill type was ranked lexicographically and compared with the top model in that interval. 

#### Data Analysis and Visualization

For the user interface, we used Streamlit to keep our code mainly in python. We used elements of CSS and HTML to help with some styling, but most of the UI is in python. This made it very easy to create and use python models for our backend. For example, our efficiency score was calculated using deep learning with PyTorch to optimize the cost and time functions. Using streamlit made it very easy to use pandas as well to read and modify datasets.
pytorch, python, pandas, numpy, matplotlib, streamlit, sci-kit, figma 
## Challenges we ran into
### Streamlit
The rigidity of streamlit coupled with the difficulty of adding HTML and CSS elements to our code posed a great challenge for us. We were able to overcome this by coming up with creative solutions.
### Understanding the given information
Due to the complexity of the dataset, it took us some time to figure how we were going to use it effectively. We were able to remove junk values, such as, negative weight and NaN. After thorough understanding of what the problem was and how we could utilize the dataset effectively, we were able to overcome this challenge by creating our scoring calculator to rank the drill bits.

## What we learned
We already had an existing knowledge of certain AI/ML algorithms. Throughout this hackathon we learnt how to use html & css components streamlined with streamlit from scratch. Some of our team members learnt how to use the pandas package to structure the "labeled data" into flexible data structures. Furthermore, we used various python packages (pytorch, python, pandas, numpy, matplotlib, streamlit, sci-kit) and gained proficiency large multi-lined code into our full stack application.

## What's next for 0ptiMine - _Incorporate into testing Future EOG expeditions and Bit Drills_
On future expeditions funded by EOG-resources and its products (Drill Bits), EOG can utilize a more powerful version of this software to determine a specific plan to mine the asteroid based on specific depth intervals. This newly collected data could improve the model for future expeditions as well as create more cost effective and time efficient journeys. This data optimization tool could also be used to test the efficiency of newly developed EOG drill bits using the performance of prior drill bits models performed in prior expeditions.
