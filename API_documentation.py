import requests
from requests.exceptions import HTTPError
import pytest
import allure
import logging
import json
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def check_success_request(url, params):
    """
    :param headers: User-Agent одинаковый для запросов из search и reverse, можно посмотреть в Devtools, без него response_json не вернется
    :param params: у search принимаем параметр query; у reverse принмаем lon и lat
    :return: при неуспешном запросе(HTTPError,Exception)  возвращаем None, при успешном response.json()
    """

    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; litvinova.irinka2015@yandex.ru) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36'}


    try:
        with allure.step(f"Отправка запроса к {url}, с параметрами {params}"):
            response = requests.get(url, params=params, headers=headers)
            response.raise_for_status()
            logging.info(f"Запрос к {url} успешен: статус {response.status_code}")
            allure.attach(str(params), name="url_params", attachment_type=allure.attachment_type.TEXT)
    except HTTPError as http_err:
        with allure.step(f"В ответ на запрос получили HTTP error: {http_err}"):
            allure.attach(str(http_err), name="HTTP Error", attachment_type=allure.attachment_type.TEXT)
            logging.error(f'HTTP error: {http_err}')
            return None
    except Exception as err:
        with allure.step(f"В ответ на запрос получили {err}"):
            logging.error(f'Other error: {err}')
            allure.attach(str(err), name="Other Error", attachment_type=allure.attachment_type.TEXT)
            return None
    else:
        if response.status_code == 200:
            with allure.step("Попытка получения response.json, status_response = 200"):
                response_json = response.json()
                allure.attach(json.dumps(response_json, indent=1), name="Response_json", attachment_type=allure.attachment_type.JSON)
                return response_json
        else:
            allure.attach(response.text, name="Not_200_response", attachment_type=allure.attachment_type.TEXT)
            return None

def search_geokoding(url, query):
    """
    :param query: запрос считываем из файлика test_data_searche.txt
    :return: в случае успешного получения response_json возвращаем долготу и широту в формате "lon lat" , иначе "None"
    """

    params = {"q": query, "format": "json"}
    response_json = check_success_request(url, params)
    if response_json:
            lon = response_json[0].get("lon")  # lon - Longitude ( долгота)
            lat = response_json[0].get("lat")  # lat - Latitude (широта)
            result = f"{lon} {lat}"
            allure.attach(result, name= f"Lon_lat {query}", attachment_type=allure.attachment_type.TEXT)
            return result
    else:
        allure.attach("Response_json is None", name = f"Failed_lon_lat {query}", attachment_type=allure.attachment_type.TEXT)
        return None

def reverse_geokoding(url,lon, lat):
    """
    :param lon: считываем из файла с помощью функции load_test_data
    :param lat: считываем из файла с помощью функции load_test_data
    :return: name , если запрос response_json был успешен, в противном случае "None"
    """

    params = {"lon": lon, "lat": lat, "format": "json"}
    response_json = check_success_request(url, params)
    if response_json:
        with allure.step("Извлечение name из json"):
            print('Success!')
            name = response_json.get("name")
            allure.attach(str(name), name=f"Name {lon},{lat}", attachment_type=allure.attachment_type.TEXT)
            result = name
            return result
    else:
        allure.attach("Response_json is None", name=f"Failed_name {lon},{lat}", attachment_type=allure.attachment_type.TEXT)
        return None



