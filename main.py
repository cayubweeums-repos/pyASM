import os
import datetime
import logging
from rich.logging import RichHandler
from rich.traceback import install
from rich import pretty
from rich.console import Console
import _pickle as pickle


from objects import targets

logo='''
===============================================================
                        █████████    █████████  ██████   ██████
                       ███░░░░░███  ███░░░░░███░░██████ ██████ 
 ████████  █████ ████ ░███    ░███ ░███    ░░░  ░███░█████░███ 
░░███░░███░░███ ░███  ░███████████ ░░█████████  ░███░░███ ░███ 
 ░███ ░███ ░███ ░███  ░███░░░░░███  ░░░░░░░░███ ░███ ░░░  ░███ 
 ░███ ░███ ░███ ░███  ░███    ░███  ███    ░███ ░███      ░███ 
 ░███████  ░░███████  █████   █████░░█████████  █████     █████
 ░███░░░    ░░░░░███ ░░░░░   ░░░░░  ░░░░░░░░░  ░░░░░     ░░░░░ 
 ░███       ███ ░███                                           
 █████     ░░██████                                            
░░░░░       ░░░░░░                                             
===============================================================
'''

"""
Initialize CLI and logging
#----------------------------------
"""
console = Console()
install()
pretty.install()
_time = datetime.date.today()
if not os.path.exists('data'):
    os.makedirs('data')
    os.makedirs('data/logs')
    os.makedirs('data/objects')
    os.mknod('data/objects/target_data.pkl')
FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
logging.basicConfig(filename='data/logs/{}.log'.format(_time), format=FORMAT, level=logging.INFO, datefmt="[%X]")
log = logging.getLogger("rich")
log.addHandler(RichHandler())
"""
#----------------------------------
"""


def main():
    console.print(f'{logo}')
    log.debug('This is an DEBUG log /testmesexy')
    log.info('This is an INFO log {"weener", "24"}')
    log.warning('This is an WARNING log hxxps[://]sexiboi[.]com')
    log.error('This is an ERROR log <module> fdj')
    log.critical('This is an CRITICAL log. GET')

    target_list = [
        targets.Target('ananke', '192.168.2.2'),
        targets.Target('echo', '192.168.2.20'),
        targets.Target('consus', '192.168.2.21')
    ]

    targets.save_object(target_list, 'data/objects/target_data.pkl')

    tmp_loaded_targets = targets.pickle_loader('data/objects/target_data.pkl')

    console.print(tmp_loaded_targets)

    console.print('Targets currently in pickle file:')
    console.print(tmp_loaded_targets[0])

    console.print("Main func over :fire:", style="bold green")


if __name__ == "__main__":
    main()