from login import send_command

def list_unreg_onus(socket, olt_name, pon_name):
    list_command = f'LST-UNREGONU::OLTID={olt_name},PONID={pon_name}:CTAG::;'
    response = send_command(socket, list_command)
    return response
