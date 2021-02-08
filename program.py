import pandas as pd
from pathlib import Path

filepath = input(
    'Please enter the filepath of the file you\'d like to use: \n')

# Allow people to type the filepath within quotes
if filepath[0] == '"' and filepath[-1] == '"':
    filepath = filepath[1:-1]

filepath = Path(filepath)
df = pd.read_csv(filepath, encoding="utf-8-sig")

# Add Title Column
df['youtube_title'] = df.apply(
    lambda row: f'{row.title} ({row.sku}) by {row.composer}' if str(row.arranger)=='nan'\
  else f'{row.title} ({row.sku}) arr. {row.arranger}', axis=1)

# Description Column
df['youtube_description'] = df.apply(
    lambda row: f'To purchase or for more information: http://www.mymusicpublisher.com/{row.sku}\
\n\nGrade {row.grade} {row.ensemble}\
\n\n{row.web_blurb}\
\n\n{row.copyright_notice}', axis=1)

df.to_csv(filepath, encoding="utf-8-sig")

print('Export Completed.')
