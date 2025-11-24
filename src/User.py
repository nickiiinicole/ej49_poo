class User: 
    # el numero de tarjeta sigue el la formual de Luhn
    def __init__(self,name,username,password, card_number):
        self.name= name
        self.username= username
        self.password= password
        self.card_number= card_number



    def check_sum(self):
        '''La fórmula de Lunh'''
        if len(self.card_number)<=1 : 
            raise
        
    