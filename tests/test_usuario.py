from src.ej49.User import *
from src.ej49.Gamin_exception import Gamin_exception

def test_valid():
    assert check_sum("4539319503436467") == True    

    try:
        check_sum("453563636346346564564645436343463") # tienne que fallar SI O si
        # si llega hasta aca esq no funcina vbien:/
        assert False, "TEnia que haber lanzado excepcion:/" 
    except Gamin_exception:
        pass 

        
    try:
        check_sum("8273 1232 7352 0569")
    except Gamin_exception as e:
        assert True

