import pandas as pd
import streamlit as st
import os
from streamlit_extras.switch_page_button import switch_page

st.markdown("""
    <style>
        img {
            position: fixed;
            width: 130px;
            height: 130px;
            top: -20px;
            left: 100px;
        }
    </style>
    """,unsafe_allow_html=True)


st.sidebar.image('optimine.png')


title = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 30px;">FAQ</p>'
st.sidebar.markdown(title, unsafe_allow_html=True)

with st.sidebar.expander("What is OptiMine?", expanded = False):
    st.write("*OptiMine* is a web app that helps users visualize asteroid mining data and uses AI/ML and advanced data analysis to provide the best drill bit to use at certain stages of the asteroid mining process.")
    
with st.sidebar.expander("How do I use this program?", expanded = False):
    st.write("1. Enter your desired total budget and maximum drilling time")
    st.write("2. If interval depth is **unknown**, then select value for number of intervals and interval depth will autofill. If interval depth is **known**, then simply slide the interval depth slider. *Please note: the number interval slider will NOT change when the interval depth slider is changed. Thank you.*")
    st.write("3. Select your desired drilling range")
    st.write("4. Get your results!")
    st.write("")
    st.write("You'll be done in a bit!")

with st.sidebar.expander("What are the meanings of the inputs?", expanded = False):
    st.write("`Budget`: Enter your budget for this run (in US Dollars)")
    st.write("`Max Time`: Enter the maximum amount of time you would like to take for this run (in hours)")
    st.write("`Number of Intervals`: Due to a max depth of 20,000 feet, enter the amount of drilling intervals you would like to check for this run")
    st.write("`Interval Depth`: Enter the depth of each drilling interval (in feet)")

with st.sidebar.expander("Why does the results page give me an error?", expanded = False):
    st.write("This is because you have tried to seek results without selecting a range. Please enter ALL information (budget, time, and interval) and select a range. Once you select a range, you will be directed to the results page. Thank you for your patience!")

st.markdown("""

<style>


 .css-1iyw2u1 {
        display: none;
    }

</style>

""", unsafe_allow_html=True)

original_title = '<p style="font-family: Courier New; color:white; text-align: center; font-size: 100px;">OptiMine</p>'
st.markdown(original_title, unsafe_allow_html=True)

st.markdown("---")

colX, colY = st.columns(2)
with colX:
    cost = st.number_input("Enter your budget (in US $): ", 100000, 1500000, step = 100000)
    
with colY:
    time = st.number_input("Enter max time (in hours): ", 100, 500, step = 50)

nums = st.select_slider("Select number of intervals", [2, 4, 5, 8, 10, 20], value = 5)

increment = st.select_slider("Select interval depth (in feet)", [1000, 2000, 2500, 4000, 5000, 10000], value = 20000/nums)

nums = int(20000/increment)

numBoxes = int(20000/int(increment))


m = st.markdown("""
<style>
:root {
    --j--: calc(500px/numBoxes);
}
div.stButton > button:first-child {
    background-color: transparent;
    color: #ffffff;
    height: 80px;
    width: 200%;

}
</style
""", unsafe_allow_html=True)


array = []
array = [0 for i in range(numBoxes)]

col1, col2 = st.columns(2)


st.markdown("""
    <style>
    [data-testid=column]:nth-of-type(1) [data-testid=stVerticalBlock]{
        gap: 0rem;
    }
    </style>
    """,unsafe_allow_html=True)

st.markdown("""
  <style>
    .css-o18uir.e16nr0p33 {
      margin-top: -10px;
    }
  </style>
""", unsafe_allow_html=True)

with col1:
    for i in range(1, numBoxes+1):
        if(st.button(str((i-1)*increment + 1) + " ft to " + str((i)*increment) + " ft")):
            f = open("demofile2.txt", "a")
            f.write(str((i-1)*increment + 1))
            f.write(",")
            f.write(str((i)*increment))
            f.write(",")
            f.write(str(cost))
            f.write(",")
            f.write(str(time))
            f.write(",")
            f.write(str(increment))
            f.write(",")
            f.write(str(nums))
            f.close()
            switch_page("Results")

st.markdown("---")

col3, col4 = st.columns(2)
with col3:
    if (st.button("Overall")):
        switch_page("Overall")

st.markdown("---")



    
