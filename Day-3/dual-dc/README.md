# avd-evpn-l3ls-atd

## Prerequisites

Run `ansible-galaxy collection list` and check the `arista.cvp` version and make sure it's 3.4.0 or
newer. 

To install arista.cvp 3.4.0 type: `ansible-galaxy collection install arista.cvp:=3.4.0`

Check the cvprac version with `pip freeze | grep cvprac` and see if it's 1.2.0 and newer. 

To install cvprc 1.2.0 type: `pip install cvprac==1.2.0`.
## Getting Started

### Lab 1 - running our first AVD playbooks

1\. Got to your Day3 directory and update the username and RADIUS passwords in all the necessary files:
- [inventory.yml](./inventory.yml) (clear-text)
- [AVD_LAB.yml](./group_vars/AVD_LAB.yml) (sha512 only)
- [cv_server.yml](./host_vars/cv_server.yml) (clear-text)
- [host1-day3.cfg](./configlets/host1-day3.cfg) (as is in the running-config)
- [host2-day3.cfg](./configlets/host2-day3.cfg) (as is in the running-config)

> NOTE: only sha512 passwords are supported on AVD which will be needed in the `AVD_LAB.yaml`. 
> One easy way to generate the hash is to go to one of the vEOS boxes like cvx set the default to sha512
> and configure the `arista` username again
> e.g.: 

```shell
cvx01(config)#management defaults 
cvx01(config-mgmt-defaults)#secret hash sha512 
cvx01(config-mgmt-defaults)#exit
cvx01(config)#username arista secret aristae3
```

Then you can grab the hash from the running-config.

#### Read this if the topology is using cEOS-lab (otherwise skip to the next step)

If ATD is deployed using cEOS-lab devices, chances are that they have `Management0` interface instead of `Management1`
In that case please:
- update [AVD_LAB.yml](./group_vars/AVD_LAB.yml) and change the interface name for the `ntp.local_interface.name`
and also add `mgmt_interface: Management0` and the end of the file.
- update [host1-day3.cfg](./configlets/host1-day3.cfg) and replace `Management1` with `Management0` (everywhere)
- update [host2-day3.cfg](./configlets/host2-day3.cfg) and replace `Management1` with `Management0` (everywhere)

2\. Execute the deploy config playbook to configure your leafs and spines

`ansible-playbook dc-fabric-deploy-cvp.yml`

3\. Once the playbook has finished, go to CVP and execute the change control in parallel and wait for 
it to finish.

Do some sanity checks from CVP:
- verify mlag status is active
- verify that you can see your vlan to VNI mappings


4\. Update the host configurations

`ansible-playbook dc-configure-hosts.yml`

Do some sanity checks on the CLI:
- check if the port-channels are up and vlan 120 is propagated
- ping SVI IP from host1 to host 2 and vice-versa

### Lab 2

Modify your AVD input data and provision a new web zone for Tenant A:
- use `vlan 124`
- call the zone: `Tenant_A_WEBZone_4`
- use a similar SVI IP address as for the other webzones

Validate that your changes work from host1 to host2.

### Lab 3

Modify your AVD input data and add back the initial AAA config

i.e. all your leafs and spines should have the following generated from AVD:

```
radius-server host 192.168.0.1 key 7 <Key>
!
aaa group server radius atds
   server 192.168.0.1
!
aaa authentication login default group atds local
aaa authorization exec default group atds local
aaa authorization commands all default local
```

### Lab 4

You might have noticed that the MLAG port-channel only has one interface configured towards the servers on each leaf!
Add the other interface into the port-channel as well.