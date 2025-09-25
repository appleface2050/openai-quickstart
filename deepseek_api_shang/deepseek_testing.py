import os
import datetime
from openai import OpenAI

# 从环境变量读取deepseek api key

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("deepseek api key 不存在")


# 初始化openai客户端
client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com"
)


def fun():
    now = datetime.datetime.now()
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "天津有什么推荐的美食？"},
        ],
        stream=False
    )
    print(response.choices[0].message.content)
    print(datetime.datetime.now() - now)

if __name__ == '__main__':
    #print("hello")
    fun()

