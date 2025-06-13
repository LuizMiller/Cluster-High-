from PIL import Image
import pytesseract

def extract_text_from_image(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image, lang='eng')
        return text.strip()
    except Exception as e:
        print(f"Erro ao processar {image_path}: {e}")
        return ""

def compare_texts(img1_path, img2_path):
    text1 = extract_text_from_image(img1_path)
    text2 = extract_text_from_image(img2_path)

    print(f"Texto da imagem 1: '{text1}'")
    print(f"Texto da imagem 2: '{text2}'")

    if text1 == text2:
        print("✅ Os textos são IGUAIS.")
    else:
        print("❌ Os textos são DIFERENTES.")

# Substitua pelos caminhos das suas imagens
image1 = "imagem1.jpg"
image2 = "imagem2.jpg"

compare_texts(image1, image2)
