import requests

url = "http://127.0.0.1:8000/generate_simple"
data = {"task": "写一个Python函数，返回两个数的和"}

response = requests.post(url, json=data)

print("状态码:", response.status_code)
print("响应文本:", response.text)   # 先看看返回的原始内容
