from cvplibrary import CVPGlobalVariables, GlobalVariableNames, Device

ips  = {"leaf1": "192.168.0.12",
        "leaf2": "192.168.0.13",
        "leaf3": "192.168.0.14",
        "leaf4": "192.168.0.15",
        "spine1": "192.168.0.10",
        "spine2": "192.168.0.11"
} 

for i in ips:
  device = Device(ips[i])
 
  res = device.runCmds(['enable','show interfaces Management1'])
  print(i + ' = ' + res[1]['response']['interfaces']['Management1']['physicalAddress'])