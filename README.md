# get_headers
A lightweight HTTP header information gathering tool built with Python.
# Get Headers 🦅

[![Platform](https://img.shields.io/badge/Platform-Kali%20Linux-blueviolet?style=for-the-badge&logo=kalilinux)](https://www.kali.org)
[![Language](https://img.shields.io/badge/Language-Python%203-blue?style=for-the-badge&logo=python)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT%20%2B%20Custom-green?style=for-the-badge)](LICENSE)
[![Stars](https://img.shields.io/github/stars/BlackCrow-Code/get_headers?style=for-the-badge&color=yellow)](https://github.com/BlackCrow-Code/get_headers/stargazers)

A lightweight HTTP header information gathering tool built with Python.

Get Headers retrieves HTTP response headers from a target URL or IP address,
supports custom request headers, and allows exporting results into JSON format.

Designed for penetration testers, security researchers, network administrators,
and students learning web technologies.

---

# 🚀 Features

- Retrieve HTTP response headers
- Support URL and IP address targets
- Add custom HTTP request headers
- JSON export support
- Clean terminal interface using Rich
- Simple command-line usage
- Lightweight and fast
- Built with Python

---

# 📋 Information Collected

The tool can display common HTTP headers such as:

| Header | Example |
|---|---|
| Server | Web server information |
| Content-Type | Response content type |
| Content-Length | Response size |
| Cookies | Set-Cookie information |
| Security Headers | Protection-related headers |

---

# 📸 Screenshots

Example:

<img width="802" height="310" alt="Screenshot From 2026-07-18 09-28-35" src="https://github.com/user-attachments/assets/a1c20d22-c1b1-417d-869f-d5f0b44a9cd0" />





# 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/BlackCrow-Code/get_headers.git
```

Enter directory:

```bash
cd get_headers
```

Install requirements:

```bash
pip install -r requirements.txt
```

---

# ▶ Usage

Basic header lookup:

```bash
python3 get_headers.py -t <target>
```

Using HTTPS:

```bash
python3 get_headers.py -t <https://target>
```

Send custom header:

```bash
python3 get_headers.py -t <target> -he "User-Agent: Mozilla/5.0"
```

Save results as JSON:

```bash
python3 get_headers.py -t <target>-s result
```

---

# 📂 Project Structure

```
get_headers/

├── get_headers.py
├── requirements.txt
├── README.md
├── LICENSE
```

---

# ⚠ Disclaimer

This tool is intended only for educational purposes, authorized security
testing, and security research.

Always obtain permission before testing systems that you do not own.

The developer is not responsible for any misuse of this software.

---

# 📜 License

Licensed under the MIT License with additional custom developer terms.

See the LICENSE file for complete details.

---

# 👨‍💻 Developer

BlackCrow-Code<img width="802" height="310" alt="Screenshot From 2026-07-18 09-28-35" src="https://github.com/user-attachments/assets/3fe6c782-8a40-4be9-be99-b1b22f5a84e8" />
