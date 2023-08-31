from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

def allClasses(apk_file_path):
    a = apk.APK(apk_file_path)
    d = dvm.DalvikVMFormat(a.get_dex())

    # Set to store the classes that meet the conditions
    classes_with_conditions = set()

    for cls in d.get_classes():
        classes_with_conditions.add(cls.get_name())
        for method in cls.get_methods():
            # Get the instructions of the onCreate() method
            classes_with_conditions.add(method.get_name())
            instructions = method.get_instructions()

            for instruction in instructions:
                    # Check if the instruction calls getExtras() or getIntent()
                 if "getExtras" in instruction.get_output() or "getIntent" in instruction.get_operands():
                        # If the condition is met, add the class to the set
                    classes_with_conditions.add(instruction.get_name())
                    classes_with_conditions.add(instruction.get_output())
                        
                        
                    break  # Exit the loop once the condition is met

    return classes_with_conditions

# Provide the path to the APK file
apk_file_path = "./input/goatdroid.apk"
target_name = 'Lorg/owasp/goatdroid/fourgoats/activities/'
classes_with_conditions = allClasses(apk_file_path)

# Print the classes that meet the conditions
for class_name in classes_with_conditions:
    print(class_name)
for method_name in classes_with_conditions:
    print(method_name)
for instr_name in classes_with_conditions:
    print(instr_name)    
 