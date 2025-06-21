import streamlit as st

st.set_page_config(page_title="🌺 Ägyptischer Escape Room", page_icon="🛡️")

st.title(":classical_building: Ägyptischer Escape Room")

st.markdown("""
Willkommen im mystischen Escape Room des alten Ägyptens.  
In jedem der 5 Räume erwarten dich drei Prüfungen.  
Wähle in jeder Prüfung die **richtige Antwort** – sie ergibt eine **Ziffer**.  
Setze am Ende alle drei Ziffern zum **Türcode** zusammen.
""")

# ============================
# Hilfsfunktionen
# ============================
def pruefung(name, frage, antworten, key):
    with st.expander(name):
        st.markdown(frage)
        return st.radio("Wähle eine Antwort:", antworten, key=key)

def pruefe_code(eingabe, korrekt, erfolg_text):
    if eingabe == korrekt:
        st.success(erfolg_text)
        st.balloons()
        return True
    else:
        st.error("❌ Falscher Code. Versuche es erneut.")
        return False

# ============================
# Raum 1: Halle der Prüfungen
# ============================
st.header("🏛️ Raum 1 – Die Halle der Prüfungen")
a1 = pruefung("📜 Prüfung 1", "**Was symbolisiert der Gott Horus?**", ["1 – Gott des Jenseits", "4 – Gott des Himmels", "7 – Gott der Unterwelt"], "r1_q1")
a2 = pruefung("🦂 Prüfung 2", "**Wie nennt man die ägyptische Bilderschrift?**", ["2 – Papyrosen", "3 – Hieroglyphen", "8 – Demotisch"], "r1_q2")
a3 = pruefung("🔺 Prüfung 3", "**Wozu dienten die großen Pyramiden?**", ["5 – Observatorien", "6 – Grabstätten", "9 – Getreidespeicher"], "r1_q3")
r1_code = st.text_input("🔐 Türcode für Raum 1:", max_chars=3, key="r1_code")
if st.button("✅ Code prüfen für Raum 1"):
    pruefe_code(r1_code, "436", "🔓 Die Tür gleitet zur Seite. Du betrittst Raum 2.")

# ============================
# Raum 2: Grabkammer der Schatten
# ============================
st.header("🏺 Raum 2 – Die Grabkammer der Schatten")
b1 = pruefung("🐍 Prüfung 1", "**Welches Tier steht für Wiedergeburt?**", ["1 – Krokodil", "5 – Skarabäus", "7 – Katze"], "r2_q1")
b2 = pruefung("🧱 Prüfung 2", "**Welches Material nutzten die Ägypter für Schriftrollen?**", ["3 – Papyrus", "6 – Ton", "9 – Leder"], "r2_q2")
b3 = pruefung("👁 Prüfung 3", "**Wessen Auge symbolisierte Schutz?**", ["2 – Anubis", "4 – Osiris", "8 – Horus"], "r2_q3")
r2_code = st.text_input("🔐 Türcode für Raum 2:", max_chars=3, key="r2_code")
if st.button("✅ Code prüfen für Raum 2"):
    pruefe_code(r2_code, "538", "🔓 Schatten lösen sich. Der Weg zu Raum 3 ist frei.")

# ============================
# Raum 3: Die Halle der Spiegel
# ============================
st.header("🪞 Raum 3 – Die Halle der Spiegel")
c1 = pruefung("⚖️ Prüfung 1", "**Was wiegt das Herz der Verstorbenen in der Unterwelt?**", ["2 – Mehr als eine Feder", "4 – Gleich viel wie die Feder", "6 – Weniger als eine Feder"], "r3_q1")
c2 = pruefung("🔊 Prüfung 2", "**Wer ist der Gott der Weisheit?**", ["3 – Thot", "5 – Bastet", "7 – Seth"], "r3_q2")
c3 = pruefung("🔓 Prüfung 3", "**Wie öffnete man Grabkammern?**", ["1 – Mit einem Goldcode", "8 – Mit einem Siegelbruch", "9 – Mit einer Opfergabe"], "r3_q3")
r3_code = st.text_input("🔐 Türcode für Raum 3:", max_chars=3, key="r3_code")
if st.button("✅ Code prüfen für Raum 3"):
    pruefe_code(r3_code, "438", "🔓 Die Spiegel verschwinden – du kannst Raum 4 betreten.")

# ============================
# Raum 4: Kammer der Elemente
# ============================
st.header("🌪 Raum 4 – Die Kammer der Elemente")
d1 = pruefung("🔥 Prüfung 1", "**Welches Element symbolisiert Macht?**", ["2 – Wasser", "6 – Feuer", "7 – Sand"], "r4_q1")
d2 = pruefung("💨 Prüfung 2", "**Womit segelten ägyptische Boote?**", ["1 – Sonnenenergie", "3 – Wind", "5 – Kamele"], "r4_q2")
d3 = pruefung("🌊 Prüfung 3", "**Welcher Fluss war heilig?**", ["4 – Nil", "8 – Tigris", "9 – Euphrat"], "r4_q3")
r4_code = st.text_input("🔐 Türcode für Raum 4:", max_chars=3, key="r4_code")
if st.button("✅ Code prüfen für Raum 4"):
    pruefe_code(r4_code, "634", "🔓 Die vier Elemente beruhigen sich – Raum 5 liegt vor dir.")

# ============================
# Raum 5: Halle der Sterne
# ============================
st.header("🌌 Raum 5 – Die Halle der Sterne")
e1 = pruefung("🌠 Prüfung 1", "**Welches Sternbild war heilig für die Ägypter?**", ["3 – Orion", "6 – Stier", "9 – Jungfrau"], "r5_q1")
e2 = pruefung("🔭 Prüfung 2", "**Was war die Funktion der Sternkarten?**", ["2 – Navigation", "4 – Ackerplanung", "7 – Grabgestaltung"], "r5_q2")
e3 = pruefung("🌙 Prüfung 3", "**Wer war die Himmelsgöttin?**", ["1 – Isis", "5 – Nut", "8 – Maat"], "r5_q3")
r5_code = st.text_input("🔐 Türcode für Raum 5:", max_chars=3, key="r5_code")
if st.button("✅ Code prüfen für Raum 5"):
    if pruefe_code(r5_code, "324", "🎉 Du hast alle Prüfungen des Tempels bestanden!"):
        st.balloons()
        st.success("🏆 Glückwunsch! Du hast den ägyptischen Escape Room gemeistert.")

