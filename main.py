from datetime import datetime

from data_loader import prepare_data
from model import (
    split_data,
    train_model,
    evaluate_model,
    predict_next_day
)


def print_header():
    print("\n" + "=" * 65)
    print("        AI STOCK PRICE PREDICTION SYSTEM")
    print("=" * 65)


def main():

    print_header()

    ticker = input(
        "\nEnter stock ticker "
        "(Example: AAPL, MSFT, TSLA): "
    ).strip().upper()

    if not ticker:
        print("Ticker cannot be empty.")
        return

    try:

        # ------------------------------------------------
        # 1. Load and prepare data
        # ------------------------------------------------

        data = prepare_data(
            ticker,
            period="5y"
        )

        print(
            f"\nDataset size: {len(data)} rows"
        )

        print(
            f"Date range: "
            f"{data['Date'].iloc[0].date()} "
            f"to "
            f"{data['Date'].iloc[-1].date()}"
        )

        # ------------------------------------------------
        # 2. Train/test split
        # ------------------------------------------------

        (
            X_train,
            X_test,
            y_train,
            y_test,
            test_data
        ) = split_data(data)

        print(
            f"\nTraining samples: {len(X_train)}"
        )

        print(
            f"Testing samples: {len(X_test)}"
        )

        # ------------------------------------------------
        # 3. Train model
        # ------------------------------------------------

        print(
            "\nTraining Random Forest model..."
        )

        model = train_model(
            X_train,
            y_train
        )

        print(
            "Model training completed."
        )

        # ------------------------------------------------
        # 4. Evaluate model
        # ------------------------------------------------

        results = evaluate_model(
            model,
            X_test,
            y_test
        )

        predictions = results[
            "Predictions"
        ]

        print("\n" + "-" * 65)
        print("MODEL PERFORMANCE")
        print("-" * 65)

        print(
            f"MAE  : ${results['MAE']:.2f}"
        )

        print(
            f"RMSE : ${results['RMSE']:.2f}"
        )

        print(
            f"R²   : {results['R2']:.4f}"
        )

        # ------------------------------------------------
        # 5. Show recent predictions
        # ------------------------------------------------

        print("\n" + "-" * 65)
        print("RECENT TEST PREDICTIONS")
        print("-" * 65)

        recent_count = min(
            10,
            len(test_data)
        )

        recent_test = test_data.tail(
            recent_count
        )

        recent_predictions = predictions[
            -recent_count:
        ]

        for date, actual, predicted in zip(
            recent_test["Date"],
            recent_test["Target"],
            recent_predictions
        ):

            print(
                f"{date.date()} | "
                f"Actual: ${actual:.2f} | "
                f"Predicted: ${predicted:.2f}"
            )

        # ------------------------------------------------
        # 6. Predict next trading day
        # ------------------------------------------------

        next_day_prediction = predict_next_day(
            model,
            data
        )

        current_price = float(
            data["Close"].iloc[-1]
        )

        difference = (
            next_day_prediction
            - current_price
        )

        percentage_change = (
            difference / current_price
        ) * 100

        print("\n" + "=" * 65)
        print("NEXT TRADING DAY PREDICTION")
        print("=" * 65)

        print(
            f"\nStock: {ticker}"
        )

        print(
            f"Latest Price: "
            f"${current_price:.2f}"
        )

        print(
            f"Predicted Price: "
            f"${next_day_prediction:.2f}"
        )

        print(
            f"Predicted Change: "
            f"{percentage_change:+.2f}%"
        )

        if percentage_change > 0:
            direction = "UP"
        elif percentage_change < 0:
            direction = "DOWN"
        else:
            direction = "UNCHANGED"

        print(
            f"Predicted Direction: {direction}"
        )

        print(
            f"\nPrediction generated: "
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print("\n" + "=" * 65)

        print(
            "\nIMPORTANT:"
        )

        print(
            "This is an educational machine-learning "
            "project. Stock prices are highly uncertain, "
            "and model predictions should not be treated "
            "as financial advice or guaranteed future prices."
        )

    except Exception as error:

        print(
            f"\nError: {error}"
        )

        print(
            "\nPlease check the ticker symbol "
            "and your internet connection."
        )


if __name__ == "__main__":
    main()