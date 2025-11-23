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
        if len(self.card_number.strip())<13 or not self.card_number.isdigit() : 
            raise Gamin_exception("Invalid card number")
        
        # digits_odd = self.card_number[::2]
        # digits_odd = [int(digit) for digit in digits_odd]
        # digits_odd = [digit*2 for digit in digits_odd]
        # hacerlo en una linea 
        digits_odd = [int(digit) * 2 for digit in self.card_number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in self.card_number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits%10 ==0 :
            return True
        else: 
            raise Gamin_exception("ERROR, INVALID COMPROBATION LUHN:/// ")

        

