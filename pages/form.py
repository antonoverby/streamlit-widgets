import streamlit as st
import sqlite3
from app.utils import page_layout, sqlite_writer

# PAGE LAYOUT / HEADER
page_layout()
st.header("Form Input Options")

# SESSION_STATE VIEWER
st.text("(Session_state dict shown here for educational purposes):")
st.session_state

# DATABASE VARIABLES
DATA_DIR = "./data"
DB_FILE = "forms.db"
TABLE = "form"
COLS = [k for k in st.session_state.keys()]
VALS = [tuple(v for v in st.session_state.values())]

if "form_data" not in st.session_state:
    st.session_state.form_data = {}

# FORM SECTION
with st.form(key="form", clear_on_submit=True):
    # DIFFERENT DATA INPUTS
    st.subheader("Text Input field:")
    name_input = st.text_input("Name", key="name")

    st.subheader("Selectbox with pre-filled choices:")
    names = ["John", "Paul", "George", "Ringo"]
    name_choice = st.selectbox("Who is your favorite Beatle?", names, key="fav_Beatle")

    st.subheader("Slider value:")
    slider_input = st.slider("How much do you like the White Album?", key="white_album_rating", min_value=1, max_value=100)

    st.subheader("Checkboxes:")
    checkbox_input = st.checkbox("Check this box if you've seen *Yellow Submarine*", key="seen_yllw_sub")
    
    submit_button = st.form_submit_button("Submit", on_click=sqlite_writer)
    

# NOTES SECTION
st.subheader("Notes:")
st.markdown("* **Validating data inputs** can be done either by checking field-by-field or by using logic connected to the state of the submit form button. Right now I'm using a series of if/elif/else statements to run warnings if an input field does not meet certain criteria. This checking logic is wrapped in a ```validate_data``` function which is the ```on_click``` argument for the submit button. The ```validate_data``` function also defines a separate session_state object ```submit_success``` which is turned ```True``` only when all of the validation criteria are met. I think this ```submit_success``` state key may be used later to make a future database addition out of form inputs.")
st.markdown("* Data validation warnings are appearing at the top of the page. Are they ok up there? I think I would prefer to have them appear near the submit button to make sure they're seen.")
st.markdown("* Having to click twice to change state when warnings are engaged...is it because of the ```validate_data``` function behavior?")
