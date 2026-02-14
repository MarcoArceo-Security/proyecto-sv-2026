import streamlit as st
import time

# --- 1. Configuración de la página y CSS ---
st.set_page_config(page_title="Terminal Confidencial", page_icon="🔒", layout="centered")

st.markdown("""
    <style>
    .stApp {
        background-color: #0e1117;
        color: #00ff00;
        font-family: 'Courier New', Courier, monospace;
    }
    h1, h2, h3, h4, p, .stTextInput > label, .stRadio > label {
        color: #00ff00 !important;
    }
    .stTextInput > div > div > input {
        color: #00ff00;
        background-color: #262730;
        border-color: #00ff00;
    }
    .stButton > button, .stFormSubmitButton > button {
        background-color: #00ff00;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid #00ff00;
        width: 100%;
    }
    .stButton > button:hover, .stFormSubmitButton > button:hover {
        background-color: #000000;
        color: #00ff00;
        border-color: #00ff00;
    }
    div[data-testid="column"]:nth-of-type(2) .stButton > button {
        background-color: #ff0000;
        border-color: #ff0000;
        color: #ffffff;
    }
    div[data-testid="column"]:nth-of-type(2) .stButton > button:hover {
        background-color: #000000;
        color: #ff0000;
    }
    </style>
""", unsafe_allow_html=True)

# --- 2. Control de Estado (Session State) ---
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0 
if 'intentos_beso' not in st.session_state:
    st.session_state.intentos_beso = 0
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 0

# --- 3. Lógica de la Aplicación ---

# ================= ETAPA 0: ¿Quieres ser mi San Valentín? =================
if st.session_state.etapa == 0:
    st.title("❤️ UNA PREGUNTA IMPORTANTE...")
    st.write("### Protocolo de inicio de sesión romántico detectado.")
    st.divider()
    
    st.write("<h1>¿Quieres ser mi San Valentín?</h1>", unsafe_allow_html=True)
    st.write("")

    col1, col2 = st.columns(2)
    with col1:
        if st.button("SÍ, ACEPTO ❤️"):
            st.session_state.etapa = 1
            st.rerun()
    with col2:
        if st.button("NO 🚫"):
            st.error("❌ Error 404: Respuesta 'NO' no encontrada en la base de datos del corazón.")

# ================= ETAPA 1: El Cuestionario Paso a Paso =================
elif st.session_state.etapa == 1:
    st.title("🔐 AUTENTICACIÓN MULTIFACTOR")
    st.write("Demuestra qué tanto conoces nuestro sistema para acceder.")
    st.divider()

    # Lista de preguntas con sus respuestas y el "ejemplo" que verá de fondo
    preguntas = [
        {"q": "¿Cuándo es nuestro aniversario? (DD/MM/AA)", "a": "25/12/23", "ej": "25/12/23"},
        {"q": "¿Cuál es mi color favorito?", "a": "rojo", "ej": "rojo"},
        {"q": "¿Cuál es mi personaje favorito?", "a": "iron man", "ej": "iron man"},
        {"q": "¿Cuándo fue nuestro primer beso? (DD/MM/AA)", "a": "10/12/23", "ej": "10/12/23"},
        {"q": "¿Cuál es nuestra serie para comer?", "a": "phineas y ferb", "ej": "phineas y ferb"},
        {"q": "Oye...", "a": "y perry?", "ej": "y perry?"}
    ]

    idx = st.session_state.pregunta_actual

    # Mostrar la pregunta actual si aún no llegamos al final
    if idx < len(preguntas):
        p = preguntas[idx]
        
        label = p["q"]
        # Mantengo tu idea original: si falla 3 veces en el beso, le da una pequeña ayudadita extra en el texto
        if idx == 3 and st.session_state.intentos_beso >= 3:
            label += " (Pista: Intenta con el 10/12/23 😉)"

        st.write(f"### Desafío {idx + 1} de {len(preguntas)}")
        
        # El formulario permite enviar la respuesta presionando Enter
        with st.form(key=f"form_{idx}"):
            respuesta = st.text_input(label, placeholder=f"Ej: {p['ej']}")
            submit = st.form_submit_button("Verificar y Siguiente")
            
            if submit:
                # Quitamos espacios extras, convertimos a minúsculas y eliminamos signos de interrogación por si acaso
                resp_usuario = respuesta.strip().lower().replace("¿", "").replace("?", "")
                resp_correcta = p["a"].lower().replace("¿", "").replace("?", "")

                if resp_usuario == resp_correcta:
                    st.session_state.pregunta_actual += 1 # Avanza a la siguiente pregunta
                    st.rerun()
                else:
                    if idx == 3:
                        st.session_state.intentos_beso += 1
                    st.error("❌ Respuesta incorrecta. Intenta de nuevo.")
    else:
        # Ya respondió todo bien
        st.success("✅ Todos los desafíos completados con éxito.")
        st.write("El servidor ha validado tu identidad. Pulsa el botón para desencriptar tu sorpresa.")
        
        if st.button("Iniciar Desencriptación Final"):
            with st.spinner('Respuestas verificadas. Iniciando secuencia de desencriptación RSA-4096...'):
                time.sleep(1)
                st.code("Cargando llave privada... [OK]", language="bash")
                time.sleep(0.8)
                st.code("Desofuscando código binario... [OK]", language="bash")
                time.sleep(1.2)
                st.code("Compilando mensaje de amor... [COMPLETADO]", language="bash")
                time.sleep(1)
            
            st.session_state.etapa = 2
            st.rerun()

# ================= ETAPA 2: La Carta Desencriptada =================
elif st.session_state.etapa == 2:
    st.balloons()
    st.title("🔓 ARCHIVO DESENCRIPTADO CON ÉXITO")
    
    st.markdown("""
    <div style='background-color: #1c1e26; padding: 25px; border-radius: 10px; border: 2px solid #00ff00;'>
        <h3>¡Hola, mi amor! ❤️</h3>
        <p>
        Si estás leyendo esto, es porque lograste superar todas las barreras de seguridad... y las de mi corazón. ¡Feliz San Valentín!
        </p>
        <p>
        Eres la persona más increíble que conozco. Admiro muchísimo tu dedicación, cómo siempre buscas aprender más y la pasión que le pones a todo. Me encanta compartir la vida contigo, desde nuestros maratones de Phineas y Ferb mientras comemos, hasta construir juntos un futuro que es aún mejor que las mejores hamburguesas de Don Yorch.
        </p>
        <p>
        Gracias por ser mi compañera de aventuras, mi apoyo incondicional y mi 'player 2' en este juego llamado vida. Cada día a tu lado es un regalo, desde ese primer beso el 10/12/23 hasta hoy. Te amo muchísimo y estoy emocionado por todo lo que viene para nosotros.
        </p>
        <p>
        Con todo mi amor,<br>
        <b>Marco. 👨‍💻</b>
        </p>
    </div>
    """, unsafe_allow_html=True)