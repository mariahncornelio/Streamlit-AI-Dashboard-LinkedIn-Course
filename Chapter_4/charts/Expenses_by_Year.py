chart = alt.Chart(df).mark_area().encode(
    x=alt.X('Year:O', title='Year'),
    y=alt.Y('sum(Total):Q', stack='zero', title='Total'),
    color='Category:N'
).transform_calculate(
    Total='datum["Expensed Equipment"] + datum["Supplies"] + datum["Computer Services"] + datum["Equipment Maintenance"] + datum["Building Maintenance"] + datum["Utilities"]'
).properties(
    width=600,
    height=400
)