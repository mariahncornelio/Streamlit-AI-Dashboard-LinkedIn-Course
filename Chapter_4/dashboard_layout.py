# Place charts in columns
col1, col2 = st.columns([2, 1])

# Display Profit_by_Year at the top
col1.altair_chart(Profit_by_Year)

# Place Revenue_and_Payroll and Taxes_by_Country next to each other
col1, col2 = st.columns(2)
col1.altair_chart(Revenue_and_Payroll)
col2.altair_chart(Taxes_by_Country)

# Display Expenses_by_Year below the two charts
st.altair_chart(Expenses_by_Year)