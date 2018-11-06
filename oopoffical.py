#Ali Tabba
#Object Orientated Programming Combat Game


import time             #importing necessary libraries
import random


##
class Race:
    def __init__(self, attack, speed, defense, name):   #race class
        self.attack = attack
        self.speed = speed
        self.defense = defense
        self.name = name                    #4 attributes of race class

    def returnAttack(self):
        return self.attack
    def returnSpeed(self):
        return self.speed
    def returnDefense(self):
        return self.defense
    def returnName(self):
        return self.name


class Elf(Race): #inherits from race
    def __init__(self):
        super().__init__(6,6,50, 'Elf') #(attack ,speed ,defense, name)

class Human(Race): #inherits from race
    def __init__(self):
        super().__init__(8,4,70, 'Human') #(attack ,speed ,defense, name)

class Orc(Race): #inherits from race
    def __init__(self):  #(a,s,d)
        super().__init__(10,3,90, 'Orc') #(attack ,speed ,defense, name)




##
class Weapon:
    def __init__(self, attack, speed, defense, name):
        self.weaponattack = attack
        self.weaponspeed = speed
        self.weapondefense = defense
        self.weaponname = name              #4 attributes of weapon class

    def ReturnWeaponAttack(self):
        return self.weaponattack
    def ReturnWeaponSpeed(self):
        return self.weaponspeed
    def ReturnWeaponDefense(self):
        return self.weapondefense
    def ReturnWeaponName(self):
        return self.weaponname

class SwordShield (Weapon): #inherits from weapon
    def __init__(self):
        super().__init__(1,1,10, 'SwordShield') #(attack ,speed ,defense, name)

class DualSword (Weapon):   #inherits from weapon
    def __init__(self):
        super().__init__(0,4,5, 'DualSword')    #(attack ,speed ,defense, name)

class BowArrow (Weapon):    #inherits from weapon
    def __init__(self):
        super().__init__(4,-1,-5, 'BowArrow')   #(attack ,speed ,defense, name)
    
class Gun (Weapon):         #inherits from weapon
    def __init__(self):
        super().__init__(6,-3,-10, 'Gun')        #(attack ,speed ,defense, name)



##
class CharacterClass:
    def __init__(self, attack, speed, defense, name):
        self.classattack = attack
        self.classspeed = speed
        self.classdefense = defense
        self.classname = name

    def returnClassAttack(self):
        return self.classattack
    def returnClassSpeed(self):
        return self.classspeed
    def returnClassDefense(self):
        return self.classdefense
    def returnClassName(self):
        return self.classname


class Mage(CharacterClass): #inherits from characterclass     
    def __init__(self):
        super().__init__(4,2,-5, 'Mage')             #(attack ,speed ,defense, name)

class Hunter(CharacterClass): #inherits from characterclass
    def __init__(self):
        super().__init__(4,1,0, 'Hunter')            #(attack ,speed ,defense, name)

class Druid(CharacterClass):    #inherits from characterclass
    def __init__(self):
        super().__init__(0,5,10, 'Druid')            #(attack ,speed ,defense, name)


##
class Player:

    def __init__(self, userClass, userWeapon):
        self._totalattack = 0
        self._totalspeed = 0
        self._totaldefense = 0
        self._userrace = ''
        self._userclass = userClass 
        self._userweapon = userWeapon 
            
    def chooseRace(self):
        print("""
Races:
1. Elf - Attack: 6, Speed: 6, Defense: 50
2. Human - Attack: 8, Speed: 4, Defense: 70
3. Orc - Attack: 10, Speed: 3, Defense: 90
 """)
        
        choice = input("Choose a race:")
        while choice not in ['1','2','3']:      
            choice = input("Try again. (1,2 or 3)")
        time.sleep(0.5)
        if choice == '1':
            self._userrace = Elf()
        elif choice == '2':
            self._userrace = Human()
        elif choice == '3':
            self._userrace = Orc()            

        self._totalattack += self._userrace.returnAttack() + self._userclass.returnClassAttack() + self._userweapon.ReturnWeaponAttack()
        self._totalspeed += self._userrace.returnSpeed() + self._userclass.returnClassSpeed() + self._userweapon.ReturnWeaponSpeed()
        self._totaldefense += self._userrace.returnDefense() + self._userclass.returnClassDefense() + self._userweapon.ReturnWeaponDefense()

    def printstats(self):
        print('\nYour Player is a', self._userrace.returnName(), self._userclass.returnClassName(), 'with a', self._userweapon.ReturnWeaponName())
        print('User Attack:', self._totalattack)
        print('User Speed:', self._totalspeed)
        print('User Defense:', self._totaldefense)

    



