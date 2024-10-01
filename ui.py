import miletone4_pyvmomi_basics
import milestone5_pyvmomi_cont

cont = "true"
main_auth_object = miletone4_pyvmomi_basics.auth()

while cont == "true":
    
    print("Options")
    print("1. Get Basic Information")
    print("2. Get Connection Information")
    print("3. Get All VM Information")
    print("4. Get Specific VM Information")
    print("5. Power On VMs")
    print("6. Power Off VMs")
    print("7. Snapshot VMs")
    print("8. Restore Snapshot")
    print("9. Change CPU Count")
    print("10. Change Network")
    print("11. Quit Program")
    option = input("Enter the number: ")
    if option == "1":
        pass
    elif option == "2":
        pass
    elif option == "3":
        pass
    elif option == "4":
        pass
    elif option == "5":
        filter_name = input("Enter search term for VMs, blank for none: ")
        if filter_name is not None:
            filtered_vms = miletone4_pyvmomi_basics.vm_info(main_auth_object,search_name=filter_name,milestone5=True)
            [print(child.config.name) for child in filtered_vms]
    else:
        cont = "false"