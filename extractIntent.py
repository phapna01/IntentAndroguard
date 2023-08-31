from androguard.core.bytecodes.apk import APK
from androguard.core.bytecodes.dvm import DalvikVMFormat
from androguard.core.analysis.analysis import Analysis
# from androguard.decompiler.decompiler  import DecompilerJADX
import lxml.etree as etree

from bs4 import BeautifulSoup


apk_file = ("D:\KienThuc\Androguard\goatdroid.apk")
a = APK(apk_file)
d = DalvikVMFormat(a)
dx = Analysis(d)
manifest_xml = a.get_android_manifest_xml()
xml_content = etree.tostring(manifest_xml, pretty_print=True, encoding='unicode')  # Convert Element to string

# phân tích cú pháp AndroidManifest.xml
soup = BeautifulSoup(xml_content, 'xml')


# trích xuất các phần tử intent-filter từ AndroidManifest.xml
intent_filters = soup.find_all('intent-filter')
permissions = soup.find_all('uses-permission')

for permission in  permissions:
    print("Permission:", permission['android:name'])

for intent_filter in intent_filters:
    # lấy các thuộc tính action và category 
    actions = intent_filter.find_all("action")
    categories = intent_filter.find_all("category")
    
    #trích xuất các action và category nếu có
    # action = [action.get('android: name') for act in action]
    # category = [cat.get('android: name') for cat in category]
    
    print('Actions: ', actions)
    print('Categories: ', categories)
    
