# leaf-3

## Management Interfaces

### Management Interfaces Summary

| Management Interface | description | VRF | IP Address | Gateway |
| -------------------- | ----------- | --- | ---------- | ------- |
| Management1 | oob_management | MGMT | 10.83.13.216/24 | 10.83.13.1 |

### Management Interfaces Device Configuration

```eos
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.83.13.216/24
!
```

## Hardware Counters

No Hardware Counters defined

## TerminAttr Daemon

### TerminAttr Daemon Summary

| CV Compression | Ingest gRPC URL | Ingest Authentication Key | Smash Excludes | Ingest Exclude | Ingest VRF |  NTP VRF |
| -------------- | --------------- | ------------------------- | -------------- | -------------- | ---------- | -------- |
| gzip | 10.83.12.79:9910 |  | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | MGMT | MGMT |

### TerminAttr Daemon Device Configuration

```eos
daemon TerminAttr
   exec /usr/bin/TerminAttr -ingestgrpcurl=10.83.12.79:9910 -cvcompression=gzip -ingestauth=key, -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -ingestvrf=MGMT -taillogs
   no shutdown
!
```

## Internal VLAN allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Configuration

```eos
vlan internal order ascending range 1006 1199
!
```

## Name Servers

### Name Servers Summary

| Name Server | Source VRF |
| ----------- | ---------- |
| 172.22.22.40 | MGMT |
| 8.8.8.8 | MGMT |

### Name Servers Device Configuration

```eos
ip name-server vrf MGMT 172.22.22.40
ip name-server vrf MGMT 8.8.8.8
!
```

## NTP

### NTP Summary

Local Interface: Management1
VRF: MGMT

| Node | Primary |
| ---- | ------- |
| 172.22.22.50 | True |

### NTP Device Configuration

```eos
ntp local-interface vrf MGMT Management1
ntp server vrf MGMT 172.22.22.50 prefer
!
```

## Spanning Tree

### Spanning Tree Summary

Mode: mstp

**MSTP Instance and Priority**:

| Instance | Priority |
| -------- | -------- |
| 0 | 4096 |

### Spanning Tree Device Configuration

```eos
spanning-tree mode mstp
no spanning-tree vlan-id 4094
spanning-tree mst 0 priority 4096
!
```

## AAA Authentication

AAA Not Configured

## Local Users

### Local Users Summary

| User | Privilege | role |
| ---- | --------- | ---- |
| cvpadmin | 15 | network-admin |

### Local Users Device Configuration

```eos
username cvpadmin privilege 15 role network-admin secret sha512 $6$WjohQO..cU0/YJq.$FWm8lvRXlxryJap9e8.8NetRLsgSKADgkg2mVNJvxPEgqsGFarTC9wI8o/hz9UZfmHTGNTbTGKpWoEhLHdDv/1
!
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 110 | Tenant_A_OP_Zone_1 | none  |
| 111 | Tenant_A_OP_Zone_2 | none  |
| 120 | Tenant_A_WEB_Zone_1 | none  |
| 121 | Tenant_A_WEBZone_2 | none  |
| 130 | Tenant_A_APP_Zone_1 | none  |
| 131 | Tenant_A_APP_Zone_2 | none  |
| 140 | Tenant_A_DB_BZone_1 | none  |
| 141 | Tenant_A_DB_Zone_2 | none  |
| 160 | Tenant_A_VMOTION | none  |
| 161 | Tenant_A_NFS | none  |
| 210 | Tenant_B_OP_Zone_1 | none  |
| 211 | Tenant_B_OP_Zone_2 | none  |
| 310 | Tenant_C_OP_Zone_1 | none  |
| 311 | Tenant_C_OP_Zone_2 | none  |
| 3009 | MLAG_iBGP_Tenant_A_OP_Zone | LEAF_PEER_L3  |
| 3010 | MLAG_iBGP_Tenant_A_WEB_Zone | LEAF_PEER_L3  |
| 3011 | MLAG_iBGP_Tenant_A_APP_Zone | LEAF_PEER_L3  |
| 3012 | MLAG_iBGP_Tenant_A_DB_Zone | LEAF_PEER_L3  |
| 3019 | MLAG_iBGP_Tenant_B_OP_Zone | LEAF_PEER_L3  |
| 3029 | MLAG_iBGP_Tenant_C_OP_Zone | LEAF_PEER_L3  |
| 4093 | LEAF_PEER_L3 | LEAF_PEER_L3  |
| 4094 | MLAG_PEER | MLAG  |

### VLANs Device Configuration

```eos
vlan 110
   name Tenant_A_OP_Zone_1
