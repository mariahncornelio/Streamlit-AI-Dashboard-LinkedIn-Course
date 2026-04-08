chart = alt.Chart(df).mark_bar().encode(
    x=alt.X('Country:N', title='Country'),
    y=alt.Y('sum(Taxes and license fees):Q', title='Total Taxes and License Fees')
).properties(
    width=400,
    height=300
)