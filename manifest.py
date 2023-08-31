from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

def allClasses(apk_file_path):
    a = apk.APK(apk_file_path)
    d = dvm.DalvikVMFormat(a.get_dex())

    # Set to store the classes that meet the conditions
    # classes_with_conditions = set()

    for cls in d.get_classes():
        print(cls.get_name())
        for method in cls.get_methods():
            print(method.get_name())
            # Get the instructions of the onCreate() method
            instructions = method.get_instructions()
            for instruction in instructions:
                print(instruction.get_name())
                print(instruction.get_output())
                
                
apk_file_path = "./input/goatdroid.apk"
classes_with_conditions = allClasses(apk_file_path)