!
vlan 111
   name Tenant_A_OP_Zone_2
!
vlan 120
   name Tenant_A_WEB_Zone_1
!
vlan 121
   name Tenant_A_WEBZone_2
!
vlan 130
   name Tenant_A_APP_Zone_1
!
vlan 131
   name Tenant_A_APP_Zone_2
!
vlan 140
   name Tenant_A_DB_BZone_1
!
vlan 141
   name Tenant_A_DB_Zone_2
!
vlan 160
   name Tenant_A_VMOTION
!
vlan 161
   name Tenant_A_NFS
!
vlan 210
   name Tenant_B_OP_Zone_1
!
vlan 211
   name Tenant_B_OP_Zone_2
!
vlan 310
   name Tenant_C_OP_Zone_1
!
vlan 311
   name Tenant_C_OP_Zone_2
!
vlan 3009
   name MLAG_iBGP_Tenant_A_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3010
   name MLAG_iBGP_Tenant_A_WEB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3011
   name MLAG_iBGP_Tenant_A_APP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3012
   name MLAG_iBGP_Tenant_A_DB_Zone
   trunk group LEAF_PEER_L3
!
vlan 3019
   name MLAG_iBGP_Tenant_B_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 3029
   name MLAG_iBGP_Tenant_C_OP_Zone
   trunk group LEAF_PEER_L3
!
vlan 4093
   name LEAF_PEER_L3
   trunk group LEAF_PEER_L3
!
vlan 4094
   name MLAG_PEER
   trunk group MLAG
!
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| MGMT |  disabled |
| Tenant_A_APP_Zone |  enabled |
| Tenant_A_DB_Zone |  enabled |
| Tenant_A_OP_Zone |  enabled |
| Tenant_A_WEB_Zone |  enabled |
| Tenant_B_OP_Zone |  enabled |
| Tenant_C_OP_Zone |  enabled |

### VRF Instances Device Configuration

```eos
vrf instance MGMT
!
vrf instance Tenant_A_APP_Zone
!
vrf instance Tenant_A_DB_Zone
!
vrf instance Tenant_A_OP_Zone
!
vrf instance Tenant_A_WEB_Zone
!
vrf instance Tenant_B_OP_Zone
!
vrf instance Tenant_C_OP_Zone
!
```

## BFD Multihop Interval

### BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 1200 | 1200 | 3 |

### BFD Multihop Device Configuration

```eos
bfd multihop interval 1200 min_rx 1200 multiplier 3
!
```

## Port-Channel Interfaces

### Port-Channel Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (trunk) | Trunk Group | MLAG ID | VRF | IP Address |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | ------- | --- | ---------- |
| Port-Channel3 | MLAG_PEER_leaf-4_Po3 | 1500 | switched | trunk | 2-4094 | LEAF_PEER_L3<br> MLAG | - | - | - |
| Port-Channel4 | server02_PortChannel1 | 1500 | switched | trunk | 210-211 | - | 4 | - | - |

### Port-Channel Interfaces Device Configuration

```eos
interface Port-Channel3
   description MLAG_PEER_leaf-4_Po3
   switchport trunk allowed vlan 2-4094
   switchport mode trunk
   switchport trunk group LEAF_PEER_L3
   switchport trunk group MLAG
!
interface Port-Channel4
   description server02_PortChannel1
   switchport trunk allowed vlan 210-211
   switchport mode trunk
   mlag 4
!
```

## Ethernet Interfaces

### Ethernet Interfaces Summary

