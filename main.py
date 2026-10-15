from maps.GakushokuSample import GakushokuSample

# ↓のリストには、メンバーの各オススメ学食が格納されます。
from maps.k24043 import k24043
from maps.k25022 import k25022
from maps.k25147 import k25147
from maps.kurisu import kurisu
# ↓のリストには、メンバーの各オススメ学食が格納されます。
data = [GakushokuSample(), 
        k24043(),
        k25022(),
        k25147(),
        kurisu()
        ]
for rank, d in enumerate(data, start=1):
    print(f"{rank}位: {d.get_menu()}")
    print("---------------------------------")
    print(d.get_summary())
    print(d.get_author())
    print()