import subprocess
from langchain_community.llms import Ollama
from wrong import check_wrong
from modify import overwrite_file
# 检测代码是否出错
def main():
    llm = Ollama(model="codellama")
    task = input("请输入要完成的任务：")
    file_path = "gen.py"
    print(f"任务: {task}")
    while True:
        print("这次的任务是:", task)
        # 1️⃣ 模型生成代码
        code = llm.invoke(task)

        # 2️⃣ 保存到.py文件
        overwrite_file(file_path, code)

        # 3️⃣ 检测是否出错
        wrong,error_msg = check_wrong(file_path)
        
        # 4️⃣ 判断是否继续循环
        if not wrong:
            print("✅ 任务完成！代码运行正常。")
            break
        else:
            # 出错，反馈给模型，修改代码
            task = f"wrong: 代码出现以下错误，请修改错误后重新生成完整函数:\n{error_msg}\n原任务:\n{task}"

if __name__ == "__main__":
    main()
