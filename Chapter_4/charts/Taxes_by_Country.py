chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Country:N', title='Country'),
    y=alt.Y('sum(Taxes and license fees):Q', title='Total Taxes and License Fees')
).properties(
    title="Total Taxes and License Fees by Country",
    width=400,
    height=300
)
chart = chart.configure_mark(color='purple')
chart = chart.properties(title="Taxes by Country")