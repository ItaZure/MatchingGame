import streamlit as st
import pandas as pd

import sys
sys.path.append('..')
import rules
import mock


st.set_page_config(
    page_title="统计",
    page_icon="📊",
)

st.write(st.session_state['mock_players'])
