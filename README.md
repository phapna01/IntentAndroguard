# IntentAndroguard
- Từ tệp goatdroid.apk -> decompiler tệp xml lấy được AndroidManifest.xml và kiểm tra các activity trong tệp AndroidManifest.xml

- file decompiler XML để lấy file AndroidManifest.xml

- Trong file allClass.py
+ Có 1 hàm lấy ra tất cả các Activity, kết quả trả về tệp Activity
+ Có 1 hàm lấy ra tất cả các classes từ các Activity 

- Trong file decompilerDEX.py:
+ Lấy ra từng class và các giá trị bên trong đó (như Method...) sẽ được lưu vào từng tệp .txt  được ghi vào folder output
+ Trong folder 

Quá trình Decode file apk
Phân tách tệp .apk thành source code riêng biệt (các class.smali) sử dụng androguard. Khi tạo 1 file .apk sẽ chứa 1 tệp .dex với binary Dalvik bytecode bên trong, platform có thể hiểu được format này. Đầu tiền cần dùng Androguard để convert tệp .dẽ sang 1 dạng con ng có thể đọc là Smali