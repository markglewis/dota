class Hero:
    def __init__(self,name,roles,ba,ga,gw,bw):
        self.name= name
        self.roles= roles
        self.ba = ba
        self.ga = ga
        self.gw = gw
        self.bw = bw
        self.score = 0
        self.ispicked = False
        self.isbanned = False
    
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