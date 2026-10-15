from maps.GakushokuSample import GakushokuSample
from maps.k25147 import k25147
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(),
        k25147()
        ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()