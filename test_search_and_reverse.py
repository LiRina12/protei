import requests
from requests.exceptions import HTTPError
import pytest
import allure
import csv
from API_documentation import check_success_request, search_geokoding, reverse_geokoding
from load_test_data__from_csv_file import load_test_data
from pathlib import Path


class Nomination:
    """
    родительский класс для классов TestSearchGeokoding и TestReverseGeokoding
    """
    url_nomination = "https://nominatim.openstreetmap.org/"


class TestSearchGeokoding(Nomination):
    """
    absolute_path: абсолютный путь к файлу test_data_searche.csv с тестовыми данными;
    test_data: список пар значений [query, expected],  считываем из файла с помощью функции load_test_data
    """
    relative_path = Path('test_data_searche.csv')
    absolute_path = relative_path.resolve()
    test_data = load_test_data(absolute_path)
    url_end = "search"
    url = Nomination.url_nomination + url_end

    @allure.feature("search_geokoding")
    @pytest.mark.parametrize("test_data", test_data)
    def test_search(self, test_data):
        query, expected = test_data
        with allure.step(f"Отправка в параметрах запроса query = {query}, извлечение  lon и lat из response_json"):
            result = search_geokoding(self.url, query)
        with allure.step(f"Сравнение полученного результата = {result}  с ожидаемым результатом = {expected}"):
            assert result == expected


class TestReverseGeokoding(Nomination):

    relative_path = Path('test_data_reverse.csv')
    absolute_path = relative_path.resolve()
    test_data = load_test_data(absolute_path)
    url_end = "reverse"
    url = Nomination.url_nomination + url_end

    @allure.feature("reverse_geokoding")
    @pytest.mark.parametrize("test_data", test_data)
    def test_reverse(self, test_data):
        lon, lat, expected = test_data
        with allure.step("Отправка в параметрах запроса lon и  lat, извлечение name из response_json "):
            result = reverse_geokoding(self.url, lon, lat)
        with allure.step(f"Сравнение полученного name = {result}  с ожидаемым результатом expected = {expected}"):
            assert result == expected
