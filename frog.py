#ユーザーインタフェース

from frog_model import Frog

def main():
    print("🐸　カエルを観察するアプリ　🐸")

    putname = input("カエルの名前を決めてね🐸： ")
    frog = Frog(name = putname)
    

    while True:
        print(f"\n{frog.days}日目🐸")
        print("コマンドを選択してください：")
        print("1. 観察記録を見る")
        print("2. 餌やり")
        print("3. 仲良くする")
        print("4. アプリ終了")

        choice = input("何をしますか？（番号を入力）：")

        if choice == "1" or choice == "１":
            status = frog.get_status()
            print(f"\n[{frog.name}のステータスです]")
            for key, val in status.items():
                print(f"{key}: {val}")

        elif choice == "2" or choice == "２":
            frog.feed()
            print("餌をあげました！\n")
            print(f"{frog.name}は喜んでいます！")
            frog.pass_day()

        elif choice == "3" or choice == "３":
            print("仲良くしよう！コマンドを選択してください：")
            print("1. 触れ合う")
            print("2. 会話する")
            fr_choice = input("何をしたいですか？（番号を入力）：")

            if fr_choice == "1" or choice == "１":
                frog.touch()
                print("触れ合いました！親密度UP")
                frog.pass_day()

            elif fr_choice == "2" or choice == "２":
                frog.talk()
                frog.pass_day()

            else:
                print("[無効]1~2で選択してください")

        elif choice == "4" or choice == "４":
            save_data()
            print("これまでの行動を記録してアプリを終了します\n")
            print("またきてね🐸")
            frog.pass_day()
            break
        else:
            print("[無効]1~4で選択してください")

if __name__ == "__main__":
    main()
