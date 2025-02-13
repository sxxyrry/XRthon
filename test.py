with open('./test.XRthon', 'r', encoding='UTF-8') as f:
    text = f.read()
    alltexts = text.split('\n')

def _():
    i = 0
    while i < len(alltexts):
        linetext = alltexts[i]
        i += 1
        if linetext.startswith('def_func'):
            name = linetext.split('{')[0][9:]
            args = linetext.split('{')[1][0:-3].replace(' ', '').split(',')
            body = ''
            try:
                exec(f'def {name}({','.join(args)}):pass')
            except Exception as e:
                print(e)
            
                return
        
            while 1:
                i += 1
                lt = alltexts[i]

                if lt.startswith('END'):
                    if lt == f'END {linetext}':
                        break

                body += lt + '\n'

            print(f'{name=}, {args=}, {body=}')

_()
