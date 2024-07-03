import pandas as pd
import streamlit as st
import numpy as np
import datetime as dt
import matplotlib.pyplot as plt
import seaborn as sns

st.title("SF Trees")
st.write("This app analyse trees in Sasn Francisco")
df = pd.read_csv("trees.csv")
X = pd.DataFrame(df.groupby(["dbh"]).count()["tree_id"])
X.columns = ["tree_count"]
st.line_chart(X)
st.bar_chart(X)
st.area_chart(X)
Y = df.dropna(subset=["longitude", "latitude"])
Y = Y.sample(n=1000)
st.map(Y)

df["age"] = (pd.to_datetime("today") - pd.to_datetime(df["date"])).dt.days

st.subheader("Seaborn Chart")
fig_sb, ax_sb = plt.subplots()
ax_sb = sns.histplot(df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_sb)

st.subheader("Matploblib Chart")
fig_mpl, ax_mpl = plt.subplots()
ax_mpl = plt.hist(df["age"])
plt.xlabel("Age (Days)")
st.pyplot(fig_mpl)