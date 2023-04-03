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

    # real
    all_pairs = algorithm.Pairs(st.session_state['answersheets'])
    if st.button('揭晓配对结果'):
        for pair in all_pairs.top_pairs():
            st.subheader(pair[0])


    # single
    for answersheet in st.session_state['answersheets']:
        pair_for_one = algorithm.PairsForOne(st.session_state['answersheets'], answersheet)
        for pair in pair_for_one.top_pairs():
            st.subheader(pair[0])
            st.subheader(pair[1])