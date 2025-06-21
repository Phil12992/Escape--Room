import streamlit as st

st.set_page_config(page_title="🛡️ Ägyptischer Escape Room", page_icon="🏺")

st.title("🛡️ Ägyptischer Escape Room – Gefangen in der Pyramide")

st.markdown("""
Du bist in einer alten ägyptischen Pyramide gefangen.  
In jedem der 5 Räume erwarten dich 3 knifflige Rätsel.  
Gib für jedes Rätsel eine Zahl ein.  
Die korrekten Zahlen ergeben am Ende den 3-stelligen Türcode, um den Raum zu verlassen.  
Pass auf: Nur wenn der Code stimmt, öffnet sich die Tür zum nächsten Raum!
""")

# =============================
# Räume und Rätsel-Daten
# =============================
raeume = {
    1: {
        "name": "Halle der Prüfungen",
        "raetsel": [
            {
                "frage": "Wie viele Seiten hat eine klassische Pyramide?",
                "antwort": 4
            },
            {
                "frage": "Wie viele Jahre dauerte ungefähr der Bau der großen Pyramide von Gizeh?",
                "antwort": 20
            },
            {
                "frage": "Wie viele Hauptgötter gab es im alten Ägypten (ungefähr)?",
                "antwort": 3
            },
        ],
        "code": "423",
    },
    2: {
        "name": "Grabkammer der Schatten",
        "raetsel": [
            {
                "frage": "Wieviele Hieroglyphen enthält das ägyptische Alphabet ungefähr?",
                "antwort": 24
            },
            {
                "frage": "Wie viele Jahre lebte Ramses II. (ungefähr)?",
                "antwort": 90
            },
            {
                "frage": "Wie viele Finger hat eine menschliche Hand?",
                "antwort": 5
            },
        ],
        "code": "245",
    },
    3: {
        "name": "Halle der Spiegel",
        "raetsel": [
            {
                "frage": "Wie viele Monate hatte der ägyptische Kalender?",
                "antwort": 12
            },
            {
                "frage": "Wie viele Tage hat das ägyptische Jahr?",
                "antwort": 365
            },
            {
                "frage": "Wie viele Flüsse gibt es, die in Ägypten wichtig sind?",
                "antwort": 1
            },
        ],
        "code": "121",
    },
    4: {
        "name": "Kammer der Elemente",
        "raetsel": [
            {
                "frage": "Wie viele Hauptfarben hatte die altägyptische Malerei?",
                "antwort": 5
            },
            {
                "frage": "Wie viele Elemente sind in der ägyptischen Mythologie besonders wichtig?",
                "antwort": 4
            },
            {
                "frage": "Wie viele Sinne hat der Mensch (klassisch)?",
                "antwort": 5
            },
        ],
        "code": "454",
    },
    5: {
        "name": "Halle der Sterne",
        "raetsel": [
            {
                "frage": "Wie viele Sternbilder waren im alten Ägypten besonders wichtig?",
                "antwort": 3
            },
            {
                "frage": "Wie viele Planeten waren den Ägyptern bekannt?",
                "antwort": 5
            },
            {
                "frage": "Wie viele Buchstaben hat das altägyptische Alphabet?",
                "antwort": 24
            },
        ],
        "code": "354",
    }
}

# =============================
# Session-State Setup
# =============================
if "aktueller_raum" not in st.session_state:
    st.session_state.aktueller_raum = 1

if "reset_inputs" not in st.session_state:
    st.session_state.reset_inputs = False

raum_nr = st.session_state.aktueller_raum
raum = raeume[raum_nr]

# Reset Inputs, wenn Flag gesetzt
if st.session_state.reset_inputs:
    for i in range(3):
        key = f"raum{raum_nr}_frage{i}"
        if key in st.session_state:
            del st.session_state[key]
    code_key = f"raum{raum_nr}_codeeingabe"
    if code_key in st.session_state:
        del st.session_state[code_key]
    st.session_state.reset_inputs = False

st.header(f"🏛️ Raum {raum_nr}: {raum['name']}")

eingaben = []
korrekt = True
for i, raetsel in enumerate(raum["raetsel"]):
    eingabe = st.text_input(f"Rätsel {i+1}: {raetsel['frage']}", key=f"raum{raum_nr}_frage{i}")
    eingaben.append(eingabe)

code_eingabe = st.text_input("🔐 Gib den 3-stelligen Türcode ein:", key=f"raum{raum_nr}_codeeingabe")

# Hilfsfunktion: Prüfe ob alle Antworten korrekt sind und generiere den Code aus richtigen Antworten
def pruefe_antworten(eingaben, raetsel_liste):
    zahlen = []
    for i, antwort in enumerate(raetsel_liste):
        try:
            zahl = int(eingaben[i])
            if zahl != antwort["antwort"]:
                return False, None  # Mindestens eine Antwort falsch
            zahlen.append(str(zahl))
        except:
            return False, None  # Eingabe nicht convertierbar
    return True, "".join([str(r["antwort"]) for r in raetsel_liste])

if st.button("🔓 Tür prüfen"):

    alle_richtig, code_erwartet = pruefe_antworten(eingaben, raum["raetsel"])

    if not alle_richtig:
        st.error("❌ Mindestens eine Antwort ist falsch oder leer. Versuche es nochmal!")
        korrekt = False
    else:
        if code_eingabe == code_erwartet:
            st.success("🎉 Tür öffnet sich! Du darfst in den nächsten Raum.")
            if raum_nr < len(raeume):
                st.session_state.aktueller_raum += 1
                st.session_state.reset_inputs = True
                st.experimental_rerun()
            else:
                st.balloons()
                st.success("🏆 Du hast alle Räume erfolgreich gemeistert! Glückwunsch!")
        else:
            st.error(f"❌ Der Code ist falsch. Überprüfe die Zahlen der richtigen Antworten. Erwarteter Code hat 3 Ziffern.")




