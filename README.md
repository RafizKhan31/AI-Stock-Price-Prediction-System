# 📈 AI Stock Price Prediction System

An end-to-end **AI/ML Stock Price Prediction System** built with Python and Machine Learning.

This project downloads historical stock market data, performs feature engineering using technical indicators, trains a **Random Forest Regression** model, evaluates its performance, and predicts the next trading day's closing price.

> ⚠️ **Disclaimer:** This project is created for educational and portfolio purposes. Stock-market predictions are inherently uncertain. The output should not be considered financial advice or a guaranteed prediction of future prices.

---

## 🚀 Project Overview

The **AI Stock Price Prediction System** uses historical market data and machine-learning techniques to estimate the next trading day's closing price.

The system automatically:

1. Downloads historical stock data.
2. Cleans and prepares the dataset.
3. Generates technical indicators.
4. Creates machine-learning features.
5. Splits the data chronologically into training and testing sets.
6. Trains a Random Forest Regression model.
7. Evaluates the model using multiple metrics.
8. Displays recent actual vs predicted prices.
9. Predicts the next trading day's closing price.
10. Calculates the predicted percentage change and direction.

---

## ✨ Features

### 📊 Stock Market Data

* Automatically downloads historical data using Yahoo Finance.
* Supports different stock tickers.
* Configurable historical data period.
* Uses daily market data.

### 🧠 Machine Learning

* Random Forest Regression
* Time-series aware train/test split
* Feature engineering
* Regression-based price prediction
* Next-day prediction

### 📈 Technical Indicators

The project generates several technical indicators, including:

* SMA 10
* SMA 20
* SMA 50
* EMA 10
* EMA 20
* RSI
* MACD
* ATR
* Daily Return
* Volatility
* Momentum

### 🔢 Lag Features

Historical closing prices are also used as machine-learning features:

* 1-day lag
* 2-day lag
* 3-day lag
* 5-day lag
* 10-day lag

### 📏 Model Evaluation

The trained model is evaluated using:

* MAE
* RMSE
* R² Score

### 🔮 Prediction

The system provides:

* Latest stock price
* Predicted next-day price
* Predicted percentage change
* Predicted direction

Example:

```text
Latest Price:       $250.32
Predicted Price:    $252.14
Predicted Change:   +0.73%
Direction:          UP
```

---

# 🏗️ System Architecture

```text
                    ┌─────────────────────┐
                    │    Yahoo Finance    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Historical Stock    │
                    │       Data          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Data Cleaning &     │
                    │ Preprocessing       │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Feature Engineering │
                    │ & Technical         │
                    │ Indicators          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Time-Series Train / │
                    │ Test Split          │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │ Random Forest       │
                    │ Regression Model    │
                    └──────────┬──────────┘
                               │
                  ┌────────────┴────────────┐
                  ▼                         ▼
        ┌─────────────────┐       ┌─────────────────┐
        │ Model Evaluation│       │ Next-Day Price  │
        │ MAE/RMSE/R²     │       │ Prediction      │
        └─────────────────┘       └─────────────────┘
```

---

# 📁 Project Structure

```text
stock-price-predictor/
│
├── data_loader.py
├── model.py
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

### `data_loader.py`

Responsible for:

* Downloading stock data
* Data preprocessing
* Technical indicator calculation
* Feature engineering
* Creating the prediction target

### `model.py`

Responsible for:

* Feature selection
* Train/test splitting
* Random Forest model training
* Model evaluation
* Next-day prediction

### `main.py`

The main application that:

* Accepts the stock ticker
* Runs the complete ML pipeline
* Displays model performance
* Displays recent predictions
* Generates the next-day prediction

---

# 🛠️ Technologies Used

| Technology           | Purpose                   |
| -------------------- | ------------------------- |
| Python               | Core programming language |
| Pandas               | Data manipulation         |
| NumPy                | Numerical computing       |
| Scikit-learn         | Machine learning          |
| yfinance             | Stock market data         |
| Random Forest        | Regression model          |
| Technical Indicators | Feature engineering       |
| Git                  | Version control           |
| GitHub               | Project hosting           |

---

# 💻 Requirements

Before installing the project, make sure you have:

* Python 3.9 or newer
* Git
* Internet connection
* Terminal / Command Prompt / PowerShell

Check Python:

```bash
python --version
```

Example:

```text
Python 3.11.8
```

Check Git:

```bash
git --version
```

---

# 📥 Clone the Repository

Open your terminal and run:

```bash
git clone https://github.com/YOUR_USERNAME/stock-price-predictor.git
```

Move into the project directory:

```bash
cd stock-price-predictor
```

Replace:

```text
YOUR_USERNAME
```

with your GitHub username.

For example:

```bash
git clone https://github.com/rafizkhan/stock-price-predictor.git
```

---

# 🐍 Create a Virtual Environment

Using a virtual environment is recommended so project dependencies don't turn your entire Python installation into a landfill.

## Windows

Create the environment:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

After activation, your terminal should show something similar to:

```text
(venv) C:\Users\YourName\stock-price-predictor>
```

---

## Linux / macOS

Create the environment:

```bash
python3 -m venv venv
```

Activate it:

```bash
source venv/bin/activate
```

---

# 📦 Install Dependencies

After activating the virtual environment, install all required packages:

```bash
pip install -r requirements.txt
```

The `requirements.txt` file contains:

```text
yfinance
pandas
numpy
scikit-learn
```

You can also install them manually:

```bash
pip install yfinance pandas numpy scikit-learn
```

---

# ▶️ Run the Project

Run the main application:

```bash
python main.py
```

You will see:

```text
=================================================================
        AI STOCK PRICE PREDICTION SYSTEM
