import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file into a DataFrame
df = pd.read_csv('E:\ECG\949.csv')

# Extract lead columns from the DataFrame
leads = ['I', 'II', 'III', 'AVR', 'AVL', 'AVF', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6']

# Plot each lead on a separate graph
fig, axs = plt.subplots(len(leads), 1, figsize=(10, 20), sharex=True)

for i, lead in enumerate(leads):
    axs[i].plot(df.index, df[lead])
    axs[i].set_ylabel(lead)
    axs[i].set_title(f'Lead {lead}')

plt.xlabel('Time')
plt.tight_layout()
plt.show()
