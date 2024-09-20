import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

lista_archivos = os.listdir(caminho)

locais = {
    "imagens": [".jpeg", ".png", ".jpg", ".img", ".gif"],
    "pdfs": [".pdf"],
    "videos": [".mp4", ".mp3", ".mov"],
    "aplicativos": [".exe"],
    "zips": [".7z", ".rar"]
}

for arquivo in lista_archivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            if not os.path.exists(f"{caminho}/{pasta}"):
                os.mkdir(f"{caminho}/{pasta}")
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}")