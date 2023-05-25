import streamlit as st
from st_pages import Page, Section, show_pages
from app.utils import page_layout

st.title("Welcome!")

 # Structure of Pages on the left sidebar. Be careful b/c adjustments may take a server reset. Switching a Page to Section method seems to trigger this
show_pages(
    [
        # Section("Home"),  
        Page("main.py", "Widgets Home"),
        # Section("Vizzes"),
        Page("pages/plotlyviz.py", "Plotly Vizzes"),
        # Section("Components"),
        Page("pages/progressbar.py", "Progress Bar")

    ]
    )


