from app.utils import page_layout 
import streamlit as st
import time
from stqdm import stqdm

page_layout()

# 0 to 100 progress bar
st.write("0 to 100 progress bar")
progress_text = "Operation in progress. Please wait."
my_bar = st.progress(0, text=progress_text)

for percent_complete in range(100):
    time.sleep(0.01)
    my_bar.progress(percent_complete + 1, text=progress_text)

st.divider()

# progress bar up to a certain point
st.write("Progress bar up to a certain point")
goal = 100
progress = 69
display_text = f"{progress}/{goal}"
prog_bar = st.progress(progress/goal, text=display_text)

for _ in range(progress):
    time.sleep(0.02)
    prog_bar.progress( _ +1, text=display_text)

st.divider()

# STqdm progress bar (goes away after it's run)
st.write("Tqdm-style progress bar")
for _ in stqdm(range(10)):
    for _ in stqdm(range(5)):
        time.sleep(0.1)

st.divider()
