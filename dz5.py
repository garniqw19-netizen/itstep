import colorama
from colorama import Fore, Back, Style
import inspect

print(type(colorama))

for method in dir(colorama):
    print(method)

dir()



print(inspect.ismodule(colorama))
print(inspect.isclass(colorama))
print(inspect.isfunction(colorama))
#перевірка на атрибути
print(getattr(colorama, 'Fore'))
print(getattr(colorama, 'Back'))
print(getattr(colorama, 'Style'))
# я дізнався що робить бібліотека. Димонстрація її можливостей
print(Fore.RED + "Цей текст червоний")
print(Fore.GREEN + "Цей текст зелений")
print(Back.YELLOW + "Жовтий фон")
print(Style.BRIGHT + "Жирний текст")
