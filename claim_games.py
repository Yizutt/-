import json, time
from playwright.sync_api import sync_playwright
from datetime import datetime

COOKIES_FILE = "steam_cookies.json"
CLAIMED_LOG = "claimed.log"
HTML_OUTPUT = "claimed_games.html"

def load_cookies(context, cookies_path):
    with open(cookies_path, "r") as f:
        cookies = json.load(f)
    context.add_cookies(cookies)

def generate_html(games):
    # 生成 HTML 文件
    with open(HTML_OUTPUT, "w") as f:
        f.write("<html><body><h1>已领取的 Steam 免费游戏</h1><table border='1'><tr><th>游戏 ID</th><th>时间</th></tr>")
        for game in games:
            f.write(f"<tr><td>{game['app_id']}</td><td>{game['claimed_at']}</td></tr>")
        f.write("</table></body></html>")
    print(f"已生成 HTML 清单：{HTML_OUTPUT}")

def claim_game(app_id):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        load_cookies(context, COOKIES_FILE)
        page = context.new_page()

        url = f"https://store.steampowered.com/app/{app_id}/"
        page.goto(url)
        try:
            # 检查是否有领取按钮
            if page.locator("text=Add to Account").is_visible():
                page.click("text=Add to Account")
                print(f"已领取游戏：{app_id}")
                time.sleep(3)
                return True
            else:
                print(f"游戏 {app_id} 无可领取按钮，可能已领取或无效。")
        except Exception as e:
            print(f"处理游戏 {app_id} 时出错：{e}")
        finally:
            browser.close()
        return False

def update_claimed_html(app_id):
    claimed_games = []
    try:
        with open(CLAIMED_LOG, "r") as f:
            claimed_games = [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        pass

    # 保存已领取游戏
    claimed_games.append(app_id)
    with open(CLAIMED_LOG, "a") as f:
        f.write(f"{app_id}
")

    # 生成 HTML 更新
    games = [{'app_id': game, 'claimed_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")} for game in claimed_games]
    generate_html(games)

if __name__ == "__main__":
    app_id = "123456"  # 示例，替换为实际需要领取的游戏ID
    if claim_game(app_id):
        update_claimed_html(app_id)
