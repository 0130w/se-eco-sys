# 软件工程经济学群活跃度统计项目

该项目采用智谱AI模型GLM-3-Turbo对群用户发言的有效性进行评估,对各模块封装性好，很容易适配于其他模型，具体见源码。

## 使用说明

1. 克隆本项目

    ```shell
    git clone 
    ```

2. 创建`.env`文件，并填写在百度智能云申请后得到的KEY，如下所示(或自行导入环境变量，或在main.py中填写api_key)

   ```text
   API_KEY=...
   ```

3. 导出群聊天记录并命名为chat.txt，放入data目录下

4. 安装运行所需库文件

   ```shell
   pip install requests zhipuai dotenv tqdm
   ```

5. 运行`main.py`

   ```shell
   python main.py
   ```
