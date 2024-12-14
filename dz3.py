import colorama
from colorama import init, Fore, Back, Style

init()
#Вывод текста красным цветом
print(Fore.RED + 'Отвал')
#Вывод текста на зеленом фоне
print(Back.GREEN + 'RTX 3060')
#Вывод яркого текста
print(Style.BRIGHT + 'GTX 750 TI')
#Вывод синего текста на желтом фоне
print(Fore.BLUE + Back.YELLOW + 'Aerocool VX Plus 600')

# Сброс всех атрибутов
print(Style.RESET_ALL)
print('Вернулись к обычным цветам')

deinit()
