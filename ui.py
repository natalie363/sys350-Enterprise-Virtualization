import miletone4_pyvmomi_basics
import milestone5_pyvmomi_cont

cont = "true"
main_auth_object = miletone4_pyvmomi_basics.auth()

while cont == "true":
    
    print("Options")
    print("1. Get Basic Information")
    print("2. Get Connection Information")
    print("3. Get VM Information")
    print("4. Power On VMs")
    print("5. Power Off VMs")
    print("6. Snapshot VMs")
    print("7. Restore Snapshot")
    print("8. Change CPU Count")
    print("9. Change Network")
    print("10. Quit Program")
    option = input("Enter the number: ")

    if option == "1":
        miletone4_pyvmomi_basics.basic_info(main_auth_object)

    elif option == "2":
        miletone4_pyvmomi_basics.session_info(main_auth_object)

    elif option == "3":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name)

    elif option == "4":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
        [print(child.config.name) for child in filtered_vms]
        proceed = input("\nPower on these VMs? (y or n): ")
        if proceed.lower() == "y":
            print("powering on VMs\n")
            milestone5_pyvmomi_cont.power_on(filtered_vms)

    elif option == "5":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
        [print(child.config.name) for child in filtered_vms]
        proceed = input("\nPower off these VMs? (y or n): ")
        if proceed.lower() == "y":
            print("powering off VMs\n")
            milestone5_pyvmomi_cont.power_down(filtered_vms)

    elif option == "6":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
        [print(child.config.name) for child in filtered_vms]
        proceed = input("Snapshot these VMs? (y or n): ")
        
        
        if proceed.lower() == "y":
            snap_name = input("\nEnter a name for your snapshot: ")
            snap_description = input(f"Enter a description for {snap_name}: ")
            print("\nSnapshotting VMs\n")
            milestone5_pyvmomi_cont.snapshot(filtered_vms, snap_name, snap_description)

    elif option == "7":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
        [print(child.config.name) for child in filtered_vms]
        proceed = input("Revert VMs to current snapshot? (y or n): ")
        if proceed.lower() == "y":
            milestone5_pyvmomi_cont.revert_snapshot(filtered_vms)

    elif option == "8":
        filter_name = input("\nEnter search term for VMs, blank for none: ")
        filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
        [print(child.config.name) for child in filtered_vms]
        proceed = input("Change CPU for these VMS? (y or n): ")
        if proceed.lower() == "y":
            count = int(input("Input the new CPU number: "))
            milestone5_pyvmomi_cont.change_cpu(filtered_vms, count)

    elif option == "9":
        pass

    else:
        cont = "false"