| Interface | Description | MTU | Type | Mode | Allowed VLANs (Trunk) | Trunk Group | VRF | IP Address | Channel-Group ID | Channel-Group Type |
| --------- | ----------- | --- | ---- | ---- | --------------------- | ----------- | --- | ---------- | ---------------- | ------------------ |
| Ethernet1 | P2P_LINK_TO_SPINE-1_Ethernet3 | 1500 | routed | access | - | - | - | 172.31.255.9/31 | - | - |
| Ethernet2 | P2P_LINK_TO_SPINE-2_Ethernet3 | 1500 | routed | access | - | - | - | 172.31.255.11/31 | - | - |
| Ethernet3 | MLAG_PEER_leaf-4_Ethernet3 | *1500 | *switched | *trunk | *2-4094 | *LEAF_PEER_L3<br> *MLAG | - | - | 3 | active |
| Ethernet4 | server02_Ethernet1 | *1500 | *switched | *trunk | *210-211 | - | - | - | 4 | active |

*Inherited from Port-Channel Interface

### Ethernet Interfaces Device Configuration

```eos
interface Ethernet1
   description P2P_LINK_TO_SPINE-1_Ethernet3
   no switchport
   ip address 172.31.255.9/31
!
interface Ethernet2
   description P2P_LINK_TO_SPINE-2_Ethernet3
   no switchport
   ip address 172.31.255.11/31
!
interface Ethernet3
   description MLAG_PEER_leaf-4_Ethernet3
   channel-group 3 mode active
!
interface Ethernet4
   description server02_Ethernet1
   channel-group 4 mode active
!
```

## Loopback Interfaces

### Loopback Interfaces Summary

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | EVPN_Overlay_Peering | Global Routing Table | 192.168.255.5/32 |
| Loopback1 | VTEP_VXLAN_Tunnel_Source | Global Routing Table | 192.168.254.5/32 |
| Loopback100 | Tenant_A_OP_Zone_VTEP_DIAGNOSTICS | Tenant_A_OP_Zone | 10.255.1.5/32 |

### Loopback Interfaces Device Configuration

```eos
interface Loopback0
   description EVPN_Overlay_Peering
   ip address 192.168.255.5/32
!
interface Loopback1
   description VTEP_VXLAN_Tunnel_Source
   ip address 192.168.254.5/32
!
interface Loopback100
   description Tenant_A_OP_Zone_VTEP_DIAGNOSTICS
   vrf Tenant_A_OP_Zone
   ip address 10.255.1.5/32
!
```

## VLAN Interfaces

### VLAN Interfaces Summary

| Interface | Description | VRF | IP Address | Virtual | IP Address Secondary | Virtual |
| --------- | ----------- | --- | ---------- | ------- | -------------------- | ------- |
| Vlan110 | Tenant_A_OP_Zone_1 | Tenant_A_OP_Zone  | 10.1.10.1/24 | True | - | - |
| Vlan111 | Tenant_A_OP_Zone_2 | Tenant_A_OP_Zone  | 10.1.11.1/24 | True | - | - |
| Vlan120 | Tenant_A_WEB_Zone_1 | Tenant_A_WEB_Zone  | 10.1.20.1/24 | True | - | - |
| Vlan121 | Tenant_A_WEBZone_2 | Tenant_A_WEB_Zone  | 10.1.21.1/24 | True | - | - |
| Vlan130 | Tenant_A_APP_Zone_1 | Tenant_A_APP_Zone  | 10.1.30.1/24 | True | - | - |
| Vlan131 | Tenant_A_APP_Zone_2 | Tenant_A_APP_Zone  | 10.1.31.1/24 | True | - | - |
| Vlan140 | Tenant_A_DB_BZone_1 | Tenant_A_DB_Zone  | 10.1.40.1/24 | True | - | - |
| Vlan141 | Tenant_A_DB_Zone_2 | Tenant_A_DB_Zone  | 10.1.41.1/24 | True | - | - |
| Vlan210 | Tenant_B_OP_Zone_1 | Tenant_B_OP_Zone  | 10.2.10.1/24 | True | - | - |
| Vlan211 | Tenant_B_OP_Zone_2 | Tenant_B_OP_Zone  | 10.2.11.1/24 | True | - | - |
| Vlan310 | Tenant_C_OP_Zone_1 | Tenant_C_OP_Zone  | 10.3.10.1/24 | True | - | - |
| Vlan311 | Tenant_C_OP_Zone_2 | Tenant_C_OP_Zone  | 10.3.11.1/24 | True | - | - |
| Vlan3009 | MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone | Tenant_A_OP_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan3010 | MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone | Tenant_A_WEB_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan3011 | MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone | Tenant_A_APP_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan3012 | MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone | Tenant_A_DB_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan3019 | MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone | Tenant_B_OP_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan3029 | MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone | Tenant_C_OP_Zone  | 10.255.251.4/31 | - | - | - |
| Vlan4093 | MLAG_PEER_L3_PEERING | Global Routing Table  | 10.255.251.4/31 | - | - | - |
| Vlan4094 | MLAG_PEER | Global Routing Table  | 10.255.252.4/31 | - | - | - |

