# Not available in main.py, but you can add it if you need it

from login import send_command

def del_onu(socket, olt_name, ponport_location, onuidtype, onu_index):
    del_command = f'DEL-ONU::OLTID={olt_name},PONID={ponport_location}:CTAG::ONUIDTYPE={onuidtype},ONUID={onu_index};'
    response = send_command(socket, del_command)
    return response
