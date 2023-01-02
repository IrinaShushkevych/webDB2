
from classes import ServiceBot

def main():
    service_bot = ServiceBot()
    while True:
        print('==============================================================')
        print('Use command "help" to get list of command')
        cmd = input('command: ').lower()
        print('==============================================================')
        service_bot.cmd(cmd)

if __name__ == '__main__':
    main()