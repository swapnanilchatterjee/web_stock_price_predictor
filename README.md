# Stock Price Predictor Web App

## Overview

This project is a web application designed to predict stock prices using machine learning. It analyzes historical stock data, focusing on moving averages from the past 100 to 250 days, and forecasts future stock performance. The application is built with Python, leveraging powerful libraries and tools such as Streamlit, TensorFlow, and Jupyterpylab. For deployment, Render is used to host the web app, ensuring it is accessible and reliable.

## Features

- **Historical Data Analysis**: Analyzes stock data from the past 10 years.
- **Moving Average Calculations**: Focuses on moving averages from the previous 100 to 250 days.
- **Machine Learning Predictions**: Utilizes TensorFlow for predicting future stock performance.
- **User-Friendly Interface**: Built with Streamlit for an intuitive and interactive experience.
- **Deployed on Render**: Ensures seamless and reliable access to the application.

## Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository

```bash
git clone https://github.com/swapnanilchatterjee/web_stock_price-_predictor.git
cd stock-price-predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

1. **Run the Application Locally**

   ```bash
   streamlit run web_stock_price_predictor.py
   ```

2. **Access the Web App**

   Open your web browser and navigate to `https://web-stock-price-predictor.onrender.com/`.

3. **Input Stock Ticker**

   Enter the stock ticker symbol for the stock you want to analyze.

4. **View Predictions**

   The app will display historical data, moving averages, and predicted future performance for the specified stock.

## Deployment

The application is deployed on Render. To deploy your own version:

1. **Create a Render Account**

   Sign up for a Render account at [render.com](https://render.com).

2. **Create a New Web Service**

   Follow the instructions on Render to create a new web service and connect it to your GitHub repository.

3. **Deploy the Application**

   Render will automatically build and deploy your application.

## Collaboration

Special thanks to Gouranga Ghosh for their invaluable collaboration on this project. Your support and expertise were instrumental!

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.


## Contact

For any questions or suggestions, please contact me at swapnanilchatterjee09@gmail.com.

---

Thank you for checking out the Stock Price Predictor web app! Your feedback is greatly appreciated.

---

### Acknowledgments

- Streamlit: [https://streamlit.io](https://streamlit.io)
- TensorFlow: [https://www.tensorflow.org](https://www.tensorflow.org)
- Render: [https://render.com](https://render.com)

---

**Disclaimer**: This tool is for educational purposes only and should not be used as financial advice. Always conduct your own research before making investment decisions.
