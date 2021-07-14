import requests, json
import json
from datetime import date




def currency(cur_name):
    current_date = date.today()
    url = f'https://www.nbrb.by/api/exrates/rates/{cur_name}?parammode=2'
    response = json.loads(requests.get(url).text)
    return f"Сегодня {current_date}. \n1 {response['Cur_Name']} стоит {response['Cur_OfficialRate']} бел.руб."


usd = currency('usd')

print(usd)
