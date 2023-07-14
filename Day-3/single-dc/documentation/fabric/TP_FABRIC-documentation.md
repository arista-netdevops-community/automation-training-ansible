# TP_FABRIC

# Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

# Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision |
| --- | ---- | ---- | ------------- | -------- | -------------------------- |
| TP_FABRIC | l3leaf | tp-avd-leaf1 | 10.83.13.214/24 | vEOS-LAB | Provisioned |
| TP_FABRIC | l3leaf | tp-avd-leaf2 | 10.83.13.215/24 | vEOS-LAB | Provisioned |
| TP_FABRIC | l3leaf | tp-avd-leaf3 | 10.83.13.216/24 | vEOS-LAB | Provisioned |
| TP_FABRIC | l3leaf | tp-avd-leaf4 | 10.83.13.217/24 | vEOS-LAB | Provisioned |
| TP_FABRIC | spine | tp-avd-spine1.tst | 10.83.13.212/24 | vEOS-LAB | Provisioned |
| TP_FABRIC | spine | tp-avd-spine2 | 10.83.13.213/24 | vEOS-LAB | Provisioned |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

## Fabric Switches with inband Management IP
| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

# Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | tp-avd-leaf1 | Ethernet1 | spine | tp-avd-spine1.tst | Ethernet1 |
| l3leaf | tp-avd-leaf1 | Ethernet2 | spine | tp-avd-spine2 | Ethernet1 |
| l3leaf | tp-avd-leaf1 | Ethernet3 | mlag_peer | tp-avd-leaf2 | Ethernet3 |
| l3leaf | tp-avd-leaf1 | Ethernet5 | mlag_peer | tp-avd-leaf2 | Ethernet5 |
| l3leaf | tp-avd-leaf2 | Ethernet1 | spine | tp-avd-spine1.tst | Ethernet2 |
| l3leaf | tp-avd-leaf2 | Ethernet2 | spine | tp-avd-spine2 | Ethernet2 |
| l3leaf | tp-avd-leaf3 | Ethernet1 | spine | tp-avd-spine1.tst | Ethernet3 |
| l3leaf | tp-avd-leaf3 | Ethernet2 | spine | tp-avd-spine2 | Ethernet3 |
| l3leaf | tp-avd-leaf3 | Ethernet3 | mlag_peer | tp-avd-leaf4 | Ethernet3 |
| l3leaf | tp-avd-leaf3 | Ethernet5 | mlag_peer | tp-avd-leaf4 | Ethernet5 |
| l3leaf | tp-avd-leaf4 | Ethernet1 | spine | tp-avd-spine1.tst | Ethernet4 |
| l3leaf | tp-avd-leaf4 | Ethernet2 | spine | tp-avd-spine2 | Ethernet4 |

# Fabric IP Allocation

## Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 172.18.255.0/24 | 256 | 16 | 6.25 % |

## Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| tp-avd-leaf1 | Ethernet1 | 172.18.255.41/31 | tp-avd-spine1.tst | Ethernet1 | 172.18.255.40/31 |
| tp-avd-leaf1 | Ethernet2 | 172.18.255.43/31 | tp-avd-spine2 | Ethernet1 | 172.18.255.42/31 |
| tp-avd-leaf2 | Ethernet1 | 172.18.255.5/31 | tp-avd-spine1.tst | Ethernet2 | 172.18.255.4/31 |
| tp-avd-leaf2 | Ethernet2 | 172.18.255.7/31 | tp-avd-spine2 | Ethernet2 | 172.18.255.6/31 |
| tp-avd-leaf3 | Ethernet1 | 172.18.255.9/31 | tp-avd-spine1.tst | Ethernet3 | 172.18.255.8/31 |
| tp-avd-leaf3 | Ethernet2 | 172.18.255.11/31 | tp-avd-spine2 | Ethernet3 | 172.18.255.10/31 |
| tp-avd-leaf4 | Ethernet1 | 172.18.255.13/31 | tp-avd-spine1.tst | Ethernet4 | 172.18.255.12/31 |
| tp-avd-leaf4 | Ethernet2 | 172.18.255.15/31 | tp-avd-spine2 | Ethernet4 | 172.18.255.14/31 |

## Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 192.168.251.0/24 | 256 | 2 | 0.79 % |
| 192.168.255.0/24 | 256 | 4 | 1.57 % |

## Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| TP_FABRIC | tp-avd-leaf1 | 192.168.255.11/32 |
| TP_FABRIC | tp-avd-leaf2 | 192.168.255.2/32 |
| TP_FABRIC | tp-avd-leaf3 | 192.168.255.3/32 |
| TP_FABRIC | tp-avd-leaf4 | 192.168.255.4/32 |
| TP_FABRIC | tp-avd-spine1.tst | 192.168.251.1/32 |
| TP_FABRIC | tp-avd-spine2 | 192.168.251.2/32 |

## VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 4 | 1.57 % |

## VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| TP_FABRIC | tp-avd-leaf1 | 192.168.254.11/32 |
| TP_FABRIC | tp-avd-leaf2 | 192.168.254.11/32 |
| TP_FABRIC | tp-avd-leaf3 | 192.168.254.3/32 |
| TP_FABRIC | tp-avd-leaf4 | 192.168.254.3/32 |
