from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

def decompile_dex_from_apk(apk_file_path):
    # Load the APK file
    a = apk.APK(apk_file_path)
    # Get the DEX file from the APK
    dex_file_path = a.get_dex()
    # Load the DEX file
    d = dvm.DalvikVMFormat(a.get_dex())
    
    target_name = 'Lorg/owasp/goatdroid/fourgoats/activities/'
    output = ""
    # Iterate over all classes in the DEX file
    for cls in d.get_classes():
            # Get the class name
        class_name = cls.get_name()
        if class_name.startswith(target_name):
            # Get the class methods    
            methods = cls.get_methods()
                # Print the class name and its methods
            output += f"Class: {class_name}\n"
            for method in methods:
                method_name = method.get_name()
                
                output += f"\tMethod: {method_name}\n"      
                bytecode = method.get_instructions() # tìm thêm các string, boolean, 
                    
                for instruction in bytecode:
                    instruction_name = instruction.get_name()
                    output += f"\t\t{instruction_name}\n"
                    operands = instruction.get_operands()
                    output += f"\t\t{operands}\n"
                    output_file.write(f"\t\t{instruction_name}, {operands}\n")

    output += "\n"
    return output

# Provide the path to the APK file
apk_file_path = "D:\KienThuc\Androguard\goatdroid.apk"

# Call the decompile_dex_from_apk function
output = decompile_dex_from_apk(apk_file_path)

# Save the output to a text file
output_file_path = "output.txt"
with open(output_file_path, "w", encoding='utf-8') as output_file:
    output_file.write(output)

print("Decompilation completed. Output saved to output.txt.")
