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

实现的价值和原因，主要之前Openai的接口魔法上网后各种不稳定，后来算了，打算自己写一个，但是问题是会有很多的基于Openai的开源项目就会被错过了。
那么就需要模拟Openai的实现方式，这样就可以继续使用之前基于Openai做的很多开源项目了。

xiaotaai的使用的是自己的大模型服务器，大家可以免费用。需要部署自己的仿openai服务器的也可以交流。
xiaotaai的使用地址是 http://www.xiaotaai.com
