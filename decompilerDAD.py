from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
from androguard.decompiler.decompiler import DecompilerDAD

apk = APK("D:\\KienThuc\\Androguard\\app-debug.apk")
dvm = DalvikVMFormat(apk)
analysis = Analysis(dvm)
decompiler = DecompilerDAD(dvm, analysis)

# set decompiler and analysis back to DalvikVMFormat
dvm.set_decompiler(decompiler)
dvm.set_vmanalysis(analysis)

f = open('decompiledCode1.txt', 'w')

for cls in dvm.get_classes():
    class_name = cls.get_name()
        
    for method in cls.get_methods():
        decompiled_code = decompiler.get_source_method(method)
        f.write(decompiled_code)
        
        
        
        
    