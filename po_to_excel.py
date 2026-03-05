import polib
import pandas as pd

po = polib.pofile("vi_VN.po")

data = []

for entry in po:
    data.append({
        "msgid": entry.msgid,
        "msgstr": entry.msgstr
    })

df = pd.DataFrame(data)
df.to_excel("translation.xlsx", index=False)

print("Exported to translation.xlsx")