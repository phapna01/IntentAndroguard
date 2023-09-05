from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

# apk_file_path = 'D:\KienThuc\Androguard\goatdroid.apk'
# a = apk.APK(apk_file_path)
# d = dvm.DalvikVMFormat(a)
# target_class_pattern = 'Lorg/owasp/goatdroid/fourgoats/activities/'

# output_file_path = 'outputClasses.txt'

# with open(output_file_path, 'w', encoding='utf-8') as output_file:
#     for cls in d.get_classes():
#         class_name = cls.get_name()
#         if class_name.startswith(target_class_pattern):
#             output_file.write(f"Class: {class_name}\n")
                              
# print("Output saved to:", output_file_path)


def allClasses(apk_file_path):
    a = apk.APK(apk_file_path)
    d = dvm.DalvikVMFormat(a.get_dex())

    # Set to store the classes that meet the conditions
    classes_with_conditions = set()

    for cls in d.get_classes():
        for method in cls.get_methods():
            instructions = method.get_instructions()

            for instruction in instructions:
                    # Check if the instruction calls getExtras() or getIntent()
                if instruction.get_name() == "invoke-virtual" and ("getExtras" in instruction.get_output() or "getIntent" in instruction.get_output()):
                        # If the condition is met, add the class to the set
                    classes_with_conditions.add(cls.get_name())
                        # Extract and print the values from getExtras() and getIntent()
                    values = extractValues(cls, instructions)
                    printValues(cls.get_name(), values)
                    break  # Exit the loop once the condition is met

    return classes_with_conditions

def extractValues(cls, instructions):
    values = []
    for instruction in instructions:
        if instruction.get_name() == "invoke-virtual":
            output = instruction.get_output()
            if "getExtras" in output or "getIntent" in output:
                value = extractValue(cls, instruction)
                if value:
                    values.append(value)
    return values

def extractValue(cls, instruction):
    value = None
    method_name = instruction.get_output().split(',')[-1].strip()
    for method in cls.get_methods():
        if method_name in method.get_name():
            value = extractValueFromMethod(method)
            break
    return value

def extractValueFromMethod(method):
    instructions = method.get_instructions()
    for instruction in instructions:
        if instruction.get_name() == "move-result-object":
            register = instruction.get_output().split(',')[-1].strip()
            for next_instruction in instructions:
                if next_instruction.get_output().startswith(register) and next_instruction.get_name() == "const-string":
                    value = next_instruction.get_output().split(',')[-1].strip()
                    return value
    return None

def printValues(class_name, values):
    if values:
        print(f"Class: {class_name}")
        print("Values:")
        for value in values:
            print(value)
        print()

# Provide the path to the APK file
apk_file_path = "D:\KienThuc\Androguard\goatdroid.apk"

# Call the allClasses function
classes_with_conditions = allClasses(apk_file_path)