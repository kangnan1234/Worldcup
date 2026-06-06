{\rtf1\ansi\ansicpg936\cocoartf2869
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 HelveticaNeue;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs32 \cf0 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import streamlit as st\
import pandas as pd\
import matplotlib.pyplot as plt\
\
# ---------------------- \uc0\u39029 \u38754 \u35774 \u32622  ----------------------\
st.set_page_config(page_title="\uc0\u19990 \u30028 \u26479 \u32479 \u35745 \u21161 \u25163 ", layout="wide")\
st.title("\uc0\u55356 \u57286  \u19990 \u30028 \u26479 \u25104 \u32489 \u32479 \u35745 \u27169 \u22411 \u65288 Skill \u29256 \u65289 ")\
st.subtitle("\uc0\u26497 \u36895 \u19978 \u32447  \'b7 \u21487 \u30452 \u25509 \u20351 \u29992 ")\
\
# ---------------------- \uc0\u21152 \u36733 \u25968 \u25454  ----------------------\
df = pd.read_csv("worldcup_data.csv")\
\
# ---------------------- \uc0\u21151 \u33021 1\u65306 \u21382 \u23626 \u20896 \u20891  ----------------------\
st.markdown("---")\
st.header("1. \uc0\u21382 \u23626 \u19990 \u30028 \u26479 \u20896 \u20891 ")\
st.dataframe(df, use_container_width=True)\
\
# \uc0\u20896 \u20891 \u32479 \u35745 \
winner_count = df["Winner"].value_counts()\
fig, ax = plt.subplots()\
winner_count.plot(kind="bar", ax=ax, color="#1f77b4")\
ax.set_title("\uc0\u21508 \u22269 \u22842 \u20896 \u27425 \u25968 ")\
ax.set_ylabel("\uc0\u27425 \u25968 ")\
st.pyplot(fig)\
\
# ---------------------- \uc0\u21151 \u33021 2\u65306 \u29699 \u38431 \u21382 \u21490  ----------------------\
st.markdown("---")\
st.header("2. \uc0\u26597 \u30475 \u29699 \u38431 \u21382 \u21490 \u25112 \u32489 ")\
team = st.selectbox("\uc0\u36873 \u25321 \u19968 \u25903 \u29699 \u38431 ", sorted(df["Winner"].unique()))\
t1 = df[df["Winner"] == team]\
t2 = df[df["Runner-Up"] == team]\
st.write(f"\uc0\u55358 \u56647  \{team\} \u22842 \u20896 \u24180 \u20221 \u65306 ", list(t1["Year"].values))\
st.write(f"\uc0\u55358 \u56648  \{team\} \u20122 \u20891 \u24180 \u20221 \u65306 ", list(t2["Year"].values))\
\
# ---------------------- \uc0\u21151 \u33021 3\u65306 \u20004 \u38431 \u23545 \u25112 \u39044 \u27979  ----------------------\
st.markdown("---")\
st.header("3. \uc0\u23545 \u25112 \u23454 \u21147 \u39044 \u27979 \u65288 Skill \u21151 \u33021 \u65289 ")\
col1, col2 = st.columns(2)\
with col1:\
    team1 = st.selectbox("\uc0\u29699 \u38431  A", sorted(df["Winner"].unique()), index=0)\
with col2:\
    team2 = st.selectbox("\uc0\u29699 \u38431  B", sorted(df["Winner"].unique()), index=1)\
\
# \uc0\u31616 \u21333 \u39044 \u27979 \u27169 \u22411 \u65288 \u22522 \u20110 \u22842 \u20896 \u27425 \u25968  + \u20915 \u36187 \u27425 \u25968 \u65289 \
def get_score(team):\
    w = len(df[df["Winner"] == team])\
    r = len(df[df["Runner-Up"] == team])\
    return w * 2 + r\
\
s1 = get_score(team1)\
s2 = get_score(team2)\
total = s1 + s2\
\
if total > 0:\
    rate1 = round(s1 / total * 100, 1)\
    rate2 = round(s2 / total * 100, 1)\
else:\
    rate1 = rate2 = 50\
\
st.success(f"\uc0\u12304 \u39044 \u27979 \u32467 \u26524 \u12305 \{team1\} \u32988 \u29575  \{rate1\}% | \{team2\} \u32988 \u29575  \{rate2\}%")\
\
st.markdown("---")\
st.caption("\uc0\u9989  \u26412 \u39033 \u30446 \u65306 \u19990 \u30028 \u26479 \u32479 \u35745 \u27169 \u22411  + \u32593 \u31449  + \u21487 \u35843 \u29992  Skill \u19977 \u21512 \u19968 \u26497 \u36895 \u29256 ")}