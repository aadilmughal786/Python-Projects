# import required modules
import pandas as pd
import sqlite3
import mechanicalsoup


# cteate browser object
url = "https://en.wikipedia.org/wiki/Comparison_of_Linux_distributions"
browser = mechanicalsoup.StatefulBrowser()
browser.open(url)

# main columns names
mcols = browser.page.find_all("th")
mcols = [val.text.replace("\n", "").replace(" ", "_").replace(
    "(", "").replace(")", "") for val in mcols]
start_col = mcols.index("Distribution")
end_col = mcols.index("Status")
mcols = mcols[start_col:end_col+1]

# distro name column
dnames = browser.page.find_all("th", attrs={"class": "table-rh"})
dnames = [val.text.replace("\n", "") for val in dnames]
index_of_zorin_os = dnames.index("Zorin OS")
dnames = dnames[:index_of_zorin_os+1]


# other columns
ocols = browser.page.find_all("td")
ocols = [val.text.replace("\n", "") for val in ocols]
start_index = ocols.index("AlmaLinux Foundation")
end_index = ocols.index("Binary blobs")
ocols = ocols[start_index:end_index]


# shape data in more structured way
dictionary = {"Distribution": dnames}  # for first distro names column

for index, key in enumerate(mcols[1:]):
    data = ocols[index::11]
    dictionary[key] = data


# make data frame from dictionary
df = pd.DataFrame(data=dictionary)

# establish connection
connection = sqlite3.connect("Linux_distro.db")

# create cursor
cur = connection.cursor()

cur.execute("create table if not exists linux (" + ",".join(mcols) + ")")

col_fil = ",".join(len(mcols)*"?")

for i in range(len(df)):
    cur.execute("insert into linux values ("+col_fil+")", df.iloc[i])

# commit the changes
connection.commit()

# close the connection
connection.close()
