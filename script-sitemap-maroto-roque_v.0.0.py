import csv

#Ler a lista de URLs da planilha
with open("urls.csv", "r") as csvfile:
    reader = csv.reader(csvfile)
    urls = list(reader)

#Adicione o lastmod, changefreq e priority a cada URL
for url in urls:
    url.append("2023-07-27")
    url.append("weekly")
    url.append("0.5")

#agora, faça a mágica acontecer e bentido seja nosso sitemap.xml de cada dia. Amém.
with open("sitemap.xml", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["loc", "lastmod", "changefreq", "priority"])
    writer.writerows(urls)