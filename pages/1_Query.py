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
    player1 = st.selectbox('玩家1', mock_answersheets, format_func=lambda answersheet: answersheet.player.name)
    player2 = st.selectbox('玩家2', mock_answersheets, format_func=lambda answersheet: answersheet.player.name)

    # print(type(player1))

    # buttom
    if st.button('查看结果'):
        score = player1.matching_score(player2)
        # st.write(player1.answers)

        col1, col2, col3 = st.columns(3)
        col1.metric(label="分数", value=score)


