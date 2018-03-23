from bs4 import BeautifulSoup
import os, os.path
import re
file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\room_lists\\"
# file_path2 = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\blockchain jobs\\jobs\\"+str(1)+".html"
# with open(file_path2, encoding="utf-8") as fp2:
#     html_doc = str(fp2.read().encode('utf-8'))
#     soup = BeautifulSoup(html_doc, 'html.parser')
#
#
# salary = soup.find('h3').findNext('p')
# print(salary)


profiles_list = []

for i in range(10):
    file_path2 = file_path + str(i) + "_room_list.html"
    with open(file_path2, encoding="utf-8") as fp2:
        html_doc = str(fp2.read().encode('utf-8'))
        soup = BeautifulSoup(html_doc, 'html.parser')

    headlines = soup.find_all("div", {"class": "info_block"})

    for x in headlines:
        profile_id = x["data-reactid"]
        profiles_list.append(profile_id)
        if profile_id not in profiles_list:
            profiles_list.append(profile_id)
    # print(profile_id)

regex = re.compile(r"\.0\.9\.0\.1\.3\.0\.3\.1\.0\.3:\$..?\.\$item_", re.IGNORECASE)
# regex2 = re.compile(r".1.1")
for x in profiles_list:
    x = regex.sub("", x)
    x = x.replace(".1.1", "")
        # x = regex2.sub("", x)
    x = "https://www.roomster.com/listings/" +x
    print(x)
