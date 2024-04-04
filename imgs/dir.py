import os
from pathlib import Path
import sys
from colorama import Fore, Style

def main(p: Path):
    for el in p.iterdir():  
        if el.is_dir():
            print(f"{Fore.YELLOW}[FOLDER]{Fore.RESET} {el}")  
            print(f"{Fore.GREEN}{"-" * 20}{Fore.RESET}")
            main(el) 
        else:
            print(f"{Fore.BLUE}[ELEMENT]{Fore.RESET} {el}") 

if __name__ == "__main__":
  try:
      dir_path = Path(sys.argv[1])
      if not dir_path.is_dir():
        print ("Это не директория, попробуйте ещё раз")
      main(dir_path)
  except Exception as e:
    print (f"Произошла ошибка: {e}")
  finally:
     input(f"{Fore.RED}{"Нажмите Enter чтобы выйти"}{Fore.RESET}")
     os.system('cls' if os.name == 'nt' else 'clear')
