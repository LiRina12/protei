import requests
from oauthlib.uri_validate import query
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
            logging.error(
                f'При отправке запроса  получили HTTP error: {http_err}')
            raise AssertionError(f"Тест упал при отправке запроса с HTTP error: {http_err}")
    except Exception as err:
        with allure.step(f"В ответ на запрос получили {err}"):
            logging.error(f'При отправке запроса получили error: {err}')
            raise AssertionError(f"Тест упал при отправке запроса с error: {err}")
    else:
        if response.status_code == 200:
            with allure.step(
                    f" Успешная отправка запроса. Попытка получения response.json "):
                response_json = response.json()
                allure.attach(json.dumps(response_json, indent=1), name="Response_json",
                              attachment_type=allure.attachment_type.JSON)
                return response_json
        else:
            with allure.step(
                    f" НЕУСПЕШНАЯ отправка запроса. status_code = {response.status_code}. "):
                allure.attach(response.text, name="response.text", attachment_type=allure.attachment_type.TEXT)
                raise AssertionError(f"Тест упал при отправке запроса")


def search_geokoding(url, query):
    """
    :param query: запрос считываем из файлика test_data_searche.txt
    :return: в случае успешного получения response_json возвращаем долготу и широту в формате "lon lat" , иначе "None"
    """

    params = {"q": query, "format": "json"}
    response_json = check_success_request(url, params)
    if response_json:
        with allure.step(
                f"Response_json был успешно получен. Попытка извлечения lon и lat (долготы и широты) из response_json"):
            lon = response_json[0].get("lon")  # lon - Longitude ( долгота)
            lat = response_json[0].get("lat")  # lat - Latitude (широта)
            if lon and lat:
                with allure.step(
                        f"lon = {lon} и lat = {lat} были успешно извлечены из response_json"):
                    result = f"{lon} {lat}"
                    return result
            else:
                allure.attach(f"Не удалось получить lon/lat из response_json", name=f"Failed_lon_lat",
                              attachment_type=allure.attachment_type.TEXT)
                raise AssertionError(f"Тест упал при попытке получения lon/lat из response_json")
    else:
        allure.attach("Response_json is None", name=f"Failed_lon_lat",
                      attachment_type=allure.attachment_type.TEXT)
        raise AssertionError(f"Тест упал при попытке получения response_json запроса")


def reverse_geokoding(url, lon, lat):
    """
    :param lon: считываем из файла с помощью функции load_test_data
    :param lat: считываем из файла с помощью функции load_test_data
    :return: name , если запрос response_json был успешен, в противном случае "None"
    """

    params = {"lon": lon, "lat": lat, "format": "json"}
    response_json = check_success_request(url, params)
    if response_json:
        with allure.step(f"Response_json был успешно получен. Попытка извлечения name из response_json"):
            name = response_json.get("name")
            if name:
                with allure.step(
                        f" name = {name} успешно извлечено из response_json"):
                    result = name
                    return result
            else:
                allure.attach(f"Не удалось получить name из response_json",
                              name=f"Failed_get_lon_lat", attachment_type=allure.attachment_type.TEXT)
                raise AssertionError(
                    f"Тест упал при попытке получения lon/lat из response_json  ")
    else:
        allure.attach("Response_json is None", name=f"Failed_name",
                      attachment_type=allure.attachment_type.TEXT)
        raise AssertionError(f"Тест упал при попытке получения response_json ")
