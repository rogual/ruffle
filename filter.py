from termcolor import colored
import sys
import re

stack = ['']

def hl_target(x):
    if '{' in x:
        i = x.index('{')
        return colored(x[:i], 'yellow') + colored(x[i:], 'cyan')
    return colored(x, 'yellow')

def log_line(text):
    print('  ' * len(stack), end='')
    print(text)

    
def log_from(target, tail):
    if tail == 'enter':
        old_target = stack[-1]
        local_target = target[len(old_target):]
        if local_target.startswith(':'):
            local_target = local_target[1:]
                                        
        log_line(hl_target(local_target) + colored(' {', 'blue'))
        stack.append(target)

    elif tail == 'exit':
        stack.pop()
        log_line(colored('}', 'blue'))

    else:
        log_line(colored(tail, 'white', attrs=['bold']))
    

for line in sys.stdin:

    if ': rga: ' in line or ': avm_trace: ' in line:
        _a, _b, line = line.split(maxsplit=2)

        target, tail = re.split(': rga: |: avm_trace: ', line)
        tail = tail.strip()

        log_from(target, tail)

    else:
        log_line(line.strip())
