import pandas as pd
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Load dataset
file_path = "C:\\Users\\pc\\Documents\\jupyter_notebook\\Online_Retail.xlsx"
data = pd.read_excel(file_path, engine="openpyxl")

# Data Preprocessing
data.dropna(subset=['CustomerID'], inplace=True)
data['InvoiceDate'] = pd.to_datetime(data['InvoiceDate'])
data['TotalPrice'] = data['Quantity'] * data['UnitPrice']

# Initialize Dash app
app = dash.Dash(__name__)
server = app.server

# Layout
app.layout = html.Div([
    html.H1("Online Retail Dashboard", style={'textAlign': 'center'}),
    
    dcc.Graph(id='sales-trend'),
    dcc.Graph(id='top-customers'),
    dcc.Graph(id='top-products'),
    dcc.Graph(id='hourly-orders')
])

# Callbacks to update graphs
@app.callback(
    Output('sales-trend', 'figure'),
    Output('top-customers', 'figure'),
    Output('top-products', 'figure'),
    Output('hourly-orders', 'figure'),
    Input('sales-trend', 'id')
)
def update_graphs(_):
    # Sales Trend
    monthly_sales = data.resample('M', on='InvoiceDate')['TotalPrice'].sum()
    fig1 = px.line(monthly_sales, x=monthly_sales.index, y=monthly_sales.values, title='Monthly Revenue Trend')
    
    # Top Customers
    top_customers = data.groupby('CustomerID')['TotalPrice'].sum().nlargest(10)
    fig2 = px.bar(top_customers, x=top_customers.index, y=top_customers.values, title='Top Customers')
    
    # Top Products
    top_products = data.groupby('StockCode')['Quantity'].sum().nlargest(10)
    fig3 = px.bar(top_products, x=top_products.index, y=top_products.values, title='Best-Selling Products')
    
    # Hourly Orders
    data['Hour'] = data['InvoiceDate'].dt.hour
    hourly_orders = data.groupby('Hour')['InvoiceNo'].count()
    fig4 = px.bar(hourly_orders, x=hourly_orders.index, y=hourly_orders.values, title='Orders by Hour of Day')
    
    return fig1, fig2, fig3, fig4

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
