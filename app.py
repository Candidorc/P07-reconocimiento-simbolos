import streamlit as st
import tensorflow as tf
import numpy as np
import json
from PIL import Image

# Cargar modelo y clases
modelo = tf.keras.models.load_model(r'C:\Users\javir\Downloads\app_hasy\modelo_hasy.h5')
with open(r'C:\Users\javir\Downloads\app_hasy\clases.json', 'r') as f:
    clases = json.load(f)

# Interfaz
st.title("🔢 Reconocimiento de Símbolos Matemáticos")
st.write("Sube una imagen de un símbolo matemático manuscrito y el modelo lo clasificará.")

imagen_subida = st.file_uploader("Sube una imagen", type=["png", "jpg", "jpeg"])

if imagen_subida is not None:
    imagen = Image.open(imagen_subida).convert('L').resize((32, 32))
    st.image(imagen, caption="Imagen subida", width=150)
    
    img_array = np.array(imagen, dtype=np.float32) / 255.0
    img_array = img_array.reshape(1, 32, 32, 1)
    prediccion = modelo.predict(img_array)
    indice = np.argmax(prediccion)
    confianza = prediccion[0][indice] * 100
    simbolo = clases[str(indice)]
    
    st.success(f"**Símbolo predicho:** {simbolo}")
    st.info(f"**Confianza:** {confianza:.2f}%")