def chooseClass():
    print('Welcome to the Combat Game')
    print('Your aim is to create your player using 1 race, 1 class, and 1 weapon')
    print('Attack = Damage per attack')
    print('Speed = Attacks per second')
    print('Defense = Total Health')
    time.sleep(3)

    print("""
Classes:
1. Mage - Attack: 4, Speed: 2, Defense: -5
2. Hunter - Attack: 4, Speed: 1, Defense: 0
3. Druid - Attack: 0, Speed: 5, Defense: 10
""")
    choice = input("Choose a Class:")
    while choice not in ['1','2','3']:
        choice = input("Try again. (1,2 or 3)")
    time.sleep(0.5)
    if choice == '1':
        class_ = Mage()
    elif choice == '2':
        class_ = Hunter()
    elif choice == '3':
        class_ = Druid()
    return class_


def chooseWeapon():
    print("""
Weapons:
1. SwordShield - Attack: 1, Speed: 1, Defense: 10
2. DualSword - Attack: 0, Speed: 4, Defense: 5
3. BowArrow - Attack: 4, Speed: -1, Defense: -5
4. Gun - Attack: 6, Speed: -3, Defense: -10
""")
    choice = input("Choose a weapon:")
    while choice not in ['1','2','3','4']:
        choice = input("Try again. (1,2,3 or 4)")
    time.sleep(0.5)
    if choice == '1':
        weapon_ = SwordShield()
    elif choice == '2':
        weapon_ = DualSword()
    elif choice == '3':
        weapon_ = BowArrow()
    elif choice == '4':
        weapon_ = Gun()
    return weapon_




class Enemy:
    def __init__(self, enemyclass, enemyweapon):
        self._enemyattack = 0
        self._enemydefense = 0
        self._enemyspeed = 0
        self._enemyrace = ''
        self._enemyweapon = enemyweapon
        self._enemyclass = enemyclass

    def EnemyRace(self):
        races=[Elf(), Human(), Orc()]
        self._enemyrace = random.choice(races)

        self._enemyattack += self._enemyrace.returnAttack() + self._enemyclass.returnClassAttack() + self._enemyweapon.ReturnWeaponAttack()
        self._enemyspeed += self._enemyrace.returnSpeed() + self._enemyclass.returnClassSpeed() + self._enemyweapon.ReturnWeaponSpeed()
        self._enemydefense += self._enemyrace.returnDefense() + self._enemyclass.returnClassDefense() + self._enemyweapon.ReturnWeaponDefense()
        

    def printenemystats(self):
        print('\nGenerating a random enemy...')
        time.sleep(1)
        print('\nEnemy is:', self._enemyrace.returnName(), self._enemyclass.returnClassName(), 'with a', self._enemyweapon.ReturnWeaponName())
        print('Enemy Attack:', self._enemyattack)
        print('Enemy Speed:', self._enemyspeed)
        print('Enemy Defense:', self._enemydefense, '\n')
        time.sleep(1)

  
def enemyclass():
    classes=[Mage(), Druid(), Hunter()]
    enemyclass = random.choice(classes)
    return enemyclass       #randomly picks enemy class

def enemyweapon():
    weapons=[SwordShield(), DualSword(), BowArrow(), Gun()]
    enemyweapon = random.choice(weapons)
    return enemyweapon      #randomly picks enemy weapon


userClass=chooseClass() #gets the users class
userWeapon=chooseWeapon() #gets the users weapon

user=Player(userClass, userWeapon) #user is object of player class
user.chooseRace() #user choosses player race
user.printstats() #prints users stats


enemyclass = enemyclass() #gets enemy class
enemyweapon = enemyweapon() #gets enemy weapon

enemy=Enemy(enemyclass, enemyweapon) #aggregation takes place
enemy.EnemyRace()
enemy.printenemystats() #prints enemy stats


#Combat Section
numbers = [1,2,3,4,5]
user._totaldefense = user._totaldefense*random.choice(numbers) #randomly multiplies health of user and enemy by 1-5
enemy._enemydefense = enemy._enemydefense*random.choice(numbers) #randomly multiplies health of user and enemy by 1-5
print('New User Health:', user._totaldefense)
print('New Enemy Health:', enemy._enemydefense) #print user/enemy new healths
print('The Battle Begins...')
time.sleep(1)

while user._totaldefense >0 and enemy._enemydefense >0:
    user._totaldefense -= (enemy._enemyattack*enemy._enemyspeed) #user health - (enemy speed * enemy attack)
    enemy._enemydefense -= (user._totalattack*user._totalspeed) #enemy health - (user speed * user attack)
    print('Your Health', user._totaldefense)
    print('Enemy Health', enemy._enemydefense, '\n')
    time.sleep(1) #wait a second till the next turn
    
if user._totaldefense <0 and enemy._enemydefense <0: #if on the same turn both user and enemy health goes below 0, tie game.
    print('TIE GAME')
elif user._totaldefense >0 and enemy._enemydefense <0: 
    print('You Win!')
else:
    print('You Lose!')
    


