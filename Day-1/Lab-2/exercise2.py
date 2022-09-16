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
              '192.168.0.16',
              '192.168.0.17'
              ]
              
# USE YOUR CREDENTIALS
USERNAME = ''
PASSWORD = ''

if __name__ == '__main__':
    payload = {'jsonrpc': '2.0',
               'method': 'runCmds',
               'params': {
                 'version': 1,
                 'cmds': ['show version', 
                          'show hostname']
               },
               'id': '1'
              }
    device_outputs = {}

    pp = PrettyPrinter()
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("exercise2.j2")

    for device in DEVICE_IPS:
        r = requests.post('https://{}:443/command-api'.format(device), json=payload, auth=(USERNAME, PASSWORD), verify=False)
        response = r.json()
        #pp.pprint(response)
        serialNumber = response['result'][0]['serialNumber']
        hostname = response['result'][1]['hostname']
        eos = response['result'][0]['version']
        device_outputs[hostname] = {'serial': serialNumber}
        device_outputs[hostname]['eos'] = eos
        # TODO: Add the architecture of EOS from the 'show version' output to the 'device_outputs' dictionary so that 
        # the info can be used in the jinja template
    else:
        pp.pprint(device_outputs)
        print(template.render(devices=device_outputs))