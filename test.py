import wfdb
import pandas as pd

for i in range(2, 1999):
    try:
        record = wfdb.rdsamp('E:/ECG/dataset/records100/00000/' + str(i).zfill(5) + '_lr')
    except FileNotFoundError:
        print(f"File not found: {i}. Skipping...")
        continue

    df = pd.DataFrame(record[0], columns=record[1]['sig_name'])
    df.to_csv(f'{i}.csv', index=False)