=================================================================

Enter stock ticker (Example: AAPL, MSFT, TSLA):
```

Enter a valid stock ticker.

For example:

```text
AAPL
```

Press **Enter**.

---

# 📊 Example Tickers

The system can work with many Yahoo Finance-supported ticker symbols.

Examples:

### 🇺🇸 US Stocks

```text
AAPL
MSFT
GOOGL
AMZN
TSLA
META
NVDA
NFLX
AMD
INTC
```

### 📈 ETFs

```text
SPY
QQQ
DIA
IWM
```

### 💰 Other Assets

Yahoo Finance supports many additional market symbols. The exact ticker format depends on the exchange.

---

# 🔄 How the System Works

## Step 1: Download Historical Data

The application uses `yfinance` to retrieve historical market data.

Example:

```python
data = yf.download(
    ticker,
    period="5y",
    interval="1d",
    auto_adjust=True
)
```

The downloaded dataset contains information such as:

* Open
* High
* Low
* Close
* Volume

---

# Step 2: Feature Engineering

The raw market data is transformed into machine-learning features.

### Moving Averages

The system calculates:

```text
SMA_10
SMA_20
SMA_50
```

and:

```text
EMA_10
EMA_20
```

These provide information about historical price trends.

---

## Step 3: RSI

The system calculates a 14-period Relative Strength Index:

```text
RSI
```

RSI is commonly used as a momentum indicator.

---

## Step 4: MACD

The system calculates:

```text
MACD
```

using exponential moving averages.

---

## Step 5: Volatility

The system calculates rolling volatility based on daily returns.

```text
Volatility_10
```

---

## Step 6: Momentum

Momentum features include:

```text
Momentum_5
Momentum_10
```

---

## Step 7: Lag Features

Previous closing prices are included as features:

```text
Close_Lag_1
Close_Lag_2
Close_Lag_3
Close_Lag_5
Close_Lag_10
```

---

# 🎯 Prediction Target

The target variable is the **next trading day's closing price**.

Conceptually:

```text
Today's Features
       ↓
Machine Learning Model
       ↓
Tomorrow's Closing Price
```

The target is generated using:

```python
df["Target"] = df["Close"].shift(-1)
```

---

# 🧪 Train/Test Split

The project uses an **80/20 chronological split**.

```text
Historical Data
│
├─────────────── 80% ───────────────┤──── 20% ────┤
│             Training              │    Testing   │
└───────────────────────────────────┴──────────────┘
```

The dataset is **not randomly shuffled**.

This is important for time-series prediction because future observations should not be allowed to leak into the training process.

---

# 🤖 Machine Learning Model

The project uses:

```python
RandomForestRegressor
```

with:

```python
n_estimators=300
max_depth=15
min_samples_split=5
min_samples_leaf=2
random_state=42
```

Random Forest is an ensemble learning method that combines predictions from multiple decision trees.

---

# 📏 Model Evaluation

The model uses three evaluation metrics.

## MAE

Mean Absolute Error:

```text
MAE = average absolute prediction error
```

If:

```text
MAE = $4.20
```

the average absolute prediction error is approximately $4.20 on the evaluated test observations.

---

## RMSE

Root Mean Squared Error:

```text
RMSE = sqrt(mean squared error)
```

RMSE gives more weight to larger errors.

---

## R² Score

R² measures the proportion of variance explained by the model relative to a baseline.

The score can be useful for evaluating the model, but it should not be interpreted as a guarantee that the model will predict future market prices accurately.

---

# 📤 Example Output

```text
=================================================================
        AI STOCK PRICE PREDICTION SYSTEM
=================================================================

Enter stock ticker (Example: AAPL, MSFT, TSLA): AAPL

Downloading data for AAPL...

Dataset size: 1190 rows
Date range: 2021-10-01 to 2026-09-23

Training samples: 952
Testing samples: 238

Training Random Forest model...
Model training completed.

-----------------------------------------------------------------
MODEL PERFORMANCE
-----------------------------------------------------------------

MAE  : $4.31
RMSE : $6.12
R²   : 0.9214

-----------------------------------------------------------------
RECENT TEST PREDICTIONS
-----------------------------------------------------------------

2026-09-10 | Actual: $245.21 | Predicted: $242.91
2026-09-11 | Actual: $247.84 | Predicted: $246.73
2026-09-14 | Actual: $249.31 | Predicted: $247.84

=================================================================
NEXT TRADING DAY PREDICTION
=================================================================

