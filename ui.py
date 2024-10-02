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
    else:
        cont = "false"