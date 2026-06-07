import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------- 页面设置 ----------------------
st.set_page_config(page_title="世界杯统计助手", layout="wide")
st.title("🏆 世界杯成绩统计模型（Skill 版）")
st.subheader("极速上线 · 可直接使用")

# ---------------------- 加载数据 ----------------------
df = pd.read_csv("worldcup_data.csv")

# ---------------------- 功能1：历届冠军 ----------------------
st.markdown("---")
st.header("1. 历届世界杯冠军")
st.dataframe(df, use_container_width=True)

# 冠军统计
winner_count = df["Winner"].value_counts()
fig, ax = plt.subplots()
winner_count.plot(kind="bar", ax=ax, color="#1f77b4")
ax.set_title("各国夺冠次数")
ax.set_ylabel("次数")
st.pyplot(fig)

# ---------------------- 功能2：球队历史 ----------------------
st.markdown("---")
st.header("2. 查看球队历史战绩")
team = st.selectbox("选择一支球队", sorted(df["Winner"].unique()))
t1 = df[df["Winner"] == team]
t2 = df[df["Runner-Up"] == team]
st.write(f"🥇 {team} 夺冠年份：", list(t1["Year"].values))
st.write(f"🥈 {team} 亚军年份：", list(t2["Year"].values))

# ---------------------- 功能3：两队对战预测 ----------------------
st.markdown("---")
st.header("3. 对战实力预测（Skill 功能）")
col1, col2 = st.columns(2)
with col1:
    team1 = st.selectbox("球队 A", sorted(df["Winner"].unique()), index=0)
with col2:
    team2 = st.selectbox("球队 B", sorted(df["Winner"].unique()), index=1)

# 简单预测模型（基于夺冠次数 + 决赛次数）
def get_score(team):
    w = len(df[df["Winner"] == team])
    r = len(df[df["Runner-Up"] == team])
    return w * 2 + r

s1 = get_score(team1)
s2 = get_score(team2)
total = s1 + s2

if total > 0:
    rate1 = round(s1 / total * 100, 1)
    rate2 = round(s2 / total * 100, 1)
else:
    rate1 = rate2 = 50

st.success(f"【预测结果】{team1} 胜率 {rate1}% | {team2} 胜率 {rate2}%")

st.markdown("---")
st.caption("✅ 本项目：世界杯统计模型 + 网站 + 可调用 Skill 三合一极速版")
