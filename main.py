import os
import sys
import datetime
import logging
from time import sleep
from rich.logging import RichHandler
from rich.traceback import install
from rich import pretty
from rich.console import Console

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
FORMAT = '%(asctime)s %(levelname)-8s %(message)s'
logging.basicConfig(filename='logs/{}.log'.format(_time), format=FORMAT, level=logging.INFO, datefmt="[%X]")
log = logging.getLogger("rich")
log.addHandler(RichHandler())
"""
#----------------------------------
"""


def main():
    if not os.path.exists('logs'):
        os.makedirs('logs')
    console.print(f'{logo}')
    log.debug('This is an DEBUG log /testmesexy')
    log.info('This is an INFO log {"weener", "24"}')
    log.warning('This is an WARNING log https://sexiboi.com')
    log.error('This is an ERROR log <module> fdj')
    log.critical('This is an CRITICAL log. GET')

    console.print("Goodbye :fire:", style="bold green")



main()