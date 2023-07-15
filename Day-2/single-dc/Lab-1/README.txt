Today we're going to start with some simple Ansible operations to get our feet wet.
You'll notice in this directory an ansible.cfg file and inventory.yaml file are already present to get you started, as well as group_vars/all/connection.yaml.
Some additional setup will be needed for this to work (your ATD topology password).

1)  Finish configuring your connection.yaml file so that you can successfully Ansible ping all devices
2)  Play around with group targeting
2a) Determine how to Ansible ping just the spines in your inventory
2b) Determine how to Ansible ping just the leafs in your inventory
3)  Take a look at the example-playbook.yaml file.
    This has been partially filled out for you already.
    Finish filling out the playbook to run commands on all devices in your inventory, and write the outputs to a file in the output directory.
    Ensure that the newlines are correct in this file, so that the information looks like what you would see on the switch CLI, and is not smashed together into a giant blob.
3a) Delete all files in the output directory.
    Change the playbook (not the command line invocation) so that it only executes against the spines in your topology.