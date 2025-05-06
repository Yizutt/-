#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] 安装依赖..."

# 切换或确认镜像源（你的脚本可能已有这部分）
termux-change-repo -y >/dev/null 2>&1

# 安装基础依赖
pkg update -y
pkg install -y python git python-pip

echo "[+] 安装 Python 库..."
if [ -f requirements.txt ]; then
    pip install --upgrade pip setuptools wheel
    pip install -r requirements.txt
else
    echo "[!] 未找到 requirements.txt，跳过依赖安装。"
fi

echo "[+] 安装完成。"