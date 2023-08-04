import csv

# Abra o arquivo urls.csv
with open('urls.csv', 'r') as f:
    reader = csv.reader(f)

    # Leia as URLs do arquivo
    for row in reader:
        url = row[0]

        # Adicione a URL dentro de <loc>URL</loc>
        sitemap = """
    <url>
        <loc>{}</loc>
        <lastmod>2023-07-18</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.5</priority>
    </url>
    """.format(url)

        # Repita esse trecho para cada URL do CSV (e faça a mágica acontecer)
        with open('sitemap.xml', 'a') as f:
            f.write(sitemap)