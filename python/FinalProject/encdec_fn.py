def enc_dec_file(key, *args):
    func = args[0]
    txtfile = args[1]
    encfile = args[2]
    if key:
        try:
            with open(txtfile, 'r') as fr:
                lines = [ line.strip() for line in fr.readlines()]
                with open(encfile, 'w') as fw:
                    for line in lines:
                        for ch in line:
                                if ch in key[func+'key'].keys():
                                    fw.write(key[func+'key'][ch])
                                else:
                                    fw.write(ch)
                        fw.write("\n")
        except FileNotFoundError:
            print('File not found.')
        except:
            print('Something went wrong, try again.')
    else:
        print('Encryption Key not found.')

    return key