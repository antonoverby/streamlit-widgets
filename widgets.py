import streamlit as st
from st_pages import Page, Section, show_pages, add_page_title

st.set_page_config(layout="wide")

st.title("Widgets Preview")
st.write("Click on a widget link on the left to see that widget in action.")

# Structure of Pages on the left sidebar. Be careful b/c adjustments may take a server reset. Switching a Page to Section method seems to trigger this
show_pages(
    [
        Page("widgets.py", "Widgets Home"),
        Page("pages/progressbar.py", "Progress Bar")
    ]
    )


