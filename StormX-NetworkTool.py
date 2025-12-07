import socket
import threading
import time
import requests
import argparse

def tcp_test(target_ip, target_port, rate):
    delay = 1.0 / rate
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            s.connect((target_ip, target_port))
            s.send(b"PING_TEST")
            s.close()
        except:
            pass
        time.sleep(delay)

def udp_test(target_ip, target_port, rate):
    delay = 1.0 / rate
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.sendto(b"PING_TEST", (target_ip, target_port))
        except:
            pass
        time.sleep(delay)

def http_test(url, rate):
    delay = 1.0 / rate
    while True:
        try:
            requests.get(url, timeout=1)
        except:
            pass
        time.sleep(delay)

def main():
    parser = argparse.ArgumentParser(
        description="Server Load Test Tool (Legal Use Only)"
    )

    parser.add_argument("mode", choices=["tcp", "udp", "http"], help="Test method")
    parser.add_argument("target", help="IP or URL")
    parser.add_argument("port", type=int, nargs="?", help="Port (for TCP/UDP)")
    parser.add_argument("rate", type=int, help="Requests per second")
    parser.add_argument("threads", type=int, help="Number of threads")

    args = parser.parse_args()

    if args.mode == "http":
        for _ in range(args.threads):
            t = threading.Thread(target=http_test, args=(args.target, args.rate))
            t.start()
    else:
        for _ in range(args.threads):
            func = tcp_test if args.mode == "tcp" else udp_test
            t = threading.Thread(target=func, args=(args.target, args.port, args.rate))
            t.start()

if __name__ == "__main__":
    main()
