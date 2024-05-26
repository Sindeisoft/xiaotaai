# 使用curl命令测试返回
# curl -X POST "http://api.xiaotaai.com:8000/v1/chat/completions" \
# -H "Content-Type: application/json" \
# -d "{\"model\": \"xiaotaai\", \"messages\": [{\"role\": \"system\", \"content\": \"你的名字叫xiaotaai，学习了人类所有工业领域的知识和技能，搞的了PLC，玩的转机械设计，画的了电路板，干的了数控编程，驾驭的了航天工程，也能工地搬砖，只要您愿意我就是你的超级打工人。老板需要什么帮助啊？.\"}, {\"role\": \"user\", \"content\": \"你好，给我讲一个故事，大概100字\"}], \"stream\": false, \"max_tokens\": 100, \"temperature\": 0.8, \"top_p\": 0.8}"
# 使用Python代码测返回
import requests
import json

base_url = "http://api.xiaotaai.com" # 本地部署的地址,或者使用你访问模型的API地址

def create_chat_completion(model, messages, use_stream=False):
    data = {
        "model": model, # 模型名称
        "messages": messages, # 会话历史
        "stream": use_stream, # 是否流式响应
        "max_tokens": 2048, # 最多生成字数
        "temperature": 1, # 温度
        "top_p": 1, # 采样概率
    }
    

    response = requests.post(f"{base_url}/v1/chat/completions", json=data, stream=use_stream)
    if response.status_code == 200:
        if use_stream:
            # 处理流式响应
            for line in response.iter_lines():
                if line:
                    decoded_line = line.decode('utf-8')[6:]
                    try:
                        response_json = json.loads(decoded_line)
                        content = response_json.get("choices", [{}])[0].get("delta", {}).get("content", "")
                        print(content)
                    except:
                        print("Special Token:", decoded_line)
        else:
            # 处理非流式响应
            decoded_line = response.json()
            print(decoded_line)
            content = decoded_line.get("choices", [{}])[0].get("message", "").get("content", "")
            print(content)
    else:
        print("Error:", response.status_code)
        return None


if __name__ == "__main__":
    chat_messages = [
        {
            "role": "system",
            "content": "你的名字叫小他AI，学习了人类所有工业领域的知识和技能，搞的了PLC，玩的转机械设计，画的了电路板，干的了数控编程，驾驭的了航天工程，也能工地搬砖，只要您愿意我就是你的超级打工人。老板需要什么帮助啊？",
        },
        {
            "role": "user",
            "content": "你好，你是谁啊？"
        }
    ]
    create_chat_completion("xiaotaai", chat_messages, use_stream=False)


