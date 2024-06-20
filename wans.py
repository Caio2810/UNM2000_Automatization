from login import send_command

def set_wan_service(socket, olt_name, ponport_location, onu_index, status, mode, connecttype, vlan, cos, qos, nat, ipmode, proxy, pppoeusername, pppoepassword, pppoename, pppoemode, uport, ssidno):
    wan_command = f'SET-WANSERVICE::OLTID={olt_name},PONID={ponport_location},ONUID={onu_index}:CTAG::STATUS={status},MODE={mode},CONNTYPE={connecttype},VLAN={vlan},COS={cos},QOS={qos},NAT={nat},IPMODE={ipmode},PPPOEPROXY={proxy},PPPOEUSER={pppoeusername},PPPOEPASSWD={pppoepassword},PPPOENAME={pppoename},PPPOEMODE={pppoemode},UPORT={uport},SSID={ssidno},WANSVC=1;'
    response = send_command(socket, wan_command)
    return response
