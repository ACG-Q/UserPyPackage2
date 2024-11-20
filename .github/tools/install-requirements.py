import os
import sys

def install_requirements(requirements_file):
    """
    使用 pip 安装 requirements 文件中列出的 Python 依赖包。
    """
    command = f"pip install -r {requirements_file}"
    return os.system(command)

def check_and_install(requirements_file):
    """
    检查 requirements 文件是否存在，如果存在则安装依赖。
    """
    if os.path.exists(requirements_file):
        print(f"发现 requirements 文件：{requirements_file}，开始安装依赖...")
        result = install_requirements(requirements_file)
        if result != 0:
            print(f"从 {requirements_file} 安装依赖时发生错误")
            sys.exit(result)
    else:
        print(f"未发现 requirements 文件：{requirements_file}，跳过依赖安装步骤。")

if __name__ == "__main__":
    # 检查命令行参数中是否提供了 requirements 文件路径
    if len(sys.argv) != 2:
        print("用法: python install-requirements.py <requirements文件路径>")
        sys.exit(1)

    requirements_file = sys.argv[1]
    check_and_install(requirements_file)  # 检查并安装依赖
