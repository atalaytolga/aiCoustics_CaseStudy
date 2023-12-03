import pandas as pd
from pathlib import Path

csv_path = Path(__file__).resolve().parent.parent / 'results' / 'NISQA_results.csv'
sorted_csv_path = Path(__file__).resolve().parent.parent / 'results' / 'NISQA_results_sorted.csv'

df = pd.read_csv(csv_path)
sorted_df = df.sort_values(by=["mos_pred"], ascending=False)
sorted_df.to_csv(sorted_csv_path, index=False)
