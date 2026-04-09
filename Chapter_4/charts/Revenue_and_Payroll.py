chart = alt.Chart(df).mark_bar().encode(
    x='Hotel ID',
    y='sum(Revenue)',
    color=alt.value('blue')
).properties(
    title='Total Annual Payroll by Hotel ID'
) + alt.Chart(df).mark_bar().encode(
    x='Hotel ID',
    y='sum(Annual payroll)',
    color=alt.value('red')
).properties(
)