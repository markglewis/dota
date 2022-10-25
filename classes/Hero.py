class Hero:
    def __init__(self,name,roles,ba,ga,gw):
        self.name= name
        self.roles= roles
        self.ba = ba
        self.ga = ga
        self.gw = gw
        self.score = 0
        self.ispicked = False
        self.isbanned = False
    
    def reset(self):
        self.score = 0
        self.ispicked = False
        self.isbanned = False
    
    def picked(self):
        self.ispicked = True
    
    def banned(self):
        self.isbanned = True