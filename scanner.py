import socket
import argparse
import threading
from datetime import datetime

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((host, port))
        if result == 0:
            print(f"[+] Porta {port} ABERTA")
        s.close()
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Scanner de Portas TCP - Pentest Study")
    parser.add_argument('--host', required=True, help='IP alvo')
    parser.add_argument('--portas', default='1-1024', help='Range ex: 1-1000')
    parser.add_argument('--threads', type=int, default=100, help='Qtd de threads')
    args = parser.parse_args()

    host = socket.gethostbyname(args.host)
    inicio, fim = map(int, args.portas.split('-'))

    print(f"[*] Escaneando {host} de {inicio} a {fim} com {args.threads} threads")
    print(f"[*] Iniciado em {datetime.now().strftime('%H:%M:%S')}")

    for porta in range(inicio, fim + 1):
        t = threading.Thread(target=scan_port, args=(host, porta))
        t.start()

if __name__ == "__main__":
    main()
