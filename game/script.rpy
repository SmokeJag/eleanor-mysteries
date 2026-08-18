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
define s = Character("The Curator", color="#d4a373")   # museum curator

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

# -------------------------------------------------------------------------------------------
# CUSTOM TRANSITIONS
# -------------------------------------------------------------------------------------------
define slow_dissolve = Dissolve(1.5)
define slow_fade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# -------------------------------------------------------------------------------------------
# EPISODE ONE — THE HAUNTED ARTIFACT
# -------------------------------------------------------------------------------------------
label start:
    # Game State
    $ clue_letter = False
    $ clue_ledger = False
    $ solved = False

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

    centered "{size=+6}{color=#d4a373}EPISODE ONE — THE HAUNTED ARTIFACT{/color}{/size}"

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

    # --- The investigation ---
    scene bg library
    with slow_fade

    "We spread the records across the library table. Three men, three deaths, one common thread—the mirror."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "The first was a banker. The second, a baron. The third, a merchant. Different lives, different deaths. But all of them—"

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

    e "We need to see the mirror. And we need to find out who sold it to Ashworth."

    n "The records will tell us. But first—"

    "She smiled, a little grim."

    n "—we need to be careful. A mirror that shows the guilty their sins is not something to look into lightly."

    e "Then we won't look into it. We'll look *at* it."

    "She raised an eyebrow."

    n "That is a very fine distinction, Eleanor."

    e "I'm a detective. Fine distinctions are my job."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE VAULT{/color}{/size}"

    pause 1.5

    # --- The vault ---
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

    "The light died. Neith staggered back, and I caught her."

    e "Neith!"

    n "I'm all right. I'm all right."

    "She looked at me, and her eyes were bright."

    n "Eleanor. It wasn't a curse that escaped. It was a *plan*."

    e "Ashworth?"

    n "He sold the mirror to each of them. He knew what it was. He *wanted* them to die."

    e "But why? What did they have in common?"

    n "I don't know yet. But I know who to ask."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE CONFRONTATION{/color}{/size}"

    pause 1.5

    # --- The confrontation ---
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

    "We took Ashworth into custody, and the mirror went into a lead-lined box, where it would trouble no one again."

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

    n "There will be other cases, Eleanor. The world is full of haunted things."

    "She was quiet for a moment, watching the fire."

    n "But I am glad this one is over. I did not like that mirror."

    e "Why?"

    n "Because it showed me what I might have been, if I had chosen differently. A century of hunger, and I could have been the one feeding it."

    "I reached out and took her hand."

    e "But you didn't. You chose mercy. And you're here, with me, in a house that used to be a curse and is now a home."

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
