from django.shortcuts import render
from django.http import JsonResponse, HttpResponseServerError
from django.db import IntegrityError
from .models import OptionChain
import json
import os
from datetime import datetime
from bs4 import BeautifulSoup
import requests
from django.db import connection

def update_data_json():
    current_directory = os.path.dirname(os.path.abspath(__file__))

    json_file_path = os.path.join(current_directory, 'data.json')

# Set the URL and headers
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

# Send a GET request to the website
    response = requests.get(url, headers=headers)

    soup = BeautifulSoup(response.text, 'lxml')
    json_data = soup.find('p').text

# Save the JSON data to a file named 'data.json'
    with open(json_file_path, 'w') as json_file:
        json.dump(json.loads(json_data), json_file, indent=2)

    print('Data saved to data.json')

def reset_auto_increment():
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='app_optionchain';")

def update_data():
    try:
        
        OptionChain.objects.all().delete()

        reset_auto_increment()

        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construct the absolute path to data.json
        json_file_path = os.path.join(current_directory, 'data.json')

        with open(json_file_path, 'r') as file:
            json_data = json.load(file)
        
        records = json_data.get('records', {})
        expiry_dates = records.get('expiryDates', [])
        option_data = records.get('data', [])

        for option_entry in option_data:
            pe_data = option_entry.get('PE', {})
            ce_data = option_entry.get('CE', {})

            try:
                obj = OptionChain.objects.create(
                OI_calls=ce_data.get('openInterest', 0),
                CHNG_IN_OI_calls=ce_data.get('changeinOpenInterest', 0),
                VOLUME_calls=ce_data.get('totalTradedVolume', 0),
                IV_calls=ce_data.get('impliedVolatility', 0),
                LTP_calls=ce_data.get('lastPrice', 0),
                CHNG_calls=ce_data.get('change', 0),
                BID_QTY_calls=ce_data.get('bidQty', 0),
                BID_calls=ce_data.get('bidprice', 0),
                ASK_calls=ce_data.get('askPrice', 0),
                ASK_QTY_calls=ce_data.get('askQty', 0),
                STRIKE=ce_data.get('strikePrice', 0),
                BID_QTY_puts=pe_data.get('bidQty', 0),
                BID_puts=pe_data.get('bidprice', 0),
                ASK_puts=pe_data.get('askPrice', 0),
                ASK_QTY_puts=pe_data.get('askQty', 0),
                CHNG_puts=pe_data.get('change', 0),
                LTP_puts=pe_data.get('lastPrice', 0),
                IV_puts=pe_data.get('impliedVolatility', 0),
                VOLUME_puts=pe_data.get('totalTradedVolume', 0),
                CHNG_IN_OI_puts=pe_data.get('changeinOpenInterest', 0),
                OI_puts=pe_data.get('openInterest', 0),
        )

                print(f"Created: {obj}")
            except IntegrityError as e:
                print(f"IntegrityError during update_or_create: {e}")
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return current_time

    except json.JSONDecodeError as e:
        return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)
    except Exception as e:
        print(f"Unexpected error: {e}")
        return HttpResponseServerError()


def display_it(request):
    update_data_json()
    time = update_data()
    option_chain_data = OptionChain.objects.all().order_by('-id')
    return render(request, 'app/display_it.html', {'option_chain_data': option_chain_data, 'time':time})

