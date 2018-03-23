from bs4 import BeautifulSoup
import os, os.path
import re
import csv
file_path = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\individual rooms\\"
# file_path2 = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\blockchain jobs\\jobs\\"+str(1)+".html"
# with open(file_path2, encoding="utf-8") as fp2:
#     html_doc = str(fp2.read().encode('utf-8'))
#     soup = BeautifulSoup(html_doc, 'html.parser')
file_input = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\all_room_ads_output.txt"
output_data = "C:\\Users\\cjwar\\Documents\\Esven Enterprises\\Roomster\\output_database.csv"
# salary = soup.find('h3').findNext('p')
# print(salary)


profiles_list = []
all_details = [[]]
room_urls_list = []

with open(file_input) as fi:
    content = fi.readlines()
    content = [x.strip() for x in content]
    for x in content:
        room_urls_list.append(x)

for i in range(358):
    # file_path2 = file_path + "0_room.html"
    file_path2 = file_path + str(i) + "_room.html"
    with open(file_path2, encoding="utf-8") as fp2:
        html_doc = str(fp2.read().encode('utf-8'))
        soup = BeautifulSoup(html_doc, 'html.parser')

    list_title = soup.find("h1", {"class": "listing__title"}).get_text()
    cost = soup.find("span", {"class": "value"}).get_text()
    location = soup.find_all("span", string="Location")[1].parent.parent.find("div", {"class": "block__content"}).find("span").get_text()
    try:
        description = soup.find_all("span", string="Description")[1].parent.parent.find("div", {"class": "block__content"}).get_text()
    except IndexError:
        description = "no data"
    try:
        is_furnished = soup.find("span", string="Furnished").parent.find_all("span")[2].get_text()
    except:
        is_funished = "no data"
    try:
        move_in_fee = soup.find("span", string="Move-in Fee").parent.find_all("span")[2].get_text()
    except AttributeError:
        is_furnished = "no data"
    try:
        host_cleanliness = soup.find("span", string="My Cleanliness").parent.find_all("span")[2].get_text()
    except AttributeError:
        host_cleanliness = "no data"

    '''Amenities under construction'''
    # amenities = soup.find("span", string="Amenities").parent
    # list_title = soup.find("h1", {"class": "listing__title"})
    # list_title = soup.find("h1", {"class": "listing__title"})
    # list_title = soup.find("h1", {"class": "listing__title"})

    print("Listing title: " + list_title)
    print("Cost: $" + cost)
    print("Location: " + location)
    print("Description: " + description)
    print("Furnished: " + is_furnished)
    print("Roommate cleanliness: " + host_cleanliness)
    print("------------------------------------------------")
    all_details[i].append(room_urls_list[i])
    all_details[i].append(list_title)
    all_details[i].append(cost)
    all_details[i].append(location)
    all_details[i].append(description)
    all_details[i].append(is_furnished)
    all_details[i].append(move_in_fee)
    all_details[i].append(host_cleanliness)
    all_details.append([])

for x in all_details:
    print(x)
with open(output_data, 'w') as csvfile:
    for x in all_details:
        for y in x:
            csvfile.write(y + "| ")
        csvfile.write("\n")
# print(all_details)
