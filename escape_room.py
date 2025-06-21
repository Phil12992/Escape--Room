# escape_room.py

import streamlit as st

st.set_page_config(page_title="Escape Room – Streamlit", page_icon="🗝️")

st.title("🧩 Das Escape Room Abenteuer")

st.markdown("""
Willkommen zu deinem Escape Room!  
Du wachst in einem dunklen Raum auf. Die Tür ist verschlossen. Du erinnerst dich nur an eines: **du musst hier raus!**

Löse die Rätsel in jedem Raum, um zu entkommen. Viel Glück...
""")

# Level-Verwaltung
if "level" not in st.session_state:
    st.session_state.level = 1

# LEVEL 1 – Das Schloss
if st.session_state.level == 1:
    st.subheader("🔒 Level 1: Das Zahlenschloss")
    st.write("Vor dir ist ein kleines Metallschloss. Es blinkt rot. Darunter steht:")
    st.code("Ich bin eine Zahl. \nMultipliziere mich mit mir selbst und du bekommst 49.")
    
    guess = st.text_input("Was ist die richtige Zahl?")
    if guess == "7":
        st.success("Klick! Das Schloss öffnet sich. Du kommst weiter.")
        st.session_state.level = 2
    elif guess:
        st.error("Das scheint nicht zu stimmen...")

# LEVEL 2 – Der geheime Code
if st.session_state.level == 2:
    st.subheader("🧠 Level 2: Die Wandinschrift")
    st.write("An der Wand steht eine kryptische Nachricht:")
    st.code("Drehe mich um, ich bin 3-5-7. Doch richtig herum wirst du frei.")

    code = st.text_input("Gib den Code ein, den du sehen würdest, wenn du ihn umdrehst:")
    if code == "753":
        st.success("Ein verstecktes Fach öffnet sich... Ein Schlüssel liegt darin!")
        st.session_state.level = 3
    elif code:
        st.error("Hmm… das scheint nicht richtig zu sein.")

# LEVEL 3 – Das Zahlenrätsel
if st.session_state.level == 3:
    st.subheader("📐 Level 3: Die Zahlenfolge")
    st.write("Auf dem Tisch liegt ein Zettel mit Zahlen:")
    st.code("2, 3, 5, 8, 13, ?")
    answer = st.text_input("Welche Zahl fehlt?")
    if answer == "21":
        st.success("Die Zahl passt – ein weiterer Hinweis erscheint.")
        st.session_state.level = 4
    elif answer:
        st.error("Das passt leider nicht in die Reihe.")

# LEVEL 4 – Das Rätsel der Karte
if st.session_state.level == 4:
    st.subheader("🗺️ Level 4: Das Kartenrätsel")
    st.write("Du findest ein Pergament mit folgender Inschrift:")
    st.code("Ich habe Städte, aber keine Häuser. Ich habe Berge, aber keine Bäume. Ich habe Wasser, aber keine Fische.")
    
    riddle = st.text_input("Was bin ich?")
    if riddle.lower().strip() == "karte":
        st.success("Du bist klug – das Rätsel ist gelöst!")
        st.session_state.level = 5
    elif riddle:
        st.error("Fast, aber nicht ganz.")

# LEVEL 5 – Das finale Rätsel
if st.session_state.level == 5:
    st.subheader("🧩 Level 5: Der letzte Schlüssel")
    st.write("Du findest eine Truhe mit einem Rätsel:")
    st.code("Je mehr du wegnimmst, desto größer werde ich. Was bin ich?")
    
    final = st.text_input("Deine Antwort:")
    if final.lower().strip() == "loch":
        st.success("Die Truhe öffnet sich, ein Tunnel erscheint...")
        st.balloons()
        st.markdown("🎉 **Herzlichen Glückwunsch! Du hast erfolgreich entkommen!**")
        st.session_state.level = 6
    elif final:
        st.error("Nicht ganz – überleg nochmal.")

# Optional: Reset
if st.session_state.level == 6:
    if st.button("🔁 Noch einmal spielen"):
        st.session_state.level = 1

