import re
import datetime

f = open(path_to_file, 'r')
w = open(path_to_file, 'w')

delimiter_exp = re.compile("_{16}")
posts = delimiter_exp.split(f.read())

def get_time(post):
    date = re.search("\d{2}[.]\d{2}[.]\d{4}[,][ ]\d{2}[:]\d{2}", post).group()
    post_datetime = datetime.datetime.strptime(date, "%d.%m.%Y, %H:%M")
    return post_datetime

posts.sort(key=get_time)

print(posts)

for post in posts:
    w.write(post + "\n")