### VLAN Interfaces Device Configuration

```eos
interface Vlan110
   description Tenant_A_OP_Zone_1
   vrf Tenant_A_OP_Zone
   ip address virtual 10.1.10.1/24
!
interface Vlan111
   description Tenant_A_OP_Zone_2
   vrf Tenant_A_OP_Zone
   ip address virtual 10.1.11.1/24
!
interface Vlan120
   description Tenant_A_WEB_Zone_1
   vrf Tenant_A_WEB_Zone
   ip address virtual 10.1.20.1/24
!
interface Vlan121
   description Tenant_A_WEBZone_2
   vrf Tenant_A_WEB_Zone
   ip address virtual 10.1.21.1/24
!
interface Vlan130
   description Tenant_A_APP_Zone_1
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.30.1/24
!
interface Vlan131
   description Tenant_A_APP_Zone_2
   vrf Tenant_A_APP_Zone
   ip address virtual 10.1.31.1/24
!
interface Vlan140
   description Tenant_A_DB_BZone_1
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.40.1/24
!
interface Vlan141
   description Tenant_A_DB_Zone_2
   vrf Tenant_A_DB_Zone
   ip address virtual 10.1.41.1/24
!
interface Vlan210
   description Tenant_B_OP_Zone_1
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.10.1/24
!
interface Vlan211
   description Tenant_B_OP_Zone_2
   vrf Tenant_B_OP_Zone
   ip address virtual 10.2.11.1/24
!
interface Vlan310
   description Tenant_C_OP_Zone_1
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.10.1/24
!
interface Vlan311
   description Tenant_C_OP_Zone_2
   vrf Tenant_C_OP_Zone
   ip address virtual 10.3.11.1/24
!
interface Vlan3009
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_OP_Zone
   vrf Tenant_A_OP_Zone
   ip address 10.255.251.4/31
!
interface Vlan3010
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_WEB_Zone
   vrf Tenant_A_WEB_Zone
   ip address 10.255.251.4/31
!
interface Vlan3011
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_APP_Zone
   vrf Tenant_A_APP_Zone
   ip address 10.255.251.4/31
!
interface Vlan3012
   description MLAG_PEER_L3_iBGP: vrf Tenant_A_DB_Zone
   vrf Tenant_A_DB_Zone
   ip address 10.255.251.4/31
!
interface Vlan3019
   description MLAG_PEER_L3_iBGP: vrf Tenant_B_OP_Zone
   vrf Tenant_B_OP_Zone
   ip address 10.255.251.4/31
!
interface Vlan3029
   description MLAG_PEER_L3_iBGP: vrf Tenant_C_OP_Zone
   vrf Tenant_C_OP_Zone
   ip address 10.255.251.4/31
!
interface Vlan4093
   description MLAG_PEER_L3_PEERING
   ip address 10.255.251.4/31
!
interface Vlan4094
   description MLAG_PEER
   no autostate
   ip address 10.255.252.4/31
!
```

## VXLAN Interface

### VXLAN Interface Summary

**Source Interface:** Loopback1
**UDP port:** 4789

**VLAN to VNI Mappings:**

| VLAN | VNI |
| ---- | --- |
| 110 | 10110 |
| 111 | 50111 |
| 120 | 10120 |
| 121 | 10121 |
| 130 | 10130 |
| 131 | 10131 |
| 140 | 10140 |
| 141 | 10141 |
| 160 | 50160 |
| 161 | 10161 |
| 210 | 20210 |
| 211 | 20211 |
| 310 | 30310 |
| 311 | 30311 |

