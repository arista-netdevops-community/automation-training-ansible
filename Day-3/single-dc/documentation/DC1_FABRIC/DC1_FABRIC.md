# DC1_FABRIC

## Table of Contents

- [DC1_FABRIC](#dc1fabric )
  - [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Topology](#fabric-topology)
  - [Fabric IP Allocation](#fabric-ip-allocation)
    - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
    - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
    - [Overlay Loopback Interfaces (BGP EVPN Peering)](#overlay-loopback-interfaces-bgp-evpn-peering)
    - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
    - [VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-leafs-only)
    - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| Node | Management IP | Platform |
| ---- | ------------- | -------- |
| DC1-SPINE1 | 10.83.13.212/24 | vEOS-LAB |
| DC1-SPINE2 | 10.83.13.213/24 | vEOS-LAB |
| DC1-LEAF1 | 10.83.13.214/24 | vEOS-LAB |
| DC1-LEAF2 | 10.83.13.215/24 | vEOS-LAB |
| DC1-LEAF3 | 10.83.13.216/24 | vEOS-LAB |
| DC1-LEAF4 | 10.83.13.217/24 | vEOS-LAB |

## Fabric Topology

| Type | Leaf Node | Leaf Interface | Peer Node | Peer Interface |
| ---- | --------- | -------------- | --------- | -------------- |
| L3 Leaf | DC1-LEAF1 | Ethernet1 | DC1-SPINE1 | Ethernet1 |
| L3 Leaf | DC1-LEAF1 | Ethernet2 | DC1-SPINE2 | Ethernet1 |
| L3 Leaf | DC1-LEAF2 | Ethernet1 | DC1-SPINE1 | Ethernet2 |
| L3 Leaf | DC1-LEAF2 | Ethernet2 | DC1-SPINE2 | Ethernet2 |
| L3 Leaf | DC1-LEAF3 | Ethernet1 | DC1-SPINE1 | Ethernet3 |
| L3 Leaf | DC1-LEAF3 | Ethernet2 | DC1-SPINE2 | Ethernet3 |
| L3 Leaf | DC1-LEAF4 | Ethernet1 | DC1-SPINE1 | Ethernet4 |
| L3 Leaf | DC1-LEAF4 | Ethernet2 | DC1-SPINE2 | Ethernet4 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| P2P Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ----------- | ------------------- | ------------------ | ------------------ |
| 172.18.255.0/24 | 256 | 16 | 6.25 % |

### Point-To-Point Links Node Allocation

| Leaf Node | Leaf Interface | Leaf IP Address | Spine Node | Spine Interface | Spine IP Address |
| --------- | -------------- | --------------- | ---------- | --------------- | ---------------- |
| DC1-LEAF1 | Ethernet1 | 172.18.255.1/31 | DC1-SPINE1 | Ethernet1 | 172.18.255.0/31 |
| DC1-LEAF1 | Ethernet2 | 172.18.255.3/31 | DC1-SPINE2 | Ethernet1 | 172.18.255.2/31 |
| DC1-LEAF2 | Ethernet1 | 172.18.255.5/31 | DC1-SPINE1 | Ethernet2 | 172.18.255.4/31 |
| DC1-LEAF2 | Ethernet2 | 172.18.255.7/31 | DC1-SPINE2 | Ethernet2 | 172.18.255.6/31 |
| DC1-LEAF3 | Ethernet1 | 172.18.255.9/31 | DC1-SPINE1 | Ethernet3 | 172.18.255.8/31 |
| DC1-LEAF3 | Ethernet2 | 172.18.255.11/31 | DC1-SPINE2 | Ethernet3 | 172.18.255.10/31 |
| DC1-LEAF4 | Ethernet1 | 172.18.255.13/31 | DC1-SPINE1 | Ethernet4 | 172.18.255.12/31 |
| DC1-LEAF4 | Ethernet2 | 172.18.255.15/31 | DC1-SPINE2 | Ethernet4 | 172.18.255.14/31 |

### Overlay Loopback Interfaces (BGP EVPN Peering)

| Overlay Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------------ | ------------------- | ------------------ | ------------------ |
| 192.168.255.0/24 | 256 | 6 | 2.35 % |

### Loopback0 Interfaces Node Allocation

| Node | Loopback0 |
| ---- | --------- |
| DC1-SPINE1 | 192.168.255.1/32 |
| DC1-SPINE2 | 192.168.255.2/32 |
| DC1-LEAF1 | 192.168.255.3/32 |
| DC1-LEAF2 | 192.168.255.4/32 |
| DC1-LEAF3 | 192.168.255.5/32 |
| DC1-LEAF4 | 192.168.255.6/32 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (Leafs Only)

| VTEP Loopback Summary | Available Addresses | Assigned addresses | Assigned Address % |
| --------------------- | ------------------- | ------------------ | ------------------ |
| 192.168.254.0/24 | 256 | 4 | 1.57 % |

### VTEP Loopback Node allocation

| Node | Loopback1 |
| ---- | --------- |
| DC1-LEAF1 | 192.168.254.3/32 |
| DC1-LEAF2 | 192.168.254.3/32 |
| DC1-LEAF3 | 192.168.254.5/32 |
| DC1-LEAF4 | 192.168.254.5/32 |
