import streamlit as st
from PIL import Image

st.set_page_config(page_title="🧩 Ägyptischer Escape Room", page_icon="🏺")

st.title("🏺 Ägyptischer Escape Room – Gefangen in der Pyramide")

st.markdown("""
Du bist in einer uralten ägyptischen Pyramide gefangen.  
Jeder Raum ist mit drei Prüfungen versehen – beantworte sie korrekt.  
Jede richtige Antwort ergibt eine **Ziffer**.  
Setze die drei Ziffern zu einem **Türcode** zusammen, um weiterzukommen.

⚠️ Du erfährst nicht sofort, ob deine Antworten richtig sind.  
Nur der Türcode verrät dir, ob du bereit bist, weiterzugehen!
""")

# Hilfsfunktion zum Anzeigen eines Bildes (optional)
def zeige_bild(pfad, beschreibung=""):
    try:
        img = Image.open(pfad)
        st.image(img, caption=beschreibung, use_column_width=True)
    except:
        pass  # Ignoriere Fehler, wenn Bild fehlt

# Hilfsfunktion für einen Raum mit 3 Fragen
def raum(nr, titel, fragen, antworten, code, sichtbar):
    if sichtbar:
        st.header(f"🏛️ Raum {nr} – {titel}")
        user_loesungen = []
        for i, frage in enumerate(fragen):
            user_input = st.text_input(frage, key=f"raum{nr}_frage{i+1}")
            user_loesungen.append(user_input.strip().lower())

        nutzer_code = st.text_input(f"🔐 Türcode für Raum {nr} eingeben:", max_chars=10, key=f"code_raum{nr}")
        if st.button(f"✅ Code prüfen für Raum {nr}", key=f"button_raum{nr}"):
            if nutzer_code == code:
                st.success(f"✅ Der Steinmechanismus rumort... Die Tür zu Raum {nr + 1} öffnet sich!")
                st.session_state[f"raum{nr+1}_offen"] = True
            else:
                st.error("❌ Der Mechanismus verweigert den Dienst. Versuche es erneut.")

# Initialisiere Sitzungsstatus
if "raum2_offen" not in st.session_state:
    for i in range(2, 7):
        st.session_state[f"raum{i}_offen"] = False

# Raum 1
raum(
    1,
    "Grabkammer des Anubis",
    [
        "Frage 1: Wie hieß der Sonnengott im alten Ägypten?",
        "Frage 2: Wie viele Pyramiden stehen in Gizeh?",
        "Frage 3: Wie nennt man das altägyptische Buch der Toten?"
    ],
    None,
    code="379",
    sichtbar=True
)

# Raum 2
raum(
    2,
    "Kammer des Skarabäus",
    [
        "Frage 1: Welches Tier steht in Ägypten für Wiedergeburt?",
        "Frage 2: Wie viele Teile hatte die Seele im ägyptischen Glauben?",
        "Frage 3: Welches Gestein nutzten die Ägypter für Statuen (z. B. Ramses)?"
    ],
    None,
    code="521",
    sichtbar=st.session_state["raum2_offen"]
)

# Raum 3
raum(
    3,
    "Halle der Prüfungen",
    [
        "Frage 1: Womit wurde der Eingang zu Gräbern versiegelt?",
        "Frage 2: Wie viele Götter saßen über das Herz der Toten zu Gericht?",
        "Frage 3: Wie nennt man das Auge, das Schutz spendet?"
    ],
    None,
    code="846",
    sichtbar=st.session_state["raum3_offen"]
)

# Raum 4
raum(
    4,
    "Kammer der Elemente",
    [
        "Frage 1: Welches Element galt als zerstörerisch und reinigend zugleich?",
        "Frage 2: Welcher Fluss war für das Leben der Ägypter zentral?",
        "Frage 3: Was symbolisierte das Ank-Zeichen?"
    ],
    None,
    code="674",
    sichtbar=st.session_state["raum4_offen"]
)

# Raum 5
raum(
    5,
    "Halle der Sterne",
    [
        "Frage 1: Welcher Stern oder welches Sternbild galt als besonders heilig?",
        "Frage 2: Welche Göttin war mit dem Nachthimmel verbunden?",
        "Frage 3: Was diente den Ägyptern zur Zeitmessung nachts?"
    ],
    None,
    code="382",
    sichtbar=st.session_state["raum5_offen"]
)

# Raum 6 (Finale)
if st.session_state["raum6_offen"]:
    st.success("🏆 Du hast alle Räume der Pyramide durchquert. Du trittst hinaus ins Licht der Wüste. Herzlichen Glückwunsch!")
    st.balloons()


