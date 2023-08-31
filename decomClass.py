from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm

apk_file_path = 'D:\KienThuc\Androguard\goatdroid.apk'
a = apk.APK(apk_file_path)
d = dvm.DalvikVMFormat(a)
target_class_pattern = 'Lorg/owasp/goatdroid/fourgoats/activities/'

output_file_path = 'outputClasses.txt'

with open(output_file_path, 'w', encoding='utf-8') as output_file:
    for cls in d.get_classes():
        class_name = cls.get_name()
        if class_name.startswith(target_class_pattern):
            output_file.write(f"Class: {class_name}\n")
                              
print("Output saved to:", output_file_path)


