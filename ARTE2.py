import streamlit as st
from datetime import datetime

# Configuración de la página
st.set_page_config(
    page_title="Creíste en mí porque sonaba como tú",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# CSS personalizado para estética minimalista y tecnológica
st.markdown("""
<style>
    /* Fondo y colores principales */
    .stApp {
        background-color: #0a0e27;
        color: #e0e0e0;
    }
    
    /* Títulos */
    h1, h2, h3 {
        color: #ffffff;
        font-family: 'Inter', sans-serif;
        font-weight: 300;
        letter-spacing: -0.5px;
    }
    
    /* Botones */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        padding: 12px 40px;
        font-size: 16px;
        font-weight: 500;
        border-radius: 8px;
        transition: all 0.3s ease;
        width: 100%;
        margin-top: 20px;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 20px rgba(102, 126, 234, 0.4);
    }
    
    /* Radio buttons */
    .stRadio > label {
        color: white;
        font-size: 14px;
        font-weight: 400;
    }
    
    .stRadio > div {
        background-color: white;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 10px;
    }
    
    /* Checkboxes */
    .stCheckbox > label {
        color: #ffffff !important;
        font-size: 15px;
    }
    
    .stCheckbox > label > div {
        color: #ffffff !important;
    }
    
    /* Progreso */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Contenedor de noticia */
    .noticia-container {
        background: linear-gradient(135deg, #1a1f3a 0%, #2d3561 100%);
        border-left: 4px solid #667eea;
        padding: 30px;
        border-radius: 12px;
        margin: 20px 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.3);
    }
    
    .noticia-titulo {
        font-size: 28px;
        font-weight: 600;
        color: #ffffff;
        margin-bottom: 15px;
        line-height: 1.3;
    }
    
    .noticia-texto {
        font-size: 16px;
        line-height: 1.7;
        color: #d0d0d0;
        margin-bottom: 20px;
    }
    
    .noticia-fuente {
        font-size: 13px;
        color: #888;
        font-style: italic;
        margin-top: 15px;
    }
    
    /* Revelación */
    .revelacion {
        background: linear-gradient(135deg, #c0392b 0%, #e74c3c 100%);
        padding: 40px;
        border-radius: 12px;
        margin-top: 40px;
        text-align: center;
        box-shadow: 0 15px 50px rgba(231, 76, 60, 0.3);
    }
    
    .revelacion-titulo {
        font-size: 36px;
        font-weight: 700;
        color: #ffffff;
        margin-bottom: 20px;
        text-transform: uppercase;
        letter-spacing: 2px;
    }
    
    .revelacion-texto {
        font-size: 18px;
        color: #ffffff;
        line-height: 1.6;
    }
    
    /* Intro */
    .intro-box {
        background-color: #151b3d;
        padding: 25px;
        border-radius: 10px;
        border: 1px solid #667eea;
        margin-bottom: 30px;
    }
    
    /* Pregunta counter */
    .pregunta-numero {
        color: #667eea;
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# Inicializar session state
if 'page' not in st.session_state:
    st.session_state.page = 'intro'
if 'respuestas' not in st.session_state:
    st.session_state.respuestas = {}
if 'pregunta_actual' not in st.session_state:
    st.session_state.pregunta_actual = 1

# Definición de preguntas
preguntas = {
    1: {
        "texto": "¿Cuál de estas situaciones te resulta más familiar?",
        "opciones": {
            "A": "Leo un titular impactante y lo comparto inmediatamente porque me parece importante",
            "B": "Veo noticias que confirman lo que ya pienso y me reconfortan",
            "C": "Me encuentro discutiendo en comentarios con personas que piensan diferente",
            "D": "Suelo scrollear sin prestar mucha atención a lo que leo"
        }
    },
    2: {
        "texto": "Cuando ves una noticia sorprendente en redes sociales, tu primera reacción es:",
        "opciones": {
            "A": "Compartirla para que otros se enteren",
            "B": "Buscar si otros medios también la publicaron",
            "C": "Revisar quién la publicó y cuándo",
            "D": "Asumir que probablemente es verdad si tiene muchos likes/shares"
        }
    },
    3: {
        "texto": "¿Qué temas te generan más interés? (Selecciona 2)",
        "tipo": "multiple",
        "opciones": {
            "A": "Salud y bienestar",
            "B": "Tecnología e innovación",
            "C": "Política y sociedad",
            "D": "Medio ambiente y clima",
            "E": "Economía y finanzas",
            "F": "Entretenimiento y cultura pop",
            "G": "Deportes"
        }
    },
    4: {
        "texto": "¿Con cuál de estas afirmaciones te identificas más?",
        "opciones": {
            "A": "Las grandes empresas/gobiernos ocultan información importante al público",
            "B": "La tecnología está mejorando el mundo más rápido de lo que pensamos",
            "C": "Los medios tradicionales ya no son confiables",
            "D": "La mayoría de problemas sociales tienen soluciones simples que nadie aplica"
        }
    },
    5: {
        "texto": "¿Cuándo fue la última vez que cambiaste de opinión sobre un tema importante después de leer algo en internet?",
        "opciones": {
            "A": "Hace poco, suelo estar abierto/a a nuevas perspectivas",
            "B": "Hace mucho, ya tengo mis posturas bastante definidas",
            "C": "Rara vez, pero considero argumentos contrarios",
            "D": "Nunca, confío en mi criterio inicial"
        }
    },
    6: {
        "texto": "¿Qué tipo de titulares te hacen dar click con más frecuencia?",
        "opciones": {
            "A": "\"Estudio revela que...\" / \"Científicos descubren...\"",
            "B": "\"Lo que no te dicen sobre...\" / \"La verdad detrás de...\"",
            "C": "\"X famoso/político hace/dice...\"",
            "D": "\"Esto cambiará tu forma de ver...\""
        }
    },
    7: {
        "texto": "Al leer noticias, tú:",
        "opciones": {
            "A": "Prefieres fuentes que confirman lo que ya sospechaba",
            "B": "Busco perspectivas variadas, incluso opuestas",
            "C": "Confío en las primeras fuentes que encuentro",
            "D": "Me guío por lo que comparte gente que admiro"
        }
    },
    8: {
        "texto": "¿Cuál crees que es tu mayor fortaleza al consumir información digital?",
        "opciones": {
            "A": "Soy escéptico/a y cuestiono todo",
            "B": "Identifico rápidamente qué es relevante",
            "C": "Busco siempre múltiples fuentes",
            "D": "Confío en mi intuición para detectar mentiras"
        }
    },
    9: {
        "texto": "Si una noticia incluye datos estadísticos y gráficos, tú:",
        "opciones": {
            "A": "La considero automáticamente más confiable",
            "B": "Reviso la metodología y fuente de los datos",
            "C": "Los datos me resultan convincentes pero no los verifico",
            "D": "No me fijo mucho en los números"
        }
    },
    10: {
        "texto": "¿Qué red social/plataforma usas más para informarte?",
        "opciones": {
            "A": "Twitter/X",
            "B": "Instagram/TikTok",
            "C": "Facebook",
            "D": "YouTube",
            "E": "Medios tradicionales digitales (periódicos online)",
            "F": "Reddit/Foros especializados"
        }
    }
}

# Noticias falsas por categoría
noticias = {
    1: {
        "titulo": "Estudio de Harvard vincula microplásticos en agua embotellada con 43% de aumento en casos de fatiga crónica",
        "texto": "Investigadores del Departamento de Salud Pública de Harvard analizaron 2,340 muestras de agua embotellada de las 15 marcas más vendidas en Latinoamérica. Los resultados muestran que el 89% contenía partículas de polietileno en concentraciones superiores a 270 nanogramos/litro, nivel asociado con alteraciones mitocondriales. ""La correlación es alarmante"", declaró la Dra. Jennifer Morrison, autora principal. ""Participantes que consumieron más de 2 litros semanales mostraron 43% más probabilidad de reportar fatiga persistente en un seguimiento de 18 meses."" Las marcas San Luis, Cielo y Aquarius mostraron las concentraciones más altas.",
        "fuente": "Environmental Health Perspectives, 2025"
    },
    2: {
        "titulo": "GPT-5 alcanza coeficiente intelectual equivalente a 147 en pruebas Stanford-Binet, superando al 99.9% de humanos",
        "texto": "OpenAI reveló ayer en una presentación cerrada en San Francisco que su próximo modelo GPT-5, programado para marzo 2026, obtuvo puntuaciones consistentes de 147 puntos en baterías completas del test Stanford-Binet administradas por psicólogos independientes de la Universidad de Berkeley. ""Es el primer sistema de IA que no solo aprueba, sino que domina consistentemente evaluaciones de razonamiento abstracto, memoria de trabajo y procesamiento espacial"", explicó Sam Altman. El modelo resolvió correctamente el 96% de problemas de la sección de razonamiento fluido, donde humanos promedio alcanzan 62%. La empresa planea integrar GPT-5 en sistemas educativos piloto en Singapur y Finlandia para inicios de 2026.",
        "fuente": "OpenAI Press Release, San Francisco 2025"
    },
    3: {
        "titulo": "Investigación revela: 34 congresistas peruanos recibieron pagos de mineras ilegales entre 2022-2024",
        "texto": "Una filtración de documentos bancarios obtenida por el Consorcio Latinoamericano de Periodismo Investigativo (CLPI) expone una red de pagos irregulares desde empresas mineras no autorizadas hacia cuentas personales y empresas offshore de 34 legisladores del actual Congreso. Los montos oscilan entre USD $12,000 y USD $340,000, según análisis forense de transacciones realizadas entre enero 2022 y octubre 2024. Destacan 7 congresistas de bancadas oficialistas y 4 de oposición. ""Los patrones son claros: pagos antes de votaciones clave sobre regulación minera"", señala el informe. La Fiscalía Supranacional recibió el dosier completo esta mañana.",
        "fuente": "Consorcio Latinoamericano de Periodismo Investigativo, 2025"
    },
    4: {
        "titulo": "Imágenes satelitales de NASA confirman: Amazonía peruana perdió área equivalente a 4 veces Lima en últimos 8 meses",
        "texto": "Análisis de imágenes del satélite Terra-MODIS revelan que entre marzo y octubre 2025, la deforestación en la Amazonía peruana alcanzó 13,200 km² - un área 4.2 veces mayor a Lima Metropolitana y 312% superior al mismo período de 2024. ""Es la tasa más acelerada registrada desde que iniciamos mediciones en 1999"", declaró la Dra. Patricia Sánchez del Earth Observatory de NASA. Los focos principales se concentran en Ucayali (38%), Madre de Dios (27%) y Loreto (19%). El informe, que será presentado en COP30 en Brasil, señala que al ritmo actual, el punto de no retorno de la selva tropical podría alcanzarse en 2031.",
        "fuente": "NASA Earth Observatory, 2025"
    },
    5: {
        "titulo": "FMI proyecta en informe filtrado: Dólar perderá 34% de su valor real contra oro para 2027",
        "texto": "Un documento interno del Fondo Monetario Internacional, obtenido por Financial Times, advierte que la acumulación de deuda estadounidense (actualmente USD $34.7 billones) provocará una devaluación estructural del dólar de entre 31-37% respecto al oro en los próximos 18 meses. ""Los modelos macroeconómicos son inequívocos"", señala el memo dirigido a bancos centrales del G20. China, Rusia e India ya habrían comenzado conversiones masivas a oro, según anexos del reporte. El precio del oro, actualmente en USD $2,045/oz, podría alcanzar USD $3,200/oz para diciembre 2026. JPMorgan y Goldman Sachs habrían recibido versiones preliminares en septiembre.",
        "fuente": "Financial Times (documento filtrado), 2025"
    },
    6: {
        "titulo": "Estudio de USC revela: 78% de influencers latinoamericanos usan IA para 'mejorar' su apariencia en contenido en vivo",
        "texto": "Investigadores del Annenberg Lab de la Universidad del Sur de California analizaron 5,400 transmisiones en vivo de los 200 influencers más seguidos de Latinoamérica, detectando el uso de filtros de IA imperceptibles en tiempo real en 78% de los casos. ""No hablamos de filtros obvios tipo Instagram. Son algoritmos de deepfake ligero que adelgazan, suavizan piel y modifican rasgos faciales sutilmente en video en vivo"", explicó el Dr. Marcus Chen, autor principal. Apps como BeautyLive AI y RealtimeGlow, usadas por creadores con más de 500K seguidores, procesan el video antes de transmitirlo. ""El espectador cree ver la realidad, pero es una versión algorítmicamente 'mejorada'"", añade el estudio.",
        "fuente": "USC Annenberg Lab, 2025"
    },
    7: {
        "titulo": "Filtración de FIFA expone: Algoritmo de VAR tiene margen de error del 23% en fueras de juego ajustados",
        "texto": "Documentos técnicos confidenciales de FIFA, revelados por Football Leaks, muestran que el sistema VAR semiautomático implementado desde Qatar 2022 presenta un margen de error de hasta 23% en jugadas de fuera de juego con menos de 8 centímetros de diferencia. El informe interno, elaborado por ingenieros de Hawk-Eye Innovations, reconoce que la sincronización de 12 cámaras genera desfases de hasta 0.07 segundos, suficiente para cambiar decisiones en velocidades de sprint superiores a 28 km/h. ""En partidos analizados de eliminatorias sudamericanas 2024, identificamos 34 decisiones potencialmente erróneas"", admite el documento. FIFA no ha comentado oficialmente la filtración.",
        "fuente": "Football Leaks / Hawk-Eye Innovations, 2025"
    },
    8: {
        "titulo": "McKinsey advierte: 42% de empleos en Latinoamérica serán automatizados antes de 2028",
        "texto": "Un reporte confidencial de McKinsey & Company, compartido con gobiernos de la región, proyecta que 67 millones de empleos en sectores administrativos, atención al cliente y logística serán reemplazados por sistemas de IA antes de finalizar 2028. Perú encabezaría la región con 47% de puestos en riesgo alto, seguido por Colombia (44%) y Chile (41%). ""Tareas repetitivas en banca, retail y call centers son particularmente vulnerables"", señala el análisis. El estudio, basado en data de 2,800 empresas, sugiere que modelos como GPT-5 y Claude 4 reducirán costos laborales hasta 73% en promedio. Gobiernos habrían solicitado que el informe permanezca reservado hasta 2026 para evitar alarma social.",
        "fuente": "McKinsey & Company (confidencial), 2025"
    },
    9: {
        "titulo": "Documentos desclasificados revelan: Proyecto 'Echo Chamber' de Meta manipuló elecciones en 11 países desde 2019",
        "texto": "Archivos internos de Meta obtenidos por The Intercept exponen la existencia de "'Echo Chamber'", un programa experimental que ajustaba algoritmos de Facebook e Instagram para amplificar contenido polarizante durante períodos electorales en 11 democracias, incluidas Perú (2021), Chile (2021) y Colombia (2022). ""El objetivo era aumentar engagement un 34% durante campañas, independientemente del impacto social"", revela un memo de 2019 firmado por ejecutivos de alto nivel. El sistema priorizaba automáticamente posts que generaban reacciones emocionales intensas. Whistleblowers declararon ante el Parlamento Europeo que el proyecto continúa activo bajo otro nombre. Meta negó las acusaciones pero no desmintió específicamente la existencia de "'Echo Chamber'".",
        "fuente": "The Intercept (whistleblower leak), 2025"
    },
    10: {
        "titulo": "Neurocientíficos de MIT descubren: Intuición humana acierta solo 34% del tiempo en entornos digitales",
        "texto": "Un estudio del MIT Media Lab que monitoreó durante 14 meses las decisiones de 4,200 participantes en entornos digitales reveló que la intuición - la sensación inmediata de si algo es verdadero o falso - tiene una precisión de apenas 34% en contextos online, comparado con 73% en interacciones presenciales. ""2El cerebro usa atajos evolutivos que funcionaban en entornos ancestrales pero fallan sistemáticamente ante información digital"", explicó el Dr. Robert Chen, neurocientífico principal del proyecto. Factores como diseño visual profesional, cifras estadísticas y lenguaje autoritativo pueden engañar incluso a personas que se consideran críticamente intuitivas. El estudio sugiere que confiar en corazonadas digitales sin verificación adicional es la principal vía de propagación de desinformación.",
        "fuente": "MIT Media Lab, 2025"
    },
    11: {
        "titulo": "Meta-análisis de Stanford confirma: Personas que verifican 'selectivamente' propagan 2.4x más desinformación",
        "texto": "Investigadores de Stanford analizaron el comportamiento de 18,000 usuarios durante 3 años y descubrieron una paradoja: quienes verifican información ocasionalmente (pero no consistentemente) propagan 2.4 veces más contenido falso que usuarios que nunca verifican o que siempre verifican. ""Es el efecto 'falsa confianza'"", explica la Dra. Sarah Mitchell, autora principal. ""Personas que verifican temas políticos pero no científicos, o viceversa, creen tener buen criterio y bajan la guardia en áreas donde no verifican. Esto las hace vectores ideales de desinformación mixta."" El estudio, publicado en Nature Human Behaviour, identificó que el 67% de este grupo comparte al menos una noticia falsa por semana, versus 41% del grupo nunca verifica y 8% del siempre verifica.",
        "fuente": "Nature Human Behaviour / Stanford, 2025"
    },
    12: {
        "titulo": "Estudio de Oxford revela: Usuarios 'minimalistas digitales' son 3x más vulnerables a noticias falsas",
        "texto": "Una investigación del Oxford Internet Institute que analizó patrones de 9,500 usuarios con bajo consumo digital (menos de 1 hora diaria en redes) encontró que este grupo es paradójicamente 3.1 veces más susceptible a creer noticias falsas cuando finalmente las encuentran. ""Al tener menos exposición, no desarrollan 'anticuerpos' contra desinformación"", explica el Prof. James Anderson. ""Cuando ven una noticia impactante, carecen del contexto y escepticismo que usuarios frecuentes adquieren por exposición repetida a contenido dudoso."" El estudio muestra que algoritmos pueden identificar estos perfiles y dirigirles contenido falso altamente persuasivo con 83% de tasa de éxito. ""Son blancos premium para campañas de manipulación precisas"", concluye el reporte.",
        "fuente": "Oxford Internet Institute, 2025"
    }
}

# Función para determinar categoría
def determinar_categoria(respuestas):
    # Lógica simplificada - ajustar según patrones más complejos
    p1 = respuestas.get(1, '')
    p2 = respuestas.get(2, '')
    p3 = respuestas.get(3, [])
    p4 = respuestas.get(4, '')
    p5 = respuestas.get(5, '')
    p6 = respuestas.get(6, '')
    p7 = respuestas.get(7, '')
    p8 = respuestas.get(8, '')
    p9 = respuestas.get(9, '')
    p10 = respuestas.get(10, '')
    
    # CATEGORÍA 1: Compartidor impulsivo saludable
    if 'A' in p3 and p1 == 'A' and p9 in ['A', 'C']:
        return 1
    
    # CATEGORÍA 2: Tecnoutópico crédulo
    if 'B' in p3 and p4 == 'B' and p9 == 'A':
        return 2
    
    # CATEGORÍA 3: Conspirador político
    if 'C' in p3 and p4 in ['A', 'C'] and p6 == 'B':
        return 3
    
    # CATEGORÍA 4: Ecologista confirmado
    if 'D' in p3 and p4 == 'A' and p6 == 'A':
        return 4
    
    # CATEGORÍA 5: Escéptico económico
    if 'E' in p3 and p4 == 'A' and p6 == 'B':
        return 5
    
    # CATEGORÍA 6: Fan crédulo de celebridades
    if 'F' in p3 and p6 == 'C' and p9 == 'A':
        return 6
    
    # CATEGORÍA 7: Deportista fanático
    if 'G' in p3 and p1 == 'A':
        return 7
    
    # CATEGORÍA 8: Tecnofóbico laboral
    if 'B' in p3 and p4 == 'D' and p8 == 'A':
        return 8
    
    # CATEGORÍA 9: Paranoico ilustrado
    if p4 == 'A' and p6 == 'B' and p8 == 'A':
        return 9
    
    # CATEGORÍA 10: Intuitivo confiado
    if p2 == 'D' and p8 == 'D' and p9 == 'A':
        return 10
    
    # CATEGORÍA 11: Verificador selectivo
    if p2 in ['B', 'C'] and p5 == 'C' and p7 == 'B':
        return 11
    
    # CATEGORÍA 12: Minimalista confiado
    if p1 == 'D' and p5 == 'A' and p10 == 'E':
        return 12
    
    # Default: asignar según tema principal de interés
    if 'A' in p3:
        return 1
    elif 'B' in p3:
        return 2
    elif 'C' in p3:
        return 3
    elif 'D' in p3:
        return 4
    elif 'E' in p3:
        return 5
    elif 'F' in p3:
        return 6
    elif 'G' in p3:
        return 7
    else:
        return 10  # Default general

# Función para generar análisis del perfil
def generar_analisis(respuestas, categoria):
    p1 = respuestas.get(1, '')
    p2 = respuestas.get(2, '')
    p3 = respuestas.get(3, [])
    p4 = respuestas.get(4, '')
    p5 = respuestas.get(5, '')
    p6 = respuestas.get(6, '')
    p7 = respuestas.get(7, '')
    p8 = respuestas.get(8, '')
    p9 = respuestas.get(9, '')
    
    analisis = {
        "comportamiento": "",
        "vulnerabilidades": [],
        "fortalezas": []
    }
    
    # Analizar comportamiento de compartir
    if p1 == 'A':
        analisis["comportamiento"] = "Tiendes a compartir información impactante rápidamente"
        analisis["vulnerabilidades"].append("Compartes antes de verificar")
    elif p1 == 'B':
        analisis["comportamiento"] = "Prefieres contenido que confirma tus creencias"
        analisis["vulnerabilidades"].append("Sesgo de confirmación activo")
    elif p1 == 'C':
        analisis["comportamiento"] = "Te involucras activamente en debates online"
        analisis["vulnerabilidades"].append("Polarización en discusiones")
    else:
        analisis["comportamiento"] = "Consumes contenido de manera pasiva"
        analisis["vulnerabilidades"].append("Baja atención crítica")
    
    # Analizar verificación
    if p2 in ['B', 'C']:
        analisis["fortalezas"].append("Intentas verificar información")
    else:
        analisis["vulnerabilidades"].append("No verificas fuentes regularmente")
    
    # Analizar datos/estadísticas
    if p9 == 'A':
        analisis["vulnerabilidades"].append("Confías automáticamente en datos numéricos")
    elif p9 == 'B':
        analisis["fortalezas"].append("Revisas metodología de estudios")
    
    # Analizar apertura mental
    if p5 == 'A':
        analisis["fortalezas"].append("Abierto/a a cambiar de opinión")
    elif p5 in ['B', 'D']:
        analisis["vulnerabilidades"].append("Resistencia a perspectivas diferentes")
    
    # Analizar autocrítica
    if p8 in ['A', 'C']:
        analisis["fortalezas"].append("Te consideras crítico/a con la información")
    
    return analisis

# PÁGINA DE INTRODUCCIÓN
if st.session_state.page == 'intro':
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>🔍 TU PERFIL DIGITAL</h1>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class='intro-box'>
    <p style='font-size: 16px; line-height: 1.8; text-align: center;'>
    Este breve cuestionario analiza cómo interactúas con información en el entorno digital.<br>
    <strong>No hay respuestas correctas o incorrectas.</strong><br>
    Responde con honestidad.
    </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("COMENZAR"):
            st.session_state.page = 'cuestionario'
            st.rerun()

# PÁGINA DE CUESTIONARIO
elif st.session_state.page == 'cuestionario':
    pregunta_num = st.session_state.pregunta_actual
    pregunta = preguntas[pregunta_num]
    
    # Barra de progreso
    progreso = (pregunta_num - 1) / len(preguntas)
    st.progress(progreso)
    
    st.markdown(f"<p class='pregunta-numero'>PREGUNTA {pregunta_num} DE {len(preguntas)}</p>", unsafe_allow_html=True)
    st.markdown(f"<h2>{pregunta['texto']}</h2>", unsafe_allow_html=True)
    
    # Pregunta múltiple (Pregunta 3)
    if pregunta.get('tipo') == 'multiple':
        st.markdown("<p style='color: #888; font-size: 14px;'>Selecciona exactamente 2 opciones</p>", unsafe_allow_html=True)
        
        seleccionadas = []
        for key, valor in pregunta['opciones'].items():
            if st.checkbox(valor, key=f"check_{pregunta_num}_{key}"):
                seleccionadas.append(key)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("SIGUIENTE", key=f"btn_{pregunta_num}"):
                if len(seleccionadas) == 2:
                    st.session_state.respuestas[pregunta_num] = seleccionadas
                    if pregunta_num < len(preguntas):
                        st.session_state.pregunta_actual += 1
                        st.rerun()
                    else:
                        st.session_state.page = 'procesando'
                        st.rerun()
                else:
                    st.error("Por favor selecciona exactamente 2 opciones")
    
    # Pregunta única
    else:
        respuesta = st.radio(
            "Selecciona una opción",
            options=list(pregunta['opciones'].keys()),
            format_func=lambda x: pregunta['opciones'][x],
            key=f"radio_{pregunta_num}",
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("SIGUIENTE", key=f"btn_{pregunta_num}"):
                st.session_state.respuestas[pregunta_num] = respuesta
                if pregunta_num < len(preguntas):
                    st.session_state.pregunta_actual += 1
                    st.rerun()
                else:
                    st.session_state.page = 'procesando'
                    st.rerun()

# PÁGINA DE PROCESANDO
elif st.session_state.page == 'procesando':
    import time
    
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>⚙️ ANALIZANDO TU PERFIL</h1>", unsafe_allow_html=True)
    
    # Contenedor para mensajes de procesamiento
    mensaje_placeholder = st.empty()
    barra_placeholder = st.empty()
    
    mensajes = [
        "🔍 Procesando respuestas...",
        "🧠 Analizando patrones de comportamiento...",
        "📊 Evaluando vulnerabilidades digitales...",
        "🎯 Identificando sesgos cognitivos...",
        "📰 Generando contenido personalizado...",
        "🖼️ Creando visualización de datos...",
        "✅ Finalizando análisis..."
    ]
    
    progreso_total = len(mensajes)
    
    for i, mensaje in enumerate(mensajes):
        mensaje_placeholder.markdown(f"""
        <div style='background-color: #151b3d; padding: 25px; border-radius: 10px; text-align: center; margin: 50px auto; max-width: 600px; border: 1px solid #667eea;'>
            <p style='font-size: 20px; color: #ffffff; margin: 0;'>{mensaje}</p>
        </div>
        """, unsafe_allow_html=True)
        
        barra_placeholder.progress((i + 1) / progreso_total)
        time.sleep(0.8)  # Pausa de 0.8 segundos entre mensajes
    
    # Mensaje final
    mensaje_placeholder.markdown("""
    <div style='background-color: #151b3d; padding: 25px; border-radius: 10px; text-align: center; margin: 50px auto; max-width: 600px; border: 1px solid #2ecc71;'>
        <p style='font-size: 20px; color: #2ecc71; margin: 0;'>✨ Análisis completado</p>
    </div>
    """, unsafe_allow_html=True)
    
    time.sleep(1)
    
    # Avanzar a resultado
    st.session_state.page = 'resultado'
    st.rerun()
    
# PÁGINA DE RESULTADO (NOTICIA FALSA)
elif st.session_state.page == 'resultado':
    categoria = determinar_categoria(st.session_state.respuestas)
    noticia = noticias[categoria]
    
    st.markdown("<h1 style='text-align: center; margin-top: 30px;'>ANÁLISIS COMPLETADO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #888; font-size: 16px; margin-bottom: 40px;'>Basado en tus respuestas, esto es lo que encontramos relevante para ti:</p>", unsafe_allow_html=True)
    
    # Mostrar imagen
    try:
        st.image(f"CATEGORIA{categoria}.jpeg", width='stretch')
    except:
        st.warning(f"Imagen CATEGORIA{categoria}.jpeg no encontrada")
    
    # Mostrar noticia
    st.markdown(f"""
    <div class='noticia-container'>
        <div class='noticia-titulo'>{noticia['titulo']}</div>
        <div class='noticia-texto'>{noticia['texto']}</div>
        <div class='noticia-fuente'>Fuente: {noticia['fuente']}</div>
    </div>
    """, unsafe_allow_html=True)
    
    # NUEVO: Botones de interacción
    col1, col2, col3 = st.columns([1, 1, 1])
    
    with col1:
        if st.button("👍 ME GUSTA", key="btn_like"):
            st.success("Te gustó esta noticia")
    
    with col2:
        if st.button("📤 COMPARTIR", key="btn_compartir"):
            st.session_state.compartio = True
            st.session_state.page = 'revelacion'
            st.rerun()
    
    with col3:
        if st.button("💬 COMENTAR", key="btn_comentar"):
            st.info("¿Qué piensas sobre esto?")
    
    st.markdown("<br>", unsafe_allow_html=True)

# PÁGINA DE REVELACIÓN
elif st.session_state.page == 'revelacion':
    categoria = determinar_categoria(st.session_state.respuestas)
    analisis = generar_analisis(st.session_state.respuestas, categoria)
    
    # Mensaje personalizado si compartió
    mensaje_compartir = ""
    if st.session_state.get('compartio', False):
        mensaje_compartir = "<p style='font-size: 22px; color: #fff; margin-top: 20px;'><strong>📤 Incluso COMPARTISTE esta noticia falsa.</strong><br>Así es exactamente como se propaga la desinformación.</p>"
    
    st.markdown("""
    <div class='revelacion'>
        <div class='revelacion-titulo'>⚠️ ESTA NOTICIA ES COMPLETAMENTE FALSA ⚠️</div>
        <div class='revelacion-texto'>
            <p><strong>Fue generada específicamente para ti</strong> basándose en tus respuestas al cuestionario.</p>
            <p>Los datos, estudios, instituciones y expertos mencionados <strong>NO EXISTEN</strong>.</p>
            <p>Esta es una demostración de cómo la información personalizada puede manipular nuestras creencias al confirmar nuestros sesgos y presentar datos que parecen legítimos.</p>
            <p style='margin-top: 30px; font-size: 20px;'><strong>¿Te pareció creíble? No estás solo/a.</strong></p>
            <p>Así es como funciona la desinformación en la era digital:</p>
            <ul style='text-align: left; display: inline-block; margin-top: 20px;'>
                <li>✓ Datos numéricos específicos (generan credibilidad)</li>
                <li>✓ Fuentes aparentemente legítimas (universidades, instituciones)</li>
                <li>✓ Temas que te interesan (captan tu atención)</li>
                <li>✓ Confirma lo que ya sospechabas (baja tu guardia crítica)</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

# Análisis personalizado del perfil
    st.markdown("""
    <div style='background-color: #1a1f3a; padding: 30px; border-radius: 10px; margin-top: 30px; border-left: 4px solid #667eea;'>
        <h2 style='text-align: center; color: #667eea; margin-bottom: 25px;'>📊 TU ANÁLISIS PERSONALIZADO</h2>
    </div>
    """, unsafe_allow_html=True)
    
    # Patrón de comportamiento
    st.markdown(f"""
    <div style='background-color: #1a1f3a; padding: 20px; margin-left: 30px; margin-right: 30px;'>
        <h3 style='color: #ffffff; font-size: 18px; margin-bottom: 10px;'>🎯 Patrón de Comportamiento:</h3>
        <p style='color: #d0d0d0; font-size: 16px; margin-left: 20px; line-height: 1.6;'>{analisis['comportamiento']}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Vulnerabilidades
    st.markdown("""
    <div style='background-color: #1a1f3a; padding: 20px; margin-left: 30px; margin-right: 30px;'>
        <h3 style='color: #e74c3c; font-size: 18px; margin-bottom: 10px;'>⚠️ Vulnerabilidades Detectadas:</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for v in analisis['vulnerabilidades']:
        st.markdown(f"<p style='color: #d0d0d0; font-size: 15px; margin-left: 70px;'>• {v}</p>", unsafe_allow_html=True)
    
    # Fortalezas
    if analisis['fortalezas']:
        st.markdown("""
        <div style='background-color: #1a1f3a; padding: 20px; margin-left: 30px; margin-right: 30px; margin-top: 20px;'>
            <h3 style='color: #2ecc71; font-size: 18px; margin-bottom: 10px;'>✅ Fortalezas Identificadas:</h3>
        </div>
        """, unsafe_allow_html=True)
        
        for f in analisis['fortalezas']:
            st.markdown(f"<p style='color: #d0d0d0; font-size: 15px; margin-left: 70px;'>• {f}</p>", unsafe_allow_html=True)
    
    # Mensaje final de compartir
    st.markdown("""
    <div style='background-color: #2d3561; padding: 20px; border-radius: 8px; margin: 30px; margin-top: 25px;'>
        <p style='color: #ffffff; font-size: 16px; text-align: center; margin: 0;'>
            <strong>📤 ACABAS DE COMPARTIR UNA NOTICIA FALSA</strong><br>
            <span style='color: #d0d0d0; font-size: 14px;'>Así es exactamente como se propaga la desinformación en redes sociales.</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div style='background-color: #151b3d; padding: 30px; border-radius: 10px; margin-top: 30px;'>
        <h2 style='text-align: center; color: #667eea;'>Reflexión Final</h2>
        <p style='font-size: 16px; line-height: 1.8; text-align: center;'>
        Este proyecto demuestra cómo los algoritmos y la información personalizada pueden manipularnos sin que nos demos cuenta.<br><br>
        <strong>La próxima vez que veas una noticia impactante:</strong><br>
        ❓ ¿Quién la publica?<br>
        ❓ ¿Qué fuentes cita?<br>
        ❓ ¿Por qué me la están mostrando justamente a mí?<br>
        ❓ ¿Confirma algo que ya creía?<br><br>
        <em>La mejor defensa contra la desinformación es el pensamiento crítico.</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("REINICIAR CUESTIONARIO", key="btn_reiniciar"):
            st.session_state.page = 'intro'
            st.session_state.respuestas = {}
            st.session_state.pregunta_actual = 1
            st.rerun()

