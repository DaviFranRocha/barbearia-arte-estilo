import os
from flask import Flask, render_template

app = Flask(__name__)

# Pasta onde ficam as fotos dos cortes
GALLERY_FOLDER = os.path.join(app.static_folder, "images", "cortes")
ALLOWED_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif"}

# Foto do barbeiro (aparece na seção "A Barbearia").
# Salve o arquivo como static/images/barbeiro.jpg (ou .png/.webp) e ela
# entra no lugar automaticamente. Sem o arquivo, mostra as iniciais "RV".
BARBER_PHOTO_NAME = "barbeiro"
IMAGES_FOLDER = os.path.join(app.static_folder, "images")


def get_gallery_images():
    """Lê a pasta static/images/cortes e devolve a lista de arquivos de imagem."""
    if not os.path.isdir(GALLERY_FOLDER):
        return []
    files = [
        f for f in os.listdir(GALLERY_FOLDER)
        if os.path.splitext(f)[1].lower() in ALLOWED_EXT
    ]
    files.sort()
    return files


def get_barber_photo():
    """Procura static/images/barbeiro.(jpg|jpeg|png|webp|gif) e devolve o nome do
    arquivo encontrado, ou None se ainda não foi adicionada nenhuma foto."""
    if not os.path.isdir(IMAGES_FOLDER):
        return None
    for ext in (".jpg", ".jpeg", ".png", ".webp", ".gif"):
        candidate = BARBER_PHOTO_NAME + ext
        if os.path.isfile(os.path.join(IMAGES_FOLDER, candidate)):
            return candidate
    return None


@app.route("/")
def home():
    imagens = get_gallery_images()
    foto_barbeiro = get_barber_photo()
    return render_template("index.html", imagens=imagens, foto_barbeiro=foto_barbeiro)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
