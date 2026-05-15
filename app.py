import streamlit as st
import pandas as pd
import plotly.express as px

# Set page title
st.set_page_config(page_title="Valcon Step Challenge 2026", layout="wide")
st.title("🏃 Valcon Step Challenge 2026")

# 1. Load the data
df = pd.read_csv("data.csv", encoding="utf-8-sig")

# 2. Individual Steps Chart (Grouped by Team Color)
st.subheader("Stanje na dan 15.05.2026, 7:45 ujutro")
# 'color' ensures same team = same color
# 'hover_data' adds the date or other info to the tooltip
fig_ind = px.bar(
    df, 
    x="hodac", 
    y="skor", 
    color="tim", 
    title="Individualni rezultati",
    labels={"skor": "Ukupno koraka do sada", "hodac": "Hodac"}
)
fig_ind.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_ind, use_container_width=True)

# 3. Team Totals Chart
#st.subheader("Timovi")
# Aggregate the data for the second chart
team_df = df.groupby("tim")["skor"].sum().reset_index()

fig_team = px.bar(
    team_df, 
    x="tim", 
    y="skor", 
    color="tim",
    title="Ukupno koraka po timu",
    #text_auto='.2s' # Shows the number on top of the bar
)
fig_team.update_layout(xaxis_tickangle=-45)
st.plotly_chart(fig_team, use_container_width=True)

# 4. Raw Data View (Optional)
if st.checkbox("Prikaži golu istinu"):
    st.write(df)
