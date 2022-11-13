import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import os
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
import numpy as np
import pdb
import math
from collections import defaultdict


if (st.sidebar.button("Back to home")):
    os.remove("demofile2.txt")
    switch_page("Home")
    
title = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 30px;">FAQ</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)

#st.markdown("<h1 style='text-align: center; color: white;'>RESULTS</h1>", unsafe_allow_html=True)
original_title = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 50px;">Results</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("---")

f = open("demofile2.txt", "r")
line = f.readline()

lowerBound = int(line[0:line.index(",")])
line = line[line.index(",")+1:]
upperBound = int(line[0:line.index(",")])
line = line[line.index(",")+1:]
totCost = int(line[0:line.index(",")])
line = line[line.index(",")+1:]
totTime = int(line[0:line.index(",")])
line = line[line.index(",")+1:]
nums = int(line[0:line.index(",")])
line = line[line.index(",")+1:]
numIntervals = int(line)

totCost = int(int(totCost)/numIntervals)
totTime = int(int(totTime)/numIntervals)


with st.sidebar.expander("Info about the chart", expanded = True):
    st.write("Full analysis for this interval given")
    st.write("`Budget` = " + "$" + str(totCost))
    st.write("`Max time` = " + str(int(totTime)) + " hours")
    st.write("`Interval` = " + str(lowerBound) + " to " + str(upperBound) + " feet")
    st.write("")
    st.write("Note: the `budget` and `max time` differ from the values you inputted in the homepage because these values correspond to the budget and max time PER INTERVAL, not the total budget and max value.")
with st.sidebar.expander("Why do I keep getting a ValueError?"):
    st.write("This is because you left the results page WITHOUT clicking 'back to home'. ")

INTERVAL_LEN = nums

files = [f'Asteroids/Asteroid {i}.csv' for i in range(1, 21)]
dfs = [pd.read_csv(file) for file in files]
for i, _ in enumerate(dfs):
    dfs[i]['Asteroid'] = i + 1
    dfs[i].dropna(inplace=True)
    dfs[i].drop(dfs[i][dfs[i]['BIT_DEPTH'] < 0].index, inplace=True)
    dfs[i].drop(dfs[i][dfs[i]['RATE_OF_PENETRATION'] < 0].index, inplace=True)
def sort_key(e):
    return e[1]
ranges = [[i, df['BIT_DEPTH'].iloc[0], df['BIT_DEPTH'].iloc[-1]] for i, df in zip(range(20), dfs)]
ranges = sorted(ranges, key=sort_key)
cost_df = pd.DataFrame({'DRILL_BIT_NAME': ['Buzz Drilldrin', 'AstroBit', 'Apollo', 'ChallengDriller'],
                        'Cost Per Run':    [5000, 3000, 1000, 10000],
                        'Cost Per Foot': [1.5, 1, 4, 0],
                        'Cost Per Hour': [0, 1500, 2500, 0]
                       })
cost_df = cost_df.set_index('DRILL_BIT_NAME')
def ran_to_str(range):
    return str(range[0]) + '-' + str(range[1])
def calc_time(examine):
    time = 0
    examine.reset_index(drop=True, inplace=True)
    redo = 1
    for i, row in examine.iterrows():
        if i == 0: continue
        delta_depth = row['BIT_DEPTH'] - examine.at[i-1, 'BIT_DEPTH']
        time += (delta_depth / row['RATE_OF_PENETRATION']) if row['RATE_OF_PENETRATION'] > 0 else 0
        if examine.at[i, 'DRILL_BIT_ID'] > examine.at[i-1, 'DRILL_BIT_ID']:
            time += examine.at[i, 'BIT_DEPTH'] / 100 * 30 / 3600 * 2
            redo+=1
    time *= (2000/len(examine.index))
    return time, redo
calc_ranges = [[INTERVAL_LEN*i, INTERVAL_LEN*(i+1)] for i in range(int(20000 / INTERVAL_LEN))]
bits = ['Apollo', 'AstroBit', 'Buzz Drilldrin', 'ChallengDriller']

keys = [ran_to_str(calc_range) for calc_range in calc_ranges]
bits_times = dict(zip(keys, [defaultdict(list) for i in range(len(keys))]))
bits_costs = dict(zip(keys, [defaultdict(list) for i in range(len(keys))]))
i=0
for calc_range in calc_ranges:
    for trial in dfs:
        examine = trial[trial['BIT_DEPTH'] > calc_range[0]]
        examine = examine[examine['BIT_DEPTH'] < calc_range[1]]
        if len(examine) == 0:
            continue
        bit = examine['DRILL_BIT_NAME'].value_counts().idxmax()
        examine = examine[examine['DRILL_BIT_NAME'] == bit]
        
        time, redo = calc_time(examine)
        depth = examine['BIT_DEPTH'].max() - examine['BIT_DEPTH'].min()
        cost = redo * cost_df.at[bit, 'Cost Per Run'] + (depth * cost_df.at[bit, 'Cost Per Foot']) + (time * cost_df.at[bit, 'Cost Per Hour'])
        
        bits_times[ran_to_str(calc_range)][bit].append(time)
        bits_costs[ran_to_str(calc_range)][bit].append(cost)
