from  ej49.Gamin_exception import Gamin_exception
class User: 
    # el numero de tarjeta sigue el la formual de Luhn
    def __init__(self,name,username,password, card_number):
        self.name= name
        self.username= username
        self.password= password
        self.__card_number= card_number.strip()



    def check_sum(self,card_number):
        '''La fórmula de Lunh'''
        if len(card_number.strip())<13 or not card_number.isdigit() : 
            raise Gamin_exception("Invalid card number")
        # digits_odd = self.card_number[::2]
        # digits_odd = [int(digit) for digit in digits_odd]
        # digits_odd = [digit*2 for digit in digits_odd]
        # hacerlo en una linea 
        digits_odd = [int(digit) * 2 for digit in card_number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in card_number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits%10 ==0 :
            return True
        else: 
            raise Gamin_exception("ERROR, INVALID COMPROBATION LUHN:/// ")

        

    @property
    def card_number(self):
        return self.__card_number
    

    @card_number.setter
    def card_number(self, value):
        if self.check_sum(value):
            self.__card_number = value
        else:
            raise ValueError("Número de tarjeta inválido")
    
#esto esta aqui vale profe pq estaba probando sola la funcion:D
def check_sum(card_number):
        '''La fórmula de Lunh'''
        card_number = card_number.strip()
        if len(card_number)<13 or not card_number.isdigit() : 
            raise Gamin_exception("Invalid card number")
        # digits_odd = self.card_number[::2]
        # digits_odd = [int(digit) for digit in digits_odd]
        # digits_odd = [digit*2 for digit in digits_odd]
        # hacerlo en una linea 
        digits_odd = [int(digit) * 2 for digit in card_number[::2]]
        
        modified_digits = [digit - 9 if digit > 9 else digit for digit in digits_odd]
        remaining_digits = [int(digit) for digit in card_number[1::2]]

        total_digits = sum(modified_digits) + sum(remaining_digits)
        
        if total_digits%10 ==0 :
            return True
        else: 
            raise Gamin_exception("ERROR, INVALID COMPROBATION LUHN:/// ")
        
