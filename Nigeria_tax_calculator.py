# -*- coding: utf-8 -*-
"""
Created on Wed Jul 23 15:13:35 2025

@author: Fampride
"""

import streamlit as st

def calculate_tax(annual_income):
    """
    Calculate Nigerian personal income tax based on 2025 tax brackets (assuming similar to current)
    """
    tax = 0
    remaining_income = annual_income
    
    # Tax brackets (these should be updated with official 2025 rates when available)
    brackets = [
        (300000, 0.07),
        (300000, 0.11),
        (500000, 0.15),
        (500000, 0.19),
        (1600000, 0.21),
        (float('inf'), 0.24)
    ]
    
    for bracket, rate in brackets:
        if remaining_income <= 0:
            break
        taxable_amount = min(remaining_income, bracket)
        tax += taxable_amount * rate
        remaining_income -= bracket
    
    return tax

def main():
    st.title("🇳🇬 Nigeria Personal Income Tax Calculator (2025)")
    st.markdown("""
    This calculator estimates your personal income tax liability based on Nigeria's tax brackets.
    *Note: This uses current tax brackets as 2025 rates aren't published yet. Update when official rates are available.*
    """)
    
    # Input options
    with st.expander("💰 Income Details", expanded=True):
        income_type = st.radio("Income Frequency", 
                              ["Monthly", "Annual"], 
                              index=0,
                              help="Select whether you're entering monthly or annual income")
        
        if income_type == "Monthly":
            monthly_income = st.number_input("Monthly Income (₦)", 
                                           min_value=0.0, 
                                           value=500000.0, 
                                           step=10000.0)
            annual_income = monthly_income * 12
        else:
            annual_income = st.number_input("Annual Income (₦)", 
                                          min_value=0.0, 
                                          value=6000000.0, 
                                          step=100000.0)
    
    # Calculate tax
    tax = calculate_tax(annual_income)
    monthly_tax = tax / 12
    
    # Display results
    st.divider()
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Annual Income", f"₦{annual_income:,.2f}")
        st.metric("Annual Tax", f"₦{tax:,.2f}")
        
    with col2:
        st.metric("Monthly Income", f"₦{annual_income/12:,.2f}")
        st.metric("Monthly Tax", f"₦{monthly_tax:,.2f}")
    
    # Breakdown
    with st.expander("📊 Detailed Breakdown"):
        st.subheader("Tax Calculation Breakdown")
        st.write(f"**Annual Taxable Income:** ₦{annual_income:,.2f}")
        st.write(f"**Total Annual Tax:** ₦{tax:,.2f}")
        st.write(f"**Effective Tax Rate:** {tax/annual_income*100:.1f}%")
        st.write(f"**Monthly Take-home Pay:** ₦{(annual_income - tax)/12:,.2f}")
    
    # Disclaimer
    st.divider()
    st.caption("""
    **Disclaimer:** This calculator provides estimates only. Actual tax liability may vary based on specific circumstances, 
    deductions, allowances, and any changes to tax laws in 2025. Consult a tax professional for accurate assessment.
    """)

if __name__ == "__main__":
    main()
