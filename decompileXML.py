from androguard.core.bytecodes.apk import APK
from lxml import etree

apk_file_path = "D:\KienThuc\Androguard\goatdroid.apk"
apk = APK(apk_file_path)

manifest_xml = apk.get_android_manifest_xml()

manifest_bytes = etree.tostring(manifest_xml, pretty_print=True)

with open("AndroidManifest.xml", "wb") as f:
    f.write(manifest_bytes )

# def get_activities(apk_file):
#     # Load the APK file
#     a = apk.APK(apk_file)

#     # Get the list of activities
#     activities = a.get_activities()

#     return activities

# if __name__ == "__main__":
#     apk_file_path = "D:\KienThuc\Androguard\goatdroid.apk"
#     activities_list = get_activities(apk_file_path)

#     # Print the list of activities
#     print("Activities in goatdroid.apk:")
#     for activity in activities_list:
#         print(activity)