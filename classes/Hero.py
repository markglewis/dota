import json
class Hero:
    def __init__(self,name):
        self.name= name
        data = {}
        with open('7.32e.json') as json_file:
            data = json.load(json_file)[name]
        print(data)
        self.roles= data['roles']
        self.ba = data['ba']
        self.ga = data['ga']
        self.gw = data['gw']
        self.bw = data['bw']
        self.score = 0
        self.ispicked = False
        self.isbanned = False
        self.str = float(data['Base strength'])
        self.strg = float(data['Strength growth per level'])
        self.str30 = float(data['Total strength at level 30 (no bonus)'])
        self.agi = float(data['Base agility'])
        self.agig = float(data['Agility growth per level'])
        self.agi30 = float(data['Total agility at level 30 (no bonus)'])
        self.int = float(data['Base intelligence'])
        self.intg = float(data['Intelligence growth per level'])
        self.int30 = float(data['Total intelligence at level 30 (no bonus)'])
        self.primaryA = None
        if self.strg > self.agig and self.strg>self.intg:
            self.primaryA = "strength"
        elif self.agig > self.strg and self.agig>self.intg:
            self.primaryA = "agility"
        elif self.intg > self.strg and self.intg>self.agig:
            self.primaryA = "intelligence"
        self.tsa = float(data['Total starting attributes'])
        self.tsag = float(data['Total attribute growth per level'])
        self.tsa30 = float(data['Total attributes at level 30 (no bonus)'])
        self.ms = float(data['Base movement speed'])
        self.sar = float(data['Starting armor'])
        self.dmgmax = float(data['Starting attack damage'])
        self.dmgmin = None
        self.ar = float(data['Attack range'])
        self.attkSpd = float(data['Attack speed'])
        self.bat = float(data['Base attack time'])
        self.atkpt = float(data['Attack point'])
        self.atkbs = float(data['Attack backswing'])
        self.vsd = float(data['Vision range during daytime'])
        self.vsn = float(data['Vision range during nighttime'])
        self.tr = float(data['Turn rate'])
        self.col = float(data['Collision size'])
        self.hps = float(data['Base health regeneration'])
        self.mps = float(data['Base mana regeneration'])
        self.legs = float(data['Legs'])

    
    def __str__(self):
        outString = ""
        outString += self.name + "\n"
        outString += "Roles: " + " ,".join(self.roles) + "\n"
        outString += "bad against: " + " ,".join(self.ba) + "\n"
        outString += "good against: " + " ,".join(self.ga) + "\n"
        outString += "good with: " + " ,".join(self.gw) + "\n"
        outString += "bad with: " + " ,".join(self.bw) + "\n"

        return outString
    
    def reset(self):
        self.score = 0
        self.ispicked = False
        self.isbanned = False
    
    def picked(self):
        self.ispicked = True
    
    def banned(self):
        self.isbanned = True