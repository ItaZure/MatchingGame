import streamlit as st
import pandas as pd
import mock
import excel_parser as ep

import time

st.set_page_config(
    page_title="首页",
    page_icon="🌏",
)

if 'mock_players' not in st.session_state:
        st.session_state['mock_players'] = mock.generate_players(20)

if 'mock_questionnaire' not in st.session_state:
    mock_questionnaire = mock.generate_questionnaire(10, 5)
    print(len(mock_questionnaire.questions))
    mock_questionnaire.scale_by_max(100)
    st.session_state['mock_questionnaire'] = mock_questionnaire

if 'mock_answersheets' not in st.session_state:
    st.session_state['mock_answersheets'] = [mock.generate_answer_sheet(player, st.session_state['mock_questionnaire']) for player in st.session_state['mock_players']]

if 'mock_pairs' not in st.session_state:
    st.session_state['mock_pairs'] = mock.algorithm.Pairs(st.session_state['mock_answersheets'])


st.session_state['real_answersheets'] = []

st.title("""暖场游戏""")

st.markdown("""
## 游戏规则
1. 扫描二维码，在规定时间内完成问卷填写。**请大胆选出内心的想法**。填写结果不会被公开。
""")

st.image("qrcode.png", width=200)

st.markdown("""
2. 根据提交的答卷，我们会为每个人匹配一个和自己灵魂契合的搭档。
3. 与你的搭档手拉手对视30秒，说出对对方的第一感受。
4. 小游戏:乱点鸳鸯
""")

uploaded_file = st.file_uploader("上传你的腾讯答卷", type="csv",label_visibility="hidden")
if uploaded_file is not None:
    csv_dataframe = pd.read_csv(uploaded_file)
    TXQuestionnaire = ep.TXQuestionnaire(csv_dataframe)
    st.session_state['real_answersheets'] = TXQuestionnaire.read_lines(csv_dataframe, st.session_state['mock_questionnaire'])





# with st.columns(3)[1]:
#     with st.empty():
#         seconds = 5 * 60
#         for i in range(seconds, 0, -1):
#             st.title("{:02d}:{:02d}".format(i // 60, i % 60))
#             time.sleep(1)







