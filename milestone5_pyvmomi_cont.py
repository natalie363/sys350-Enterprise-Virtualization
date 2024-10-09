import miletone4_pyvmomi_basics
from pyVim.task import WaitForTask
from pyVmomi import vim
import time

# Very helpful resource!! 
# https://www.ntpro.nl/blog/archives/3751-Mastering-vCenter-Operations-with-Python-A-Script-to-Manage-Your-VMs.html 

def power_on(set_vms):
    """Powers on set of filtered VMs"""
    for vm in set_vms:
        vm_name = vm.config.name
        if vm.runtime.powerState != "poweredOn":
            WaitForTask(vm.PowerOnVM_Task())
            print(f"Current State of {vm_name}: {vm.runtime.powerState}\n")
        else:
            print(f"{vm_name} is already powered on. \n")

def power_down(set_vms):
    """Powers off a set of filtered VMs"""
    for vm in set_vms:
        vm_name = vm.config.name
        if vm.runtime.powerState != "poweredOff":
            WaitForTask(vm.PowerOffVM_Task())
            print(f"Current State of {vm_name}: {vm.runtime.powerState}\n")
        else:
            print(f'{vm_name} is already powered off.\n')

def revert_snapshot(set_vms):
    """Revert to previous snapshot"""
    for vm in set_vms:
        WaitForTask(vm.RevertToCurrentSnapshot_Task())
        print(f'\n{vm.config.name} reverted to the latest snapshot\n')

# https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/snapshot_operations.py
def snapshot(set_vms, snapshot_name="newSnap", snapshot_description="pyvmomi snapshot"):
    """Take a snapshot of selected VMs"""
    for vm in set_vms:
        vm_name = vm.config.name
        WaitForTask(
        vm.CreateSnapshot(snapshot_name, snapshot_description, False, False)
        )
        print(f'{snapshot_name} created for {vm_name}')

def change_cpu(set_vms, count):
    """Change CPU of VM"""
    power_down(set_vms)
    for vm in set_vms:
        config = vim.vm.ConfigSpec(numCPUs = count)
        WaitForTask(vm.Reconfigure(config))
        print(f"Current CPU for {vm.config.name} is {vm.config.hardware.numCPU}\n")
    power_on(set_vms)

# https://github.com/vmware/pyvmomi-community-samples/blob/master/samples/execute_program_in_vm.py
def run_command(vm, command, auth, username, password):
    """run command on vm"""
    vm = vm[0]
    specs = vim.vm.guest.ProcessManager.ProgramSpec(programPath=command)
    profile = auth.content.guestOperationsManager.processManager
    vm_login = vim.vm.guest.NamePasswordAuthentication(username=username, password=password)
    results = profile.StartProgramInGuest(vm, vm_login, specs)
    time.sleep(2)
    print(f'PID is {results}')
    time.sleep(2)
    exit_code = profile.ListProcessesInGuest(vm, vm_login, [results]).pop().exitCode
    print(f'Exit code {exit_code}')

