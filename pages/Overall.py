import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import pandas as pd
from IPython.display import display
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pdb



if (st.sidebar.button("Back to home")):
    switch_page("Home")

original_title = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 50px;">Overall Analysis</p>'
st.markdown(original_title, unsafe_allow_html=True)

our_df = pd.read_csv('neil_df.csv')
df4 = pd.DataFrame({'Interval':our_df["interval"],'Name': our_df["name"]})
st.markdown("----")

with st.sidebar.expander("Info about 'Overall Suggestion Table", expanded = False):
    st.write("The `overall drill bit suggestion` table portrays the best drill bit to use while drilling in a certain interval depth range. This value is derived from the best average score across all drill bits used on all asteroids in that certain depth range.")
with st.sidebar.expander("Info about 'Cost vs Depth' graph", expanded = False):
    st.write("Based off the asteroid selected, the `cost vs depth` graph displays the drilling cost as the drilling depth increases.")
with st.sidebar.expander("Info about 'Time vs Depth' graph", expanded = False):
    st.write("Based off the asteroid selected, the `time vs depth` graph displays the drilling time as the drilling depth increases.")

#st.subheader("Our Drill Bit Suggestions per Interval")
header1 = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 20px;">Overall drill bit suggestion for every 2000 feet drilled</p>'
st.markdown(header1, unsafe_allow_html=True)
st.table(df4)
st.markdown("----")
#Variables that will be given
header1 = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 22px;">Graphs for each individual asteroid</p>'
st.markdown(header1, unsafe_allow_html=True)
meteor = st.slider("Select an Asteroid", 1, 20) - 1
total_height = 20000

height_interval = 2000

df = pd.read_csv('data/Asteroid_' + str(meteor) + '_for_saroo.csv')
df.head()

cost_df = pd.DataFrame({'DRILL_BIT_NAME': ['Buzz Drilldrin', 'AstroBit', 'Apollo', 'ChallengDriller'],
                        'Cost Per Run':    [5000, 3000, 1000, 10000],
                        'Cost Per Foot': [1.5, 1, 4, 0],
                        'Cost Per Hour': [0, 1500, 2500, 0]
                       })
cost_df = cost_df.set_index('DRILL_BIT_NAME')
# cost_df

delta_depth = []
time = []
cost = []
new_depth = []
our_cost = []

#Cost Lists
total_cost = []

for i in range(1, len(df.index)):
  delta_depth.append(df.iat[i,1] - df.iat[i - 1,1])

  if df.at[i,'RATE_OF_PENETRATION'] > 0:
    # if i == 4008: pdb.set_trace()
    time_curr = delta_depth[i-1] / df.at[i,'RATE_OF_PENETRATION']
  else:
    time_curr = 0

  if(df.at[i,'DRILL_BIT_ID'] != df.at[i-1,'DRILL_BIT_ID']):
    time_curr += 2 * ((df.at[i,'BIT_DEPTH'] / 100) * 30) / 3600
  
  if i > 1:
    time_curr += time[i-2]
  # print(i)
  time.append(time_curr)
  new_depth.append(df.at[i, 'BIT_DEPTH'])
  
  #Cost Calc
  curr_cost = 0

  curr_bit_name = df.at[i, 'DRILL_BIT_NAME']
  if(curr_bit_name == df.at[i-1, 'DRILL_BIT_NAME'] and df.at[i, 'DRILL_BIT_ID'] == df.at[i-1, 'DRILL_BIT_ID']):
    curr_cost += ((delta_depth[i-1] * cost_df.at[curr_bit_name, 'Cost Per Foot']) + ((time[i-1] - time[i-2]) * cost_df.at[curr_bit_name, 'Cost Per Hour']))
  else:
    curr_cost += cost_df.at[curr_bit_name, 'Cost Per Run']
    print(curr_bit_name)
  
  if i > 1:
    curr_cost += total_cost[i-2]
  total_cost.append(curr_cost)



#plt.plot(time, total_cost)
#plt.show()
#
#plt.plot(new_depth, total_cost)
#plt.show()
#our_cost.append(our_df.at[i, 'cost'])


#st.markdown("----")

#df5 = pd.DataFrame({'Interval': our_df["interval"], 'Cost': our_df["cost"] })
#st.line_chart(df5,x='Interval', y = 'Cost')



header2 = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 22px;">Cost vs Depth</p>'
st.markdown(header2, unsafe_allow_html=True)

df2 = pd.DataFrame({'Depth': new_depth, 'Cost': total_cost, })
st.line_chart(df2,x='Depth', y = 'Cost')

header3 = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 22px;">Time vs Depth</p>'
st.markdown(header3, unsafe_allow_html=True)

df3 = pd.DataFrame({'Depth': new_depth, 'Time': time})
st.line_chart(df3,x='Depth', y = 'Time')
