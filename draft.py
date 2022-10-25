from classes.Hero import Hero
import sys

HEROSK = {
    **dict.fromkeys(["abaddon"], "Abaddon"),
    **dict.fromkeys(["alchemist", "alch"], "Alchemist"),
    **dict.fromkeys(["axe"], "Axe"),
    **dict.fromkeys(["beastmaster"], "Beastmaster"),
    **dict.fromkeys(["brewmaster", "brew"], "Brewmaster"),
    **dict.fromkeys(["bb", "bristleback"], "Bristleback"),
    **dict.fromkeys(["ck", "chaosknight"], "Chaos_Knight"),
    **dict.fromkeys(["clockwerk", "clock"], "Clockwerk"),
    **dict.fromkeys(["dawnbreaker"], "Dawnbreaker"),
    **dict.fromkeys(["doom"], "Doom"),
    **dict.fromkeys(["dragonknight", "dk"], "Dragon_Knight"),
    **dict.fromkeys(["earthspirit"], "Earth_Spirit"),
    **dict.fromkeys(["earthshaker"], "Earthshaker"),
    **dict.fromkeys(["eldertitan", "et"], "Elder_Titan"),
    **dict.fromkeys(["huskar"], "Huskar"),
    **dict.fromkeys(["io", "wisp"], "Io"),
    **dict.fromkeys(["kunkka"], "Kunkka"),
    **dict.fromkeys(["legioncommander", "lc","legion"], "Legion_Commander"),
    **dict.fromkeys(["lifestealer", "lf"], "Lifestealer"),
    **dict.fromkeys(["lycan"], "Lycan"),
    **dict.fromkeys(["magnus"], "Magnus"),
    **dict.fromkeys(["marci"], "Marci"),
    **dict.fromkeys(["mars"], "Mars"),
    **dict.fromkeys(["nightstalker", "ns"], "Night_Stalker"),
    **dict.fromkeys(["omniknight"], "Omniknight"),
    **dict.fromkeys(["phoenix"], "Phoenix"),
    **dict.fromkeys(["primalbeast", "primal"], "Primal_Beast"),
    **dict.fromkeys(["pudge"], "Pudge"),
    **dict.fromkeys(["sandking", "sk"], "Sand_King"),
    **dict.fromkeys(["slardar"], "Slardar"),
    **dict.fromkeys(["snapfire", "snap"], "Snapfire"),
    **dict.fromkeys(["spiritbreaker", "sb"], "Spirit_Breaker"),
    **dict.fromkeys(["sven"], "Sven"),
    **dict.fromkeys(["tidehunter"], "Tidehunter"),
    **dict.fromkeys(["timbersaw"], "Timbersaw"),
    **dict.fromkeys(["tiny"], "Tiny"),
    **dict.fromkeys(["treantprotector"], "Treant_Protector"),
    **dict.fromkeys(["tusk"], "Tusk"),
    **dict.fromkeys(["underlord"], "Underlord"),
    **dict.fromkeys(["undying"], "Undying"),
    **dict.fromkeys(["wraithking", "wk"], "Wraith_King"),
    **dict.fromkeys(["antimage", "am"], "Anti-Mage"),
    **dict.fromkeys(["arcwarden"], "Arc_Warden"),
    **dict.fromkeys(["bloodseeker", "bs"], "Bloodseeker"),
    **dict.fromkeys(["bountyhunter", "bh"], "Bounty_Hunter"),
    **dict.fromkeys(["broodmother"], "Broodmother"),
    **dict.fromkeys(["clinkz"], "Clinkz"),
    **dict.fromkeys(["drowranger", "drow"], "Drow_Ranger"),
    **dict.fromkeys(["emberspirit"], "Ember_Spirit"),
    **dict.fromkeys(["facelessvoid"], "Faceless_Void"),
    **dict.fromkeys(["gyrocopter", "gyro"], "Gyrocopter"),
    **dict.fromkeys(["hoodwink"], "Hoodwink"),
    **dict.fromkeys(["juggernaut", "jugg"], "Juggernaut"),
    **dict.fromkeys(["lonedruid", "ld"], "Lone_Druid"),
    **dict.fromkeys(["luna"], "Luna"),
    **dict.fromkeys(["medusa"], "Medusa"),
    **dict.fromkeys(["meepo"], "Meepo"),
    **dict.fromkeys(["mirana"], "Mirana"),
    **dict.fromkeys(["monkeyking", "mk"], "Monkey_King"),
    **dict.fromkeys(["morphling", "morph"], "Morphling"),
    **dict.fromkeys(["nagasiren", "naga"], "Naga_Siren"),
    **dict.fromkeys(["nyxassassin", "nyx"], "Nyx_Assassin"),
    **dict.fromkeys(["pangolier", "pango"], "Pangolier"),
    **dict.fromkeys(["phantomassassin", "pa"], "Phantom_Assassin"),
    **dict.fromkeys(["phantomlancer", "pl"], "Phantom_Lancer"),
    **dict.fromkeys(["razor"], "Razor"),
    **dict.fromkeys(["riki"], "Riki"),
    **dict.fromkeys(["shadowfiend", "sf"], "Shadow_Fiend"),
    **dict.fromkeys(["slark"], "Slark"),
    **dict.fromkeys(["sniper"], "Sniper"),
    **dict.fromkeys(["spectre"], "Spectre"),
    **dict.fromkeys(["templarassassin", "ta","templar"], "Templar_Assassin"),
    **dict.fromkeys(["terrorblade"], "Terrorblade"),
    **dict.fromkeys(["trollwarlord", "troll"], "Troll_Warlord"),
    **dict.fromkeys(["ursa"], "Ursa"),
    **dict.fromkeys(["vengefulspirit", "venge"], "Vengeful_Spirit"),
    **dict.fromkeys(["venomancer"], "Venomancer"),
    **dict.fromkeys(["viper"], "Viper"),
    **dict.fromkeys(["weaver"], "Weaver"),
    **dict.fromkeys(["ancientapparition", "aa"], "Ancient_Apparition"),
    **dict.fromkeys(["bane"], "Bane"),
    **dict.fromkeys(["batrider"], "Batrider"),
    **dict.fromkeys(["chen"], "Chen"),
    **dict.fromkeys(["crystalmaiden", "cm"], "Crystal_Maiden"),
    **dict.fromkeys(["darkseer"], "Dark_Seer"),
    **dict.fromkeys(["dark_willow"], "Dark_Willow"),
    **dict.fromkeys(["dazzle"], "Dazzle"),
    **dict.fromkeys(["deathprophet", "dp"], "Death_Prophet"),
    **dict.fromkeys(["disruptor"], "Disruptor"),
    **dict.fromkeys(["enchantress", "ench"], "Enchantress"),
    **dict.fromkeys(["enigma", "nigma"], "Enigma"),
    **dict.fromkeys(["grimstroke"], "Grimstroke"),
    **dict.fromkeys(["invoker", "carl"], "Invoker"),
    **dict.fromkeys(["jakiro"], "Jakiro"),
    **dict.fromkeys(["keeperofthelight", "kotl"], "Keeper_of_the_Light"),
    **dict.fromkeys(["leshrac", "lesh"], "Leshrac"),
    **dict.fromkeys(["lich"], "Lich"),
    **dict.fromkeys(["lina"], "Lina"),
    **dict.fromkeys(["lion"], "Lion"),
    **dict.fromkeys(["naturesprophet", "np"], "Nature's_Prophet"),
    **dict.fromkeys(["necrophos", "necro"], "Necrophos"),
    **dict.fromkeys(["ogremagi", "ogre"], "Ogre_Magi"),
    **dict.fromkeys(["oracle"], "Oracle"),
    **dict.fromkeys(["outworlddestroyer", "od"], "Outworld_Destroyer"),
    **dict.fromkeys(["puck"], "Puck"),
    **dict.fromkeys(["pugna"], "Pugna"),
    **dict.fromkeys(["queenofpaion", "qop"], "Queen_of_Pain"),
    **dict.fromkeys(["rubick"], "Rubick"),
    **dict.fromkeys(["shadowdemon", "sd"], "Shadow_Demon"),
    **dict.fromkeys(["shadowshaman", "ss","shaman"], "Shadow_Shaman"),
    **dict.fromkeys(["silencer"], "Silencer"),
    **dict.fromkeys(["skywrathmage", "sky"], "Skywrath_Mage"),
    **dict.fromkeys(["stormspirit", "storm"], "Storm_Spirit"),
    **dict.fromkeys(["techies"], "Techies"),
    **dict.fromkeys(["tinker"], "Tinker"),
    **dict.fromkeys(["visage"], "Visage"),
    **dict.fromkeys(["voidspirit"], "Void_Spirit"),
    **dict.fromkeys(["Warlock"], "Warlock"),
    **dict.fromkeys(["windranger", "wr"], "Windranger"),
    **dict.fromkeys(["winterwyvern", "ww"], "Winter_Wyvern"),
    **dict.fromkeys(["withdoctor", "wd"], "Witch_Doctor"),
    **dict.fromkeys(["zeus"], "Zeus"),
}


