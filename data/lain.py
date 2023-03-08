#######################################################
# Name           : Brute Facebook (BF)                #
# File           : lain.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############

from rich import print as prints
from rich.panel import Panel

from yz.chs import Cek_Crack
from yz import cok as cinta

from .ffbfb import Bot_Facebook
from .iwjd import Ngocok

merah  = '[#FF0022]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'

M = '\x1b[1;91m' # MERAH
N = '\x1b[0m'    # WARNA MATI

class Xnxx:

    def __init__(self, cok, tok):
        self.tok = tok
        self.cok = cok

    def kontol(self):
        prints(Panel("""[[bold cyan]01[/]] Check hasil crack       [[bold cyan]03[/]] bot facebook
[[bold cyan]02[/]] auto pasang a2f         [[bold red]00[/]] kembali""", title=f'{merah}•{kuning}•{hijau}•{hijau} FITURE LAINNYA {hijau}•{kuning}•{merah}•[/]', padding=(0,5), style="bold white", width=70))
        pil = input(f"[{M}?{N}] pilih: ")
        if pil in[""," "]:
            prints(Panel("[[bold red]![/]] jangan kosong", style="bold white", width=70));self.kontol()
        elif pil in["1","01"]:
            Cek_Crack().hasil()
        elif pil in["2", "02"]:
            Ngocok().menu()
        elif pil in["3", "03"]:
            Bot_Facebook(self.cok, self.tok).menu()
        elif pil in["0", "00"]:
            cinta.Cindy_aulia()
        else:
            prints(Panel("[[bold red]![/]] input yang benar", style="bold white", width=70));self.kontol()
