import os

with open("meus_livros.csv", "w") as arquivo:
    arquivo.write("Título,Autor,Ano de publicação,Número de páginas\n")
    arquivo.write("Lovecraft,H P LOVECRAFT,2017,384\n")
    arquivo.write("Orwell,George,1984,1949,328 \n")
    arquivo.write("Rowling,J.K.,Harry Potter e a Pedra Filosofal, 1997,254 \n")
    arquivo.write("Tolkien, J.R.R.,O Senhor dos Anéis: A Sociedade do Anel, 1954,480\n")
    arquivo.write("Atwood,Margaret,O Conto da Aia, 1985,311\n")
    arquivo.write("Bradbury,Ray,Fahrenheit 451, 1953,227\n")
    arquivo.write("Huxley,Aldous,Admirável Mundo Novo, 1932,288\n")
    arquivo.write("Vonnegut,Kurt,Matadouro 5, 1969,275\n")
    arquivo.write("Gaiman,Neil,American Gods, 2001,635\n")
    arquivo.write("Murakami,Haruki,Kafka à Beira-Mar, 2002,615\n")
    arquivo.close()

print(os.path.abspath("meus_livros.csv"))


