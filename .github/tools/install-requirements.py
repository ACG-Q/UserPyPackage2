import os
import sys

def install_requirements(requirements_file):
    """
    使用 pip 安装 requirements 文件中列出的 Python 依赖包。
    """
    command = f"pip install -r {requirements_file}"
    return os.system(command)

def check_requirements_file(requirements_file):
    """
    检查 requirements 文件是否存在。
    """
    if not os.path.exists(requirements_file):
        print(f"错误：文件 '{requirements_file}' 不存在。")
        sys.exit(1)

if __name__ == "__main__":
    # 检查命令行参数中是否提供了 requirements 文件路径
    if len(sys.argv) != 2:
        print("用法: python install-requirements.py <requirements文件路径>")
        os.sys.exit(1)

    requirements_file = sys.argv[1]
    check_requirements_file(requirements_file)  # 检查 requirements 文件是否存在
    result = install_requirements(requirements_file)  # 安装依赖
    
    # 检查命令执行的退出状态码
    if result != 0:
        print(f"从 {requirements_file} 安装依赖时发生错误")
        os.sys.exit(result)
