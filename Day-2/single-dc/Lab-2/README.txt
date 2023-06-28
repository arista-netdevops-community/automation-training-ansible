For this lab, we're going to be extending what you've done so far with Jinja and Ansible to start configuring devices directly from Ansible, with per-device customization.
In additional, we'll add a few small tasks to expose you to various modules in the arista.eos collection.

1) Taking what you've learned so far about group_vars and host_vars, create the directories and files needed to set a template directory per group (spine/leaf/endhosts).
   The template directories have already been provided for you in this lab under templates/, along with suitable templates to emit different banners for each group.
2) Build a playbook using the arista.eos collection modules to collect the device hostname and serial number from each device.
   Use this information with the templates provided to create a banner for each device, and push it to the device config.
3) Create a task in your playbook to set the logging severity on all devices to emergency (use eos_logging_global) for the forwarding facility.
4) Create a task in your playbook to ensure eAPI is enabled for all devices.