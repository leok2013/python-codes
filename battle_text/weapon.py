# ------------ class setup ------------
class Weapon:
    def __init__(self,
                 name: str,
                 weapon_type: str,
                 damage: int,
                 value: int
                 ) -> None:
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value


# ------------ object creation ------------
iron_sword = Weapon(name="Iron Sword",
                    weapon_type="sharp",
                    damage=5,
                    value=10)

short_bow = Weapon(name="Short Bow",
                   weapon_type="ranged",
                   damage=4,
                   value=8)

fists = Weapon(name="Fists",
               weapon_type="blunt",
               damage=2,
               value=0)

sigma_aura = Weapon(name="Sigma Aura",
               weapon_type="magical",
               damage=20,
               value=90)

desert_eagle = Weapon(name="Desert Eagle",
               weapon_type="Gun",
               damage=15,
               value=50)

driver = Weapon(name="Drunk driver in a shcool zone",
               weapon_type="insanity",
               damage=100000000000000000000,
               value=100000000000000000000)

ar_15 = Weapon(name="ar-15 automatic rifle ",
               weapon_type="gun",
               damage=80,
               value=15)

haha = Weapon(name="saying the enemy is a kim kardasian simp ",
               weapon_type="crowd summon",
               damage=1500,
               value=0)