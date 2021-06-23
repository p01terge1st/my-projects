import requests, json

def unp_check(unp):
    url = f'http://www.portal.nalog.gov.by/grp/getData?unp={unp}&type=json'
    response = json.loads(requests.get(url).text)
    
    return (f"Наименование: {response['ROW']['VNAIMK']}\
    \nУНП организации: {response['ROW']['VUNP']} \
    \nЮридический адрес:/{response['ROW']['VPADRES']} \
    \nСостояние контрагента по МНС: {response['ROW']['VKODS']}")

    
print(unp_check(input('Введи УНП организации: \n')))