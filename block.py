import sys
import platform
import pathlib

class Block():

    def __init__(self):

        if platform.system == 'Windows':
            self.hosts_path = "C:\Windows\System32\drivers\etc\hosts"
        else:
            self.hosts_path = "/etc/hosts"

        self.redirect = '127.0.0.1'

        with open(f"{pathlib.Path().absolute()}/blacklist.txt") as file:
            self.website_list = [line.strip() for line in file.readlines()]


    def block(self):
        print("Bloqueando...") 
        with open(self.hosts_path, 'r+') as file: 
            content = file.read() 
            for website in self.website_list: 
                if website in content: 
                    pass
                else: 
                    file.write(self.redirect + " " + website + "\n") 
        print("Sites bloqueados, work hard.")

    def unblock(self):
        with open(self.hosts_path, 'r+') as file: 
            content=file.readlines() 
            file.seek(0) 
            for line in content: 
                if not any(website in line for website in self.website_list): 
                    file.write(line)
                    file.truncate()
        print("Sites desbloqueados, have a joy :D")

    def execute(self, command):
        getattr(globals()['Block'](), command.strip())()

if __name__ == "__main__":
    b = Block()
    cmd = sys.argv[1].strip()
    b.execute(cmd)