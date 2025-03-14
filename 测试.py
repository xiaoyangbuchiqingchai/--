from openai import OpenAI
import os

client = OpenAI(api_key="sk-e40055510ec94b78abe9e5a2246c4269", base_url="https://api.deepseek.com")

# 初始化对话历史（含系统指令）
messages = [
    {"role": "system", "content": "你是一个乐于助人的助手，用中文简洁回答问题。"}
]

def main():
    print("--- DeepSeek 终端对话程序 ---")
    print("输入内容开始对话，输入 'exit' 或按 Ctrl+C 退出\n")

    try:
        while True:
            # 获取用户输入
            user_input = input("你: ")
            
            # 退出条件
            if user_input.lower() in ["exit", "quit", "退出"]:
                print("对话结束。")
                break
            
            # 将用户输入添加到对话历史
            messages.append({"role": "user", "content": user_input})

            # 调用 API
            response = client.chat.completions.create(
                model="deepseek-chat",
                messages=messages,
                stream=False  # 非流式模式
            )

            # 提取回复并更新对话历史
            assistant_reply = response.choices[0].message.content
            messages.append({"role": "assistant", "content": assistant_reply})

            # 输出回复
            print("\nAssistant:", assistant_reply, "\n")

    except KeyboardInterrupt:
        print("\n对话被中断。")

if __name__ == "__main__":
    main()