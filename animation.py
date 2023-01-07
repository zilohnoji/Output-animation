from termcolor import colored
from colorama import Fore, init
from time import sleep
from sys import stdout
from re import search

init(convert=True)
def animation(var: str) -> None:
     if var == "Você Perdeu":
        color = Fore.RED
     elif search("Voce Ganhou", var):
        color = Fore.GREEN
     else:
        color = Fore.WHITE

     list_var = [broken for broken in var]
     for n in list_var:
            stdout.write(colored(f"{color}{n}{Fore.RESET}"))
            stdout.flush()
            sleep(.1)
     print("\n")
            
            
animation("Voce Ganhou")
animation("Voce Perdeu")
animation("Programa de animação")