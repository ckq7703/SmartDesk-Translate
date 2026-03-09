import polib
import pandas as pd

# đọc file excel
df = pd.read_excel("Translation-SmartDesk.xlsx")

# tạo file po mới
po = polib.POFile()
po.metadata = {
    "Project-Id-Version": "GLPI",
    "Content-Type": "text/plain; charset=utf-8",
}

# đọc từng dòng excel
for _, row in df.iterrows():
    
    msgid = str(row["msgid"])
    msgstr = str(row["msgstr"]) if not pd.isna(row["msgstr"]) else ""

    entry = polib.POEntry(
        msgid=msgid,
        msgstr=msgstr
    )

    po.append(entry)

# lưu file po
po.save("vi_VN.po")

print("Convert Excel → vi_VN.po thành công!")