# Online Retail Dashboard

## Overview
This dashboard is designed to analyze the Online Retail dataset, providing insights into sales trends, customer behavior, and product performance. The dashboard is built using Python with **Dash and Plotly**, offering interactive visualizations.

## Features

### 1. **Monthly Revenue Trend**
- Displays revenue trends over time.
- Helps identify peak sales periods and seasonal patterns.
- Data is resampled on a monthly basis.

### 2. **Top Customers**
- Highlights the highest-spending customers.
- Useful for customer segmentation and targeted marketing.
- Data is aggregated based on total spending per customer.

### 3. **Best-Selling Products**
- Shows the most popular products based on quantity sold.
- Helps businesses optimize stock levels.
- Data is grouped by product codes.

### 4. **Orders by Hour of the Day**
- Analyzes when customers place the most orders.
- Useful for optimizing marketing campaigns and customer engagement strategies.
- Data is grouped based on invoice timestamps.

## Installation & Usage

### **Requirements**
Ensure you have the following dependencies installed:
```bash
pip install dash plotly pandas openpyxl
```

### **Run the Dashboard**
1. Clone the repository:
   ```bash
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```bash
   cd online-retail-dashboard
   ```
3. Run the script:
   ```bash
   python online.py
   ```
4. Open your browser and go to `http://127.0.0.1:8050/`

## Future Improvements
- Add **date filters** for more dynamic analysis.
- Include **geographic visualizations** if location data is available.
- Implement **customer segmentation** using RFM analysis.

## Contributing
Feel free to submit pull requests for improvements or new features.



