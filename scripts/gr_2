import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")
bec = [
    "болезнь ученика",
    "поздняя отмена (<12 ч)",
    "семейные обстоятельства",
    "перенос репетитором",
    "технические проблемы",
]

otmen = df[df['completed'] == 0]

group = otmen.groupby('cancellation_reason')['price_rub'].sum().reindex(bec, fill_value=0) / 1000

plt.barh(bec, group)
plt.ylabel('Причины отмены')
plt.xlabel('Сумма, тыс. руб')
plt.title('Сумма несостоявшихся занятий по причинам отмены')
plt.tight_layout()
plt.savefig('gr_2.png', dpi=150, bbox_inches='tight')
plt.show()