**VRF to VNI Mappings:**

| VLAN | VNI |
| ---- | --- |
| Tenant_A_APP_Zone | 12 |
| Tenant_A_DB_Zone | 13 |
| Tenant_A_OP_Zone | 10 |
| Tenant_A_WEB_Zone | 11 |
| Tenant_B_OP_Zone | 20 |
| Tenant_C_OP_Zone | 30 |

### VXLAN Interface Device Configuration

```eos
interface Vxlan1
   vxlan source-interface Loopback1
   vxlan virtual-router encapsulation mac-address mlag-system-id
   vxlan udp-port 4789
   vxlan vlan 110 vni 10110
   vxlan vlan 111 vni 50111
   vxlan vlan 120 vni 10120
   vxlan vlan 121 vni 10121
   vxlan vlan 130 vni 10130
   vxlan vlan 131 vni 10131
   vxlan vlan 140 vni 10140
   vxlan vlan 141 vni 10141
   vxlan vlan 160 vni 50160
   vxlan vlan 161 vni 10161
   vxlan vlan 210 vni 20210
   vxlan vlan 211 vni 20211
   vxlan vlan 310 vni 30310
   vxlan vlan 311 vni 30311
   vxlan vrf Tenant_A_APP_Zone vni 12
   vxlan vrf Tenant_A_DB_Zone vni 13
   vxlan vrf Tenant_A_OP_Zone vni 10
   vxlan vrf Tenant_A_WEB_Zone vni 11
   vxlan vrf Tenant_B_OP_Zone vni 20
   vxlan vrf Tenant_C_OP_Zone vni 30
!
```

## Virtual Router MAC Address & Virtual Source NAT

### Virtual Router MAC Address and Virtual Source NAT Summary

**Virtual Router MAC Address:** 00:dc:00:00:00:0a
### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IP Address |
| -------------- | --------------------- |
| Tenant_A_OP_Zone | 10.255.1.5 |

### Virtual Router MAC Address Device and Virtual Source NAT Configuration

```eos
ip virtual-router mac-address 00:dc:00:00:00:0a
ip address virtual source-nat vrf Tenant_A_OP_Zone address 10.255.1.5
!
```

## Static Routes

### Static Routes Summary

| VRF | Destination Prefix | Fowarding Address / Interface |
| --- | ------------------ | ----------------------------- |
| MGMT | 0.0.0.0/0 | 10.83.13.1 |

### Static Routes Device Configuration

```eos
ip route vrf MGMT 0.0.0.0/0 10.83.13.1
!
```

## IP Routing

### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| MGMT | False |
| Tenant_A_APP_Zone | True |
| Tenant_A_DB_Zone | True |
| Tenant_A_OP_Zone | True |
| Tenant_A_WEB_Zone | True |
| Tenant_B_OP_Zone | True |
| Tenant_C_OP_Zone | True |

### IP Routing Device Configuration

```eos
ip routing
no ip routing vrf MGMT
ip routing vrf Tenant_A_APP_Zone
ip routing vrf Tenant_A_DB_Zone
ip routing vrf Tenant_A_OP_Zone
ip routing vrf Tenant_A_WEB_Zone
ip routing vrf Tenant_B_OP_Zone
ip routing vrf Tenant_C_OP_Zone
!
```

## Prefix Lists

### Prefix Lists Summary

**PL-LOOPBACKS-EVPN-OVERLAY:**

| Sequence | Action |
| -------- | ------ |
| 10 | permit 192.168.255.0/24 eq 32 |
| 20 | permit 192.168.254.0/24 eq 32 |

**PL-P2P-UNDERLAY:**

| Sequence | Action |
| -------- | ------ |
| 10 | permit 172.31.255.0/24 le 31 |
| 20 | permit 10.255.251.0/24 le 31 |

### Prefix Lists Device Configuration

```eos
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 192.168.255.0/24 eq 32
   seq 20 permit 192.168.254.0/24 eq 32
!
ip prefix-list PL-P2P-UNDERLAY
   seq 10 permit 172.31.255.0/24 le 31
   seq 20 permit 10.255.251.0/24 le 31
!
```

