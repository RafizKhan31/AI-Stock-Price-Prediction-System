import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)


FEATURES = [
    "Open",
    "High",
    "Low",
    "Close",
    "Volume",

    "SMA_10",
    "SMA_20",
    "SMA_50",

    "EMA_10",
    "EMA_20",

    "Daily_Return",
    "Volatility_10",

    "Momentum_5",
    "Momentum_10",

    "RSI",
    "MACD",
    "ATR",

    "Close_Lag_1",
    "Close_Lag_2",
    "Close_Lag_3",
    "Close_Lag_5",
    "Close_Lag_10"
]


def split_data(data, train_ratio=0.80):
    """
    Split time-series data chronologically.

    Do NOT randomly shuffle stock market data.
    """

    split_index = int(
        len(data) * train_ratio
    )

    train_data = data.iloc[:split_index]
    test_data = data.iloc[split_index:]

    X_train = train_data[FEATURES]
    y_train = train_data["Target"]

    X_test = test_data[FEATURES]
    y_test = test_data["Target"]

    return (
        X_train,
        X_test,
        y_train,
        y_test,
        test_data
    )


def train_model(X_train, y_train):
    """
    Train Random Forest regression model.
    """

    model = RandomForestRegressor(
        n_estimators=300,
        max_depth=15,
        min_samples_split=5,
        min_samples_leaf=2,
        random_state=42,
        n_jobs=-1
    )

    model.fit(
        X_train,
        y_train
    )

    return model


def evaluate_model(model, X_test, y_test):
    """
    Evaluate model performance.
    """

    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions
    )

    rmse = np.sqrt(
        mean_squared_error(
            y_test,
            predictions
        )
    )

    r2 = r2_score(
        y_test,
        predictions
    )

    return {
        "MAE": mae,
        "RMSE": rmse,
        "R2": r2,
        "Predictions": predictions
    }


def predict_next_day(model, latest_data):
    """
    Predict the next trading day's closing price.
    """

    latest_features = latest_data[
        FEATURES
    ].iloc[[-1]]

    prediction = model.predict(
        latest_features
    )[0]

    return prediction