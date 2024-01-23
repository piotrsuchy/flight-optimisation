import matplotlib.pyplot as plt

# Hardcoded average values from the table
average_values = {
    "ZPI_1 I": 517667,
    "ZPI_2 I": 538667,
    "ZPII_1 I": 3439333,
    "ZPII_2 I": 3488333,
    "ZPI_1 II": 1491550,
    "ZPI_3 II": 1547404,
    "ZPII_1 II": 6952333,
    "ZPII_3 II": 7157333,
    "ZPI_4 III": 4231528,
    "ZPI_2 III": 4357552,
    "ZPII_1 III": 23210667,
    "ZPII_3 III": 25075000
}

colors = ['skyblue' if 'ZPII' not in key else 'salmon' for key in average_values.keys()]

plt.figure(figsize=(12, 6))
bars = plt.bar(average_values.keys(), average_values.values(), color=colors)
plt.xlabel('Zbiór parametrów')
plt.ylabel('Średnia wartość')
# plt.title('Porównanie średnich wartości z 3 najlepszych uruchomień algorytmu dla różnych zbiorów danych')
plt.xticks(rotation=45)

# Adding values on the bars
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval), va='bottom', ha='center')

# Adding vertical lines to separate different data sets
plt.axvline(3.5, color='gray', linestyle='--')
plt.axvline(7.5, color='gray', linestyle='--')

# Adjusting text labels position
label_height = max(average_values.values()) * 0.65  # Lower position for the labels
plt.text(1.5, label_height, 'Zbiór danych I', horizontalalignment='center', fontweight='bold')
plt.text(5.5, label_height, 'Zbiór danych II', horizontalalignment='center', fontweight='bold')
plt.text(10, label_height, 'Zbiór danych III', horizontalalignment='center', fontweight='bold')

plt.grid(axis='y')
plt.tight_layout()
plt.savefig('aaaa')
plt.show()