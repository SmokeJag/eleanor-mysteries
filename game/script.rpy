# -------------------------------------------------------------------------------------------
# ELEANOR: THE MANSION MYSTERIES
# A companion series to the SmokeJaguar Trilogy
# SmokeJaguar Studios
# -------------------------------------------------------------------------------------------
#
# CHARACTER DEFINITIONS
# -------------------------------------------------------------------------------------------
define e = Character("Eleanor", color="#c8a2c8")
define n = Character("Neith", color="#e8d8e8")
define c = Character("Mr. Ashworth", color="#8fb3a8")   # the client
define w = Character("Mrs. Bell", color="#d4a373")      # the banker's widow
define cu = Character("The Curator", color="#b08050")   # antiquities dealer who sourced the mirror
define g = Character("Giles", color="#888888")          # the Ashworth butler

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Backgrounds (reused from the trilogy)
# -------------------------------------------------------------------------------------------
image bg mansion_ext = "images/backgrounds/bg_mansion_ext.webp"
image bg hallway = "images/backgrounds/bg_hallway.webp"
image bg library = "images/backgrounds/bg_library.webp"

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Characters (placeholders; reuse trilogy sprites when available)
# -------------------------------------------------------------------------------------------
image eleanor_neutral = Solid("#c8a2c8")
image eleanor_determined = Solid("#c8a2c8")
image neith_neutral = Solid("#e8d8e8")
image curator = Solid("#b08050")

# -------------------------------------------------------------------------------------------
# CUSTOM TRANSITIONS
# -------------------------------------------------------------------------------------------
define slow_dissolve = Dissolve(1.5)
define slow_fade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# -------------------------------------------------------------------------------------------
# EPISODE ONE — UPON REFLECTION
# -------------------------------------------------------------------------------------------
label start:
    # Game State
    $ clue_letter = False
    $ clue_ledger = False
    $ clue_origin = False
    $ mirror_read = False
    $ tempted = False
    $ ashworth_guilty = True

    scene bg mansion_ext
    with slow_fade

    "The Thorne mansion no longer loomed. It *welcomed*."

    "Three years had passed since the hunger was ended. The black stone had been scrubbed clean, the broken windows replaced, and the gardens—once choked with shadow—now bloomed with roses."

    "It was still a strange house, full of old secrets. But it was *our* house now."

    scene bg hallway
    with slow_dissolve

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Neith. The post."

    n "On the table. There's a letter with a very expensive seal."

    "I picked it up. The wax was deep crimson, pressed with a crest I did not recognise—a rearing griffin."

    e "Who sends us a letter with a griffin on it?"

    n "Someone who wants to be noticed. Read it."

    "I broke the seal and read aloud."

    e "'To the Ladies of Thorne House. I have a problem that money cannot solve, and I am told you are the only ones who might. My name is Ashworth. I collect antiquities. And something in my collection has begun to... kill.'"

    "I looked up at Neith. She was already reaching for her coat."

    n "A haunted artifact. I knew the day would come."

    e "You sound almost pleased."

    n "It beats cataloguing the library. Come on, Sherlock. We have a case."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPISODE ONE — UPON REFLECTION{/color}{/size}"

    pause 1.5

    # --- The client ---
    scene bg library
    with slow_fade

    "Mr. Ashworth was a thin, nervous man with the hunted look of someone who had not slept in a week. He sat in our library, twisting his hat in his hands, and did not touch the tea Neith had set before him."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    c "Three men, ladies. Three men in six months. All of them bought the same piece from me, and all of them died within a fortnight."

    e "What piece?"

    c "A mirror. An old hand-mirror, silver, from the reign of—"

    "He swallowed."

    c "—of a queen who was not known for her mercy."

    n "Which queen?"

    c "Mary. The first. They called her Bloody Mary."

    "The name hung in the air. Neith went very still."

    e "You think the mirror is cursed."

    c "I *know* it is. I have seen what it does. I sold it to a man who laughed at the stories. A week later, his servants found him staring into it, his face frozen in a scream."

    "I exchanged a glance with Neith. This was not a case for the police. This was a case for us."

    e "Where is the mirror now?"

    c "In my vault. I have not dared to touch it. I brought you the only thing I could—the records of the three men who died."

    "He set a folder on the table. Neith reached for it."

    n "We'll take the case, Mr. Ashworth. But I have one question first."

    c "Anything."

    n "Why did you sell it, if you knew what it was?"

    "Ashworth's face went pale. He looked away."

    c "Because I am a collector, and I did not believe. Not truly. Not until it was too late."

    "He stood, and I saw the guilt in his eyes—the weight of three deaths he had sold."

    c "Please. End this. Before it takes anyone else."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE INVESTIGATION{/color}{/size}"

    pause 1.5

    # --- The investigation: where to begin ---
    scene bg library
    with slow_fade

    "We spread the records across the library table. Three men, three deaths, one common thread—the mirror."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "The first was a banker, James Bell. The second, a baron, Lord Whitmore. The third, a merchant, Silas Grant. Different lives, different deaths. But all of them—"

    "I tapped the page."

    e "—all of them died looking into the mirror."

    n "And all of them, I'd wager, had something to hide."

    e "What do you mean?"

    n "The mirror does not kill the innocent, Eleanor. It kills the guilty. It shows them what they have done—and they cannot look away."

    "I studied the records. There was something there, a pattern I was missing."

    e "Neith. Look at the dates. The banker died in March. The baron in April. The merchant in May. One a month, like clockwork."

    n "And the mirror was sold to each of them a fortnight before they died."

    e "So whoever is selling it—"

    n "—is feeding it. Deliberately."

    "The realisation settled over us like a cold shadow. This was not a cursed object that had escaped. This was a *weapon*, and someone was using it."

    e "Two ways to crack this open. We can talk to the families of the dead—find out what they had in common. Or we can trace the mirror itself—find out who sold it to Ashworth."

    n "The records say Ashworth bought it from a dealer in the East End. A man they call the Curator."

    e "Then we have a choice. Where do we start?"

    menu:
        "Visit the banker's widow — Mrs. Bell":
            jump investigate_family

        "Track down the Curator — the mirror's dealer":
            jump investigate_curator

    return

