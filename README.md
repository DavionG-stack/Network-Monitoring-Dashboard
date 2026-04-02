# 📡 Network Monitoring Dashboard
A lightweight IT monitoring tool built with Python and Flask that simulates real-time network device monitoring through a web-based dashboard.

## 🚀 Overview
This project monitors multiple network devices using ICMP ping requests and displays their real-time status in a simple, modern web dashboard.

It simulates a basic **Network Operations Center (NOC)** view used in IT support environments.

## ✨ Features
- 📶 Monitor multiple devices (IP addresses / domains)
- 🟢 Real-time UP / DOWN status detection
- 🔁 Auto-refreshing web dashboard
- ⚠️ Status change detection
- 🌐 Web-based UI using Flask

## 🛠️ Tech Stack

- Python 3
- Flask
- HTML / CSS / JavaScript
- Windows ping (ICMP)

## 📁 Project Structure
```bash
network-monitoring-dashboard/
│
├── app.py                 # Flask web server (dashboard backend)
├── monitor.py             # Network monitoring / ping logic
├── devices.txt            # List of devices to monitor
├── requirements.txt       # Python dependencies
│
├── templates/
│   └── dashboard.html     # Web dashboard UI
│
├── static/
│   └── style.css          # Dashboard styling
│
├── assets/
│   └── dashboard.png      # Screenshot of the dashboard
│
└── README.md              # Project documentation
```

## ⚙️ Installation & Setup

Follow these steps to run the project locally on your machine.

### 1. Clone the repository

```bash
git clone https://github.com/DavionG-stack/network-monitoring-dashboard.git
cd network-monitoring-dashboard
```
### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Add devices to monitor
Edit devices.txt and add IP addresses or hostnames (I used Google and Cloudflare DNS)

### 4. Run the application
```bash
python app.py
```

### 5. Open the dashboard
Open your browser and go to:
http://127.0.0.1:5000

<div align="center">

### ✨ <b>Ta-da! You’re now running the Network Monitoring Dashboard</b>

</div>
