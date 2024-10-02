import miletone4_pyvmomi_basics
import time

# Very helpful resource!! 
# https://www.ntpro.nl/blog/archives/3751-Mastering-vCenter-Operations-with-Python-A-Script-to-Manage-Your-VMs.html 

def power_on(set_vms):
    """Powers on set of filtered VMs"""
    for vm in set_vms:
        vm_name = vm.config.name
        if vm.runtime.powerState != "poweredOn":
            print(vm.PowerOnVM_Task())
            time.sleep(3)
            print(f"Current State of {vm_name}: {vm.runtime.powerState}\n")
        else:
            print(f"{vm_name} is already powered on. \n")

def power_down(set_vms):
    """Powers off a set of filtered VMs"""
    for vm in set_vms:
        vm_name = vm.config.name
        if vm.runtime.powerState != "poweredOff":
            print(vm.PowerOffVM_Task())
            time.sleep(3)
            print(f"Current State of {vm_name}: {vm.runtime.powerState}\n")
        else:
            print(f'{vm_name} is already powered off.\n')