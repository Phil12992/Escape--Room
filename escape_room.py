import streamlit as st

st.set_page_config(page_title="🌺 Ägyptischer Escape Room", page_icon="🛡️")

st.title(":classical_building: Ägyptischer Escape Room")
st.markdown("""
Du bist in einer alten Pyramide gefangen. Um zu entkommen, musst du in jedem Raum drei Rätsel lösen.  
Gib bei jeder Frage eine Antwort ein. Die richtigen Antworten ergeben zusammen einen 3-stelligen Code,  
den du am Ende des Raums eingeben musst, um die Tür zu öffnen und in den nächsten Raum zu gelangen.
""")

# Hilfsfunktion: Bild anzeigen (aus dem Ordner "bilder")
def zeige_bild(pfad, alt_text="Bild"):
    st.image(pfad, caption=alt_text)

# Räume und ihre Fragen + Antwort-Schlüssel (Schlüsselwörter und jeweilige Ziffer)
raeume = {
    1: {
        "name": "🏛️ Raum 1 – Halle der Prüfungen",
        "fragen": [
            "Wie heißt der Sonnengott im alten Ägypten?",
            "Wie viele Pyramiden stehen in Gizeh?",
            "Wie heißt das altägyptische Buch der Toten?"
        ],
        "antworten": {
            "sonnengott": "3",  # z.B. "Ra" oder "Re" -> "sonnengott"
            "3": "3",  # wenn jemand "ra" schreibt
            "pyramiden": "7",   # 3 große Pyramiden + 4 kleine
            "gizeh": "7",
            "sieben": "7",
            "buch der toten": "9",
            "totenbuch": "9",
            "buch": "9"
        },
        "code": "379",
        "bild": "bilder/pyramide.jpg"
    },
    2: {
        "name": "🏺 Raum 2 – Grabkammer der Schatten",
        "fragen": [
            "Welches Tier steht im alten Ägypten für Wiedergeburt?",
            "Woraus wurden die meisten Schriftrollen hergestellt?",
            "Welches Auge symbolisierte Schutz?"
        ],
        "antworten": {
            "skarabäus": "5",
            "papyrus": "3",
            "hieroglyphe": "2",
            "horus": "8",
            "auge des horus": "8",
            "auge": "8"
        },
        "code": "538",
        "bild": "bilder/grabkammer.jpg"
    },
    3: {
        "name": "🪞 Raum 3 – Die Halle der Spiegel",
        "fragen": [
            "Was wird im Totengericht mit dem Herzen verglichen?",
            "Wer ist der Gott der Weisheit?",
            "Wie öffnete man im alten Ägypten Grabkammern?"
        ],
        "antworten": {
            "feder": "4",
            "herz": "4",
            "thot": "3",
            "weisheit": "3",
            "siegelbruch": "8",
            "siegel": "8",
            "opfergabe": "9"
        },
        "code": "438",
        "bild": "bilder/spiegelhalle.jpg"
    },
    4: {
        "name": "🌪 Raum 4 – Kammer der Elemente",
        "fragen": [
            "Welches Element symbolisiert Macht?",
            "Womit segelten die alten Ägypter auf dem Nil?",
            "Welcher Fluss war der wichtigste in Ägypten?"
        ],
        "antworten": {
            "feuer": "6",
            "wind": "3",
            "nil": "4",
            "wasser": "2",
            "boot": "3",
            "segel": "3"
        },
        "code": "634",
        "bild": "bilder/elemente.jpg"
    },
    5: {
        "name": "🌌 Raum 5 – Halle der Sterne",
        "fragen": [
            "Welches Sternbild war im alten Ägypten heilig?",
            "Wozu dienten Sternkarten?",
            "Wer war die ägyptische Himmelsgöttin?"
        ],
        "antworten": {
            "orion": "3",
            "navigation": "2",
            "nut": "5",
            "stern": "2",
            "planung": "4",
            "maat": "8",
            "himmlisch": "5"
        },
        "code": "325",
        "bild": "bilder/sterne.jpg"
    }
}

# Session-State zur Raumsteuerung
if "aktueller_raum" not in st.session_state:
    st.session_state.aktueller_raum = 1

aktueller_raum = st.session_state.aktueller_raum

# Funktion zum Prüfen der Antworten und Bildung des Codes
def berechne_code(eingaben, antworten):
    code = ""
    for eingabe in eingaben:
        ziffer = "0"  # Default für falsche Antwort
        for schluesselwort, zahl in antworten.items():
            if schluesselwort in eingabe.lower():
                ziffer = zahl
                break
        code += ziffer
    return code

def spielraum(raum_nr):
    raum = raeume[raum_nr]
    st.header(raum["name"])

    # Bild anzeigen, falls vorhanden
    try:
        zeige_bild(raum["bild"], alt_text=raum["name"])
    except Exception:
        pass  # Bild kann fehlen

    eingaben = []
    for i, frage in enumerate(raum["fragen"]):
        eingabe = st.text_input(frage, key=f"raum{raum_nr}_frage{i}")
        eingaben.append(eingabe.strip())

    code_berechnet = berechne_code(eingaben, raum["antworten"])

    code_eingabe = st.text_input("Gib hier den 3-stelligen Türcode ein:", key=f"raum{raum_nr}_codeeingabe")

    if st.button("Code prüfen", key=f"raum{raum_nr}_button"):
        if code_eingabe == raum["code"]:
            st.success("✅ Die Tür öffnet sich! Du kannst weitergehen.")
            st.session_state.aktueller_raum += 1
        else:
            st.error(f"❌ Falscher Code. Dein Code basierend auf deinen Antworten ist: {code_berechnet}")
            st.info("Überprüfe deine Antworten und versuche es erneut.")

# Hauptspielablauf
if aktueller_raum <= len(raeume):
    spielraum(aktueller_raum)
else:
    st.balloons()
    st.success("🎉 Herzlichen Glückwunsch! Du hast den ägyptischen Escape Room erfolgreich gemeistert!")

