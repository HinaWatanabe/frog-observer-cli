#ユーザーインタフェース

from frog_model import Frog

def main():
    print("🐸　カエルを観察するアプリ　🐸")

    putname = input("カエルの名前を決めてね🐸")
    frog = Frog(name = putname)
    

    while True:
        print(f"\n{frog.days}日目🐸")
        print("\nコマンドを選択してください：")
        print("1. 観察記録を見る")
        print("2. 餌やり")
        print("3. 仲良くする")
        print("4. アプリ終了")

        choice = input("何をしますか？（番号を入力）：")

        if choice == "1":
            status = frog.get_status()
            print(f"\n[{frog.name}のステータスです]\n")
            for key, val in status.items():
                print(f"{key}: {val}")

        elif choice == "2":
            frog.feed()
            print("餌をあげました！\n")
            print(f"{frog.name}は喜んでいます！")

        elif choice == "3":
            print("仲良くしよう！コマンドを選択してください：")
            print("1. 触れ合う")
            print("2. 会話する")
            fr_choice = input("何をしたいですか？（番号を入力）：")

            if fr_choice == "1":
                frog.touch()
                print("触れ合いました！親密度UP")

            elif fr_choice == "2":
                frog.talk()

            else:
                print("[無効]1~2で選択してください")

        elif choice == "4":
            save_data()
            print("これまでの行動を記録してアプリを終了します\n")
            print("またきてね🐸")
            break
        else:
            print("[無効]1~4で選択してください")

        days += 1

if __name__ == "__main__":
    main()
