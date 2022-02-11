# Justin Ventura

'''
what it do

how to run: `python3 justin.py`
'''
from os import system, name
  
# Import sleep to show output for some time period
from time import sleep
  
# define our clear function
def clear():
    # For windows
    if name == 'nt':
        _ = system('cls')

    # For mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

# Main:
def _main(verbose: bool = False):
    clear()
    print('jenna likes turtles')
    sleep(5)
    clear()

    # Variables needed for turtle:
    turt_colors = '\033[92m', '\033[0m'
    turt = ['     ****   ',
            '*  ******** ',
            ' ***********',
            '  *       * ']
    spacing = '                       '

    # Print a turtle to the console:
    for i in range (len(spacing), -1, -1):
        for j in range(0, len(turt)):
            print(spacing[:i], turt_colors[0], turt[j], turt_colors[1])
        sleep(2)
        clear()

    print('jenna is awesome but its ok i like her anyway') 


# Run script directly:
if __name__ == '__main__':
    _main()