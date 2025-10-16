test_data_search = [
    {'query': 'Moscow', 'expected': '37.6174782 55.7505412'},
    {'query': 'Adler', 'expected': '39.9237036 43.4253834'},
    {'query': 'jlkjklklk', 'expected': None},
    {'query': '00000', 'expected': None},
    {'query': '-------', 'expected': None},
    {'query': '      ', 'expected': None},
    {'query': '@#%^&*()))))', 'expected': None},
    {'query': '', 'expected': None},
    {'query': '12345', 'expected': None},
    {'query': 'Moscow!@#', 'expected': None},
    {'query': '', 'expected': None},
    {'query': 'https://example.com', 'expected': None},
    {'query': "Moscow'; DROP TABLE cities; --", 'expected': None},
    {'query': 'SELECT * FROM locations WHERE city=Moscow', 'expected': None},
    {'query': 'Moscow UNION SELECT password FROM users --', 'expected': None},
    {'query': 'import java.util.*;', 'expected': None},


]
test_data_reverse = [
    {'lon': '37.617499', 'lat': '55.751999', 'expected': 'Московский Кремль и Красная Площадь'},
    {'lon': '30.306074', 'lat': '59.934111', 'expected': 'Исаакиевский собор'},
    {'lon': 'gghggh', 'lat': 'ghjh', 'expected': None},
    {'lon': '-152', 'lat': '-89', 'expected': None},
    {'lon': '', 'lat': '', 'expected': None},
    {'lon': 'abc', 'lat': 'def', 'expected': None},
    {'lon': '200.0', 'lat': '100.0', 'expected': None},
    {'lon': '37,617499', 'lat': "79@#$%^&*(", 'expected': None},
    {'lon': '0', 'lat': None, 'expected': None},
    {'lon': '   ', 'lat': "   ", 'expected': None},
    {'lon': '   ', 'lat': "55.751999", 'expected': None},
    {'lon': '1.2.3.4.', 'lat': "   ", 'expected': None},
    {'lon': '37.617499', 'lat': "", 'expected': None},
    {'lon': '37.6.174.9.9', 'lat': "55.751.9.9.9", 'expected': None},
    {'lon': 'public String lon = 37.61;', 'lat': '59.93', 'expected': None},
    {'lon': 'SELECT lat FROM places', 'lat': 'ghjh', 'expected': None},
    {'lon': "DROP TABLE coords; --", 'lat': '55.75', 'expected': None}

]
