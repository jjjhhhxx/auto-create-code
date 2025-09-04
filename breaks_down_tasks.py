from langchain_community.llms import Ollama
import json

def breaks_down_tasks():
    llm = Ollama(model="codegemma")

    # 输入大任务
    task = input("请输入要完成的任务：")

    # 构建提示词，要求输出 JSON 格式的子任务
    prompt = f"""
    请将以下任务分解为5或更多个具体可以编写函数来完成的任务用以输入codellama模型编写函数代码，并以 JSON 列表的形式返回：
    "{task}"
    格式示例：
    [
        "子任务1描述",
        "子任务2描述",
        "子任务3描述",
        "子任务4描述",
        "子任务5描述"
    ]
    """

    # 调用模型
    response = llm.invoke(prompt)

    # 尝试解析 JSON
    try:
        code = json.loads(response)
        if not isinstance(code, list):
            print("分解任务失败，返回结果不是列表")
            code = [str(code)]
    except json.JSONDecodeError:
        # 如果模型输出无法直接解析为 JSON，就把原始文本存入 code
        print("分解任务失败")
        code = response
       

    return code


