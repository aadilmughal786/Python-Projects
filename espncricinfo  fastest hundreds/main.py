# import required modules
import pandas as pd
import sqlite3
import mechanicalsoup


# cteate browser object
url = "https://stats.espncricinfo.com/ci/content/records/211608.html"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

# main columns names
mcols = browser.page.find_all("th")
mcols = [val.text.replace("\n", "").replace(" ", "_").replace(
    "(", "").replace(")", "") for val in mcols]
mcols[2] = "sixes"
mcols[3] = "fours"

# other columns
ocols = browser.page.find_all("td")
ocols = [val.text.replace("\n", "") for val in ocols]

dictionary = {}

for index, key in enumerate(mcols):
    data = ocols[index::len(mcols)]
    dictionary[key] = data


# make data frame from dictionary
df = pd.DataFrame(data=dictionary)
# print(df)

# establish connection
connection = sqlite3.connect("fastestHundreds.db")

# create cursor
cur = connection.cursor()

cur.execute("create table if not exists FHundreds (" + ",".join(mcols) + ")")

col_fil = ",".join(len(mcols)*"?")

for i in range(len(df)):
    cur.execute("insert into FHundreds values ("+col_fil+")", df.iloc[i])

# commit the changes
connection.commit()

# close the connection
connection.close()
