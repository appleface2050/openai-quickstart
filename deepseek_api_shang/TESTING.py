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

now = datetime.datetime.now()

def fun():
    prompt = """
    请帮我用HTML生成一个五子棋游戏，所有代码保存在一个HTML中。
    """
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个专业的web开发助手，擅长使用HTML CSS JAVASCRIPT。"},
            {"role": "user", "content": prompt},
        ],
        temperature=0.7,
        stream=False,
        max_tokens=8192,
    )

    print(response.choices[0].message.content)

    print(datetime.datetime.now() - now)

if __name__ == '__main__':
    fun()
