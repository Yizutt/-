# Steam 免费游戏自动领取器（Termux 版）

## 使用步骤

1. 打开 Termux，执行：
```bash
git clone https://github.com/你的仓库名/steam_free_claimer.git
cd steam_free_claimer
bash install.sh
```

2. 运行手动登录：
```bash
python login_steam.py
```

3. 登录成功后运行自动领取：
```bash
python main.py
```

## 功能
- 自动获取 steamdb.info 免费游戏
- 自动模拟点击领取按钮
- 自动记录已领取游戏
