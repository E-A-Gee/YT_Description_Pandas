import pandas as pd

filepath = input(
    'Please enter the filepath of the file you\'d like to use: \n')

filepath = filepath.replace('\\', '\\\\')
df = pd.read_csv(filepath, encoding="utf-8-sig")

df['youtube_description'] = df.apply(
    lambda row: f'To purchase or for more information: http://www.mymusicpublisher.com/{row.sku}\
\n\nGrade {row.grade} {row.ensemble}\
\n\n{row.web_blurb}\
\n\n{row.copyright_notice}', axis=1)

df.to_csv(filepath, encoding="utf-8-sig")

print('Export Completed.')
