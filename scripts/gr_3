import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")
mas = ["абонемент", "разовая"]

group = df.groupby('payment_type')['completed'].mean().reindex(mas, fill_value=0) * 100
plt.ylim(0, 100)
plt.bar(mas, group, width=0.6)

plt.xlabel('Вид занятия')
plt.ylabel('Процент посещаемости')
plt.title('Посещаемость: Абонемент/Разовая')
plt.tight_layout()
sred = df['completed'].mean() * 100
plt.axhline(sred, color='orange', linestyle='--', label='Среднее по всем')
plt.legend()
plt.savefig('gr_3.png', dpi=150, bbox_inches='tight')
plt.show()
