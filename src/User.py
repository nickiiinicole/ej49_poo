import Gamin_exception 
class User: 
    # el numero de tarjeta sigue el la formual de Luhn
    def __init__(self,name,username,password, card_number):
        self.name= name
        self.username= username
        self.password= password
        self.card_number= card_number



    def check_sum(self):
        '''La fórmula de Lunh'''
        if len(self.card_number.strip())<=1 and not self.card_number.isdigit() : 
            raise Gamin_exception
        
        digits_odd = self.card_number[::2]
        digits_odd = [int(digit) for digit in digits_odd]
        digits_odd = [digit*2 for digit in digits_odd]
        
        for digit in digits_odd:
            if digit>9:
                digit-=9
        
        if digits_odd.sum()%10 ==0 :
            return digits_odd
        else: 
            raise Gamin_exception

        

