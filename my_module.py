import os
import colorama
from colorama import Fore,Back,Style
colorama.init(autoreset=True)

"""
Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
Style: DIM, NORMAL, BRIGHT, RESET_ALL
"""

def toGetFilesize(path):
    if os.path.isfile(path):
        BYTES = os.path.getsize(path)
        KB=BYTES/1024
        MB=KB/1024
        GB=MB/1024
    else:
        print("檔案不存在。")
        return 0
    return GB

def toGetMessage(fsize):
    if fsize < 8.0:        
        return "不需執行封存和壓縮！"    
    elif 8.0 <= fsize <40.0:       
        return "請撥空執行封存和壓縮！"    
    else:       
        return "立刻執行封存和壓縮！"

#return Fore.GREEN+"不需執行封存和壓縮！"
#return Fore.YELLOW+"請撥空執行封存和壓縮！" 
#return Fore.RED+"立即執行封存和壓縮！

#設定標籤文字顏色       
def setfontcolor(fsize):
    if fsize<8.0:
        return "black"
    if 8.0 <= fsize <40.0:
        return "green"
    if fsize >= 40.0:
        return "red"
