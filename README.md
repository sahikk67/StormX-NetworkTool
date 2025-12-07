# StormX-NetworkTool

A DDoS attack tool by Sahikk (sahikk67)

## Description

StormX-NetworkTool is a Python script designed to perform Distributed Denial of Service (DDoS) attacks. It supports TCP, UDP, and HTTP attack types, allowing you to simulate a large number of requests to a target server.

## Features

- **TCP DDoS Attack**: Sends a large number of TCP packets to the target.
- **UDP DDoS Attack**: Sends a large number of UDP packets to the target.
- **HTTP DDoS Attack**: Sends a large number of HTTP requests to the target.

## Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/StormX-NetworkTool.git
Navigate to the repository directory:
cd StormX-NetworkTool

Ensure you have Python installed on your system.
Usage
To run the DDoS attack tool, use the following command format:

python StormX-NetworkTool.py <target_ip> <target_port> <target_url> <attack_type> <packets_per_second> <requests_per_second> <num_threads>

Examples
TCP DDoS Attack:

python StormX-NetworkTool.py 192.168.1.1 80 http://example.com tcp 1000 500 500

UDP DDoS Attack:

python StormX-NetworkTool.py 192.168.1.1 80 http://example.com udp 1000 500 500

HTTP DDoS Attack:

python StormX-NetworkTool.py 192.168.1.1 80 http://example.com http 1000 500 500

Help Message:

python StormX-NetworkTool.py -h

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Contact
For any questions or suggestions, feel free to reach out to Sahikk (sahikk67) on Instagram: @ixe.67_.


