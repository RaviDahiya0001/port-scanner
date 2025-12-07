🔍 Detailed Port Scanner

A fast, multi‑threaded, Python‑based port scanner that detects open ports, identifies common services, and grabs server banners — similar to a lightweight Nmap.

🚀 Features

Multi‑threaded scanning (super fast)

Scans ports 1–10,000

Service detection (FTP, SSH, HTTP, HTTPS, MySQL, Redis, etc.)

Banner grabbing for server details

Domain & IP support

Detailed summary output

Lightweight & beginner‑friendly

📂 Project Structure
📁 Port Scanner
│── detailed_port_scanner.py
│── README.md
│── LICENSE

🛠 Requirements

Python 3.x

No extra libraries (uses only built‑in modules)

▶️ How to Run

Open terminal in project folder:

cd "D:\Project\Port Scanner"
python detailed_port_scanner.py


Then enter target:

Example:

Enter Target IP/Domain: 127.0.0.1

🧪 Output Example
Scanning Target: 127.0.0.1
---------------------------------------------
[OPEN] Port 22   | SSH             | Banner: SSH-2.0-OpenSSH_8.2
[OPEN] Port 80   | HTTP            | Banner: Apache/2.4.41 (Ubuntu)
[OPEN] Port 443  | HTTPS           | Banner: No Banner
...
---------------------------------------------
Scan Completed!
Total Time: 4.82 seconds

📘 How It Works

Creates hundreds of threads

Each thread checks a port

If port is open → service name + banner fetches

Summarizes open ports

💡 Use Cases

Security testing

Ethical hacking

Local network analysis

Finding exposed services

Server auditing

⚠️ Legal Disclaimer

This tool is for educational & ethical testing.
Do NOT scan systems without permission.

📜 License

This project is licensed under the MIT License.
See LICENSE file for details.

🤝 Contributing

Pull requests are welcome!
Open an issue for feature requests.

⭐ Support

If you like this project, please give it a ⭐ on GitHub!