import random
import time

class GameStage:
    def __init__(self):
        self.hp = 100
        self.stage = 1

    def play_stage(self):
        print(f"現在のHP＝{self.hp}")
        print(f"今のステージ＝{self.stage}")

        print("a, b, c のどれを選びますか？")
        choice = input().lower()
        # ロード中を表示する
        print("ロード中", end='', flush=True)

        time.sleep(3)  # 3秒のタイムラグ
        # ロード中を非表示にして入力結果を表示する
        print('\r', end='')  # カーソルを行頭に戻す

        damage = 0
        if choice == "a":
            damage = random.choice(range(-30, 12, 2))  # 偶数の範囲から選択
        elif choice == "b":
            damage = random.choice(range(-29, 12, 2))  # 奇数の範囲から選択
        elif choice == "c":
            damage = random.randint(-30, 10)

        print(f"あなたの選択＝{choice}")
        print(f"選択の結果、ダメージ＝{damage}")

        self.hp += damage
        if self.hp < 0:
            self.hp = 0
        
        print(f"現在のHP＝{self.hp}")
        print("----------")
        self.stage += 1

if __name__ == "__main__":
    print("[a,d,c]を選んで高スコア、高ステージを目指そう！！")
    game = GameStage()
    while game.hp > 0:
        game.play_stage()
        if game.stage > 10 and game.hp > 0:
            print("ステージ10を超えました！ゲームクリア!")
            break
    else:
        print("ゲームオーバー")



