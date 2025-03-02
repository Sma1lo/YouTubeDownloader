RED = "\033[91m"
WHITE = "\033[97m"
RESET = "\033[0m"

LOGO = """
 ██╗   ██╗████████╗██████╗ 
 ╚██╗ ██╔╝╚══██╔══╝██╔══██╗
  ╚████╔╝    ██║   ██║  ██║
   ╚██╔╝     ██║   ██║  ██║
    ██║      ██║   ██████╔╝
    ╚═╝      ╚═╝   ╚═════╝ 
                          
"""

def print_logo():
    print(f"{RED}{LOGO}{RESET}")

def show_menu():
    print_logo()
    print(f"      {RED}v 1.0{RESET}, Author: Sma1lo\n")
    print(f"{RED}[{WHITE}1{RED}]{RESET} Download a single video")
    print(f"{RED}[{WHITE}2{RED}]{RESET} Download a playlist")
    print(f"{RED}[{WHITE}3{RED}]{RESET} Download all videos from a channel")
    print(f"{RED}[{WHITE}0{RED}]{RESET} Exit")