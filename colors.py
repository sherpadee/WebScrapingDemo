from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Fore.BLACK + Back.YELLOW + 'and with a yellow background')
print(Style.RESET_ALL)
print(Style.DIM + 'and in dim text')
print(Fore.WHITE + Back.GREEN + 'and with a green  background')
print(Style.RESET_ALL)
print('back to normal now')
