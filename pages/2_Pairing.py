import streamlit as st
import pandas as pd

import sys
sys.path.append('..')
import rules
import mock
import algorithm

st.set_page_config(
    page_title="配对",
    page_icon="❤️",
)

if __name__ == "__main__":
    st.title('配对')

    # mock
    all_pairs = algorithm.Pairs(st.session_state['real_answersheets'])

    # real
    # all_pairs = algorithm.Pairs(st.session_state['real_answersheets'])
    if st.button('揭晓配对结果'):
        for pair in all_pairs.top_pairs():
            st.subheader(pair[0])

