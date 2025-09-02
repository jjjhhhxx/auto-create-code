import subprocess
#这是一个检查脚本是否有错误的脚本
# 如果脚本运行时有报错，或者返回码非0，就认为是 wrong

def check_wrong(file_path):
    try:    
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=10
        )
        # 如果有报错输出或者返回码非0，就认为 wrong
        if result.returncode != 0 or result.stderr:
            print("❌ 运行错误:", result.stderr)
            return True,result.stderrs
        return False,""
    except Exception as e:
        print("❌ 异常:", e)
        return True,str(e)

# 使用示例
wrong = check_wrong("gen.py")
print(wrong)