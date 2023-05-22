import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title
from streamlit_extras.app_logo import add_logo

st.set_page_config(layout="wide")

# Add a logo
add_logo("assets/aclogotransparent.png", 10)

show_pages(
    [
        Page("widgets.py", "Widgets Home"),
        Page("pages/progressbar.py", "Progress Bar")
    ])

st.title("Widgets Preview")
st.write("Click on a widget link on the left to see that widget in action.")