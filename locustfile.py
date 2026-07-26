import time
import sys
import random

# Cyberpunk UI Colors & Effects
CYAN = "\033[96m"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RESET = "\033[0m"
BOLD = "\033[1m"

def display_banner():
    print(f"{CYAN}{BOLD}")
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║            NEXUS-MD | ADVANCED SECURITY OPERATIONS           ║")
    print("║                     DEVELOPER: SASINDA                      ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print(f"{RESET}{YELLOW}  [!] STATUS: SECURE GATEWAY OPEN | MODULE: WA-BAN-SIMULATOR{RESET}\n")

def simulate_ban():
    phone = input(f"{CYAN}{BOLD}[?] ENTER TARGET WHATSAPP NUMBER (+94xxxxxxxxx) > {RESET}")
    
    if not phone:
        phone = "+94771234567"
        
    print(f"\n{RED}{BOLD}[+] TARGET ACQUIRED SUCCESSFULLY: {phone}{RESET}")
    print(f"{MAGENTA}[*] Establishing encrypted tunnel to Meta API Gateway...{RESET}")
    time.sleep(1)

    # ප්‍රොෆෙෂනල් ලොග්ස් සහ ස්ටේජස්
    stages = [
        "Bypassing Cloudflare DDoS Protection...",
        "Extracting target device session tokens...",
        "Injecting payload to WhatsApp Business API...",
        "Overriding system logs and security firewalls...",
        "Disabling two-step verification bypass..."
    ]

    for stage in stages:
        sys.stdout.write(f"{CYAN}[X]{RESET} {stage} ")
        for _ in range(4):
            time.sleep(0.3)
            sys.stdout.write(".")
            sys.stdout.flush()
        print(f" {GREEN}[OK]{RESET}")

    # ලොකු ලෝඩින් බාර් එකක්
    print(f"\n{YELLOW}[*] Processing final ban sequence... Please wait.{RESET}")
    total = 50
    for i in range(total + 1):
        percent = int(i / total * 100)
        bar = '█' * i + '-' * (total - i)
        sys.stdout.write(f'\r{CYAN}PROGRESS: |{bar}| {percent}%{RESET}')
        sys.stdout.flush()
        time.sleep(0.04)

    # අවසාන සාර්ථක වීමේ පණිවිඩය (ලොකු බොක්ස් එකක් ඇතුළේ)
    print(f"\n\n{RED}{BOLD}╔══════════════════════════════════════════════════════════════╗")
    print(f"║                   CRITICAL BAN EXECUTED!                     ║")
    print(f"║     Target: {phone}                                     ║")
    print(f"║     Reason: Violation of Terms of Service (Section 12.4)     ║")
    print(f"║     Status: PERMANENTLY RESTRICTED                           ║")
    print(f"╚══════════════════════════════════════════════════════════════╝{RESET}")
    
    print(f"\n{GREEN}{BOLD}[!] Target account will be suspended within 24 hours.{RESET}")
    print(f"{CYAN}================================================================")
    print(f"          POWERED BY DEVELOPER SASINDAA | NEXUS TEAM           ")
    print(f"================================================================{RESET}")

if __name__ == "__main__":
    display_banner()
    simulate_ban()
