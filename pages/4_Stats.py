import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import graphviz

import sys
sys.path.append('..')
import algorithm
import rules
import mock



st.set_page_config(
    page_title="统计",
    page_icon="📊",
)

if __name__ == "__main__":
    st.title('性别比例')
    all_pairs = algorithm.Pairs(st.session_state['answersheets'])
    gender_ratio = pd.DataFrame({
        "男":[all_pairs.male_num],
        "女":[all_pairs.female_num]
        }
        )
    # st.table(gender_ratio.transpose())
    st.bar_chart(gender_ratio.transpose(),width = 1)
    # plt.bar()
    
    # 生成一个饼状图，统计性别人数


    # st.title('各题统计')
    # st.table(st.session_state['raw_answersheets'])
    for i in range(10):
        df = st.session_state['raw_answersheets']
        column_name = df.columns.values[2+i]
        st.subheader("第" + str(i+1) + "题" + " " + column_name.lstrip("3.对于以下10个观点/偏好，你的态度是？:"))
        st.write("1分表示非常不认同，5分表示非常认同")
        # draw a bar chart for each question, count the number of each answer
        st.bar_chart(df[column_name].value_counts())

        # st.write("标准差:",df[column_name].std())

        # analysis by gender
        # df_male = df[df['2.性别'] == 1][column_name]
        # df_female = df[df['2.性别'] == 2][column_name]
        
        # st.write("男均值:",df_male.mean())
        # st.table(df_male)
        # st.write("女均值:",df_female.mean())
        # st.write("差值:",df_male.mean() - df_female.mean())



    st.title('默契拍档')
    st.write("说明：下图中，如果玩家A指向玩家B，表示玩家B在所有玩家中和A的问卷匹配度最高")
    graph = graphviz.Digraph()
    # if palyer A is matched with player B, then draw a edge from A to B
    for answersheet in st.session_state['answersheets']:
        pair_for_one = algorithm.PairsForOne(st.session_state['answersheets'], answersheet)
        for pair in pair_for_one.top_pairs():
            graph.edge(pair[0][0].name, pair[0][1].name)
        
    st.graphviz_chart(graph)

    st.title('一些小观察')
    st.markdown("""
    1. 所有问题中,分歧最大的问题是第8题「不以结婚为目的的谈恋爱都是耍流氓」
    2. 所有问题中,男女回答差异最大的问题第4题「中医远远落后于现代医学」，男性更偏向于认同而女性更偏向于不认同
    """
    )