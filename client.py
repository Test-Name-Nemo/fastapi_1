
import requests


response = requests.post(
    "http://127.0.0.1:8080/v1/advertisement",
    json={
        "title": "Дрель",
        "description": "Качественная",
        "price": 4.01,
        "author": "Igor",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/v1/advertisement",
    json={
        "title": "Рюкзак",
        "description": "Красный",
        "price": 10.33,
        "author": "Eugene",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.patch("http://127.0.0.1:8080/v1/advertisement/1", json={
    "title": "Перфоратор",
    "price": 6.01,
})
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement/1",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement/2",
)
print(response.status_code)
print(response.json())


response = requests.delete(
    "http://127.0.0.1:8080/v1/advertisement/2",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement/2",
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/v1/advertisement",
    json={
        "title": "Шапка",
        "description": "В хорошем состоянии",
        "price": 1.02,
        "author": "Igor",
    },
)
print(response.status_code)
print(response.json())


response = requests.post(
    "http://127.0.0.1:8080/v1/advertisement",
    json={
        "title": "Шуруповерт",
        "description": "Хорошее состояние",
        "price": 6.01,
        "author": "Victor",
    },
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?title=Перфоратор",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?description=сост",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?price=6.01",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?creator=Victor",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?description=сост&price=1.02",
)
print(response.status_code)
print(response.json())


response = requests.get(
    "http://127.0.0.1:8080/v1/advertisement?creator=Ivan",
)
print(response.status_code)
print(response.json())
