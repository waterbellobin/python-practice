# Marine: attack, soldier, gun

# name = "Marine"
# hp = 40
# damage = 5

# print("{0} unit is built.".format(name))
# print("hp: {0}, attack: {1}\n".format(hp, damage))

# tank_name = "Tank"
# tank_hp = 150
# tank_damage = 35

# print("{0} unit is built.".format(tank_name))
# print("hp: {0}, attack: {1}\n".format(tank_hp, tank_damage))

# def attack(name, location, damage):
#     print("{0}: {1} direction attack. [damage: {2}]".format(name, location, damage))
# attack(name, "West", damage)
# attack(tank_name, "West", tank_damage)

#############################################################################

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} unit is built.".format(name))
#         print("hp: {0}, attack: {1}\n".format(hp, damage))

# # marine1 = Unit("Marine", 40, 5)
# # marine2 = Unit("Marine", 40, 5)
# # tank = Unit("Tank", 150, 35)

# wraith1 = Unit("Wraith", 80, 5)
# print("Unit name: {0}, attack: {1}".format(wraith1.name, wraith1.damage))

# wraith2 = Unit("lost Wraith", 80, 5)
# wraith2.clocking = True

# if wraith2.clocking == True:
#     print("{0} is clocking".format(wraith2.name))

#############################################################################

# class Unit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} unit is built.".format(name))
#         print("hp: {0}, attack: {1}\n".format(hp, damage))

# class AttackUnit:
#     def __init__(self, name, hp, damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} unit is built.".format(name))
#         print("hp: {0}, attack: {1}\n".format(hp, damage))

#     def attack(self, location):
#         print("{0}: {1} direction attack".format(self.name, location))  # location has no "self"

# firebat1 = AttackUnit("Firebat", 50, 16)
# firebat1.attack("East")

############################################################################

### 상속
# class Unit:
#     def __init__(self, name, hp):
#         self.name = name
#         self.hp = hp
#         print("{0} unit is built.".format(name))
        
# class AttackUnit(Unit):
#     def __init__(self, name, hp, damage):
#         Unit.__init__(self, name, hp)
#         self.damage = damage
#         print("{0} unit is built.".format(name))
#         print("hp: {0}, attack: {1}\n".format(hp, damage))

#     def attack(self, location):
#         print("{0}: {1} direction attack".format(self.name, location))  # location has no "self"

# firebat1 = AttackUnit("Firebat", 50, 16)
# firebat1.attack("East")

### 다중 상속도 있음

##########################################################################

# SUPER

# class Unit:
#     def __init__(self):
#         print("Unit made")

# class Flyable:
#     def __init__(self):
#         print("Flyable made")

# # class FlyableUnit(Unit, Flyable):
# #     def __init__(self):
# #         super().__init__() # super를 쓰려면 다중상속의 순서가 중요함

# # To use both Unit and Flyable,

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         Unit.__init__(self)
#         Flyable.__init__(self)

# dropship = FlyableUnit()

###########################################################################
