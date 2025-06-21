import streamlit as st

st.set_page_config(page_title="🦂 Tempel der Prüfungen", page_icon="🗝️")

st.title("🏺 Tempel der Prüfungen – Ein ägyptisches Escape-Rätsel")

# Session-State initialisieren
if "raum" not in st.session_state:
    st.session_state.raum = 1
if "schlüssel" not in st.session_state:
    st.session_state.schlüssel = []

# Hilfsfunktion: Fortschritt pro Raum
def init_raum(raum_nummer):
    st.session_state[f"r{raum_nummer}_score"] = 0
    st.session_state[f"r{raum_nummer}_solved"] = [False, False, False]

if f"r{st.session_state.raum}_score" not in st.session_state:
    init_raum(st.session_state.raum)

# ---------- RAUM 1 ----------
if st.session_state.raum == 1:
    st.subheader("🧮 Raum 1: Die Halle der Zahlen")
    st.markdown("Wände voller Hieroglyphen. Eine steinerne Tafel leuchtet in mattem Gold.")

    # RÄTSEL 1
    if not st.session_state.r1_solved[0]:
        q1 = st.text_input("🔢 Rätsel 1: Was ist das Ergebnis von 12 - (2 × 5)?", key="r1q1")
        if q1.strip() == "2":
            st.success("Das Fragment `𓂀` erscheint.")
            st.session_state.schlüssel.append("𓂀")
            st.session_state.r1_score += 1
            st.session_state.r1_solved[0] = True
        elif q1:
            st.error("Die Götter lächeln nicht.")

    # RÄTSEL 2
    if not st.session_state.r1_solved[1]:
        q2 = st.text_input("📏 Rätsel 2: Ich bin in deinem Kopf, kann jedoch nie berührt werden. Was bin ich?", key="r1q2")
        if q2.lower().strip() in ["gedanke", "ein gedanke"]:
            st.success("Das Fragment `𓃰` erscheint.")
            st.session_state.schlüssel.append("𓃰")
            st.session_state.r1_score += 1
            st.session_state.r1_solved[1] = True
        elif q2:
            st.error("Die Antwort bleibt verborgen...")

    # RÄTSEL 3
    if not st.session_state.r1_solved[2]:
        q3 = st.text_input("🧿 Rätsel 3: ROT13-Verschlüsselung von `Funq vf gur Qnex Orfg`", key="r1q3")
        if q3.lower().strip() == "shad is the dark best":
            st.success("Das Fragment `𓆣` erscheint.")
            st.session_state.schlüssel.append("𓆣")
            st.session_state.r1_score += 1
            st.session_state.r1_solved[2] = True
        elif q3:
            st.error("Die Götter verstehen deine Worte nicht.")

    # Weiter wenn 3/3 gelöst
    if st.session_state.r1_score == 3:
        st.success("Die Tür öffnet sich – du betrittst den nächsten Raum...")
        if st.button("➡️ Weiter zu Raum 2"):
            st.session_state.raum = 2
            init_raum(2)

# ---------- RAUM 2 ----------
if st.session_state.raum == 2:
    st.subheader("🔐 Raum 2: Die Kammer der Geheimnisse")
    st.markdown("In der Mitte ein leuchtendes Auge. Du spürst eine Präsenz.")

    if not st.session_state.r2_solved[0]:
        q1 = st.text_input("📜 Rätsel 1: Ich spreche ohne Mund und höre ohne Ohren. Was bin ich?", key="r2q1")
        if q1.lower().strip() == "echo":
            st.success("Fragment `𓉐` erhalten.")
            st.session_state.schlüssel.append("𓉐")
            st.session_state.r2_score += 1
            st.session_state.r2_solved[0] = True
        elif q1:
            st.error("Es hallt zurück – aber falsch.")

    if not st.session_state.r2_solved[1]:
        q2 = st.text_input("🪞 Rätsel 2: Wenn du mich nennst, bin ich schon vorbei.", key="r2q2")
        if q2.lower().strip() in ["die stille", "stille"]:
            st.success("Fragment `𓏏` erhalten.")
            st.session_state.schlüssel.append("𓏏")
            st.session_state.r2_score += 1
            st.session_state.r2_solved[1] = True
        elif q2:
            st.error("Die Kammer schweigt…")

    if not st.session_state.r2_solved[2]:
        q3 = st.text_input("🌒 Rätsel 3: Zwei Väter und zwei Söhne gingen in die Wüste. Sie waren drei. Wie ist das möglich?", key="r2q3")
        if q3.lower().strip() in ["großvater, vater und sohn", "es sind großvater, vater und sohn"]:
            st.success("Fragment `𓋹` erhalten.")
            st.session_state.schlüssel.append("𓋹")
            st.session_state.r2_score += 1
            st.session_state.r2_solved[2] = True
        elif q3:
            st.error("Zähl nochmal nach...")

    if st.session_state.r2_score == 3:
        st.success("Ein Geheimgang öffnet sich zwischen den Säulen.")
        if st.button("➡️ Weiter zu Raum 3"):
            st.session_state.raum = 3
            init_raum(3)

# ---------- RAUM 3 ----------
if st.session_state.raum == 3:
    st.subheader("⚰️ Raum 3: Die Gruft des Pharaos")
    st.markdown("Goldene Masken blicken auf dich herab. Es riecht nach Sand und Ewigkeit.")

    if not st.session_state.r3_solved[0]:
        q1 = st.text_input("🗿 Rätsel 1: Was wiegt mehr – 1 kg Federn oder 1 kg Gold?", key="r3q1")
        if q1.lower().strip() in ["gleich", "beides gleich viel", "sie wiegen gleich"]:
            st.success("Fragment `𓁹` erhalten.")
            st.session_state.schlüssel.append("𓁹")
            st.session_state.r3_score += 1
            st.session_state.r3_solved[0] = True
        elif q1:
            st.error("Der Pharao runzelt die Stirn...")

    if not st.session_state.r3_solved[1]:
        q2 = st.text_input("⏳ Rätsel 2: Ich kann fliegen, aber habe keine Flügel. Ich kann weinen, aber habe keine Augen. Was bin ich?", key="r3q2")
        if q2.lower().strip() == "wolke":
            st.success("Fragment `𓊽` erhalten.")
            st.session_state.schlüssel.append("𓊽")
            st.session_state.r3_score += 1
            st.session_state.r3_solved[1] = True
        elif q2:
            st.error("Das ist nicht ägyptisch genug...")

    if not st.session_state.r3_solved[2]:
        q3 = st.text_input("🔺 Rätsel 3: Welches Symbol ist auf jeder Seite einer echten ägyptischen Pyramide?", key="r3q3")
        if q3.lower().strip() == "dreieck":
            st.success("Letztes Fragment `𓂻` erhalten.")
            st.session_state.schlüssel.append("𓂻")
            st.session_state.r3_score += 1
            st.session_state.r3_solved[2] = True
        elif q3:
            st.error("Schau dir die Pyramide nochmal an!")

    if st.session_state.r3_score == 3:
        st.balloons()
        st.success("🎉 Du hast alle Schlüsselsegmente gesammelt!")
        st.markdown("**Geheimer Pharao-Schlüssel:** `" + ''.join(st.session_state.schlüssel) + "`")
        st.markdown("🏆 **Du entkommst dem Tempel – und nimmst den Schatz mit.**")

        if st.button("🔁 Neu starten"):
            for key in st.session_state.keys():
                del st.session_state[key]

