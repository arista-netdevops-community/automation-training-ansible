import requests
from jinja2 import Environment, FileSystemLoader
from pprint import PrettyPrinter

# disable warnings about self-signed certs
import urllib3
urllib3.disable_warnings()

CVP_IP = "192.168.0.5"
              
# TODO: USE YOUR CREDENTIALS
USERNAME = ''
PASSWORD = ''

if __name__ == '__main__':
    pp = PrettyPrinter()
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template("example.j2")

    with open('this.will.not.work.for.you') as infile:
        access_token = infile.read()

    s = requests.session()
    s.verify = False
    s.cookies.set("access_token", access_token)

    # TODO: Change 'imageurl' to the actual endpoint you find in the REST API explorer
    r = s.get('https://{}/imageurl'.format(CVP_IP))
    response = r.json()
    # TODO: Store the result in a variable
    # images = ...
    
    # TODO: Change 'containerurl' to the actual endpoint you find in the REST API explorer
    r = s.get('https://{}/containerurl'.format(CVP_IP))
    response = r.json()
    # TODO: Store the result in a variable
    # containers = ...


    # Pass the data you collected above to the jinja tempalte
    print(template.render(images=images, containers=containers))