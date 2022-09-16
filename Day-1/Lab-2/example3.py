import requests
from jinja2 import Environment, FileSystemLoader
from pprint import PrettyPrinter

# disable warnings about self-signed certs
import urllib3
urllib3.disable_warnings()

DEVICE_IPS = ['192.168.0.10',
              '192.168.0.11',
              '192.168.0.12',
              '192.168.0.13',
              '192.168.0.14',
              '192.168.0.15',
              ]
           
# USE YOUR CREDENTIALS
USERNAME = ''
PASSWORD = ''

if __name__ == '__main__':
    payload = {'jsonrpc': '2.0',
               'method': 'runCmds',
               'params': {
                 'version': 1,
                 'cmds': ['show lldp neighbors detail', 
                          'show hostname']
               },
               'id': '1'
              }
    device_outputs = {}

    pp = PrettyPrinter()
    env = Environment(loader=FileSystemLoader("."), lstrip_blocks=True, trim_blocks=True)
    template = env.get_template("example3.j2")

    for device in DEVICE_IPS:
        r = requests.post('https://{}:443/command-api'.format(device), json=payload, auth=(USERNAME, PASSWORD), verify=False)
        response = r.json()
        #pp.pprint(response)
        hostname = response['result'][1]['hostname']
        lldp_neighbors = response['result'][0]['lldpNeighbors']
        device_outputs[hostname] = {}
        device_outputs[hostname]['lldpNeighbors'] = lldp_neighbors
    else:
        pp.pprint(device_outputs)
        print(template.render(devices=device_outputs))