## MLAG

### MLAG Summary

| domain-id | local-interface | peer-address | peer-link |
| --------- | --------------- | ------------ | --------- |
| DC1_LEAF2 | Vlan4094 | 10.255.252.5 | Port-Channel3 |

### MLAG Device Configuration

```eos
mlag configuration
   domain-id DC1_LEAF2
   local-interface Vlan4094
   peer-address 10.255.252.5
   peer-address heartbeat 10.83.13.217 vrf MGMT
   peer-link Port-Channel3
   dual-primary detection delay 5 action errdisable all-interfaces
   reload-delay mlag 360
   reload-delay non-mlag 300
!
```

## Route Maps

### Route Maps Summary

**RM-CONN-2-BGP:**

| Sequence | Type | Match |
| -------- | ---- | ----- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY |
| 20 | permit | ip address prefix-list PL-P2P-UNDERLAY |

### Route Maps Device Configuration

```eos
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 20
   match ip address prefix-list PL-P2P-UNDERLAY
!
```

## Peer Filters

No Peer Filters defined

## Router BGP

### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65102|  192.168.255.5 |

| BGP Tuning |
| ---------- |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 2 ecmp 2 |

### Router BGP Peer Groups

**EVPN-OVERLAY-PEERS**:

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| remote_as | 65001 |
| source | Loopback0 |
| bfd | True |
| ebgp multihop | 3 |
| send community | true |
| maximum routes | 0 (no limit) |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 192.168.255.1 | *65001  |
| 192.168.255.2 | *65001  |

*Inherited from peer group

**IPv4-UNDERLAY-PEERS**:

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| remote_as | 65001 |
| send community | true |
| maximum routes | 12000 |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 172.31.255.8 | *65001  |
| 172.31.255.10 | *65001  |

*Inherited from peer group

**MLAG-IPv4-UNDERLAY-PEER**:

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| remote_as | 65102 |
| next-hop self | True |
| send community | true |
| maximum routes | 12000 |
**Neighbors:**

| Neighbor | Remote AS |
| -------- | ---------
| 10.255.251.5 | *65102  |

*Inherited from peer group

### Router BGP EVPN Address Family

#### Router BGP EVPN MAC-VRFs

**VLAN aware bundles:**

| VLAN Aware Bundle | Route-Distinguisher | Route Target | Redistribute | VLANs |
| ----------------- | ------------------- | ------------ | ------------ | ----- |
| Tenant_A_APP_Zone | 192.168.255.5:12 | both 12:12 | learned | 130-131 |
| Tenant_A_DB_Zone | 192.168.255.5:13 | both 13:13 | learned | 140-141 |
| Tenant_A_NFS | 192.168.255.5:10161 | both 10161:10161 | learned | 161 |
| Tenant_A_OP_Zone | 192.168.255.5:10 | both 10:10 | learned | 110-111 |
| Tenant_A_VMOTION | 192.168.255.5:50160 | both 50160:50160 | learned | 160 |
| Tenant_A_WEB_Zone | 192.168.255.5:11 | both 11:11 | learned | 120-121 |
| Tenant_B_OP_Zone | 192.168.255.5:20 | both 20:20 | learned | 210-211 |
| Tenant_C_OP_Zone | 192.168.255.5:30 | both 30:30 | learned | 310-311 |

#### Router BGP EVPN VRFs

| VRF | Route-Distinguisher | Route Target | Redistribute |
| --- | ------------------- | ------------ | ------------ |
| Tenant_A_APP_Zone | 192.168.255.5:12 | import 12:12<br> export 12:12 | connected |
| Tenant_A_DB_Zone | 192.168.255.5:13 | import 13:13<br> export 13:13 | connected |
| Tenant_A_OP_Zone | 192.168.255.5:10 | import 10:10<br> export 10:10 | connected |
| Tenant_A_WEB_Zone | 192.168.255.5:11 | import 11:11<br> export 11:11 | connected |
| Tenant_B_OP_Zone | 192.168.255.5:20 | import 20:20<br> export 20:20 | connected |
| Tenant_C_OP_Zone | 192.168.255.5:30 | import 30:30<br> export 30:30 | connected |

