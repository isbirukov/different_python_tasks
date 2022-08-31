import requests

url = "https://stepic.org/media/attachments/course67/3.6.3/"
path_to_file = "C:\\Users\\isbir\\Downloads\\dataset_3378_3.txt"
path_out = "C:\\Users\\isbir\\Downloads\\result.txt"
s = ""
next_file = ""
with open (path_to_file) as file:
    s = file.read()

while not s.startswith("We"):
    lst = s.split("/")
    print("LST", lst)
    next_file = lst[-1].strip("\n")
    print("Name next file", next_file)
    print("URL next file", url + next_file)
    r = requests.get(url + next_file)
    s = r.text
    print(s)

with open(path_out, 'w') as f:
    f.write(s)