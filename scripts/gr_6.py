import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")

df = df[df['payment_status'] == 'paid']
dates = [1, 2, 3, 4, 5, 6, 7, 8, 9]
df['week'] = pd.to_datetime(df['date']).dt.isocalendar().week
group = df.groupby('week')['price_rub'].sum() / 1000
plt.axhline(group.mean(), color='orange', linestyle='--', label='Средняя выручка в неделю')
plt.plot(dates, group, marker='o', label='Выручка')
plt.title('Динамика фактической выручки по неделям')
plt.xlabel('Номер недели')
plt.ylabel('Сумма (тыс. руб.)')
plt.legend()
plt.grid()
plt.savefig('gr_6.png', dpi=150, bbox_inches='tight')
plt.show()
