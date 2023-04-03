import streamlit as st
import sys
sys.path.append("..")
import rules
import mock


st.set_page_config(
    page_title="查询",
    page_icon="🔍",
)

if __name__ == "__main__":
    st.title('查询匹配分数')
    
    # use the mock data
    mock_answersheets = st.session_state['real_answersheets']

    # select 2 players and show the matching score
    sheet1 = st.selectbox('玩家1', mock_answersheets, format_func=lambda answersheet: answersheet.player.name)
    sheet2 = st.selectbox('玩家2', mock_answersheets, format_func=lambda answersheet: answersheet.player.name)

    # print(type(player1))

        


