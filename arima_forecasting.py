
    import numpy as np
    import pandas as pd
try:
    from statsmodels.tsa.arima.model     import ARIMA

def arima_forecasting(data):
    try:
        model = ARIMA(data, order=(5, 1, 0))
        model_fit = model.fit()
        forecast = model_fit.forecast(steps=10)
        print(f"ARIMA Forecast: {forecast}")
        return forecast
    except Exception as e:
        print(f"ARIMA Error: {e}")
        return None