Stock: AAPL

Latest Price: $250.32
Predicted Price: $252.14
Predicted Change: +0.73%
Predicted Direction: UP
```

The numbers above are **illustrative output**. Your results will change depending on the stock, date, downloaded data, and model behavior.

---

# ⚠️ Important Limitations

Stock-price prediction is a difficult machine-learning problem.

This project does **not** account for every factor that can influence markets.

For example:

* Company earnings
* Breaking news
* Economic data
* Interest rates
* Government policy
* Geopolitical events
* Market sentiment
* Unexpected announcements
* Institutional trading
* Global market movements

Technical indicators and historical prices alone cannot fully explain future market behavior.

Therefore:

> **Do not use this project as a guaranteed trading strategy or financial advice.**

It is primarily an **AI/ML portfolio and educational project** demonstrating data collection, feature engineering, regression, evaluation, and prediction.

---

# 🔐 Data Privacy

This project does not require:

* Personal information
* Database credentials
* Brokerage credentials
* Trading account credentials
* Private API keys

Market data is retrieved from Yahoo Finance through the `yfinance` Python library.

---

# 🐛 Troubleshooting

## `ModuleNotFoundError`

If you see:

```text
ModuleNotFoundError: No module named 'yfinance'
```

install the dependencies:

```bash
pip install -r requirements.txt
```

---

## Python Command Not Found

If:

```bash
python --version
```

does not work, make sure Python is installed and added to your system PATH.

On some Linux/macOS systems, use:

```bash
python3 --version
```

and:

```bash
python3 main.py
```

---

## No Data Found

If the application displays:

```text
No data found for AAPL
```

check:

1. The ticker symbol.
2. Your internet connection.
3. Whether Yahoo Finance currently provides data for that symbol.

For example:

```text
AAPL
```

is generally preferable to entering a company name such as:

```text
Apple
```

---

## SSL / Network Errors

If Yahoo Finance cannot be reached, check your:

* Internet connection
* Firewall
* VPN
* Proxy
* Python environment

The application requires internet access because historical data is downloaded when it runs.

---

# 🧹 Deactivate Virtual Environment

When you're finished:

```bash
deactivate
```

---

# 🔄 Update the Project

If you cloned the repository earlier and want the latest GitHub version:

```bash
git pull origin main
```

Then update dependencies:

```bash
pip install -r requirements.txt --upgrade
```

---

# 🧑‍💻 Development Workflow

A typical development workflow is:

```bash
git clone https://github.com/YOUR_USERNAME/stock-price-predictor.git

cd stock-price-predictor

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python main.py
```

---

# 📌 Future Improvements

Possible future versions of this project could include:

* [ ] LSTM neural network
* [ ] GRU model
* [ ] XGBoost
* [ ] LightGBM
* [ ] Transformer-based forecasting
* [ ] Hyperparameter optimization
* [ ] Walk-forward validation
* [ ] Automated model retraining
* [ ] Interactive Streamlit dashboard
* [ ] Real-time price monitoring
* [ ] Candlestick charts
* [ ] Prediction confidence intervals
* [ ] Portfolio prediction
* [ ] Multiple-stock comparison
* [ ] News sentiment analysis
* [ ] Financial news integration
* [ ] PostgreSQL database
* [ ] REST API using FastAPI
* [ ] Docker deployment
* [ ] Cloud deployment

---

# 🧠 Machine Learning Pipeline

```text
Data Collection
      ↓
Data Cleaning
      ↓
Technical Indicators
      ↓
Feature Engineering
      ↓
Target Generation
      ↓
Chronological Train/Test Split
      ↓
Random Forest Regression
      ↓
Model Evaluation
      ↓
Next-Day Prediction
```

---

# 📚 Learning Objectives

This project demonstrates practical knowledge of:

* Python programming
* Object-oriented/data-oriented ML workflows
* Data collection
* Pandas
* NumPy
* Feature engineering
* Time-series preprocessing
* Technical indicators
* Regression
* Ensemble learning
* Random Forest
* Model evaluation
* Data leakage prevention
* Prediction pipelines
* Git/GitHub project organization

---

# 👨‍💻 Author

**Md Rafej Khan**

AI/ML Engineer | Python Developer | Data Analyst

Interested in:

```text
Artificial Intelligence
Machine Learning
Generative AI
Python Development
Backend Development
Data Science
Deep Learning
```

---

# ⭐ Support

If you find this project useful for learning or portfolio development, consider giving the repository a ⭐ on GitHub.

Every star is apparently a tiny dopamine molecule for open-source developers.

---

# 📄 License

This project is intended for educational and portfolio purposes.

You are free to modify and extend the code for your own learning and development.

---

## ⚠️ Financial Disclaimer

This software is **not financial advice**.

Predictions generated by this project are estimates produced by a machine-learning model based on historical market data and engineered features.

Past market behavior does not guarantee future results.

The author is not responsible for financial losses resulting from decisions made using this software.

Use it to learn machine learning, not to outsource your financial decisions to a Random Forest that has never even paid an electricity bill.

## Author

Md Rafej Khan
