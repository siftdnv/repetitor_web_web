import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")

pivod = pd.pivot_table(df, index = 'lesson_hour',columns='weekday',values='lesson_id',aggfunc='count',fill_value=0).reindex(columns=['Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб', 'Вс'],fill_value=0)
plt.imshow(pivod, cmap='Blues', interpolation='nearest')
plt.colorbar(label='Кол-во уроков')
plt.xticks((0,1,2,3,4,5,6),pivod.columns)
plt.yticks((0,1,2,3,4,5,6,7,8,9),pivod.index)
plt.savefig('gr_4.png', dpi=150, bbox_inches='tight')
plt.show()
