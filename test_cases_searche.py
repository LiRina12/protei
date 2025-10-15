test_data_search = [
    {'query': 'Moscow', 'expected': '37.6174782 55.7505412'},
    {'query': 'Adler', 'expected': '39.9237036 43.4253834'},
    {'query': 'jlkjklklk', 'expected': 'None'}

]
test_data_reverse = [
    {'lon': '37.617499', 'lat': '55.751999', 'expected': 'Московский Кремль и Красная Площадь'},
    {'lon': '30.306074', 'lat': '59.934111', 'expected': 'Исаакиевский собор'},
    {'lon': 'gghggh', 'lat': 'ghjh', 'expected': 'None'}
]