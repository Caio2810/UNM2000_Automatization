from login import send_command

def add_onu(socket, olt_name, ponport_location, authtype, onu_index, name, onutype):
    add_command = f'ADD-ONU::OLTID={olt_name},PONID={ponport_location}:CTAG::AUTHTYPE={authtype},ONUID={onu_index},NAME={name},ONUTYPE={onutype};'
    response = send_command(socket, add_command)
    return response
