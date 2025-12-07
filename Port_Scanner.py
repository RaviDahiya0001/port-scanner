import socket
import threading
import time

print("\n=== Detailed Port Scanner ===\n")

target = input("Enter Target IP/Domain: ")

try:
    target_ip = socket.gethostbyname(target)
except socket.gaierror:
    print("Invalid domain or IP!")
    exit()

print(f"\nScanning Target: {target} ({target_ip})")
print("---------------------------------------------")

open_ports = []
lock = threading.Lock()

# Common ports with service names
service_dict = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP", 68: "DHCP", 69: "TFTP", 80: "HTTP",
    110: "POP3", 123: "NTP", 137: "NetBIOS", 139: "NetBIOS",
    143: "IMAP", 161: "SNMP", 389: "LDAP", 443: "HTTPS", 
    445: "SMB", 587: "SMTP TLS", 631: "IPP", 993: "IMAP SSL",
    995: "POP3 SSL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    6379: "Redis", 8080: "HTTP Proxy", 8443: "HTTPS Alt"
}

def scan_port(port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5)

        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = service_dict.get(port, "Unknown Service")

            # Try grabbing banner
            try:
                sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                banner = banner.split("\n")[0] if banner else "No Banner"
            except:
                banner = "No Banner"

            with lock:
                print(f"[OPEN] Port {port:<5} | Service: {service:<15} | Banner: {banner}")
                open_ports.append((port, service, banner))

        sock.close()

    except Exception:
        pass


# MULTI‑THREADED SCAN
threads = []
start_time = time.time()

print("\nScanning ports 1–10000, please wait...\n")

for port in range(1, 10001):
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

# Wait for all threads
for t in threads:
    t.join()

end_time = time.time()

print("---------------------------------------------")
print("Scan Completed!")
print(f"Total Time: {end_time - start_time:.2f} seconds")

# Summary
if open_ports:
    print("\n=== OPEN PORTS SUMMARY ===")
    for p, s, b in open_ports:
        print(f"Port {p:<5} | {s:<15} | {b}")
else:
    print("\nNo open ports found.")
