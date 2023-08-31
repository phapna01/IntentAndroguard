from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

def findOnCreate(apk_file_path):
    a = apk.APK(apk_file_path)
    d = dvm.DalvikVMFormat(a.get_dex())
    
    classes_with_oncreate = set()
    
    for cls in d.get_classes():
        for method in cls.get_methods():
            if method.get_name() == 'onCreate':
                classes_with_oncreate.add(cls.get_name())
                
    return classes_with_oncreate

apk_file_path = './input/goatdroid.apk'
classes_with_oncreate = findOnCreate(apk_file_path)
for class_name in classes_with_oncreate:
    print(class_name)