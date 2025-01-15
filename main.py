# Importing the necessary libraries
import streamlit as st
import requests
from dotenv import load_dotenv
import os
load_dotenv()
apikey = os.getenv("CURRENCY_API_KEY")
st.set_page_config(page_title='Currency Converter', page_icon='https://th.bing.com/th/id/R.9276ab18437e37c4867777093ffb7f9d?rik=gQVDTfaIv4zFNw&pid=ImgRaw&r=0', layout='centered')
# using html and css for more interactive
st.markdown('''
    <div class='container' style="text-align: center; color: white; font-size: 50px; font-weight: bold;">
        Currency Converter
        <img src='https://img.icons8.com/ios/50/FFFFFF/refresh--v1.png' alt="Refresh Icon">
    !</div>
''', unsafe_allow_html=True)

# Adding some blank lines
st.markdown('<br>', unsafe_allow_html=True)
st.markdown('<br>', unsafe_allow_html=True)


url = f'https://v6.exchangerate-api.com/v6/{apikey}/latest/USD'
data = requests.get(url).json()
currency_codes = list(data['conversion_rates'].keys())

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown('')
    cur1 = st.selectbox('FROM WHICH?', options=[code for code in currency_codes], key=f'currency_one_{[code for code in currency_codes]}')
    modified_url = f'https://v6.exchangerate-api.com/v6/{apikey}/latest/{cur1}' # Changing the base case for each selection of the currency Code
    data1 = requests.get(modified_url).json()
    
with col2:
    st.markdown(
        """
        <div style="text-align: center;">
            <span style="font-size: 70px;">&#x21bb;</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown('')
    cur2 = st.selectbox('TO WHICH?', options=[code for code in currency_codes], key=f'Currency_two_{[code for code in currency_codes]}')
amt = st.text_input(label="Amount",placeholder='Enter Amount')
if st.button("Convert!"):
    if data1['result'] == 'success':
        conversion_rate2 = data1['conversion_rates'][cur2]
        if not amt:
            st.error("Please enter amount!")
        else:
            
            st.write(f"1 {cur1} = {round(conversion_rate2, 3)} {cur2}")
            amount = int(amt) * conversion_rate2

            st.success(f"{amt} {cur1} = {round(amount, 2)} {cur2}")
    else:
        st.error("Error occured in fetching data!")
