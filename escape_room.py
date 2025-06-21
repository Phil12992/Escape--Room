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
        "codes": ["3", "7", "9"]  # richtige Ziffern pro Frage
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
        "codes": ["5", "3", "8"]
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
        "codes": ["4", "3", "9"]
    }
}

if "aktueller_raum" not in st.session_state:
    st.session_state.aktueller_raum = 1

raum_nr = st.session_state.aktueller_raum

st.header(raeume[raum_nr]["name"])

antworten_user = []
richtig_zahlen = []

for i, frage in enumerate(raeume[raum_nr]["fragen"]):
    antwort = st.text_input(f"Frage {i+1}: {frage}", key=f"raum{raum_nr}_frage{i}")
    antworten_user.append(antwort.strip().lower())

# Prüfe Antworten und baue Code
alle_richtig = True
for ua, ra in zip(antworten_user, raeume[raum_nr]["antworten"]):
    if any(schluesselwort in ua for schluesselwort in ra):
        # richtige Antwort
        pass
    else:
        alle_richtig = False

if alle_richtig and all(antworten_user):
    code_anzeige = "".join(raeume[raum_nr]["codes"])
    st.success(f"Dein zusammengesetzter Türcode lautet: **{code_anzeige}**")
else:
    if any(antworten_user):
        st.info("Die Antworten sind noch nicht alle korrekt oder vollständig.")

code_versuch = st.text_input("Gib den 3-stelligen Türcode ein:", key=f"raum{raum_nr}_codeeingabe")

if st.button("Tür öffnen"):
    if not all(antworten_user):
        st.error("Bitte beantworte alle Fragen, bevor du den Code eingibst.")
    else:
        if alle_richtig:
            if code_versuch == "".join(raeume[raum_nr]["codes"]):
                st.success("✅ Die Tür öffnet sich! Weiter zum nächsten Raum.")
                st.session_state.aktueller_raum += 1
                st.experimental_rerun()
            else:
                st.error("❌ Falscher Code. Versuch es noch einmal.")
        else:
            st.error("Mindestens eine Antwort ist falsch. Überprüfe deine Eingaben.")

if st.session_state.aktueller_raum > len(raeume):
    st.balloons()
    st.success("🎉 Glückwunsch! Du hast alle Räume des ägyptischen Escape Rooms erfolgreich gelöst!")



