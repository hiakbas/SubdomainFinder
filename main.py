import requests
import threading
#Best Keywords for subdomain names
keywords = ["mail", "admin", "webmail", "dashboard", "portal", "vpn", "remote", "ftp", "ssh", "vpn", "cpanel", "api",
            "blog","wiki", "shop", "forum", "news", "support", "status", "test", "dev", "staging", "mail", "smtp",
            "pop", "imap", "mx", "blog", "news", "support", "help", "forum"]

#function seperate web site from // and return subdomain names
def subdomain_creater_for_web(url, subdomain):
    new_url = url.split("//")
    return new_url[0] + "//" + subdomain + "." + new_url[1]

#Thread class for get function
class Request_subdomain(threading.Thread):
    def __init__(self, url):
        self.url = url
        super().__init__()

    def run(self):
        response = requests.get(self.url)
        return response

#input for website for findind subdomains
web_site = input("Please write a web site without www:   ")
# try and expect block for preventing errors
for i in keywords:
    subdomain_website = subdomain_creater_for_web(web_site, i)
    try:
        getting_data = Request_subdomain(subdomain_website)
        getting_data.run()
        print(subdomain_website)
    except:
        pass
