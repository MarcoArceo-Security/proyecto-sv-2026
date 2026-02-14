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
    /* Estilo para los inputs */
    .stTextInput > div > div > input {
        color: #00ff00;
        background-color: #262730;
        border-color: #00ff00;
    }
    /* Estilo para botones primarios (SÍ / Verificar) */
    .stButton > button {
        background-color: #00ff00;
        color: #000000;
        font-weight: bold;
        border-radius: 5px;
        border: 2px solid #00ff00;
        width: 100%;
    }
    .stButton > button:hover {
        background-color: #000000;
        color: #00ff00;
        border-color: #00ff00;
    }
    /* Estilo específico para el botón NO (rojo) */
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
# Inicializamos las variables para saber en qué etapa estamos
if 'etapa' not in st.session_state:
    st.session_state.etapa = 0 # 0: Pregunta SV, 1: Cuestionario, 2: Carta
if 'intentos_beso' not in st.session_state:
    st.session_state.intentos_beso = 0

# --- 3. Lógica de la Aplicación ---

# ================= ETAPA 0: ¿Quieres ser mi San Valentín? =================
if st.session_state.etapa == 0:
    st.title("❤️ UNA PREGUNTA IMPORTANTE...")
    st.write("### Protocolo de inicio de sesión romántico detectado.")
    st.divider()
    
    st.write("<h1>¿Quieres ser mi San Valentín?</h1>", unsafe_allow_html=True)
    st.write("") # Espacio

    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("SÍ, ACEPTO ❤️", key="btn_si"):
            st.session_state.etapa = 1
            st.rerun()
            
    with col2:
        if st.button("NO 🚫", key="btn_no"):
            st.error("❌ Error 404: Respuesta 'NO' no encontrada en la base de datos del corazón. Por favor, intenta de nuevo con la opción correcta.")

# ================= ETAPA 1: El Cuestionario de Seguridad =================
elif st.session_state.etapa == 1:
    st.title("🔐 AUTENTICACIÓN MULTIFACTOR")
    st.write("¡Excelente elección! Para acceder al archivo encriptado, demuestra qué tanto conoces nuestro sistema.")
    st.divider()

    # --- Las Preguntas ---
    q_aniversario = st.text_input("1. ¿Cuándo es nuestro aniversario? (DD/MM/AA)", placeholder="Ej: 25/12/23")
    q_color = st.text_input("2. ¿Cuál es mi color favorito?")
    q_personaje = st.text_input("3. ¿Cuál es mi personaje favorito?")
    
    # Lógica especial para la pregunta del beso
    label_beso = "4. ¿Cuándo fue nuestro primer beso? (DD/MM/AA)"
    if st.session_state.intentos_beso >= 3:
        label_beso += " (Pista: La respuesta es 10/12/23 😉)"
    
    q_beso = st.text_input(label_beso, placeholder="Ej: 10/12/23")
    
    q_serie = st.text_input("5. ¿Cuál es nuestra serie para comer?")
    q_perry = st.text_input("6. Oye... ¿y Perry?")

    st.divider()
    
    if st.button("Verificar Respuestas y Desencriptar"):
        # Respuestas correctas
        a_aniversario = "25/12/23"
        a_color = "rojo"
        a_personaje = "iron man"
        a_beso = "10/12/23"
        a_serie = "phineas y ferb"
        a_perry = [
            "es un ornitorrinco", 
            "¡ahí estás perry!", 
            "grrr", 
            "agente p", 
            "haciendo nada",
            "no se"
        ] # Varias opciones válidas para Perry

        # Validación
        errores = []
        if q_aniversario.strip() != a_aniversario:
            errores.append("Fecha de aniversario incorrecta.")
        if q_color.strip().lower() != a_color:
            errores.append("Color favorito incorrecto.")
        if q_personaje.strip().lower() != a_personaje:
            errores.append("Personaje favorito incorrecto.")
        
        # Validación especial del beso
        if q_beso.strip() != a_beso:
            errores.append("Fecha del primer beso incorrecta.")
            st.session_state.intentos_beso += 1
        
        if q_serie.strip().lower() != a_serie:
            errores.append("Serie incorrecta.")
        
        # Validación flexible para Perry (si contiene alguna de las frases clave)
        perry_correcto = False
        resp_perry_usuario = q_perry.strip().lower()
        for opcion in a_perry:
            if opcion in resp_perry_usuario and resp_perry_usuario != "":
                 perry_correcto = True
                 break
        if not perry_correcto and resp_perry_usuario != "no se": # Aceptamos "no se" como válida también si quieres ser amable
             # Si quieres ser estricto y que tenga que decir la frase, quita el 'and resp_perry_usuario != "no se"'
             # Si quieres que cualquier cosa que no sea vacía cuente, cambia la lógica.
             # Por ahora, dejemos que si no atina a las frases clave, sea error.
             if resp_perry_usuario == "":
                 errores.append("¿Y Perry? ¡No dejaste respuesta!")
             else:
                 # Si quieres que "no se" sea válida, descomenta esto:
                 # if resp_perry_usuario == "no se": pass 
                 # else: errores.append("Respuesta sobre Perry incorrecta.")
                 
                 # Si quieres ser estricto:
                 errores.append("Respuesta sobre Perry incorrecta. ¿Dónde está?")

        # Resultado de la validación
        if not errores:
            # --- Animación de Desencriptación ---
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
        else:
            st.error("⚠️ ACCESO DENEGADO. Se encontraron errores:")
            for error in errores:
                st.write(f"- {error}")
            if st.session_state.intentos_beso > 0 and st.session_state.intentos_beso < 3:
                 st.warning(f"Llevas {st.session_state.intentos_beso} intento(s) fallido(s) en la pregunta del beso.")


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
        Eres la persona más increíble que conozco. Admiro muchísimo tu dedicación a la educación, cómo siempre buscas aprender más y la pasión que le pones a todo. Me encanta compartir la vida contigo, desde nuestros maratones de Phineas y Ferb mientras comemos, hasta construir juntos un futuro que es aún mejor que las mejores hamburguesas de Don Yorch.
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