import csv

file_path = "spotify-2023.csv"

def process_csv(file_path):
    top_songs = {}  

    with open(file_path, "r", encoding="latin-1") as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  

        for row in reader:
            ano_de_lançamento = int(row[3])
            if 2012 <= ano_de_lançamento <= 2022:
                if "," in row[0] or "," in row[1] or '"' in row[0] or '"' in row[1]:
                    continue  
                if ano_de_lançamento not in top_songs or int(row[8]) > top_songs[ano_de_lançamento][3]:
                    top_songs[ano_de_lançamento] = [row[0], row[1], ano_de_lançamento, int(row[8])]

    return list(top_songs.values())

top_songs_list = process_csv(file_path)

print(top_songs_list)