# --- Branch A: the victim's family ---
label investigate_family:
    scene bg hallway
    with slow_fade

    "Mrs. Bell lived in a modest house in a quiet square—a widow's home, kept neat and spare, with the photographs of a dead man still on the mantel."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    w "You say you're investigating my husband's death. The police called it a seizure. They said he died staring at his own reflection, like a man who had seen a ghost."

    e "We believe there was more to it, Mrs. Bell. Your husband bought a mirror shortly before he died. Do you remember it?"

    "Her face went pale."

    w "The mirror. Yes. He brought it home and he was *different* after that. Secretive. Guilty. He spent his last week in his study, staring at that terrible thing."

    e "Guilty about what?"

    "She hesitated, then went to a drawer and drew out a letter, yellowed with age."

    w "James was not a good man, ladies. I loved him, but I knew what he was. He was a banker who had ruined families—who had taken their homes and their savings and called it business."

    w "This letter came from a man named Ashworth, weeks before James died. He accused James of destroying his father. Of driving him to the workhouse, and then to his grave."

    e "Ashworth wrote to your husband?"

    w "Yes. James laughed at it. Said Ashworth was a fool who couldn't prove a thing. But I saw him look at the mirror after that. As if it knew."

    "I took the letter. It was the same griffin seal as the one on our doorstep."

    $ clue_letter = True

    "I tucked Ashworth's letter carefully into my coat. It might matter later."

    e "Mrs. Bell, you may have just saved lives. Thank you."

    w "Just... end it. Whatever it is. My husband was a sinner, but he was my husband. No one should die like that."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE TRACE{/color}{/size}"

    pause 1.5

    jump investigate_curator

