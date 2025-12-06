# Mitmproxy Proxy Server

This document provides instructions on how to set up and run the mitmproxy server using the provided `main.py` script. This proxy allows you to intercept and log network traffic from your computer or mobile devices.

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1.  **Install mitmproxy:**
    Open your terminal or command prompt and install `mitmproxy` using pip:

    ```bash
    pip install mitmproxy
    ```

2.  **Get the script:**
    Clone this repository or download the `main.py` script to your local machine.
    ```bash
    git clone https://github.com/muhammadAbdulMannan2022/myproxy.git
    ```

## Running the Proxy Server

The proxy server is run using the `mitmdump` command, which is part of the `mitmproxy` suite.

### For Local Traffic (On the same machine)

To run the proxy and only capture traffic from your local machine, use the following command:

```bash
mitmdump -s main.py
```

### For External Devices (Android, iOS, etc.)

To allow other devices on your network to connect to the proxy, you need to bind the proxy to all network interfaces.

1.  **Find your computer's local IP address.**

    - **Windows:** Open Command Prompt and type `ipconfig`. Look for the "IPv4 Address".
    - **macOS/Linux:** Open a terminal and type `ifconfig` or `ip addr`. Look for the `inet` address.

2.  **Run the proxy:**
    Use the following command, which starts the proxy on port 8080. You can use a different port if you prefer.

    ```bash
    mitmdump -s main.py --listen-host 0.0.0.0 --listen-port 8080
    ```

## Configuring Client Devices

To capture traffic from a mobile device, you must configure it to use the proxy and install the mitmproxy CA certificate.

### On your mobile device:

1.  Connect to the **same Wi-Fi network** as your computer running the proxy.
2.  Navigate to your Wi-Fi settings and configure a **manual HTTP proxy**.
    - **Server/Host:** Enter your computer's local IP address (from the step above).
    - **Port:** Enter the port you are using (e.g., `8080`).

### Installing the CA Certificate

With the proxy configured, open a web browser on your mobile device and go to:

**http://mitm.it**

Follow the instructions for your specific operating system to download and install the certificate.

#### Android Configuration

1.  After downloading the certificate from `mitm.it`, you may be prompted to name it. Give it a descriptive name (e.g., "mitmproxy").
2.  The system will require you to set a PIN or password for your device if you haven't already.

#### iOS Configuration

1.  After downloading the certificate from `mitm.it`, go to **Settings > General > VPN & Device Management**.
2.  Tap on the downloaded "mitmproxy" profile and tap **Install**.
3.  After installation, go to **Settings > General > About > Certificate Trust Settings**.
4.  Find the "mitmproxy" root certificate and **enable full trust** for it.

**Note:** If you cannot connect to the internet on your device after setting up the proxy, make sure the `mitmdump` script is running on your computer.

## Logging

All intercepted traffic will be processed by `main.py`.

- **Console:** Real-time logs are printed to the console where `mitmdump` is running.
- **File:** A detailed log of requests and responses is saved to the `mitm_logs.txt` file in the same directory.
