class Cat:
    voice = 'Мяу'

    def __init__(self, weight: float, is_man: bool, color: str, name: str,  mimimi: bool = True, hungry: bool = True):
        self.mimimi = mimimi
        self._weight = weight
        self.hungry = hungry
        self.is_man = is_man
        self.color = color
        self.name = name

    def __str__(self):
        return self.name

    def tigidik(self):
        if self._weight <= 3:
            print('тыгыдык')
        else:
            print('ТЫГЫДЫКККК!!!')

    def speak(self):
        print(self.voice)


c = Cat(2, True, 'Полосатый', 'Барсик')
print(c._weight)
c.speak()
c.tigidik()