### Router BGP Device Configuration

```eos
router bgp 65102
   router-id 192.168.255.5
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   maximum-paths 2 ecmp 2
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65001
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS password 7 q+VNViP5i4rVjW1cxFv2wA==
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-UNDERLAY-PEERS peer group
   neighbor IPv4-UNDERLAY-PEERS remote-as 65001
   neighbor IPv4-UNDERLAY-PEERS password 7 AQQvKeimxJu+uGQ/yYvv9w==
   neighbor IPv4-UNDERLAY-PEERS send-community
   neighbor IPv4-UNDERLAY-PEERS maximum-routes 12000
   neighbor MLAG-IPv4-UNDERLAY-PEER peer group
   neighbor MLAG-IPv4-UNDERLAY-PEER remote-as 65102
   neighbor MLAG-IPv4-UNDERLAY-PEER next-hop-self
   neighbor MLAG-IPv4-UNDERLAY-PEER password 7 vnEaG8gMeQf3d3cN6PktXQ==
   neighbor MLAG-IPv4-UNDERLAY-PEER send-community
   neighbor MLAG-IPv4-UNDERLAY-PEER maximum-routes 12000
   neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
   neighbor 172.31.255.8 peer group IPv4-UNDERLAY-PEERS
   neighbor 172.31.255.10 peer group IPv4-UNDERLAY-PEERS
   neighbor 192.168.255.1 peer group EVPN-OVERLAY-PEERS
   neighbor 192.168.255.2 peer group EVPN-OVERLAY-PEERS
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan-aware-bundle Tenant_A_APP_Zone
      rd 192.168.255.5:12
      route-target both 12:12
      redistribute learned
      vlan 130-131
   !
   vlan-aware-bundle Tenant_A_DB_Zone
      rd 192.168.255.5:13
      route-target both 13:13
      redistribute learned
      vlan 140-141
   !
   vlan-aware-bundle Tenant_A_NFS
      rd 192.168.255.5:10161
      route-target both 10161:10161
      redistribute learned
      vlan 161
   !
   vlan-aware-bundle Tenant_A_OP_Zone
      rd 192.168.255.5:10
      route-target both 10:10
      redistribute learned
      vlan 110-111
   !
   vlan-aware-bundle Tenant_A_VMOTION
      rd 192.168.255.5:50160
      route-target both 50160:50160
      redistribute learned
      vlan 160
   !
   vlan-aware-bundle Tenant_A_WEB_Zone
      rd 192.168.255.5:11
      route-target both 11:11
      redistribute learned
      vlan 120-121
   !
   vlan-aware-bundle Tenant_B_OP_Zone
      rd 192.168.255.5:20
      route-target both 20:20
      redistribute learned
      vlan 210-211
   !
   vlan-aware-bundle Tenant_C_OP_Zone
      rd 192.168.255.5:30
      route-target both 30:30
      redistribute learned
      vlan 310-311
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
      no neighbor IPv4-UNDERLAY-PEERS activate
      no neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-UNDERLAY-PEERS activate
      neighbor MLAG-IPv4-UNDERLAY-PEER activate
   !
   vrf Tenant_A_APP_Zone
      rd 192.168.255.5:12
      route-target import evpn 12:12
      route-target export evpn 12:12
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_A_DB_Zone
      rd 192.168.255.5:13
      route-target import evpn 13:13
      route-target export evpn 13:13
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_A_OP_Zone
      rd 192.168.255.5:10
      route-target import evpn 10:10
      route-target export evpn 10:10
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_A_WEB_Zone
      rd 192.168.255.5:11
      route-target import evpn 11:11
      route-target export evpn 11:11
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_B_OP_Zone
      rd 192.168.255.5:20
      route-target import evpn 20:20
      route-target export evpn 20:20
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
   !
   vrf Tenant_C_OP_Zone
      rd 192.168.255.5:30
      route-target import evpn 30:30
      route-target export evpn 30:30
      neighbor 10.255.251.5 peer group MLAG-IPv4-UNDERLAY-PEER
      redistribute connected
!
```
