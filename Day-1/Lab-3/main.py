import requests
from jinja2 import Environment, FileSystemLoader
from pprint import PrettyPrinter

# disable warnings about self-signed certs
import urllib3
urllib3.disable_warnings()

CVP_IP = "192.168.0.5"
              
# USE YOUR CREDENTIALS
USERNAME = ''
PASSWORD = ''

if __name__ == '__main__':
    pp = PrettyPrinter()
    env = Environment(loader=FileSystemLoader("/home/coder/project/labfiles/day1/lab3/"))
    template = env.get_template("pretty.j2")

    with open('/home/coder/project/labfiles/day1/lab3/this.will.not.work.for.you') as infile:
        access_token = infile.read()

    s = requests.session()
    s.verify = False
    s.cookies.set("access_token", access_token)

    r = s.get('https://{}/cvpservice/image/getImages.do?startIndex=0&endIndex=0'.format(CVP_IP))
    response = r.json()
    eos_images = [x['name'] for x in response['data']]
    
    r = s.get('https://{}/cvpservice/inventory/containers'.format(CVP_IP))
    response = r.json()
    containers = [x['Name'] for x in response]

    
    print(template.render(images=eos_images, containers=containers))