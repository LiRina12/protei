import requests
from requests.exceptions import HTTPError
import pytest
import allure
from API_documentation import check_success_request, search_geokoding, reverse_geokoding
from test_cases_searche import test_data_search, test_data_reverse


class Nomination:
    """
    родительский класс для классов TestSearchGeokoding и TestReverseGeokoding
    """

    url_nomination = "https://nominatim.openstreetmap.org/"

class TestSearchGeokoding(Nomination):
    """
    test_data - список значений query expected, который формируем из словаря test_data_search
    """
    test_data = [(number_case['query'], number_case['expected']) for number_case in test_data_search]
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
    test_data = [(number_case['lon'], number_case['lat'], number_case['expected']) for number_case in test_data_reverse]
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
