from src.User import *

user_valid = User("nicki", "nickiiinicole", "12344", "79927398713")
user_invalid = User("dayaraaa", "nayancc", "334324", "79927398714")
user_non_digit = User("jesuu", "star", "6565", "45A9319503436467")
user_non_digit = User("enrique", "gamin", "909r88r", "45A9319503436467")


assert user_valid.check_sum() == True
try:
    user_invalid.check_sum() # tienne que fallar SI O si
    # si llega hasta aca esq no funcina vbien:/
    assert False, "TEnia que haber lanzado excepcion:/" 
except Gamin_exception:
    pass 

try:
    user_non_digit.check_sum()
except Gamin_exception as e:
    assert True