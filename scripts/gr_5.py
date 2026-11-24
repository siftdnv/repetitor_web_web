import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("../tutor_lessons.csv")
platform = df['platform'].value_counts()
plt.title('Распределение занятий по онлайн платформам')
plt.pie(platform, wedgeprops={'width': 0.65, 'edgecolor': 'white', 'linewidth': 2},
        colors=['#2A9D8F', '#E9C46A', '#F4A261', '#E76F51'], labels=platform.index, autopct='%1.0f%%')
plt.savefig('gr_5.png', dpi=150, bbox_inches='tight')
plt.show()
