from openai import OpenAI

client = OpenAI(
    api_key="sk-e40055510ec94b78abe9e5a2246c4269",
    base_url="https://api.deepseek.com"
)

# 强化版系统提示词
system_prompt = """
你是一个智能对话助手，请遵循以下规则：
1. 如果用户想要结束对话，请在你的回复最后一行单独添加标记 <!--EXIT-->
2. 不要主动建议用户退出
3. 当且仅当用户明确表达退出意愿时添加标记
4. 用自然的中文进行回复
"""

messages = [{"role": "system", "content": system_prompt}]

#print("\n欢迎使用DeepSeek对话助手！可随时表达退出意愿结束对话\n")

while True:
    try:
        user_input = input("你：")
    except KeyboardInterrupt:
        print("\n再见！")
        break
    
    messages.append({"role": "user", "content": user_input})
    
    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=messages,
            temperature=0.3,  # 降低随机性
            max_tokens=300
        )
        
        full_reply = response.choices[0].message.content
        
        # 检测退出标记
        if "<!--EXIT-->" in full_reply:
            # 清除标记并显示最终回复
            clean_reply = full_reply.replace("<!--EXIT-->", "").strip()
            print(f"\n助理：{clean_reply}\n")
            print("对话已结束")
            break
            
        # 正常对话处理
        messages.append({"role": "assistant", "content": full_reply})
        print(f"\n助理：{full_reply}\n")
        
    except Exception as e:
        print(f"请求出错：{str(e)}")
        continue