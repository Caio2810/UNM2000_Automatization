from login import login
from onus import list_unreg_onus
from add_onus import add_onu
from wans import set_wan_service

# Request user information
server = input("server_ip")
user = input("user_login")
password = input("password_login")

# Connect and log in
s, login_response = login(server, user, password)
print("Login response:", login_response)

# Display unauthorized ONUs
unreg_onus = list_unreg_onus(s, olt_name, pon_name)
print("ONUs:", unreg_onus)

# Add ONU
add_response = add_onu(s, olt_name, ponport_location, authtype, onu_index, name, onutype)
print("Add ONU response:", add_response)

# Configure WANService line
wan_response = set_wan_service(s, olt_name, ponport_location, onu_index, status, mode, connecttype, vlan, cos, qos, nat, ipmode, proxy, pppoeusername, pppoepassword, pppoename, pppoemode, uport, ssidno)
print("WAN Service response:", wan_response)
