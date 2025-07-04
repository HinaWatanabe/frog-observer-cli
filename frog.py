#ユーザーインタフェース

def main():
    print("🐸　カエルを観察するアプリ　🐸")

    days = 1

    while True:
        print(f"\n{days}日目🐸")
        print("\nコマンドを選択してください：")
        print("1. 観察記録を見る")
        print("2. 餌やり")
        print("3. アプリ終了")

        choice = input("何をしますか？（番号を入力）：")

        if choice == "1":
            print("[観察記録]まだこれから")
        elif choice == "2":
            print("[餌やり]まだこれから")
        elif choice == "3":
            save_data()
            print("これまでの行動を記録してアプリを終了します\n")
            print("またきてね🐸")
            break
        else:
            print("[無効]1~3で選択してください")

        days += 1

if __name__ == "__main__":
    main()
