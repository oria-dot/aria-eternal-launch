
import numpy as np

def backtest_strategy(strategy, historical_data):
    profits = []
    for i in range(1, len(historical_data)):
        # Simulate the trade using the strategy
        decision = strategy(historical_data[i-1:i])  # Assume strategy returns 'buy' or 'sell'
        if decision == "buy":
            profit = historical_data[i] - historical_data[i-1]
        else:
            profit = historical_data[i-1] - historical_data[i]
        profits.append(profit)
    
    total_profit = np.sum(profits)
    return total_profit

# Example: Test a simple strategy using backtesting
def simple_strategy(data):
    return "buy" if data[-1] > data[0] else "sell"

historical_data = [100, 105, 102, 110, 108]
total_profit = backtest_strategy(simple_strategy, historical_data)
print(f"Total Profit: {total_profit}")
