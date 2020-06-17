import idautils
import enumerators
        
def export_data_and_code():
    """
    Iterates over each head, marking if it is code or data
    """
    with open("exported_data_code.txt", "w") as fileobj:
        for head in Heads():
            flags = GetFlags(head)
            if isData(flags):
                if is_strlit(flags): # If it is a string:
                    fileobj.write("%s:string\n" % (hex(int(head))))
                else: # If it is just data
                    fileobj.write("%s:data:%s\n" % (hex(int(head)), ItemSize(head)))
            elif isCode(flags):
                fileobj.write("%s:code\n" % hex(int(head)))
            elif isUnknown(flags):
                fileobj.write("%s:unknown\n" % hex(int(head)))
        for undef in enumerators.Undefs(0):
           fileobj.write("%s:undef\n" % hex(int(undef)))

def export_strings():
    with open("exported_strings.txt", "w") as fileobj:
        for string in idautils.Strings():
            fileobj.write("%s:%s:%s\n" % (hex(int(string.ea)), string.length, string.strtype))
            
def export_offsets():
    pass

def export_functions():
    with open("exported_functions.txt", "w") as fileobj:
        for funcea in Functions():
            function_name = GetFunctionName(funcea)
            fileobj.write("%s:%s\n" % (hex(int(funcea)), function_name))
            
def main():
    export_data_and_code()
    export_functions()
    export_strings()
    
if __name__ == "__main__":
    main()