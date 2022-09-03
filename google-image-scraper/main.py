import mechanicalsoup

url  = "https://images.google.com/"

browser = mechanicalsoup.StatefulBrowser()
browser.open(url)
# print(browser.get_url())
# print(browser.get_current_page())

# target the search input 
browser.select_form()
# browser.get_current_form().print_summary()
# search term 
item = input("Enter item name : ")
browser["q"] = item

# submit or search btn 
# browser.launch_browser()
browser.submit_selected()

# new url after btn clicked 
# print(browser.get_url())

new_url = browser.get_url()
browser.open(new_url)

page = browser.get_current_page()
all_images = page.find_all("img")
# print(all_images)

#target the src attribute of img tag

images = []
for src in all_images:
	src = src.get("src")
	images.append(src)


# correct url 
images = [src for src in images if src.startswith("https")]


# to create folder 
import os
# path = os.getcwd()
folder_name = item + "s"
os.mkdir(folder_name) 
os.chdir(folder_name)


import wget
for index,src in enumerate(images):
	save_as = f"cat{index}.jpg"
	wget.download(src,save_as)

