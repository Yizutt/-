#!/data/data/com.termux/files/usr/bin/bash
set -e

echo "[+] 安装依赖..."
pkg update -y
pkg install -y python git

echo "[+] 安装 Python 库..."
pip install --upgrade pip
pip install playwright beautifulsoup4 requests

echo "[+] 初始化 Playwright（首次运行需）..."
playwright install

echo "[+] 安装完成！"
echo ">> 第一步：运行 python login_steam.py 手动登录 Steam"
echo ">> 第二步：运行 python main.py 自动获取并领取可用免费游戏"
