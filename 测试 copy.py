from openai import OpenAI

client = OpenAI(api_key="sk-e40055510ec94b78abe9e5a2246c4269", base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "第一句话请用中文回复我"},
        {"role": "user", "content": "介绍一下你自己"},
    ],
    stream=False
)

print(response.choices[0].message.content)  # 应输出b'...'格式