
# Способы обработки исключений:

try: 
     '123456789'.index('0')
except:
     print('0 нет в строке 123456789')
 
 

try:
    if not '123456789'.index('0'):
        raise Exception
except Exception:
    print('except')
    # exit()  # Это остановит программу
    # quit()  # Это тоже остановит программу







