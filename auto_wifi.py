import json
import templates
import wifi

def apply():
    with open('auto_wifi.json') as f:
        known = json.load(f)
        print(f"Known knetworks: {[network['ssid'] for network in known]}")
        found = [network.ssid for network in wifi.radio.start_scanning_networks()]
        print(f"Found knetworks: {found}")
        wifi.radio.stop_scanning_networks()
        for network in known:
            if network['ssid'] in found:
                print(f"Found known network {network['ssid']}")
                print("Applying all templates")
                templates.apply_all(network)
                break
