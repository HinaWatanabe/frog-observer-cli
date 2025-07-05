import random

#カエルの状態
class Frog:
    def __init__(self, name):
        self.name =name
        self.days = 1
        self.weight = 10.0
        self.fullstom = 100
        self.bodytemp = 20.0
        self.friend = 0


    def feed(self, food=10):
            self.fullstom = min(100, self.fullstom + food)
            self.weight += 1  # 餌10で1g増える
    
    def pass_day(self):
        self.days += 1
        self.fullstom = max(0, self.fullstom - 10)
        if self.fullstom < 30:
            self.weight -= 0.2  # 空腹だと痩せる
            self.friend -= 3
            
        elif self.fullstom > 60:
            self.friend += 3

        else:
            pass
    
    def get_status(self):
        return {
            "日数": self.days,
            "名前": self.name,
            "親密度": f"{self.friend:.1f}/100",
            "体重": f"{self.weight:.1f}g",
            "満腹度": self.fullstom,
            "体温": f"{self.bodytemp:.1f}℃"
        }
    
    def touch(self):
        self.friend += 5
    
    def talk(self):
        word = input("話しかけてみよう！（話したいことを入力）：")

        if "ケロ" in word or "ゲロ" in word or "ゲコ" in word:
            responses = [
                "ケロケロッ！",
                "ケロケーロ、ケロ！",
                "グワッグワッ",
                "ゲコゲコゲコ！"
            ]
            print(random.choice(responses))
            self.friend += 5
        
        else:
            print(f"{self.name}は首をかしげている🐸？")
    
    