# --- Branch B: the Curator ---
label investigate_curator:
    scene bg library
    with slow_fade

    "The Curator's shop was a cramped, dusty den of curiosities in a forgotten corner of the East End—a place that smelled of old paper, beeswax, and secrets."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    "The man himself was thin and sharp, with the quick, watchful eyes of a dealer who had sold many things and asked no questions."

    show curator at center
    with dissolve

    cu "Ladies. You have the look of people who want something they cannot name."

    e "We want to know about a mirror. A silver hand-mirror, sold to a Mr. Ashworth. The one that kills."

    "The Curator's smile did not waver, but something in his eyes went cold."

    cu "I sell many mirrors, miss. I do not keep a ledger of their sins."

    n "But you remember this one. I can see it in your face. You know what it does."

    "He was silent for a long moment. Then he reached beneath the counter and drew out a small, worn book."

    cu "I keep records. It is good for business, and better for protection. This mirror—"

    "He opened the ledger."

    cu "—was not mine to sell. It was placed in my hands by a man in a dark coat, who paid me well and told me to pass it on to a specific buyer."

    e "Ashworth?"

    cu "No. He told me to sell it to *whoever* was buying—and that the man who sold it would come for it again. It has been sold three times in six months. Each time, the buyer died."

    n "And each time, the man in the dark coat came back."

    cu "You are quick, priestess. Yes. He collects them, you see. The returned artifacts. The ones that feed."

    "I felt a chill. This was bigger than Ashworth."

    e "Who is he? The man in the dark coat?"

    cu "I do not know his name. But I can tell you this—he is not the first to have sold such things. And he will not be the last."

    "He closed the ledger and slid it toward us."

    cu "Take it. I have carried this secret long enough. Perhaps you can do what I could not."

    $ clue_origin = True

    "I took the ledger, heavy with a hundred secrets."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE VAULT{/color}{/size}"

    pause 1.5

    jump investigate_vault

# --- The vault ---
label investigate_vault:
    scene bg library
    with slow_fade

    "Ashworth's vault was a windowless room behind a steel door, lined with shelves of antiquities. And there, on a velvet stand in the centre, sat the mirror."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    "It was beautiful—silver, ornate, its handle carved with a serpent. It caught the lamplight and threw it back in a way that seemed almost alive."

    e "It's just a mirror."

    n "It is not. Can you feel it, Eleanor? The cold?"

    "I could. The air around the mirror was colder than the rest of the room, and it seemed to *lean* toward us, waiting."

    e "How do we destroy it?"

    n "We don't. Not yet. We need to know who is using it. And the mirror will tell us—if we ask it the right way."

    e "You want to look into it."

    n "I want to *read* it. There is a difference. The mirror shows the guilty their sins. But it also remembers every face it has ever shown. I can read those memories."

    e "Is that safe?"

    n "For me, yes. I have faced the Devourer, Eleanor. A mirror cannot frighten me."

    "She stepped toward the mirror, and I caught her arm."

    e "Neith. Be careful."

    "She looked back at me, and her eyes were warm."

    n "I always am, when you're watching."

    "She turned to the mirror, and laid her hand upon the glass."

    with flash

    "The room went dark. And then the mirror blazed with light—not silver, but *red*, and in its depths, I saw faces."

    "Three faces, one after another. The banker. The baron. The merchant. Each one staring into the mirror, their eyes wide, their mouths open in silent screams."

    "And then, behind them, a fourth face. A man in a dark coat, watching them die with a cold, satisfied smile."

    "Ashworth."

    $ mirror_read = True

    "The light died. Neith staggered back, and I caught her."

    e "Neith!"

    n "I'm all right. I'm all right."

    "She looked at me, and her eyes were bright."

    n "Eleanor. It wasn't a curse that escaped. It was a *plan*."

    e "Ashworth?"

    n "He sold the mirror to each of them. He knew what it was. He *wanted* them to die."

    e "But why? What did they have in common?"

    n "I don't know yet. But I know who to ask."

    "She looked at the mirror, still cold and waiting on its stand."

    n "Eleanor. There is one thing the mirror can show us that we have not asked. What it would show *you*."

    e "Me? I'm not guilty of anything."

    n "Every soul has a reflection, Eleanor. The mirror shows the guilty their sins. But it shows the innocent what they *fear* they have done."

    "I looked at the mirror. It seemed to watch me back."

    menu:
        "Look into the mirror — face what it shows":
            jump mirror_temptation

        "Refuse — do not look":
            "I shook my head."
            e "No. I will not give it that hold over me. We know enough. Ashworth is guilty. Let us end this."
            n "A wise choice, Eleanor. The mirror has no power over those who will not look."
            jump confrontation

    return

