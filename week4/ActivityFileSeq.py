# data = open("./sample_junk_mail.csv")
# for line in data:
#   print(line[0:-1])
# data.close()

import pandas as pd
df = pd.read_csv('sample_junk_mail.csv')
print(df.head())