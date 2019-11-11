#!/usr/bin/env python3

print('Testing Netconf ncclient')


from ncclient import manager
user = 'admin'
passwd = 'admin'
host_name = '192.168.1.117'
netconf_connector = manager.connect(host = host_name, port = 830, username = user, password = passwd, hostkey_verify = False, timeout=10, allow_agent=False, look_for_keys=False, device_params={'name':'default'})

print ('Connection status :')

print(netconf_connector.connected)

print('Capabilities --')

for capability in netconf_connector.server_capabilities:
	
	print(capability)
print('------------------get config----------------')

out = netconf_connector.get_config(source='running').data_xml

print(out)

print('------------------Edit config----------------')

in_config_sample= """
<config>
<switch xmlns="http://ruggedcom.com/ns/rmf_ifswitch">
 <vlans>
 <static-vlan>
 <vid>0087</vid>
 </static-vlan>
 </vlans>
 </switch>
</config>
"""

in_config_ospf_disable = """
<config>
	<routing xmlns:nc="urn:ietf:params:xml:ns:netconf:base:1.0" xmlns="http://ruggedcom.com/ns/rmf_routing">
     <dynamic>
      <ospf nc:operation="delete">
       <enabled/>
      </ospf>
     </dynamic>
    </routing>
</config>
"""

create_config = netconf_connector.edit_config(target='running',config = in_config_sample)


print ('Netconf edit status:')

print(create_config.ok)

netconf_connector.close_session()


print ('Connection status :')

print(netconf_connector.connected)
