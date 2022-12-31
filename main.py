
from classes import Helper

def main():
    helper = Helper()
    while True:
        print('==============================================================')
        print('Use command "help" to get list of command')
        cmd = input('command: ').lower()
        print('==============================================================')
        helper.cmd(cmd)

if __name__ == '__main__':
    main()