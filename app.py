import streamlit as st
from PIL import Image
# from model_load import load_model_LC
import time

@st.cache_resource(show_spinner='Model Was Loading')
def load_m():
    print('Model was loaded..')
    time.sleep(15)
    return 0

def load_page_model(in_st):

    # Read the logo png
    icon_img = Image.open('png_data\icon.png')
    # set the page config
    in_st.set_page_config(page_title = 'AI Bot Interviewer', # page title
                    page_icon = icon_img, # logo image
                    layout = 'centered', # layout is centered
                    initial_sidebar_state = 'auto' # removing the sidebar {By default it will come}
                    )
    # Set the page Header
    in_st.title('DS Interview By Llama-2 ')
    
    # adding optional topics for the user
    topic = st.sidebar.radio(
            "Choose Prefered Topic ",
            key="topic",
            index= 0,
            # on_change = Create_LLM_chain(model_obj=model),
            horizontal = False,
            options=["All",
                    "Statistics",
                    "Data Cleaning",
                    "Data Preprocessing",
                    "Machine Learning",
                    "Deep Learning",
                    "Large Language Models",
                    "Natural Language Models",
                    "Computer Vision",
                    ],
        )
    
    print('By default topic selected ...',topic)
    load_m()
    return 0

if __name__=="__main__":

    load_page_model(st)
    # model = load_model_LC()
    print('New Prompt was generated..',st.session_state.topic)
