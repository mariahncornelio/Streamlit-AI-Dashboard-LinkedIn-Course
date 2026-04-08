chart = alt.Chart(df).mark_line().encode(
    x='Year',
    y='sum(Profit):Q'
).properties(
    title='Total Profit by Year',
    width=600,
    height=400
)