tc = []
time_cost = dict(zip(keys, [{} for i in range(len(keys))]))
i=0
for calc_range in calc_ranges:
    for bit in bits_times[ran_to_str(calc_range)]:
        time_cost[ran_to_str(calc_range)][bit] = {}
        time_cost[ran_to_str(calc_range)][bit]['time'] = np.mean(bits_times[ran_to_str(calc_range)][bit])
        time_cost[ran_to_str(calc_range)][bit]['cost'] = np.mean(bits_costs[ran_to_str(calc_range)][bit])
        tc.append([time_cost[ran_to_str(calc_range)][bit]['time'], time_cost[ran_to_str(calc_range)][bit]['cost']])
        
tca = np.array(tc).T
tca = np.mean(tca, axis=1)
def score(time, cost):
    ret = 10 - cost / tca[1] * 2.5 - time / tca[0] * 2.5
    if ret > 9.5:
        return 9.5
    elif ret < 0.5:
        return 0.5
    else:
        return ret
scores = []
for calc_range in time_cost:
    for bit in time_cost[calc_range]:
        score_ = score(time_cost[calc_range][bit]['time'], time_cost[calc_range][bit]['cost'])
        time_cost[calc_range][bit]['score'] = score_
        scores.append(score_)
    
def sort_sug(bit):
    return bit[3]

def ret_sorted(vals):
    # pdb.set_trace()
    names = vals.keys()
    times = [vals[bit]['time'] for bit in vals]
    costs = [vals[bit]['cost'] for bit in vals]
    scores = [vals[bit]['score'] for bit in vals]
    vals = [[name, time, cost, score] for name, time, cost, score in zip(names, times, costs, scores)]
    vals = sorted(vals, key=sort_sug, reverse=True)
    ret = {}
    for i, val in enumerate(vals):
        ret[i + 1] = {'name': val[0],
                      'time': val[1],
                      'cost': val[2],
                      'score': val[3]
                     }
    return ret
suggestions = dict(zip(keys, [{} for i in range(len(keys))]))
for calc_range in time_cost:
    new_dict = ret_sorted(time_cost[calc_range])
    suggestions[calc_range] = new_dict
time_cost = suggestions

stringRange = str(lowerBound-1) + "-" + str(upperBound)

st.subheader("Most efficient drill to use in this scenario: " + str(time_cost[stringRange][1]["name"]))

st.markdown("---")

col1, col2, col3, col4 = st.columns(4)

names = {
    "ChallengDriller" : "Challeng",
    "Buzz Drilldrin" : "Buzz",
    "AstroBit" : "AstroBit",
    "Apollo": "Apollo"
}

col1.metric("Name", names[time_cost[stringRange][1]["name"]], "1", delta_color = "off")
col1.metric("Name", names[time_cost[stringRange][2]["name"]], "2", delta_color = "off")
col1.metric("Name", names[time_cost[stringRange][3]["name"]], "3", delta_color = "off")
col1.metric("Name", names[time_cost[stringRange][4]["name"]], "4", delta_color = "off")

col2.metric("Time", str(int(time_cost[stringRange][1]["time"])) + " hours", str(int(time_cost[stringRange][1]["time"]) - int(totTime)) + " hours", delta_color = "inverse")
col2.metric("Time", str(int(time_cost[stringRange][2]["time"])) + " hours", str(int(time_cost[stringRange][2]["time"]) - int(totTime)) + " hours", delta_color = "inverse")
col2.metric("Time", str(int(time_cost[stringRange][3]["time"]))+ " hours", str(int(time_cost[stringRange][3]["time"]) - int(totTime)) + " hours", delta_color = "inverse")
col2.metric("Time", str(int(time_cost[stringRange][4]["time"])) + " hours", str(int(time_cost[stringRange][4]["time"]) - int(totTime)) + " hours", delta_color = "inverse")

col3.metric("Cost", "$" + str(int(time_cost[stringRange][1]["cost"])),  str(int(time_cost[stringRange][1]["cost"]) - int(totCost)) + " USD", delta_color = "inverse")
col3.metric("Cost", "$" + str(int(time_cost[stringRange][2]["cost"])), str(int(time_cost[stringRange][2]["cost"]) - int(totCost)) + " USD", delta_color = "inverse")
col3.metric("Cost", "$" + str(int(time_cost[stringRange][3]["cost"])), str(int(time_cost[stringRange][3]["cost"]) - int(totCost)) + " USD", delta_color = "inverse")
col3.metric("Cost", "$" + str(int(time_cost[stringRange][4]["cost"])), str(int(time_cost[stringRange][4]["cost"]) - int(totCost)) + " USD", delta_color = "inverse")

highestScore = round((time_cost[stringRange][1]["score"]), 1)
col4.metric("Score", str(highestScore), "0");

temp2 = round((time_cost[stringRange][2]["score"]), 1)
diff2 = round((temp2 - highestScore), 1)
col4.metric("Score", str(temp2), str(diff2))

temp3 = round((time_cost[stringRange][3]["score"]), 1)
diff3 = round((temp3 - highestScore), 1)
col4.metric("Score", str(temp3), str(diff3))

temp4 = round((time_cost[stringRange][4]["score"]), 1)
diff4 = round((temp4 - highestScore), 1)
col4.metric("Score", str(temp4), str(diff4))
