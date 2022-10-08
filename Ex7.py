import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

# Первый вопрос
response = requests.get(url=url)
print("Get без параметра: ", response.text)
response = requests.post(url=url)
print("POST без параметра: ", response.text)
response = requests.put(url=url)
print("PUT без параметра: ", response.text)
response = requests.delete(url=url)
print("DELETE без параметра: ", response.text)

# Второй вопрос
response = requests.head(url=url)
print("HEAD без параметра: ", response.text)

# Третий вопрос
value = {"method": "GET"}
response = requests.get(url=url, params=value)
print("Get c параметром: ", response.text)

value = {"method": "POST"}
response = requests.post(url=url, data=value)
print("POST с параметром: ", response.text)

value = {"method": "PUT"}
response = requests.put(url=url, data=value)
print("PUT с параметром: ", response.text)

value = {"method": "DELETE"}
response = requests.delete(url=url, data=value)
print("DELETE с параметром: ", response.text)

# Четвертый вопрос

methods_all = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD']
i = 0

while i < len(methods_all):
    payload = {'method': methods_all[i]}
    response = requests.get(url=url, params=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i],
          "Код ответа сервера: ", response.status_code, "Текст ответа: ", response.text)

    response = requests.post(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i],
          "Код ответа сервера: ", response.status_code, "Текст ответа: ", response.text)

    response = requests.put(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i],
          "Код ответа сервера: ", response.status_code, "Текст ответа: ", response.text)

    response = requests.delete(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i],
          "Код ответа сервера: ", response.status_code, "Текст ответа: ", response.text)

    response = requests.head(url=url, data=payload)
    print("Метод запроса: ", response.request, "Значение метода в параметрах запроса: ", methods_all[i],
          "Код ответа сервера: ", response.status_code, "Текст ответа: ", response.text)

    i += 1

