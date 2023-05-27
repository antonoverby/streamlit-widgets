import streamlit as st
from app.utils import page_layout

page_layout()

st.title("How Many Armadillos is That? An exercise in unit conversion")

"st.session_state object", st.session_state

def lbs_to_dillo():
    st.session_state.dillos = st.session_state.lbs/9

def dillo_to_lbs():
    st.session_state.lbs = st.session_state.dillos*9

col1, buff, col2 = st.columns([2,1,2])
with col1:
    armadillos = st.number_input("Armadillos", key="dillos", on_change= dillo_to_lbs)

with buff:
    _, mid, _ = st.columns(3)
    with mid:
        st.subheader("is")

with col2:
    pounds = st.number_input("Pounds", key="lbs", on_change= lbs_to_dillo)
   

st.subheader(f"{st.session_state.dillos} armadillos is {st.session_state.lbs} pounds")

