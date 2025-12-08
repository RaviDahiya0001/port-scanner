import socket
import threading
import time
import streamlit as st

st.set_page_config(page_title="Advanced Port Scanner", layout="wide")

st.title("🔎 Advanced Port Scanner")
st.write("Scan open ports, detect services, and grab banners in real-time.")

target = st.text_input("Enter Target IP or Domain:", "scanme.nmap.org")

service_dict = {
    20: "FTP Data", 21: "FTP Control", 22: "SSH", 23: "Telnet", 25: "SMTP",
    53: "DNS", 67: "DHCP", 68: "DHCP", 69: "TFTP", 80: "HTTP",
    110: "POP3", 123: "NTP", 137: "NetBIOS", 139: "NetBIOS",
    143: "IMAP", 161: "SNMP", 389: "LDAP", 443: "HTTPS",
    445: "SMB", 587: "SMTP TLS", 631: "IPP", 993: "IMAP SSL",
    995: "POP3 SSL", 3306: "MySQL", 3389: "RDP", 5432: "PostgreSQL",
    6379: "Redis", 8080: "HTTP Proxy", 8443: "HTTPS Alt"
}

open_ports = []
lock = threading.Lock()


def scan_port(port, target_ip, progress_bar, progress_text):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.3)
        result = sock.connect_ex((target_ip, port))

        if result == 0:
            service = service_dict.get(port, "Unknown Service")

            # Banner grabbing
            try:
                sock.send(b"HEAD / HTTP/1.1\r\n\r\n")
                banner = sock.recv(1024).decode(errors="ignore").strip()
                banner = banner.split("\n")[0] if banner else "No Banner"
            except:
                banner = "No Banner"

            with lock:
                open_ports.append([port, service, banner])

        sock.close()
    except:
        pass


if st.button("Start Scan"):
    try:
        target_ip = socket.gethostbyname(target)
    except:
        st.error("❌ Invalid domain or IP!")
        st.stop()

    st.info(f"Scanning Target: **{target} ({target_ip})**")
    progress_bar = st.progress(0)
    progress_text = st.empty()

    threads = []
    total_ports = 1000  # You can increase to 10000 if needed

    start_time = time.time()

    for port in range(1, total_ports + 1):
        t = threading.Thread(target=scan_port, args=(port, target_ip, progress_bar, progress_text))
        threads.append(t)
        t.start()

        progress_bar.progress(port / total_ports)
        progress_text.text(f"Scanning port {port}/{total_ports}")

    for t in threads:
        t.join()

    end_time = time.time()

    st.success(f"Scan Completed in {end_time - start_time:.2f} seconds!")

    if open_ports:
        st.subheader("📌 Open Ports Found")
        st.table(open_ports)
    else:
        st.warning("No open ports found.")
