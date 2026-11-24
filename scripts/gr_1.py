import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")
months = ['сентябрь', 'октябрь']
paid = df[df['payment_status'] == 'paid']
pending = df[df['payment_status'] == 'pending']
unpaid = df[df['payment_status'] == 'unpaid']

paid = paid.groupby('month')['price_rub'].sum().reindex(months, fill_value=0) / 1000
pending = pending.groupby('month')['price_rub'].sum().reindex(months, fill_value=0) / 1000
unpaid = unpaid.groupby('month')['price_rub'].sum().reindex(months, fill_value=0) / 1000

plt.bar(months, paid, color='#2A9D8F', label='Оплачено')
plt.bar(months, pending, bottom=paid, label='Ожидает оплаты')
plt.bar(months, unpaid, color='#E63946', bottom=pending + paid, label='Потеряно из-за отмен')

plt.ylabel('Сумма в тыс.руб')
plt.title('Выручка, дебиторка и потери по месяцам')
plt.legend()
plt.savefig('gr_1.png', dpi=150)
plt.show()
