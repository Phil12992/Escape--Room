import streamlit as st

st.set_page_config(page_title="Ägyptischer Escape Room", page_icon="🛡️")
st.title("🏺 Ägyptischer Escape Room")

raeume = {
    1: {
        "name": "Raum 1 – Die Halle der Prüfungen",
        "fragen": [
            "Wie heißt der Sonnengott im alten Ägypten?",
            "Wie viele große Pyramiden gibt es in Gizeh?",
            "Wie heißt das altägyptische Buch der Toten?"
        ],
        "antworten": [
            {"ra", "re", "sonnengott"},   # für erste Frage
            {"3", "drei"},                # zweite Frage
            {"totenbuch", "buch der toten"} # dritte Frage
        ],
        "code": "379"
    },
    2: {
        "name": "Raum 2 – Grabkammer der Schatten",
        "fragen": [
            "Welches Tier steht im alten Ägypten für Wiedergeburt?",
            "Woraus wurden die meisten Schriftrollen hergestellt?",
            "Welches Auge symbolisierte Schutz?"
        ],
        "antworten": [
            {"skarabäus"},
            {"papyrus"},
            {"horus", "auge des horus"}
        ],
        "code": "538"
    },
    3: {
        "name": "Raum 3 – Die Halle der Spiegel",
        "fragen": [
            "Was wird im Totengericht mit dem Herzen verglichen?",
            "Wer ist der Gott der Weisheit?",
            "Wie öffnete man im alten Ägypten Grabkammern?"
        ],
        "antworten": [
            {"feder"},
            {"thot"},
            {"siegelbruch", "opfergabe"}
        ],
        "code": "439"
    }
}

if "aktueller_raum" not in st.session_state:
    st.session_state.aktueller_raum = 1

raum_nr = st.session_state.aktueller_raum

st.header(raeume[raum_nr]["name"])

antworten_user = []

for i, frage in enumerate(raeume[raum_nr]["fragen"]):
    antwort = st.text_input(f"Frage {i+1}: {frage}", key=f"raum{raum_nr}_frage{i}")
    antworten_user.append(antwort.strip().lower())

def pruefe_antworten(user_antworten, richtige_antworten):
    code = ""
    for ua, ra in zip(user_antworten, richtige_antworten):
        if any(schluesselwort in ua for schluesselwort in ra):
            # Wenn richtig, eine Ziffer aus der Reihenfolge 3,7,9,5,3,8... nehmen (nur Beispiel)
            # Hier einfach 3,7,9 für Raum 1, 5,3,8 für Raum 2 etc. (hart kodiert)
            pass
        else:
            return None  # mindestens eine Antwort falsch
    # Wenn alle richtig, Code aus raum info zurückgeben
    return raeume[raum_nr]["code"]

code_versuch = st.text_input("Gib den 3-stelligen Türcode ein:", key=f"raum{raum_nr}_codeeingabe")

if st.button("Tür öffnen"):
    code_errechnet = pruefe_antworten(antworten_user, raeume[raum_nr]["antworten"])
    if code_errechnet is None:
        st.error("Mindestens eine Antwort ist falsch. Überprüfe deine Eingaben.")
    else:
        if code_versuch == code_errechnet:
            st.success("✅ Die Tür öffnet sich! Weiter zum nächsten Raum.")
            st.session_state.aktueller_raum += 1
            st.experimental_rerun()
        else:
            st.error("❌ Falscher Code. Versuch es noch einmal.")

if st.session_state.aktueller_raum > len(raeume):
    st.balloons()
    st.success("🎉 Glückwunsch! Du hast alle Räume des ägyptischen Escape Rooms erfolgreich gelöst!")


