import streamlit as st
import time

# 1. Configuración de la página
st.set_page_config(page_title="Terminal Confidencial", page_icon="🔒", layout="centered")

# 2. Inyección de CSS para estilo Hacker (Cybersecurity Vibe)
st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3, h4, p {
        color: #00ff00 !important;
    }
    .stButton>button {
        background-color: #00ff00;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid #00ff00;
    }
    .stButton>button:hover {
        background-color: #000000;
        color: #00ff00;
    }
    </style>
""", unsafe_allow_html=True)

# 3. Control de estado para saber si ya adivinó la contraseña
if 'acceso_concedido' not in st.session_state:
    st.session_state.acceso_concedido = False

# 4. Pantalla de Bloqueo (Login)
if not st.session_state.acceso_concedido:
    st.title("🖥️ SISTEMA DE ARCHIVOS ENCRIPTADO")
    st.write("### ADVERTENCIA: ACCESO RESTRINGIDO")
    st.write("Detectando conexión entrante... Para desencriptar el paquete 'San_Valentin_2026.enc', debe superar la validación de seguridad cognitiva.")
    
    st.divider()
    
    st.write("#### Pregunta de Seguridad (Nivel: Ciencias de la Educación)")
    # Puedes cambiar la pregunta por algo que ella sepa perfecto
    respuesta = st.text_input("¿Quién es el famoso autor de la teoría del desarrollo cognitivo? (Pista: Empieza con P)", type="password")
    
    if st.button("Ejecutar Desencriptación"):
        # Validación de la respuesta (ignora mayúsculas y espacios)
        if respuesta.strip().lower() in ["piaget", "jean piaget"]:
            with st.spinner('Evadiendo firewall y desencriptando llaves RSA...'):
                time.sleep(2.5) # Pausa dramática
            st.session_state.acceso_concedido = True
            st.rerun()
        elif respuesta != "":
            st.error("❌ ACCESO DENEGADO. Intento registrado en el log de seguridad.")
            
# 5. Pantalla de Éxito (Payload Romántico)
else:
    st.balloons() # Lluvia de globos nativa de Streamlit
    st.title("🔓 ¡Acceso Concedido!")
    st.write("### Desencriptación exitosa al 100%.")
    st.divider()
    
    # Tu carta
    st.write("¡Feliz San Valentín! ❤️")
    st.write("Lograste bypassear la seguridad de mi sistema (y la de mi corazón).")
    st.write("Quería prepararte algo diferente, mezclando mis códigos con tus conocimientos. Estoy muy orgulloso de todo lo que estás logrando en tu carrera.")
    st.write("")
    st.write("🎁 **Carga útil entregada:**")
    st.write("- Un vale válido por una cena VIP con menú ilimitado en Don Yorch.")
    st.write("- Muchos abrazos y besos (sin encriptar).")
    st.write("")
    st.write("Con cariño, Marco. 👨‍💻")