def addenemy(pickedhero):
    heros[pickedhero].ispicked = True
    ba = heros[pickedhero].ba
    ga = heros[pickedhero].ga
    for hero in ba:
        if hero in heros:
            heros[hero].score += 2
    for hero in ga:
        if hero in heros:
            heros[hero].score -= 2

def addteamate(pickedhero):
    heros[pickedhero].ispicked = True
    gw = heros[pickedhero].gw
    for hero in gw:
        if hero in heros:
            heros[hero].score += 2

def displaybest():
    score = {}
    for key, val in heros.items():
        if not val.ispicked and not val.isbanned:
            score[key] = val.score
    score = dict(sorted(score.items(), key=lambda item: item[1]))
    print(score)

def banhero( pickedhero):
    heros[pickedhero].isbanned = True
    ga = heros[pickedhero].ga
    for hero in ga:
        if hero in heros:
            heros[hero].score += 1

def displaypicked():
    for key,value in heros.items():
        if value.ispicked:
            print(key)


def reset():
    print(heros)
    for key, val in heros.items():
        val.reset()
    


f = open("7.32.txt", "r")

heros = {}

line= f.readline()


while line:
    name = line.strip('\n')

    roles = f.readline().strip('\n').split()

    ba = f.readline().strip('\n').split()

    ga = f.readline().strip('\n').split()

    gw = f.readline().strip('\n').split()

    heros[name] = Hero(name,roles,ba,ga,gw)
    
    line=f.readline()
    line=f.readline()
f.close

userI = ""
while True:
    userI = input()
    if userI == "addenemy":
        print("Enter Hero")
        hero = input()
        if hero == "exit":
            sys.exit()
        elif hero in HEROSK.keys():
            addenemy(HEROSK[hero])
        else:
            print("hero not found")

    elif userI == "addteamate":
        print("Enter Hero")
        hero = input()
        if hero == "exit":
            sys.exit()
        elif hero in HEROSK.keys():
            addteamate(HEROSK[hero])
        else:
            print("hero not found")

    elif userI == "ban":
        print("Enter Hero")
        hero = input()
        if hero == "exit":
            sys.exit()
        elif hero in HEROSK.keys():
            banhero(HEROSK[hero])
        else:
            print("hero not found")

    elif userI == "displaypicked":
        displaypicked()
    
    elif userI == "displaybest":
        displaybest()
        

    elif userI == "reset":
        reset()

    elif userI == "help":
        print("commands")
        print("addenemy, addteamate, ban, displaypicked, displaybest, reset")

    elif userI == "exit":        
        sys.exit()

