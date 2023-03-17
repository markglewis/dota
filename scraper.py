from bs4 import BeautifulSoup
from collections import defaultdict
import requests
import json

heroesls=["Abaddon","Alchemist","Axe","Beastmaster","Brewmaster","Bristleback", "Centaur Warrunner", "Chaos Knight", "Clockwerk", "Dawnbreaker", "Doom", "Dragon Knight", "Earth Spirit", "Earthshaker", "Elder Titan", "Huskar", "Io","Kunkka", "Legion Commander", "Lifestealer", "Lycan", "Magnus", "Marci" , "Mars", "Night Stalker", "Omniknight", "Phoenix", "Primal Beast" ,"Pudge", "Sand King", "Slardar", "Snapfire", "Spirit Breaker", "Sven", "Tidehunter", "Timbersaw", "Tiny", "Treant Protector", "Tusk", "Underlord", "Undying","Wraith King","Anti-Mage", "Arc Warden", "Bloodseeker", "Bounty Hunter", "Broodmother", "Clinkz", "Drow Ranger", "Ember Spirit", "Faceless Void", "Gyrocopter", "Hoodwink", "Juggernaut", "Lone Druid", "Luna" , "Medusa", "Meepo", "Mirana", "Monkey King", "Morphling", "Naga Siren", "Nyx Assassin", "Pangolier", "Phantom Assassin", "Phantom Lancer","Razor", "Riki", "Shadow Fiend", "Slark", "Sniper", "Spectre" ,"Templar Assassin", "Terrorblade", "Troll Warlord", "Ursa", "Vengeful Spirit", "Venomancer", "Viper", "Weaver", "Ancient Apparition", "Bane", "Batrider", "Chen", "Crystal Maiden", "Dark Seer", "Dark Willow", "Dazzle", "Death Prophet", "Disruptor", "Enchantress", "Enigma", "Grimstroke", "Invoker", "Jakiro" , "Keeper of the Light", "Leshrac", "Lich", "Lina", "Lion", "Nature's Prophet", "Necrophos", "Ogre Magi", "Oracle", "Outworld Destroyer", "Puck", "Pugna", "Queen of Pain", "Rubick", "Shadow Demon", "Shadow Shaman", "Silencer", "Skywrath Mage", "Storm Spirit", "Techies", "Tinker", "Visage", "Void Spirit", "Warlock", "Windranger", "Winter Wyvern", "Witch Doctor", "Zeus","Muerta"]

baseurl = "https://dota2.fandom.com/wiki/"

out = json.loads('{}') 
for hero in heroesls:

    url = baseurl + hero.replace(" ","_")
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")

    
    if soup.find_all("div", {"class": "noarticletext mw-content-ltr"}):
        print(hero)
        print("Page Not Found")

    fRoles = soup.find('th', string="Roles:\n").parent
    fRoles = fRoles.findAll('a')
    roles = []
    for a in fRoles:
        if a.get_text() not in roles and a.get_text() != '':
            roles.append(a.get_text())
    
    
    url += "/Counters"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    content = soup.find("div", {"class": "mw-parser-output"})

    attributes = defaultdict(list)
    attributes['ba'] = []
    attributes['ga'] = []
    attributes['gw'] = []
    attributes['bw'] = []
    key = "ba"
    sections = content.find_all(['h2','b'])


    for sec in sections:
        text = sec.text
        if text == "Bad against...[]":
            key = 'ba'
        elif text == "Good against...[]":
            key = 'ga'
        elif text == "Works well with...[]":
            key = 'gw'
        elif text == "Works poorly with...[]":
            key = 'bw'
        elif text != "Contents" and text != "" and text != None:
            attributes[key].append(text.replace(" ","_"))

    
    
    attributes['roles']= roles
    temp = {hero.replace(" ","_"):attributes}
    out.update(temp)
    print(out)
  
with open("7.32e.json", "w") as outfile:
    json.dump(out,outfile)