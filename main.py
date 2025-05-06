from get_free_games import fetch_free_games
from claim_games import claim_game

claimed_log = "claimed.log"

def load_claimed():
    try:
        with open(claimed_log, "r") as f:
            return set(f.read().splitlines())
    except:
        return set()

def save_claimed(app_id):
    with open(claimed_log, "a") as f:
        f.write(f"{app_id}
")

if __name__ == "__main__":
    claimed = load_claimed()
    games = fetch_free_games()

    for app_id in games:
        if app_id not in claimed:
            claim_game(app_id)
            save_claimed(app_id)
        else:
            print(f"已跳过已领取游戏：{app_id}")
