import tkinter as tk
import customtkinter as ctk
import requests
import time
import threading

class ProxyTester:
    def __init__(self) -> None:
        self.root = ctk.CTk()
        self.root.geometry('1000x800')
        self.root.title("Proxy Tester")
        ctk.set_appearance_mode('dark')

    def check_proxy_speed(self, proxy,website):
        self.headers = {
            'Host': 'www.google.pl',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 OPR/98.0.0.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'Accept-Language': 'pl-PL,pl;q=0.9,en-US;q=0.8,en;q=0.7',
        }
        proxyDict = dict()
        ip = proxy.split(":")[0]
        port = proxy.split(":")[1]
        login = proxy.split(":")[2]
        passwd = proxy.split(":")[3]

        https_proxy_format = "https://" +login+":"+passwd+"@"+ip+":"+port
        http_proxy_format = "http://" +login+":"+passwd+"@"+ip+":"+port
        proxyDict['https'] = https_proxy_format
        proxyDict['http'] = http_proxy_format
        try:
            startTime = time.time()
            r = requests.get(website,headers=self.headers,proxies=proxyDict)
            endTime = time.time()

            speed = str(round((endTime - startTime)*1000)) + "ms"
        except:
            speed = "Not working"

        proxy_label = ctk.CTkLabel(self.resultsFrame, text=f"{proxy.split(':')[0]} | {speed}",font=('Arial',18))
        proxy_label.pack(pady=3)

    def clearPage(self):    
        for widget in self.root.winfo_children():
            widget.pack_forget()

    def startPage(self):
        self.clearPage()

        self.Title = ctk.CTkLabel(self.root, text="Proxy Tester",font=('Arial',30))
        self.Title.pack(pady=30)

        self.website = ctk.CTkLabel(self.root, text="Which website should i test?",font=('Arial',15))
        self.website.pack()

        self.websiteInput = ctk.CTkTextbox(self.root, width=500,height=20)
        self.websiteInput.pack(pady=(0,10))

        proxyLabel = ctk.CTkLabel(self.root, text="Paste proxies here",font=('Arial',15))
        proxyLabel.pack()

        self.proxyInput = ctk.CTkTextbox(self.root,width=475,height=500)
        self.proxyInput.pack()
        

        submit_button = ctk.CTkButton(self.root, text="Check Proxy",font=('Arial',20),command=self.checking_scene)
        submit_button.pack(pady='10')

        self.root.mainloop()

    def checking_scene(self):
        self.clearPage()
        Title = ctk.CTkLabel(self.root, text="Proxy Tester",font=('Arial',30))
        Title.pack(pady=30)

        resultsLabel = ctk.CTkLabel(self.root, text="Here are results:",font=('Arial',20))
        resultsLabel.pack(pady=10)

        proxies = list(self.proxyInput.get("1.0",'end-1c'))
        proxyList = list()
        temp = ''
        for letter in proxies:
            if letter != '\n':
                temp+=letter
            else:
                proxyList.append(temp)
                temp = ''

        self.resultsFrame = ctk.CTkScrollableFrame(self.root, width=500,height=500)
        self.resultsFrame.pack()

        if self.websiteInput.get("1.0",'end-1c') == "":
            websiteTest = 'https://www.google.com/'
        else:
            websiteTest = self.websiteInput.get("1.0",'end-1c')

        for proxy in proxyList:
            self.check_proxy_speed(proxy,websiteTest)
        
        back_button = ctk.CTkButton(self.root, text="Back",font=('Arial',20),command=self.startPage)
        back_button.pack(pady='5')
 
if __name__ == "__main__":
    Tester = ProxyTester()
    Tester.startPage()