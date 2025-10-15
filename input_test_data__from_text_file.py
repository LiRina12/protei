def load_test_data(file_path, Flag):
    """
    :param file_path: путь к файлу, из которого считываем входные данные и ожидаемый результат
    :param Flag: если True, то делим query на две строки по " " (в случае reverse, чтобы получить lon и lan), если False то не делим query достаточно(в случае searche)
    :return:test_data - список с тестовыми данными
    """
    # функция для считывания данных из файла и создания списка с парами значений запрос/ожидаемы результат
    test_data = []

    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            parts = line.split(',')  # Делим строку запятой, создаем список parts из двух частей
            query = parts[0].strip()
            expected = parts[1].strip()
            if Flag == True:
                coordinat = query.split(" ") # создаем список из "lon lat" деля по пробелу
                lon = coordinat[0].strip() # 0 элемент списка coordinat это  lon
                lat = coordinat[1].strip() # 1 элемент списка coordinat это  lat
                test_data.append([lon, lat, expected])  # создаем список из взодных значений lon, lat и ожидаемого результата expected  для reverse
            else:
                test_data.append([query, expected])  # создаем список из пар-значений для search
    return test_data