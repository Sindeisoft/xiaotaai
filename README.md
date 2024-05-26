Openai 接口平替方案
按照Openai接口功能，用python复现了一个，对接的是国产GPT模型。避免了GPT瞎说八道国内坏话的问题。

postman 测试地址 http://api.xiaotaai.com/v1/chat/completions

{
  "model": "紫鈊大模型",
  "messages": [
    {
      "role": "system",
      "content": "你是超级SQL大模型，优秀的数据库管理员和数据库开发者。"
    },
    {
      "role": "user",
      "content": "编写一个查询学生是否已经毕业的示例呢"
    }
  ]
}
