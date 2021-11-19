class bcolors:
    HEADER = '\033[95m'
    Magenta = '\033[35m'
    Cyan = '\033[36m'
    Red = '\033[91m'

    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


print(f"{bcolors.WARNING}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(f"{bcolors.Red}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.Cyan}Warning: No active frommets remain. Continue?{bcolors.ENDC}")

print(f"{bcolors.Magenta}Warning: No active frommets remain. Continue?{bcolors.ENDC}")
print(bcolors.HEADER)
print("testes")