To finish up day 2, we're going to use Ansible with CVP to deploy configurations to the devices.
You'll notice your inventory file for this lab has an additional entry for CVP now.

1)  Start the lab by going to CVP, and rolling back your device configurations to the current DC (designed configuration) in CVP.
2)  Update your group_vars for the cvp_nodes group with your password for CVP.
3)  Make sure you have the most up-to-date version of the arista.cvp collection installed by running `ansible-galaxy collection install arista.cvp`
4)  Now, we're going to apply (roughly) configurations you did to customize your devices in lab 6, but by using CVP, not direct eAPI calls.
    Feel free to reuse existing templates and plays you have from lab 6 to speed this lab up.
    You may compose as many or as few configlets as desired to achieve your desired device configs in CVP.
    For this lab, you need to apply the following customizations to your existing base configs by creating additional CVP configlets and mapping them to your devices:
4a) Customized, per device login banner using Jinja template files and eos_facts from devices.
    The templates have been provided for you (same as lab 6)
4b) An uncustomized MOTD banner for all devices.
    The banner to apply is in configs/
5)  Once your configlets are created and mapped to your devices, look at CVP.
    You will see tasks generated, as the DC (designed configuration) for your devices has changed.
    Package these into a CC (change control) and execute it.