import streamlit as st
import re
from collections import OrderedDict

st.set_page_config(page_title="Generador Poético con Pi", layout="wide")

st.title("📐 Generador Poético con los decimales de π")
st.markdown("Transforma cualquier texto en un poema único utilizando los decimales de π como clave matemática.")

# Limpia y normaliza el texto
def limpiar_texto(texto):
    palabras = re.findall(r"\b[a-záéíóúüñ]+\b", texto.lower())
    palabras_unicas = list(OrderedDict.fromkeys(palabras))
    return palabras_unicas

# Carga los decimales de pi
@st.cache_data
def cargar_decimales_pi():
    with open("pi_decimals.txt", "r") as f:
        return f.read().strip().replace("\n", "")

archivo_subido = st.file_uploader("📄 Sube un archivo .txt", type="txt")

if archivo_subido:
    texto = archivo_subido.read().decode("utf-8")
    palabras = limpiar_texto(texto)
    total = len(palabras)
    st.success(f"✔️ El texto contiene {total} palabras únicas.")

    pi = cargar_decimales_pi()
    usados = set()
    resultado = []
    i = 0

    while len(usados) < total and i + 4 <= len(pi):
        bloque = int(pi[i:i+4])
        if 1 <= bloque <= total and bloque not in usados:
            resultado.append(palabras[bloque - 1])
            usados.add(bloque)
        i += 1

    poema = " ".join(resultado)
    st.markdown("### ✨ Poema generado:")
    st.text_area("Poema:", poema, height=300)
    st.download_button("💾 Descargar poema", poema, file_name="poema_pi.txt", mime="text/plain")

else:
    st.info("📥 Sube un archivo .txt para comenzar.")