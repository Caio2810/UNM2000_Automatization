# UNM2000 and FiberHome ONUs Management With Python

## Description
This Python script provides a management tool for the UNM2000 platform and FiberHome ONUs, allowing users to perform various operations such as logging in, listing unauthorized ONUs, adding/removing ONUs and even configuring WAN services.

I created this code to help me automate some tasks I do at work involving UNM2000 and FiberHome modems.

Feel free to clone this repository and modify it according to your needs!

## Requirements
- Python
- UNM2000 server accessible over TCP/IP

## Usage
<strong>(make sure to fill in the variables related to the OLT/ONU information at each .py file)<strong>
1. Run the main script: `python main.py`
2. Follow the on-screen prompts to enter the server IP, admin login, and admin password
3. The script will connect to the UNM2000 server and perform the requested operations.

## Commands
- `login`: Logs into the UNM2000 server with the provided credentials.
- `list_unreg_onus`: Lists unauthorized ONUs.
- `add_onu`: Adds a new ONU to the OLT.
- `set_wan_service`: Configures WAN services for an ONU.
- `del_onu`: Removes an ONU from the OLT.

---

## Using PuTTY

You can also use UNM2000 command lines in PuTTY. Initially, you only need to make an access (in this case, Telnet was used):

![PuTTY1](https://i.imgur.com/YancsTN.png)

After establishing the connection, you can enter the commands in the console (which are listed in the TL1commands.txt file):

![PuTTY2](https://i.imgur.com/bGXW4Qq.png)

---

<strong>*** All commands and information were taken from the official UNM2000's manual pdf. Any doubts or additional information can be obtained through it.*** <strong>
