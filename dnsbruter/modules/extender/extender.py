import platform
import os 
import resource
from colorama import Fore,Back,Style


red =  Fore.RED

green = Fore.GREEN

magenta = Fore.MAGENTA

cyan = Fore.CYAN

mixed = Fore.RED + Fore.BLUE

blue = Fore.BLUE

yellow = Fore.YELLOW

white = Fore.WHITE

reset = Style.RESET_ALL

bold = Style.BRIGHT

colors = [ green, cyan, blue]



def extender():  
    try:
        
        soft , hard = resource.getrlimit(resource.RLIMIT_NOFILE)
        
        new = 100000
        
        osname = platform.system()
        
        if osname == "Linux" or  osname == "Darwin":
            
            
            
            resource.setrlimit(resource.RLIMIT_NOFILE, (new, hard))
            
    except KeyboardInterrupt as e:
        
        quit()
        
    except Exception as e:
        
        pass
        