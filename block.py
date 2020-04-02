import sys
import platform

class Block():

    def __init__(self):

        if platform.system == 'Windows':
            self.hosts_path = "C:\Windows\System32\drivers\etc\hosts"
        else:
            self.hosts_path = "/etc/hosts"

        self.redirect = '127.0.0.1'
        self.website_list = ["www.facebook.com","facebook.com", "www.youtube.com", "web.whatsapp.com", "www.twitter.com", "www.instagram.com", "youtube.com", "twitter.com", "instagram.com"]


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