# --- The darker path: the mirror tempts Eleanor ---
label mirror_temptation:
    "I stepped toward the mirror, my heart steady, and I looked into the glass."

    "For a moment, nothing. And then—"

    "I saw my reflection. But it was not the woman I had become."

    "It was the woman I might have been, if I had claimed the jewel. If I had fed the hunger. If I had become the Devourer."

    "She wore a crown of gold, and her eyes burned with a cold, familiar light. She was beautiful, and terrible, and she was *me*."

    "And she spoke."

    "Not aloud. In my mind. A voice that was mine and not mine."

    "You could have had it all, Eleanor. The power. The name. The world at your feet. And you threw it away for—what? A quiet house? A woman who fears the dark?"

    "The image flickered. Behind my golden self, I saw Neith—but Neith was afraid. Neith was watching me with the eyes of a stranger."

    "You could have her too. Forever. You could make her never leave. You could bind her to you, as the jaguar bound your ancestors. All you have to do is reach into the glass."

    "The mirror's cold crept up my arm. I could feel its hunger, patient and vast, waiting for me to *choose*."

    $ tempted = True

    menu:
        "Resist — pull away from the mirror":
            "I tore my hand away from the glass, gasping. The vision shattered into shards of silver light."
            e "No. I am not that woman. I will never be that woman."
            "The mirror's light died, and the room was cold and ordinary again."
            n "Eleanor. You looked. What did it show you?"
            "I met her eyes, and I did not look away."
            e "A woman I refuse to become. That's all."
            "Neith studied me for a long moment, then nodded."
            n "Good. The mirror shows the truth, Eleanor. And the truth is that you are stronger than it knows."
            jump confrontation

        "Give in — let the mirror's power tempt you":
            "The cold surged up my arm, and for a terrible, seductive moment, I *wanted* it. The power. The certainty. The endless, perfect control."
            "My hand closed on the mirror's handle, and it was warm in my grip—alive."
            e "Neith... it's so cold. And so warm. I can feel it—"
            "Her hand closed over mine, and pulled me back from the glass."
            n "Eleanor. Look at me. Not at it."
            "I blinked, and the spell broke. The mirror went cold and dead in my hand."
            e "I almost—"
            n "I know. But you didn't. You are not your ancestors, Eleanor. And this mirror will not claim you."
            "I set the mirror down, my hand trembling. But I had passed the test."
            jump confrontation

    return

