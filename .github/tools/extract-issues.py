import sys
import re
import os

def extract_info(issue_body):
    python_version = None
    target_platform = None
    zip_link = None

    # 提取 Python 版本
    python_version_match = re.search(r'### Python版本\s*\n\s*(.*?)\s*\n', issue_body, re.MULTILINE)
    if python_version_match:
        python_version = python_version_match.group(1).strip()
        if python_version == "_No response_":
            python_version = "3.6.5"

    # 提取目标平台
    target_platform_match = re.search(r'### 目标平台\s*\n\s*(.*?)\s*\n', issue_body, re.MULTILINE)
    if target_platform_match:
        target_platform = target_platform_match.group(1).strip()
        if not target_platform or target_platform == "_Noresponse_":
            target_platform = "ubuntu-latest"
    # 转换为数组
    target_platform = target_platform.split(",")

    # 提取 ZIP 文件链接
    zip_link_match = re.search(r'https://github\.com/[^"]+\/files/[^"]+\.zip', issue_body)
    if not zip_link_match:
        print("未找到 ZIP 文件链接，任务终止")
        sys.exit(1)
    zip_link = zip_link_match.group(0)

    return python_version, target_platform, zip_link

def main():
    if len(sys.argv) != 2:
        print("Usage: python extract-issues.py <issue_body>")
        sys.exit(1)

    issue_body = sys.argv[1]
    python_version, target_platform, zip_link = extract_info(issue_body)

    # 输出到 GitHub Actions 的 $GITHUB_OUTPUT
    # with open(os.environ['GITHUB_OUTPUT'], 'a') as f:
    #     f.write(f"python-version={python_version}\n")
    #     f.write(f"target-platform={target_platform}\n")
    #     f.write(f"zip-link={zip_link}\n")

    print(f'::set-output name=python-version::{python_version}')
    print(f'::set-output name=target-platform::{json.dumps(target_platform)}')
    print(f'::set-output name=zip-link::{json.dumps(zip_link)}')

if __name__ == "__main__":
    main()
