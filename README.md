小他AI接口平替

api 地址：http://api.xiaotaai.com/v1
postman 测试 http://api.xiaotaai.com/v1/chat/completions

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
