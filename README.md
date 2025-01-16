# Currency Converter Web App

A simple and interactive **Currency Converter** web app built using **Streamlit** and the **ExchangeRate-API**. This app allows users to convert amounts between different currencies with real-time exchange rates.

---

## Features
- Real-time currency conversion using ExchangeRate-API.
- Interactive user interface with dropdown selections for "From" and "To" currencies.
- Displays conversion rates and calculates the converted amount.
- User-friendly layout and design.

---

## Requirements
### Prerequisites
- Python 3.7 or higher
- An API key from [ExchangeRate-API](https://www.exchangerate-api.com/)

### Python Libraries
- `streamlit`
- `requests`
- `python-dotenv`

---

## Installation
### 1. Clone this repository:
   ```bash
   git clone https://github.com/bigyan22/Currency-Converter.git
   cd Currency-Converter
```
### 2. Install the required dependencies:
You can install the require libraries by using the following command:
```bash
pip install -r requirements.txt
```

### 3. Set up an API key:
- Create a *.env* file in the root directory of the project.
- Add the following line to the *.env*
```bash
CURRENCY_API_KEY = your_api_key_from_exchangerate.com
```

### 4. Finally run the app
You can run the app by using the following command:
```bash
streamlit run main.py
```

## Usage:
- Open the app in your browser.
- Select the base currency and the target currency from the dropdown menus.
- Enter the amount you wish to convert.
- Click the **Convert** button to view the conversion rates and converted amount.


## Contributions

Contributions are welcome from developers, designers, and enthusiasts to enhance the Currency Converter app.
