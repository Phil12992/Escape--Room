# escape_room.py

import streamlit as st

st.title("🔐 Escape Room: Das virtuelle Abenteuer")

# Zustand speichern
if "level" not in st.session_state:
    st.session_state.level = 1

# Level 1
if st.session_state.level == 1:
    st.subheader("Level 1: Die verschlossene Tür")
    code = st.text_input("Gib den 3-stelligen Code ein, um die Tür zu öffnen:")
    if code == "735":
        st.success("Richtig! Du hast die Tür geöffnet.")
        st.session_state.level = 2
    elif code:
        st.error("Falsch! Versuche es nochmal.")

# Level 2
if st.session_state.level == 2:
    st.subheader("Level 2: Das Zahlenrätsel")
    st.write("Welche Zahl kommt als nächstes in der Reihe: 2, 4, 8, 16, ?")
    answer = st.text_input("Deine Antwort:")
    if answer == "32":
        st.success("Perfekt! Du hast das Rätsel gelöst.")
        st.session_state.level = 3
    elif answer:
        st.error("Leider falsch.")

# Level 3
if st.session_state.level == 3:
    st.subheader("Level 3: Das finale Rätsel")
    riddle = st.text_input("Ich habe Städte, aber keine Häuser. Ich habe Berge, aber keine Bäume. Ich habe Wasser, aber keine Fische. Was bin ich?")
    if riddle.lower() == "karte":
        st.success("Du hast das Escape Room-Spiel geschafft! 🎉")
        st.balloons()
        st.session_state.level = 4
    elif riddle:
        st.error("Das ist nicht die richtige Antwort.")
