# Stock Portfolio Tracker

A beginner-friendly Python project for building and tracking a stock market portfolio with data visualization and analysis tools. This application allows you to manage your stock investments, track performance, and analyze your portfolio's gains and losses.

## Features

- Add and remove stocks from your portfolio
- Track purchase prices and current market values
- Calculate gains/losses and percentage returns
- Real-time stock price fetching using Yahoo Finance
- Clean tabular display of portfolio data
- Persistent data storage in JSON format
- Interactive command-line interface

## Setup

### Prerequisites

- Python 3.6 or higher
- Internet connection (for fetching stock prices)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/CODER7657/port_stock.git
   cd port_stock
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

```bash
python portfolio.py
```

### Menu Options

When you run the application, you'll see a menu with the following options:

1. **View Portfolio** - Display your current stock holdings with real-time prices
2. **Add Stock** - Add a new stock to your portfolio or increase shares of existing stock
3. **Remove Stock** - Remove stocks from your portfolio (partial or complete)
4. **Exit** - Save and exit the application

### Adding Stocks

To add a stock:
1. Select option 2 from the main menu
2. Enter the stock symbol (e.g., AAPL, GOOGL, TSLA)
3. Enter the number of shares
4. Enter the purchase price per share

### Viewing Portfolio

The portfolio view displays:
- Stock symbol
- Number of shares owned
- Average purchase price
- Current market price
- Total cost (what you paid)
- Current value (market value)
- Gain/Loss in dollars and percentage

### Example Output

```
=== STOCK PORTFOLIO ===
+--------+--------+-----------+---------------+------------+---------------+-----------+-----------+
| Symbol | Shares | Avg Price | Current Price | Total Cost | Current Value | Gain/Loss | Gain/Loss %|
+--------+--------+-----------+---------------+------------+---------------+-----------+-----------+
|  AAPL  |  10.00 |  $150.00  |    $175.50    |  $1500.00  |   $1755.00    |  $255.00  |   17.00%  |
|  GOOGL |   5.00 |  $120.00  |    $130.25    |   $600.00  |    $651.25    |   $51.25  |    8.54%  |
+--------+--------+-----------+---------------+------------+---------------+-----------+-----------+

Portfolio Summary:
Total Cost: $2100.00
Current Value: $2406.25
Total Gain/Loss: $306.25 (14.58%)
```

## Project Structure

```
port_stock/
├── portfolio.py          # Main application file
├── requirements.txt      # Python dependencies
├── README.md            # Project documentation
├── .gitignore          # Git ignore rules
└── portfolio.json      # Portfolio data (created automatically)
```

## Dependencies

- **yfinance**: For fetching real-time stock market data from Yahoo Finance
- **prettytable**: For displaying portfolio data in a formatted table

## Technical Details

### Data Storage

Portfolio data is stored locally in a JSON file (`portfolio.json`) with the following structure:

```json
{
  "AAPL": {
    "shares": 10.0,
    "avg_price": 150.0,
    "total_cost": 1500.0,
    "date_added": "2025-08-21"
  }
}
```

### Stock Price Fetching

The application uses the `yfinance` library to fetch real-time stock prices from Yahoo Finance. Stock symbols should follow Yahoo Finance conventions (e.g., AAPL for Apple Inc.).

## Contributing

This is a beginner-friendly project! Contributions are welcome. Some ideas for improvements:

- Add charts and visualizations
- Support for different currencies
- Portfolio performance over time
- Export to CSV/Excel
- Web interface using Flask/Django
- Support for dividends tracking

## License

This project is open source and available under the MIT License.

## Disclaimer

This tool is for educational and personal use only. Stock prices are fetched from Yahoo Finance and may have delays. This is not financial advice - always do your own research before making investment decisions.
