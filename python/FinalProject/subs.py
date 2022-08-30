import sys
from general_fn import *
from encdec_fn import *

def enc_init():
    commands = {'newkey': enc_newkey, 'info': enc_info, 'load': enc_load, 'save': enc_save, 'enc': enc_dec_file, 'dec': enc_dec_file}
    return commands

def main_cli():
    commands = enc_init()
    cli_end = False
    key = {}
    while not cli_end:
        cmd_str = input('subs>')
        cmd = cmd_str.split()
        if cmd and cmd[0] in commands.keys():
            key = commands[cmd[0]](key, *cmd)
        if cmd and cmd[0] == 'done':
            cli_end = True

if __name__ == '__main__':
    main_cli()
    sys.exit()
