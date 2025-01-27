
Port Scanner GUI is a simple application designed to help users scan the ports of a target IP address or hostname. It allows you to check for open or closed ports within a specified range using a graphical user 
interface (GUI) built with `Tkinter`. The scanner leverages socket connections to determine the port status, providing results in a user-friendly output window.

Features-
- Graphical interface for ease of use.
- Specify target IP address or hostname.
- Scan ports within a custom range (e.g., 1 to 65535).
- Displays open and closed ports in real-time.
- Error handling for invalid input or unreachable hosts.

How it works
1. Enter the **Target IP Address** or **Hostname** you want to scan.
2. Specify the **Start Port** and **End Port** of the range to scan.
3. Click the **Scan** button to start the scanning process.
4. The output displays:
   - Open ports: Indicated with a positive status (`Port X is open`).
   - Closed ports: Indicated with a negative status (`Port X is closed`).
