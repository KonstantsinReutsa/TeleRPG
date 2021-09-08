# -*- coding: utf-8 -*-

import random
from time import sleep



"""
Рпг-игра, на классах и сценариях. В качестве интерфейса - вывод текстовой информации в консоль.
Для запуска игры необходимо сохранить код в файл с расширением .py; 
Игра совместима с версией Python 3.4 и выше;
В игре не исключено наличие некоторого количества грамматических и синтаксических ошибок.
"""


class Print:
    def __repr__(self):
        print('\n--------------%s--------------\n' % (self.__class__.__name__))
        return self.__attrnames()

    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\t%s=%s\n' % (attr, self.__dict__[attr])
        return result


class Bandit(Print):
    def __init__(self, name, attack, armor, health=60, hp=60, state='[ЗДОРОВ]'):
        self.health = health
        self.name = name
        self.attack = attack
        self.armor = armor
        self.hp = hp
        self.state = state

    def takeDamage(self, damage, who):
        self.hp = self.hp - damage // self.armor
        if self.hp == self.health:
            self.state = '[ЗДОРОВ]'
        if (self.hp * 100 // self.health) < 100:
            self.state = '[ЛЕГКО РАНЕН]'
        if (self.hp * 100 // self.health) < 70:
            self.state = '[РАНЕН]'
        if (self.hp * 100 // self.health) < 40:
            self.state = '[ТЯЖЕЛО РАНЕН]'
        if (self.hp * 100 // self.health) < 15:
            self.state = '[ПОЧТИ МЕТРВ]'
        if self.hp <= 0:
            self.state = '[МЕРТВ]'
            self.death()
        print('\n%s получил от %s %s урона, состояние здоровья %s\n\n' % (
        self.name, who, damage // self.armor, self.state))

    def doDamage(self, person):
        damage = self.attack * random.choice(range(80, 150)) // 100
        person.takeDamage(damage, self.name)

    def death(self):
        print('\n\n%s убит\n' % (self.name))
        player.increase()


class Strong_Bandit(Bandit):
    def __init__(self, name, attack, armor):
        Bandit.__init__(self, name, attack, armor, health=90, hp=90)

    def takeDamage(self, damage, who, resist=80):
        Bandit.takeDamage(self, damage * resist // 100, who)

    def doDamage(self, person):
        damage = self.attack * random.choice(range(80, 150)) // 80
        person.takeDamage(damage, self.name)


class Boss(Bandit):
    def __init__(self, name, attack, armor):
        Bandit.__init__(self, name, attack, armor, health=200, hp=200)

    def takeDamage(self, damage, who, resist=60):
        Bandit.takeDamage(self, damage * resist // 100, who)

    def doDamage(self, person):
        damage = self.attack * random.choice(range(80, 150)) // 60
        person.takeDamage(damage, self.name)


class Enemys:
    def __init__(self, *args):
        self.enemys = list(args)

    def addEnemy(self, enemy):
        self.enemys.append(enemy)

    def deleteEnemy(self, enemy):
        self.enemys.remove(enemy)

    def view(self):
        for enemy in self.enemys:
            print(enemy)


class Weapon():
    def __init__(self, name, damage, cost):
        self.name = name
        self.damage = damage
        self.cost = cost

    def __repr__(self):
        result = ''
        for attr in self.__dict__:
            result += '%s=%s\n' % (attr, self.__dict__[attr])
        return result


class Armor():
    def __init__(self, name, armor, cost):
        self.name = name
        self.armor = armor
        self.cost = cost

    def __repr__(self):
        result = ''
        for attr in self.__dict__:
            result += '%s=%s\n' % (attr, self.__dict__[attr])
        return result


class Shop():
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        print('\n\n\n--------------ТОВАРЫ В МАГАЗИНЕ---------------\n')
        result = ''
        for x in enumerate(shop.args):
            result += ('\n---%s---\n%s' % (x[0], x[1]))
        return result + '\nКаждое зелье лечения [hp_bottle] стоит 100$. Зелья лечения возврату или обмену не подлежат.\nВаши деньги %s$\n-----------\nДля покупки оружия или брони введите:[buy №], где № - номер товара в списке\nДля покупки зелея лечения введите:[buy bottle]\nДля продажи своего оружия введите:[sell weapon]\nдля продажи своей брони введите:[sell defence]\n-----------\n\n' % (
            player.money)


class Player(Print):
    def __init__(self, attack=10, armor=4, health=70, hp=70, exp=0, level=1, money=500, weapon='[fist]', defence=None,
                 hp_bottle=1):
        self.attack = attack
        self.armor = armor
        self.health = health
        self.hp = hp
        self.exp = exp
        self.level = level
        self.money = money
        self.weapon = weapon
        self.defence = defence
        self.hp_bottle = hp_bottle

    def buy(self, arg):
        if arg.name.split('_')[1] == 'Armor]':
            self.takeArmor(arg)
        else:
            self.takeWeapon(arg)

    def takeWeapon(self, weapon):
        if self.money >= weapon.cost:
            self.money = self.money - weapon.cost
            self.attack = 10 + weapon.damage
            self.weapon = weapon.name
            print(
                '\nВы купили %s за %s$, он отлично ложится в Вашу руку. Денег осталось %s$.\nВаша аттака теперь равна %s\n' % (
                weapon.name, weapon.cost, self.money, self.attack))
        else:
            if self.money <= weapon.cost:
                print('\nНе хватает денег. Есть %s$ надо %s$\n' % (self.money, weapon.cost))

    def takeArmor(self, armor):
        if self.money >= armor.cost:
            self.money = self.money - armor.cost
            self.armor = 5 + armor.armor
            self.defence = armor.name
            print('\nВы купили %s за %s$, как раз Ваш размер. Денег осталось %s$.\nВаша защита теперь равна %s\n' % (
            armor.name, armor.cost, self.money, self.armor))
        else:
            if self.money < armor.cost:
                print('\nНе хватает денег. Есть %s$ надо %s$\n' % (self.money, armor.cost))

    def takeHpBottle(self):
        if self.money >= 100:
            self.money = self.money - 100
            self.hp_bottle = self.hp_bottle + 1
            print('\nВы купили зелье лечения за 100$. Теперь у Вас их %s\n' % (self.hp_bottle))
        else:
            print('\nНа покупку зелья лечения не хватает денег. У Вас осталось всего %s$\n' % (self.money))

    def healself(self):
        if self.hp_bottle > 0:
            if self.hp < self.health:
                self.hp = self.hp + 50
                self.hp_bottle = self.hp_bottle - 1
                if self.hp > self.health:
                    self.hp = self.health
                print(
                    '\nВы используете зелье лечения. Дышать становится заметно лучше. Ваше здоровье = %s. Банок лечения осталось %s\n' % (
                    self.hp, self.hp_bottle))
            else:
                self.hp_bottle = self.hp_bottle - 1
                print(
                    '\nВы использовали лечение. Ваше здоровье и без того было полным.\nВаше здоровье = %s. Зелей осталось %s\n' % (
                    self.hp, self.hp_bottle))
        else:
            print(
                '\nВы пытаетесь использовать зелье лечения, но не находите его в своем инвентаре. Очка действия потеряно.\n')

    def sellWeapon(self):
        if self.weapon == 'fist':
            print('\nУ Вас нету оружия на продажу\n')
        for arg in shop.args:
            if arg.name == self.weapon:
                self.money = self.money + arg.cost * 80 // 100
                self.attack = self.attack - arg.damage
                self.weapon = 'fist'
                print('\nВы продали свой %s за %s$ - 80 процентов начальной стоимости. Денег осталось %s$\n' % (
                arg.name, arg.cost * 70 // 100, self.money))

    def sellArmor(self):
        if self.defence == None:
            print('\nУ Вас нету брони на продажу\n')
        for arg in shop.args:
            if arg.name == self.defence:
                self.money = self.money + arg.cost * 80 // 100
                self.armor = self.armor - arg.armor
                self.defence = None
                print('\nВы продали свой %s за %s$ - 80 процентов начальной стоимости. Денег осталось %s$\n' % (
                arg.name, arg.cost * 70 // 100, self.money))

    def takeDamage(self, damage, who):
        self.hp = self.hp - damage // self.armor
        print('\nВы получили %s урона от %s. Ваше здоровье = %s' % (damage // self.armor, who, self.hp))
        if (self.hp * 100 // self.health) < 70 and (self.hp * 100 // self.health) > 25:
            print('\nИз ваших ран обильно течет кровь\n')
        if (self.hp * 100 // self.health) <= 25:
            print(
                'От полученых повреждений мутнеет в голове. Вы чувствуете как Смерть где то рядом звенит своей ржавой косой\n\n')
        if self.hp <= 0:
            self.death()

    def doDamage(self, person):
        damage = self.attack * random.choice(range(80, 150)) // 100
        person.takeDamage(damage, self.__class__.__name__)

    def increase(self):
        money = random.choice(range(20, 30))
        exp = random.choice(range(51, 70))
        self.money = self.money + money
        self.exp = self.exp + exp
        print('Обыскав труп вы находите %s$. За убийство врага Вы получаете %s опыта.' % (money, exp))
        self.levelup()

    def levelup(self):
        if self.exp >= 100 and self.level < 2:
            self.level = 2
            self.attack += 5
            self.armor += 2
            self.health += 10
            print(
                '\n\n--------------------------------------LEVEL UP (%s)-------------------------------------\n\nПолучено необходимое количество опыта - %s. Вы достигаете уровня %s. Характеристики персонажа увеличены.\n\n' % (
                self.level, self.exp, self.level))
            sleep(2)
        if self.exp >= 300 and self.level < 3:
            self.level = 3
            self.attack += 5
            self.armor += 2
            self.health += 10
            print(
                '\n\n--------------------------------------LEVEL UP (%s)-------------------------------------\n\nПолучено необходимое количество опыта - %s. Вы достигаете уровня %s. Характеристики персонажа увеличены.\n\n' % (
                self.level, self.exp, self.level))

    def death(self):
        print(
            '\n\n\n\n---------------------------------------YOU DIE-------------------------------------\n\n\n\n...На этом Ваше преключение заканчивается. Бандиты так и остануться без заслуженного наказания. Стервятники на деверьях у входа в логово будут весьма рады такому повороту событий...')
        key = input('\n\n\nВас убили. Нажмите любую клавишу:')
        if len(key) >= 0:
            print(
                '\n\n\n\n\n--------------------------------------GAME OVER-------------------------------------\n\n\n\nGame created by (с)Woobinda\nContact - woobinda@voliacable.com\n\n')
            sleep(2)
            exit()


if __name__ == '__main__':
    player = Player()
    Pistol_6mm = Weapon('[Pistol_6mm]', random.choice(range(30, 50)), random.choice(range(100, 200)))
    Hunter_Rife = Weapon('[Hunter_Rife]', random.choice(range(50, 80)), random.choice(range(200, 300)))
    Plazma_Rife = Weapon('[Plazma_Rife]', random.choice(range(80, 110)), random.choice(range(300, 400)))
    Gauss_Rife = Weapon('[Gauss_Rife]', random.choice(range(130, 160)), random.choice(range(400, 500)))
    TECH_Weapon = Weapon('[HI-TECH_Weapon]', random.choice(range(180, 220)), random.choice(range(700, 900)))
    Light_Armor = Armor('[Light_Armor]', random.choice(range(4, 6)), random.choice(range(100, 200)))
    Advanced_Armor = Armor('[Advanced_Armor]', random.choice(range(6, 8)), random.choice(range(200, 300)))
    Heavy_Armor = Armor('[Heavy_Armor]', random.choice(range(9, 11)), random.choice(range(300, 400)))
    Titanium_Armor = Armor('[Titanium_Armor]', random.choice(range(12, 14)), random.choice(range(400, 500)))
    TECH_Armor = Armor('[HI-TECH_Armor]', random.choice(range(18, 22)), random.choice(range(700, 900)))
    shop = Shop(Pistol_6mm, Hunter_Rife, Plazma_Rife, Gauss_Rife, TECH_Weapon, Light_Armor, Advanced_Armor, Heavy_Armor,
                Titanium_Armor, TECH_Armor)

    print(
        '\n\n\n--------------------------------------START GAME-------------------------------------\n\n\n\nВаш персонаж обладает характеристиками:\n[armor] - защита, уменьшает количество получаемых Вами повреждений\n[attack] - аттака, влияет на количество наносимого Вами урона\n[exp] - опыт, полученный за убийство врагов\n[health] - максимальное количество здоровья персонажа\n[hp] - текущее здоровье персонажа\n[level] - уроень персонажа, повышается при необходимом количестве опыта exp. При повышении уровня персонаж повышает характеристики.\n\nСлоты аммуниции:\n[money] - деньги($), необходимые для совершения покупок в магазине\n[weapon]- используемое персонажем оружие\n[defence] - надетая на персонажа броня\n[hp_bottle] - количество целебных зелей. Каждое зелье востанавливает персонажу 50 здоровья\n\n')
    sleep(2)
    key = input('\n\n\nЧтобы продолжить. Нажмите любую клавишу:')
    if len(key) >= 0:
        print('\nНа этом наш рассказ начинается...\n\n\n\n')
        sleep(2)
    print(
        ' ...Вы спускаетесь с небольшого пригорка и видите перед собой полуразрушенный дом. Это подходит под описания логова ублюдков, о котором Сью говорила в таверне. Оторвать им головы...и забрать деньги...Лучшее что эти парни заслужили...Но как говорил мой дед - кто понял жизнь тот не торопится. Тем более с голыми руками лезть туда явно самоубийство. Не плохо бы сначала заглянуть в ближайшую лавку торговца, там у них в последнее время полно оружия, а у меня как раз вроде осталось пару долларов...\n')
    sleep(2)
    key = input('\n\n\nЧтобы продолжить. Нажмите любую клавишу:')
    if len(key) >= 0:
        print(
            '\n\n\n\n Для покупки первичного снаряжения посетите магазин. Продажа товаров обратно в магазин осуществляется по 80% от начальной стоимости. Для экономии денег, перед покупкой нового оружия или брони рекомендуется продать старые. Для просмотра характеристик и надетой на персонажа аммуниции войдите в режим просмотра персонажа - [v].\n\n   ...Вы приближаетесь к таверне. На вид здание представляет из себя добротное сооружение из бревен и камня. Кажется что звон бокалов и хохот местных завсегдатаев появились тут вместе с заложенным фундаментом. Таверна - лучшее место где чтобы продумать свои планы. Чтобы войти в таверну введите в стоке ввода букву, которая находится в квадратных скобках - [t]\n\n\n')
        sleep(2)


    def final():
        money = random.choice(list(range(350, 600)))
        player.money = player.money + money
        key = input('\n\n\nВ это сложно верится но толстяк мертв. Нажмите любую клавишу:')
        if len(key) >= 0:
            print(
                '\n\n\n\n***************************************************************************\n\n\n\n  ...Последнии пули приходятся толстяку в голову. Его огроммная туша оседает по стене, оставляя красные полосы. Надо все хорошенько осмотреть. В углу зала вы находите сейф...')
            sleep(2)
            print('\n\n ...Это явно того стоило...Обыскав сейф вы находите %s$. Теперь у Вас %s$.\n\n' % (
            money, player.money))
            sleep(2)
            print(
                ' ...С такими деньгами можно начинать планировать более крупную операцию. Вы берете с пепельницы не докуреную сигару, делаете затяжку и заговорчески улыбаетесь и направляетесь в сторону таверны...\n')
            sleep(2)
            key = input('\n\n\nНа этом наш рассказ завершается. Нажмите любую клавишу:')
            if len(key) >= 0:
                print(
                    '\n\n\n\n*************************************THE END***************************************\n\n\nСпасибо что играли :)\n\n')
                print('Game created by (с)Woobinda\nContact - woobinda@voliacable.com\n\n')
                sleep(2)
                exit()


    def battle(points):
        if len(enemys.enemys) == 0:
            key = input('\n\n\nВы убили последнего врага. Нажмите любую клавишу:')
            if len(key) >= 0:
                money = random.choice(list(range(100, 150)))
                player.money = player.money + money
                player.hp = player.health
                print(
                    '\n\n\n\n************************************************************************\n\n\n\n ...Ваши враги валяются на земле в лужах крови и гноя. Вы переводите дыхание и обыскиваете сумку одного из убитых.')
                print('Вы находите %s$ бонусных денег. Денег всего %s$.\n' % (money, player.money))
                sleep(2)
                print(
                    ' ...Не плохо бы передохнуть, прежде чем двинуться дальше. Вы возвращаетесь в таверну и сразу же поднявшись в свой номер придаетесь крепкому сну.\nЗдоровье персонажа полностью востановленно.\n\n\n')
            tavern()
        if points == 0:
            print('\n***********\nУ Вас закончились очки действия, нажмите [end] для передачи хода противнику.\n')
            sleep(1)
        choice = input('\nДля просмотра доступных действий нажмите [h]elp. Ваше действие:')
        if choice == 'h':
            print(
                '\n\n[v]iev - просмотр персонажа\n[e]nemy - просмотр врагов\n[a]ttack [№] - аттака врага, где № - номер врага\n[bottle] - использовать зелье лечения\n[end] - передача хода\n[q]uit - выйти из игры\n\n')
        if choice == 'q':
            print(
                '\n\n\n\n--------------------------------------GAME OVER-------------------------------------\n\n\n\nGame created by (с)Woobinda\nContact - woobinda@voliacable.com\n\n')
            sleep(2)
            exit()
        if choice == 'v':
            print(player)
        if choice == 'e':
            for x in enumerate(enemys.enemys):
                print('                (%s)              \n\n%s' % (x[0], x[1]))
        if len(choice) == 3 and choice.split()[0] == 'a':
            if points == 0:
                print('\n')
            else:
                try:
                    number = int(choice.split()[1])
                except ValueError:
                    return tavern()
                try:
                    enemys.enemys[number]
                except IndexError:
                    return battle(points)
                sleep(1)
                player.doDamage(enemys.enemys[number])
                sleep(1)
                points -= 1
                for enemy in enemys.enemys:
                    if enemy.name == 'Evil Boss' and enemy.state == '[МЕРТВ]':
                        final()
                    if enemy.state == '[МЕРТВ]':
                        enemys.deleteEnemy(enemy)
                else:
                    return battle(points)
        if choice == 'end':
            for enemy in enemys.enemys:
                enemy.doDamage(player)
                sleep(2)
            return battle(3)
        if choice == 'bottle':
            if points == 0:
                print('\n')
            else:
                player.healself()
                sleep(2)
                points -= 1
        return battle(points)


    def tavern():
        menulist = '\n\n[v]iev - просмотр персонажа\n[s]hop - зайти в магазин\n[b]attle - войти в бандитское логово\n[q]uit - выйти из игры\n\n'
        choice = input('\nДля возврата в таверну нажмите [t]avern. Ваше действие:')
        if choice == 't':
            print(menulist)
        if choice == 'v':
            print(player)
        if choice == 's':
            print(
                '\n\nЗавидив Вас, старый робот - хозяин магазина начинает смахивать пыль с залежавшегося товара\n\n\n-Вы только посмотрите на мои новейшие разработки!')
            sleep(2)
            print(shop)
        if choice == 'sell weapon':
            player.sellWeapon()
        if choice == 'sell defence':
            player.sellArmor()
        if choice == 'buy bottle':
            player.takeHpBottle()
        if choice == 'q':
            print(
                '\n\n\n\n--------------------------------------GAME OVER-------------------------------------\n\n\n\nGame created by (с)Woobinda\nContact - woobinda@voliacable.com\n\n')
            sleep(2)
            exit()
        if len(choice) == 5:
            if choice.split()[0] == 'buy':
                try:
                    number = int(choice.split()[1])
                except ValueError:
                    return tavern()
                try:
                    shop.args[number]
                except IndexError:
                    return tavern()
                player.buy(shop.args[number])
        if choice == 'b':
            if player.level == 1:
                print(
                    '\n\n ...Вы осторожно подкрадываетесь к полуразрушенному зданию, входные двери на удивление не заперты. Складывается чувство что кто то приготовил для Вас ловушку. Вы проходите пару коридоров и видете из за угла двух бандитов. Еще не поздно повернуть назад...\n\n[any key] - нажмите любую клавишу, чтобы вернутся в таверну\n[b]attle - напасть\n')
                sleep(2)
                choice = input('Какими будут Ваши дальнейшие действия?:')
                if choice == 'b':
                    global enemys
                    enemys = Enemys()
                    Bandit1 = Bandit('Bandit1', random.choice(range(60, 90)), random.choice(range(5, 10)))
                    Bandit2 = Bandit('Bandit2', random.choice(range(60, 90)), random.choice(range(5, 10)))
                    enemys.addEnemy(Bandit1)
                    enemys.addEnemy(Bandit2)
                    print(
                        '\n\n\n\n--------------------------------------BATTLE-------------------------------------\n\n\n  ...Вы выходите из своего укрытия, эти два бандита явно не ожидали гостей, разобраться с ними не составит труда.\n\n"""\nВ течение боя, в зависимости от нанесенных вами повреждений, состояние здоровья противников меняется от [ЗДОРОВ] до [МЕРТВ]. Чем ближе враг к смерти, тем хуже его состояние здоровья. Если [hp] Вашего персонажа опустится до 0, персонаж умрет, используйте зелья лечения, чтобы не допустить этого. В течение одного хода персонаж имеет 3 очка действия. За одно очко действия можно либо провести аттаку по врагу, либо использовать зелье лечения. Когда очков действий не останится, необходимо окончить ход командой [end], после чего будет ходить противник. С начала следующего хода у Вас будет опять 3 очка действий.\n"""\n\nНапомним что наносимый вами урон зависит от величены показателя [attack] Вашего персонажа, а получаемый персонажем урон от показателя [armor]. Для просмотра персонажа введите [v]iew.\n\n\n----------Список доступных действий. Для вызова этого списка введите [h]elp---------\n\n[v]iev - просмотр персонажа\n[e]nemy - просмотр врагов\n[a]ttack [№] - аттака врага, где № - номер врага\n[bottle] - использовать зелье лечения\n[end] - передача хода\n[q]uit - выйти из игры\n\nДля начала боя выведите список врагов [e]nemy и аттакуйте противника введя [a №], где № - номер противника из списка.\n\n')
                    sleep(2)
                    battle(3)
            if player.level == 2:
                print(
                    '\n\n ...Вы пробираетесь еще глубже и поднимаетесь на следующий этаж. Вы видите перед собой двух типичных разбойников и огромнного здоровяка. Наверное ищут виновника недавно найденых трупов. Один из них выглядит особо опасным, может не стоит показыватся им на глаза...\n\n[any key] - нажмите любую клавишу, чтобы вернутся в таверну\n[b]attle - напасть\n')
                sleep(2)
                choice = input('Какими будут Ваши дальнейшие действия?:')
                if choice == 't':
                    tavern()
                if choice == 'b':
                    global enemys1
                    enemys1 = Enemys()
                    Bandit1 = Bandit('Bandit1', random.choice(range(80, 100)), random.choice(range(8, 12)))
                    Bandit2 = Bandit('Bandit2', random.choice(range(100, 120)), random.choice(range(7, 10)))
                    Bandit3 = Strong_Bandit('Strong Bandit', random.choice(range(120, 150)), random.choice(range(6, 9)))
                    enemys1.addEnemy(Bandit1)
                    enemys1.addEnemy(Bandit2)
                    enemys1.addEnemy(Bandit3)
                    print(
                        '\n\n\n\n--------------------------------------BATTLE-------------------------------------\n\n\n  ...Вы задерживаете дыхание и готовитесь аттаковать как только наступит удачный момент\n\n')
                    sleep(2)
                    battle(3)
            if player.level == 3:
                print(
                    '\n\n ...Вы уже с легкостью ориентируетесь в этом лабиринте коридоров. И подходите к недавно запримеченной стальной двери. В дверной глазок видно сидящего в кресле толстяка, он явно тут главный...Хотя он и не может Вас видеть, складывается впечатление что он готов к вашему приходу. Возможно стоит вернутся когда он будет менее насторожен...\n\n[any key] - нажмите любую клавишу, чтобы вернутся в таверну\n[b]attle - напасть\n')
                choice = input('Ваши действия:')
                if choice == 't':
                    tavern()
                if choice == 'b':
                    global enemys2
                    enemys2 = Enemys()
                    EvilBoss = Boss('Evil Boss', random.choice(range(180, 220)), random.choice(range(6, 8)))
                    enemys2.addEnemy(EvilBoss)
                    print(
                        '\n\n\n\n--------------------------------------BATTLE-------------------------------------\n\n\n  ...Вы внезапно распахиваете дверь и аттакуете толстяка.\n\n')
                    sleep(2)
                    battle(3)
        return tavern()


    tavern()