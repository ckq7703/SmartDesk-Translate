# Hướng dẫn Dịch thuật SmartDesk (GLPI Plugin)

Tài liệu này hướng dẫn chi tiết quy trình cập nhật ngôn ngữ cho plugin SmartDesk trong hệ thống GLPI, sử dụng file Excel làm nguồn dữ liệu chính.

## 1. Chuẩn bị (Prerequisites)

Để chạy các script chuyển đổi, máy tính của bạn cần cài đặt:

- **Python 3.x**
- **Thư viện cần thiết:** Cài đặt qua lệnh sau trong terminal:
  ```bash
  pip install polib pandas openpyxl
  ```

## 2. Các file quan trọng trong dự án

- `Translation-SmartDesk.xlsx`: File Excel chính chứa các bản dịch (cột `msgid` là mã gốc, `msgstr` là bản dịch).
- `excel_to_po.py`: Script chuyển đổi dữ liệu từ Excel sang file định dạng `.po`.
- `vi_VN.po`: File ngôn ngữ định dạng văn bản (Gettext).
- `vi_VN.mo`: File ngôn ngữ đã được biên dịch thành mã máy (đây là file GLPI sẽ đọc).

## 3. Quy trình thực hiện chi tiết

### Bước 1: Cập nhật nội dung dịch
Mở file `Translation-SmartDesk.xlsx` và cập nhật các bản dịch trong cột `msgstr` tương ứng với `msgid`. Lưu lại file sau khi hoàn tất.

### Bước 2: Chuyển đổi Excel sang PO
Chạy script `excel_to_po.py` để tạo file `vi_VN.po` mới nhất từ file Excel:
```bash
python excel_to_po.py
```
Sau khi chạy xong, bạn sẽ thấy file `vi_VN.po` được cập nhật trong thư mục.

### Bước 3: Biên dịch file PO sang MO
Vì GLPI sử dụng file `.mo` để hiển thị ngôn ngữ, bạn cần biên dịch file `.po` vừa tạo:
1. Truy cập trang web: [https://pofile.net/free-po-editor](https://pofile.net/free-po-editor)
2. Tải file `vi_VN.po` lên.
3. Nhấn biên dịch/tải về để nhận file `vi_VN.mo`.

### Bước 4: Triển khai vào hệ thống GLPI
Copy cả 2 file `vi_VN.po` và `vi_VN.mo` vào thư mục ngôn ngữ của plugin SmartDesk trong thư mục cài đặt GLPI:
- Đường dẫn tham khảo: `glpi/locales/`

## 4. Lưu ý
- Luôn giữ file `Translation-SmartDesk.xlsx` làm "nguồn gốc chuẩn" (Source of Truth). 
- Nếu có các chuỗi mới từ mã nguồn, hãy đảm bảo chúng được thêm vào file Excel trước khi thực hiện quy trình trên.
