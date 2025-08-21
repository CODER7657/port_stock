#!/usr/bin/env python3
"""
Stock Portfolio Management System
A beginner-friendly Python project for building and tracking a stock market portfolio
with data visualization and analysis tools.
"""

import yfinance as yf
from prettytable import PrettyTable
import json
import os
from datetime import datetime

class StockPortfolio:
    def __init__(self, portfolio_file='portfolio.json'):
        self.portfolio_file = portfolio_file
        self.portfolio = self.load_portfolio()
    
    def load_portfolio(self):
        """Load portfolio from JSON file"""
        if os.path.exists(self.portfolio_file):
            with open(self.portfolio_file, 'r') as f:
                return json.load(f)
        return {}
    
    def save_portfolio(self):
        """Save portfolio to JSON file"""
        with open(self.portfolio_file, 'w') as f:
            json.dump(self.portfolio, f, indent=2)
    
    def add_stock(self, symbol, shares, purchase_price):
        """Add a stock to the portfolio"""
        symbol = symbol.upper()
        if symbol in self.portfolio:
            # Update existing holding
            current_shares = self.portfolio[symbol]['shares']
            current_value = self.portfolio[symbol]['total_cost']
            new_total_shares = current_shares + shares
            new_total_cost = current_value + (shares * purchase_price)
            self.portfolio[symbol] = {
                'shares': new_total_shares,
                'avg_price': new_total_cost / new_total_shares,
                'total_cost': new_total_cost,
                'date_added': self.portfolio[symbol]['date_added']
            }
        else:
            # Add new stock
            self.portfolio[symbol] = {
                'shares': shares,
                'avg_price': purchase_price,
                'total_cost': shares * purchase_price,
                'date_added': datetime.now().strftime('%Y-%m-%d')
            }
        self.save_portfolio()
        print(f"Added {shares} shares of {symbol} at ${purchase_price:.2f} per share")
    
    def remove_stock(self, symbol, shares=None):
        """Remove a stock from the portfolio"""
        symbol = symbol.upper()
        if symbol not in self.portfolio:
            print(f"Stock {symbol} not found in portfolio")
            return
        
        if shares is None:
            # Remove all shares
            del self.portfolio[symbol]
            print(f"Removed all shares of {symbol} from portfolio")
        else:
            # Remove partial shares
            current_shares = self.portfolio[symbol]['shares']
            if shares >= current_shares:
                del self.portfolio[symbol]
                print(f"Removed all {current_shares} shares of {symbol} from portfolio")
            else:
                self.portfolio[symbol]['shares'] -= shares
                self.portfolio[symbol]['total_cost'] -= shares * self.portfolio[symbol]['avg_price']
                print(f"Removed {shares} shares of {symbol} from portfolio")
        
        self.save_portfolio()
    
    def get_current_price(self, symbol):
        """Get current stock price using yfinance"""
        try:
            stock = yf.Ticker(symbol)
            data = stock.history(period='1d')
            if not data.empty:
                return data['Close'].iloc[-1]
            else:
                return None
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None
    
    def display_portfolio(self):
        """Display the current portfolio in a formatted table"""
        if not self.portfolio:
            print("Portfolio is empty")
            return
        
        table = PrettyTable()
        table.field_names = ['Symbol', 'Shares', 'Avg Price', 'Current Price', 'Total Cost', 'Current Value', 'Gain/Loss', 'Gain/Loss %']
        
        total_cost = 0
        total_value = 0
        
        for symbol, data in self.portfolio.items():
            shares = data['shares']
            avg_price = data['avg_price']
            cost = data['total_cost']
            
            current_price = self.get_current_price(symbol)
            if current_price is None:
                current_price = 0
                current_value = 0
                gain_loss = 0
                gain_loss_pct = 0
            else:
                current_value = shares * current_price
                gain_loss = current_value - cost
                gain_loss_pct = (gain_loss / cost) * 100 if cost > 0 else 0
            
            total_cost += cost
            total_value += current_value
            
            table.add_row([
                symbol,
                f"{shares:.2f}",
                f"${avg_price:.2f}",
                f"${current_price:.2f}" if current_price > 0 else "N/A",
                f"${cost:.2f}",
                f"${current_value:.2f}",
                f"${gain_loss:.2f}",
                f"{gain_loss_pct:.2f}%"
            ])
        
        print("\n=== STOCK PORTFOLIO ===")
        print(table)
        
        total_gain_loss = total_value - total_cost
        total_gain_loss_pct = (total_gain_loss / total_cost) * 100 if total_cost > 0 else 0
        
        print(f"\nPortfolio Summary:")
        print(f"Total Cost: ${total_cost:.2f}")
        print(f"Current Value: ${total_value:.2f}")
        print(f"Total Gain/Loss: ${total_gain_loss:.2f} ({total_gain_loss_pct:.2f}%)")

def main():
    """Main function to run the portfolio manager"""
    portfolio = StockPortfolio()
    
    while True:
        print("\n=== STOCK PORTFOLIO MANAGER ===")
        print("1. View Portfolio")
        print("2. Add Stock")
        print("3. Remove Stock")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == '1':
            portfolio.display_portfolio()
        
        elif choice == '2':
            symbol = input("Enter stock symbol: ").strip().upper()
            try:
                shares = float(input("Enter number of shares: "))
                price = float(input("Enter purchase price per share: $"))
                portfolio.add_stock(symbol, shares, price)
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
        
        elif choice == '3':
            symbol = input("Enter stock symbol to remove: ").strip().upper()
            remove_all = input("Remove all shares? (y/n): ").strip().lower()
            if remove_all == 'y':
                portfolio.remove_stock(symbol)
            else:
                try:
                    shares = float(input("Enter number of shares to remove: "))
                    portfolio.remove_stock(symbol, shares)
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == '4':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
