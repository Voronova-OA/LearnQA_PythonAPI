import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

n = len(response.history)

url_text = response.url

i = 0

while i < n:
    print(str(i+1) + "-й редирект: " + response.history[i].url)
    i += 1

print("Число редиректов: " + str(n))
print("Конечный url: " + url_text)

