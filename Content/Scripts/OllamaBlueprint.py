import unreal
import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {
        "model": "deepseek-coder-v2",
        "prompt": f"Напиши логику Blueprint для: {prompt}. Опиши пошагово, какие узлы (Nodes) использовать.",
        "stream": False
    }
    response = requests.post(url, json=data)
    return response.json()['response']

# Пример вызова
response = ask_ollama("Создать спавнер объектов, которые меняют цвет при клике")
print(response)