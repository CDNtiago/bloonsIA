from PIL import Image, ImageDraw, ImageFont
import os

# Configurações
fonte_caminho = '.\\archives\\fonte\\LuckiestGuy-Regular.ttf'
tamanho_imagem = (260, 80)
diretorio_base = '.\\archives\\imagens\\'
espessura_contorno = 2
numeros = range(1000)  # De 0 a 999

os.makedirs(diretorio_base, exist_ok=True)
fonte = ImageFont.truetype(font=fonte_caminho, size=36)

def desenhar_contorno(draw, texto, posicao, fonte, espessura, cor_contorno):
    x, y = posicao
    for dx in range(-espessura, espessura + 1):
        for dy in range(-espessura, espessura + 1):
            draw.text((x + dx, y + dy), texto, font=fonte, fill=cor_contorno)

for numero in numeros:
    # Formatar o número como string com ponto e símbolo de dollar
    if numero >= 1000:
        numero_str = f"${numero // 1000}.{numero % 1000:03d}"
    else:
        numero_str = f"${numero}"

    diretorio_numero = os.path.join(diretorio_base, str(numero))
    os.makedirs(diretorio_numero, exist_ok=True)

    imagem = Image.new('L', tamanho_imagem, 'white')
    desenho = ImageDraw.Draw(imagem)
    caixa_texto = desenho.textbbox((0, 0), numero_str, font=fonte)
    largura_texto = caixa_texto[2] - caixa_texto[0]
    altura_texto = caixa_texto[3] - caixa_texto[1]
    posicao_texto = ((tamanho_imagem[0] - largura_texto) // 2, (tamanho_imagem[1] - altura_texto) // 2)
    
    desenhar_contorno(desenho, numero_str, posicao_texto, fonte, espessura_contorno, 'black')
    desenho.text(posicao_texto, numero_str, fill='white', font=fonte)

    caminho_saida = os.path.join(diretorio_numero, f'{numero}.png')
    imagem.save(caminho_saida)