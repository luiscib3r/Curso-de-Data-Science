import streamlit as st
import pandas as pd


def load_data() -> pd.DataFrame:
    data = pd.read_excel('data/home_store.xlsx')
    data.drop(data.tail(1).index, inplace=True)
    data.drop(['date'], inplace=True, axis=1)
    return data


def income_statement(data: pd.DataFrame) -> pd.DataFrame:

    # Incomes
    sales_A = data['sales'].sum()
    sales_B = sales_A * 1.15
    cogs_A = data['cogs'].sum()
    cogs_B = cogs_A * 1.15
    gross_profit_A = sales_A - cogs_A
    gross_profit_B = sales_B - cogs_B

    # Operating Expenses
    advertising_A = 3000
    advertising_B = 3000
    salaries_A = 1500
    salaries_B = 1500
    rent_A = 6000
    rent_B = 8000
    total_operating_expenses_A = advertising_A + salaries_A + rent_A
    total_operating_expenses_B = advertising_B + salaries_B + rent_B
    operating_profit_A = gross_profit_A - total_operating_expenses_A
    operating_profit_B = gross_profit_B - total_operating_expenses_B

    # Other incomes
    investments_A = 2500
    investments_B = 2500

    # Other expenses
    lost_claim_A = 1000
    lost_claim_B = 1000

    # Profit before tax
    profit_before_tax_A = operating_profit_A + investments_A - lost_claim_A
    profit_before_tax_B = operating_profit_B + investments_B - lost_claim_B

    # Net Profit
    net_profit_A = profit_before_tax_A - (profit_before_tax_A * 0.30)
    net_profit_B = profit_before_tax_B - (profit_before_tax_B * 0.30)

    # Percentage of Net Profit
    net_profit_percentage_A = net_profit_A / sales_A * 100
    net_profit_percentage_B = net_profit_B / sales_B * 100

    income_statement = pd.DataFrame(
        {
            'A': [
                sales_A, cogs_A, gross_profit_A,
                advertising_A, salaries_A, rent_A, total_operating_expenses_A, operating_profit_A,
                investments_A, lost_claim_A, profit_before_tax_A, net_profit_A,
                net_profit_percentage_A,
            ],
            'B': [
                sales_B, cogs_B, gross_profit_B,
                advertising_B, salaries_B, rent_B, total_operating_expenses_B, operating_profit_B,
                investments_B, lost_claim_B, profit_before_tax_B, net_profit_B,
                net_profit_percentage_B,
            ]
        },
        index=[
            'sales', 'cogs', 'gross_profit',
            'advertising', 'salaries', 'rent', 'total_operating_expenses', 'operating_profit',
            'investments', 'lost_claim', 'profit_before_tax', 'net_profit', 'net_profit_percentage',
        ]
    )

    return income_statement


def main():
    st.write('# Home Store')

    data = load_data()

    
    sales = data['sales'].sum().round(2)
    cogs = data['cogs'].sum().round(2)
    gross_profit = (sales - cogs).round(2)

    col1, col2, col3 = st.columns(3)
    col1.metric(label="Sales", value=f"$ {sales}")
    col2.metric(label="COGS", value=f"$ {cogs}")
    col3.metric(label="Gross Profit", value=f"$ {gross_profit}")

    with st.expander('Data'):
        st.dataframe(data, height=500)

    st.write('### Income statement')
    st.table(income_statement(data))


if __name__ == '__main__':
    main()
