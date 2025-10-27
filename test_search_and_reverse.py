import requests
from requests.exceptions import HTTPError
import pytest
import allure
from API_documentation import API_nomination
from test_cases_searche import test_data_search, test_data_reverse



class TestSearchGeokoding:
    """
    test_data - список значений query expected, который формируем из словаря test_data_search
    """
    test_data = [(number_case['query'], number_case['expected']) for number_case in test_data_search]

    @allure.feature("начало search_geokoding")
    @pytest.mark.parametrize("test_data", test_data)
    def test_search(self, test_data):
        query, expected = test_data
        with allure.step(f"Отправка в параметрах запроса query = {query}, извлечение  lon и lat из response_json"):
            result = API_nomination.search_geokoding(query)
        with allure.step(f"Сравнение полученного результата = {result}  с ожидаемым результатом = {expected}"):
            assert result == expected


class TestReverseGeokoding:
    test_data = [(number_case['lon'], number_case['lat'], number_case['expected']) for number_case in test_data_reverse]

    @allure.feature("начало reverse_geokoding")
    @pytest.mark.parametrize("test_data", test_data)
    def test_reverse(self, test_data):
        lon, lat, expected = test_data
        with allure.step("Отправка в параметрах запроса lon и  lat, извлечение name из response_json "):
            result = API_nomination.reverse_geokoding(lon, lat)
        with allure.step(f"Сравнение полученного name = {result}  с ожидаемым результатом expected = {expected}"):
            assert result == expected
