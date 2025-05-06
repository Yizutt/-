from playwright.sync_api import sync_playwright
import os, json

COOKIES_FILE = "steam_cookies.json"

def save_steam_cookies():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # 手机模拟：使用 user agent
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Linux; Android 10; Mobile; Chrome/90.0.0.0)"
        )
        page = context.new_page()
        page.goto("https://store.steampowered.com/login/")
        print("请手动登录 Steam 并完成 Steam Guard 验证...")

        input("登录完成后按 Enter 保存 cookie")
        cookies = context.cookies()
        with open(COOKIES_FILE, "w") as f:
            json.dump(cookies, f)
        print("已保存登录状态 cookie。")
        browser.close()

if __name__ == "__main__":
    save_steam_cookies()
