import sys
import time
import random
import requests
from datetime import datetime
from colorama import init, Fore, Style
from pyfiglet import Figlet
from termcolor import colored

init(autoreset=True)

def get_ip_address():
    try:
        response = requests.get('https://api.ipify.org?format=json', timeout=5)
        return response.json()['ip']
    except:
        return "Tidak terdeteksi"

def typing_text(text, delay=0.05, color=Fore.WHITE):
    for char in text:
        sys.stdout.write(color + char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def blinking_text(text, times=5, delay=0.3, color=Fore.RED):
    for _ in range(times):
        sys.stdout.write(color + text)
        sys.stdout.flush()
        time.sleep(delay)
        sys.stdout.write('\r' + ' ' * len(text) + '\r')
        sys.stdout.flush()
        time.sleep(delay)
    print(color + text)

def typing_lolcat(text, delay=0.05):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    for char in text:
        if char.strip() == '':
            sys.stdout.write(char)
        else:
            sys.stdout.write(colored(char, random.choice(colors), attrs=['bold']))
        sys.stdout.flush()
        time.sleep(delay)
    print()

def banner_panel_with_cat(text):
    f = Figlet(font='big')
    ascii_art = f.renderText(text)
    cat_art = [
        r" /\_/\  ",
        r"( o.o ) ",
        r" > ^ <  "
    ]
    
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ip_address = get_ip_address()
    author_info = [
        f"Author    : Restu",
        f"IG        : @rstuuramadhan",
        f"Real Time : {now}",
        f"IP Addr   : {ip_address}"
    ]
    
    art_lines = ascii_art.split('\n') + author_info
    max_len = max(len(line) for line in art_lines)
    cat_width = max(len(line) for line in cat_art)
    total_width = max_len + cat_width + 6

    border_char = "■"
    print(Fore.CYAN + border_char * total_width)
    print(Fore.CYAN + border_char + " " * (total_width - 2) + border_char)

    max_lines = max(len(art_lines), len(cat_art))
    for i in range(max_lines):
        left_part = art_lines[i] if i < len(art_lines) else ""
        right_part = cat_art[i] if i < len(cat_art) else ""
        left_part_colored = colored(left_part.ljust(max_len), "cyan", attrs=["bold"])
        right_part_colored = colored(right_part.ljust(cat_width), "magenta", attrs=["bold"])
        print(Fore.CYAN + border_char + "  " + left_part_colored + "  " + right_part_colored + "  " + border_char)

    print(Fore.CYAN + border_char + " " * (total_width - 2) + border_char)
    print(Fore.CYAN + border_char * total_width)

def print_options_table():
    options = [
        ("banget", "✔ ketik ini kalau kamu sangat setuju!"),
        ("GA", "✘ ketik ini kalau kamu tidak setuju!"),
        ("exit", "⏹ Keluar dari program")
    ]
    col1_width = max(len(opt[0]) for opt in options) + 4
    col2_width = max(len(opt[1]) for opt in options) + 4

    print(Fore.YELLOW + "┌" + "─" * col1_width + "┬" + "─" * col2_width + "┐")
    print(Fore.YELLOW + "│" + " Pilihan ".center(col1_width) + "│" + " Keterangan ".center(col2_width) + "│")
    print(Fore.YELLOW + "├" + "─" * col1_width + "┼" + "─" * col2_width + "┤")
    for key, desc in options:
        print(Fore.GREEN + f"│ {key.ljust(col1_width-2)}│ " + Fore.WHITE + f"{desc.ljust(col2_width-1)}│")
    print(Fore.YELLOW + "└" + "─" * col1_width + "┴" + "─" * col2_width + "┘")

def input_with_border(prompt):
    border_h = "─" * (len(prompt) + 4)
    print(Fore.CYAN + f"┌{border_h}┐")
    print(Fore.CYAN + f"│  {prompt}  │")
    print(Fore.CYAN + f"└{border_h}┘")
    return input(Fore.YELLOW + "➡️ ").strip().lower()

def loading_spinner(duration=3, message="Memuat"):
    spinner = ['|', '/', '-', '\\']
    print(Fore.MAGENTA + message, end=" ")
    for i in range(duration * 10):
        sys.stdout.write(Fore.MAGENTA + spinner[i % len(spinner)])
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
    print()

def final_crash_animation():
    print()
    bar_length = 50
    for i in range(bar_length + 1):
        filled = '█' * i
        empty = '-' * (bar_length - i)
        percent = int((i / bar_length) * 100)
        sys.stdout.write(f"\rProgress akhir: |{filled}{empty}| {percent}%")
        sys.stdout.flush()
        time.sleep(0.04)
    print("\n")
    typing_text("Sistem crash please RESTART! your fucking android", delay=0.07, color=Fore.RED + Style.BRIGHT)

def simulate_deletion_android():
    files = [
        "Android", "Download", "Storage/emulated/0",
        "dir", "com.mobile.legends", "com.FF.GameBurik",
        "revisi skripsi", "Dosa", "obb", "bkp"
    ]
    print(Fore.RED + "\n[!] Memulai penghapusan SystemAndorid...\n")
    time.sleep(1)

    total_files = len(files)
    for idx, file in enumerate(files, 1):
        bar_length = 40
        for i in range(bar_length + 1):
            filled = '█' * i
            empty = '-' * (bar_length - i)
            percent = int((i / bar_length) * 100)
            sys.stdout.write(f"\r{Fore.RED}Menghapus {file.ljust(15)} |{filled}{empty}| {percent}%")
            sys.stdout.flush()
            time.sleep(0.02)
        sys.stdout.write(" ")
        print(colored("SUCCESS!", "green", attrs=["bold"]))
        time.sleep(0.3)

        overall_percent = int((idx / total_files) * 100)
        sys.stdout.write(f"\r{Fore.YELLOW}Total Progress: [{int(overall_percent/2)*'█'}{(50 - int(overall_percent/2))*'-'}] {overall_percent}%\n")
        sys.stdout.flush()
        time.sleep(0.2)

    print(Fore.WHITE + Style.BRIGHT + "\n" + "="*60)
    blinking_text(colored("⚠️ WARNING: SISTEM AKAN MENGALAMI KERUSAKAN!", "yellow", "on_red"), times=8, delay=0.4)
    blinking_text(colored(":( Android kamu mengalami masalah dan perlu RESTART", "white", "on_red"), times=8, delay=0.4)
    print("Kami hanya mengumpulkan beberapa informasi kesalahan lalu kami akan restart untuk Anda.")
    print(colored("0% selesai", "white", "on_red"))
    print("="*60)
    time.sleep(2)

    final_crash_animation()

    typing_lolcat("\nAWKAOKWOAKAK MAMPUA🤣\n")

def cat_walk_animation(steps=20, delay=0.1):
    cat_frames = [
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r" /| |\  ",
            r"/_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"  /| |\ ",
            r" /_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"   /| |\ ",
            r"  /_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"  /| |\ ",
            r" /_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r" /| |\  ",
            r"/_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"   /| |\ ",
            r"  /_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"    /| |\ ",
            r"   /_|_|_\ "
        ],
        [
            r" /\_/\  ",
            r"( o.o ) ",
            r" > ^ <  ",
            r"  /| |\ ",
            r" /_|_|_\ "
        ],
    ]
    for step in range(steps):
        sys.stdout.write("\033[H\033[J")
        padding = " " * step
        frame = cat_frames[step % 8]
        for line in frame:
            print(padding + line)
        time.sleep(delay)
    print()

def main():
    banner_panel_with_cat("HAWOOO")
    print(Fore.CYAN + Style.BRIGHT + "="*60)
    loading_spinner()

    while True:
        print_options_table()
        jawaban = input_with_border("Beru Gantenk?")

        if jawaban == "exit":
            typing_text("\nTerima kasih sudah mencoba program ini! Sampai jumpa! 👋\n", delay=0.05, color=Fore.CYAN)
            break
        elif jawaban == "banget":
            typing_lolcat("\n🎉 Selamat! Kredit sosial Anda bertambah +9999! 🎉\n")
            cat_walk_animation()
        elif jawaban == "ga":
            typing_text("\nwoy!", delay=0.07, color=Fore.RED)
            blinking_text("Selamat kamu akan kehilangan semua data di HP mu :)", times=6, delay=0.4, color=Fore.RED)
            simulate_deletion_android()
        else:
            typing_text("\nketik yang bener kocak! 'banget', 'GA', atau 'exit'.\n", delay=0.05, color=Fore.MAGENTA)

if __name__ == "__main__":
    main()

