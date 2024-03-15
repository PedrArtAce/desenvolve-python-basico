urls = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
dom = []

for i in urls:
    dom.append(i[4:-4])

print(dom)