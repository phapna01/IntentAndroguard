#Class: AddVenue.txt
#	DoComment$DoCo
#	SocialAPIAuthentication
#	ViewProfile

from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

def allClasses(apk_file_path, target_name, output_directory):
    a = apk.APK(apk_file_path)
    d = dvm.DalvikVMFormat(a.get_dex())
    
    for cls in d.get_classes():
        class_name = cls.get_name()
        if class_name.startswith(target_name):
            suffix = class_name[len(target_name):].replace(';', '')
            methods = cls.get_methods()
            output_file_path = output_directory + suffix + '.txt'
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for method in methods:
                    method_name = method.get_name()
                    bytecode = method.get_instructions()
                   
                    for instruction in bytecode:
                        instruction_name = instruction.get_name()
                        if instruction.get_name() == "invoke-virtual" and ("getExtras" in instruction.get_output() or "getIntent" in instruction.get_output()):
                            output_file.write(f'Class: {class_name}\n')
                            output_file.write(f'\tMethods: {method_name}\n')
                            operands = instruction.get_operands()
                            # has_get_extras = any("invoke-virtual {v0}, Landroid/content/Intent;->getExtras()Landroid/content/Intent;" in instruction.get_operands() for instruction in bytecode)  
                            output_file.write(f"\t\t {instruction_name}, {operands}\n")

apk_file_path = './input/goatdroid.apk'
output_directory = './output1/'
target_name = 'Lorg/owasp/goatdroid/fourgoats/activities/'
allClasses(apk_file_path, target_name, output_directory)


      
def viewActivity(apk_file_path):
    a = apk.APK(apk_file_path)         
    d = dvm.DalvikVMFormat(a.get_dex())
    output_file_path = 'outputActivity.txt'
    activities = a.get_activities()
    with open(output_file_path, 'w') as output_file:
        for activity in activities:
            output_file.write(f'Activity: {activity}\n')



# viewActivity(apk_file_path)