# --- The confrontation ---
label confrontation:
    scene bg library
    with slow_fade

    "We found Ashworth in the library, waiting for us. He looked up as we entered, and I saw the mask slip—just for a moment—before the nervous collector returned."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    c "Did you find anything? Is the mirror—"

    e "The mirror is fine, Mr. Ashworth. It's you we have questions about."

    "He went very still."

    c "I don't understand."

    n "I read the mirror's memories, Mr. Ashworth. I saw you. Watching. Smiling. As each of those men died."

    "The mask fell away. Ashworth's face hardened, and the nervousness was gone, replaced by something cold and old."

    c "You should not have looked into that mirror, priestess. Some things are better left unseen."

    e "Why did you do it? Why kill those men?"

    c "Because they deserved it. All of them. They were the men who ruined my family—who took my father's fortune, who drove him to his death. I have spent twenty years waiting for the means to make them pay."

    c "And then I found the mirror. And I found that it was hungry."

    "He smiled, and it was not a pleasant smile."

    c "It was the perfect instrument. It killed them, and it fed. And no one would ever know."

    e "Except us."

    c "Except you."

    "He reached into his coat."

    c "And I'm afraid I cannot allow that."

    "He drew a small revolver, and the room went cold."

    if clue_origin:
        e "It's over, Ashworth. We know about the Curator. We know about the man in the dark coat. The mirror was never yours to control—you were just another tool."

    menu:
        "Disarm him — rush him":
            "I did not hesitate. I lunged across the table, and the revolver went off—"
            with flash
            "—but Neith had already moved. She struck Ashworth's wrist, and the gun clattered to the floor."
            n "I told you, Eleanor. I always watch."
            "I kicked the revolver away, and Ashworth sagged, defeated."

        "Talk him down — appeal to his conscience":
            "I did not move. I held his gaze, steady and calm."
            e "You've already lost, Mr. Ashworth. The mirror is in our hands. The records are in our hands. And the police are on their way."
            e "But I want to know—was it worth it? Twenty years of hate, and three deaths. Did it bring your father back?"
            "His hand trembled. The revolver wavered."
            c "No. It didn't. It never does."
            "He lowered the gun, and the fight went out of him."
            c "I just wanted them to pay. That's all I ever wanted."

    "We took Ashworth into custody, and the mirror went into a lead-lined box."

    if tempted:
        "I looked at the lead box, and I felt a faint echo of the cold—the temptation—still curling in the back of my mind."
        "I had looked into the mirror, and I had seen the woman I refused to become. It would not claim me. But it would remember me."
        e "Neith. Burn it. Do not bury it. We cannot risk anyone finding it again."
        n "Are you sure?"
        e "Yes. Some doors should not be left unlocked."
        "We carried the box out to the garden and set it on the pyre. As the flames took it, the silver screamed—a sound like a thousand voices, silenced at last."
        "And I felt the temptation die with it."
    else:
        "I did not look into the mirror. I did not need to. I knew the woman I was, and I did not need a cursed glass to tell me."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPILOGUE{/color}{/size}"

    pause 1.5

    # --- Epilogue ---
    scene bg hallway
    with slow_fade

    "The mansion was quiet that night. The fire crackled in the library, and the rain tapped against the windows."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "A haunted mirror. A vengeful collector. And we solved it before dinner."

    n "You sound almost disappointed."

    e "A little. I was hoping for something more... mysterious."

    "Neith was quiet for a moment, watching the fire."

    n "The mirror is gone, Eleanor. But the man in the dark coat—the one the Curator spoke of, who collects the returned artifacts—he is still out there."

    e "You think there are more?"

    n "I know there are. The mirror was not the first. And it will not be the last. Someone is gathering them."

    "I looked at her, and in the firelight, I saw the weight of it in her eyes."

    e "Then we'll be ready when they surface."

    n "I know. But I am glad this one is over. I did not like that mirror."

    e "Why?"

    n "Because it showed me what I might have been, if I had chosen differently. A century of hunger, and I could have been the one feeding it."

    if tempted:
        "I was quiet for a moment, remembering the cold of the glass, the voice that was mine and not mine."
        e "It showed me the same thing, Neith. A woman I refused to become."
        "She looked at me, surprised."
        n "You looked into it. And you walked away."
        e "I had something to hold onto. A reason to resist."
    else:
        e "But you didn't. You chose mercy."

    "I reached out and took her hand."

    e "And you're here, with me, in a house that used to be a curse and is now a home."

    "She looked at me, and in the firelight, her eyes were soft."

    n "I know. And I would not trade it for anything."

    "We sat together in the quiet, the rain falling, the fire burning, and the mansion—once a house of horrors—felt, for the first time in its long, dark history, like a place of peace."

    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Mansion Mysteries will return...{/color}{/size}"

    pause 2.0

    centered "{size=+6}{color=#d4a373}END OF EPISODE ONE{/color}{/size}"

    pause 2.0

    return
