import streamlit as st
import pandas as pd

import sys
sys.path.append('..')
import rules
import mock
import algorithm

st.set_page_config(
    page_title="排名",
    page_icon="🔍",
)

if __name__ == "__main__":
    st.title('排名')

    # rank of matching score of a specific player

    # mock
    # player = st.selectbox('玩家', st.session_state['mock_answersheets'], format_func=lambda answersheet: answersheet.player.name + "(" + str(answersheet.player.gender) + ")")

    # real
    player = st.selectbox('玩家', st.session_state['real_answersheets'], format_func=lambda answersheet: answersheet.player.name + "(" + str(answersheet.player.gender) + ")")

    only_hexo = st.checkbox('只看异性', value=True)

    # button
    if st.button('谁和TA最默契'):
        pair_for_one = algorithm.PairsForOne(st.session_state['real_answersheets'], player)
        pair_for_one.sort_by_score()
        if only_hexo:
            pair_for_one.only_hexo()
        st.table(pair_for_one.dataframe())

        # st.table(st.session_state['mock_pairs'].transform_to_df())


    st.header("总排行")
    all_pairs = algorithm.Pairs(st.session_state['real_answersheets'])
    all_pairs.sort_by_score()
    st.table(all_pairs.dataframe())
