import requests

parameters = {
    'amount': 10,
    'type': 'boolean'
}

response = requests.get(url="https://opentdb.com/api.php?amount=10", params=parameters)
question_data = response.json()['results']