import rpdb

def undefine_range(addr, length):
    for startaddress in range(addr, addr+length+1):
        MakeUnkn(startaddress, 1)

def import_data_and_code():
    """
    """
    with open("exported_data_code.txt", "r") as fileobj:
        for line in fileobj:
            address = line.split(":")[0]
            hex_address = int(address, 16)
            attribute = line.split(":")[1].strip()
            if attribute == "code":
                MakeCode(hex_address)
            if attribute == "data":
                idc.create_dword(address)
                idc.create_word(address)
                idc.create_byte(address)

            if attribute == "undef":
                MakeUnkn(hex_address, 1)

def import_functions():
    with open("exported_functions.txt", "r") as fileobj:
        for line in fileobj:
            address = line.split(":")[0]
            hex_address = int(address, 16)
            function_name = line.split(":")[1].strip()
            MakeFunction(hex_address)
            if function_name.startswith("sub_"):
                continue
            MakeName(hex_address, function_name)
            
def import_strings():
    with open("exported_strings.txt", "r") as fileobj:
        for line in fileobj:
            address = int(line.split(":")[0], 16)
            length = int(line.split(":")[1])
            strtype = int(line.split(":")[2].strip())
            undefine_range(address, length)
            idaapi.make_ascii_string(address, length, strtype)
                
def import_offsets():
    ida_offset.op_offset(0x8006740, 0, idc.REF_OFF32)
    
def main():
    import_data_and_code()
    import_functions()
    import_strings()
    
if __name__ == "__main__":
    main()