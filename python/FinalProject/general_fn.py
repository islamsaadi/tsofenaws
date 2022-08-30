import random
import json

def enc_newkey(key, *args):
    if key and key['file'] is False:
        print('Are you sure you want to override the current UNSAVED key named ('+key['keyname']+') ?!')
        cmd_str = input('subs (y,n)>')
        cmd = cmd_str.split()
        if cmd[0] == 'n':
            return key
    keyname = args[1]
    letters = 'abcdefghijklmnopqrstuvwxyz'
    letters_list = [*letters]
    random.shuffle(letters_list)
    shuffled = ''.join(letters_list)
    enckey = {letters[i]:shuffled[i] for i in range(len(letters))}
    deckey = {list(enckey.values())[i]:list(enckey.keys())[i] for i in range(len(enckey))}
    sorted_deckey = dict(sorted(deckey.items()))
    print('A new key called '+keyname+' was created.')
    return {'keyname': keyname, 'file': False , 'enckey': enckey, 'deckey': sorted_deckey}

def enc_info(key, *args):
    if key:
        print('Current key: ', key['keyname'])
        print('State: saved in ' + key['file'] if key['file'] else 'State: not saved')
        print('Encryption:')
        print( ''.join(key['enckey'].keys()) )
        print( ''.join(key['enckey'].values()) )
        print('Decryption:')
        print( ''.join(key['enckey'].keys()) )
        print( ''.join(key['deckey'].values()) )
    else:
        print('No key')
    return key

def enc_save(key, *args):
    filename = args[1]
    if key:
        try:
            key['file'] = filename
            with open(filename, "w") as fp:
                json.dump(key,fp)
            print('Enc/Dec keys saved in '+filename+' file')
        except:
            key['file'] = False
            print("Something went wrong while saving the file")
    else:
        print('No Key')
    return key

def enc_load(key, *args):
    filename = args[1]
    if key and key['file'] == filename:
        print('The key already loaded')
    else:
        try:
            with open(filename, 'r') as f:
                key = json.load(f)
        except FileNotFoundError:
            print("No such key")
        except:
            print("Something went wrong while opening the file")
    return key
