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
define l = Character("Lord Marlow", color="#8fb3a8")    # the cursed family patriarch
define m2 = Character("Lady Marlow", color="#d4a373")   # his wife
define r = Character("Rowan", color="#e8d8e8")           # their daughter
define pa = Character("Professor Ashe", color="#8fb3a8")   # Egyptologist
define j = Character("The Jaguar", color="#8fb3a8")        # the freed spirit

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Backgrounds (reused from the trilogy)
# -------------------------------------------------------------------------------------------
image bg mansion_ext = "images/backgrounds/bg_mansion_restored.webp"
image bg hallway = "images/backgrounds/bg_hallway.webp"
image bg library = "images/backgrounds/bg_library.webp"

# -------------------------------------------------------------------------------------------
# IMAGE ALIASES — Characters (placeholders; reuse trilogy sprites when available)
# -------------------------------------------------------------------------------------------
image eleanor_neutral = Solid("#c8a2c8")
image eleanor_determined = Solid("#c8a2c8")
image neith_neutral = Solid("#e8d8e8")
image curator = Solid("#b08050")
image corvus = "images/sprites/corvus.png"
image scarab_amulet = "images/ui/scarab_amulet.png"
image jaguar_spirit = Solid("#1a3a1a")

# -------------------------------------------------------------------------------------------
# CUSTOM TRANSITIONS
# -------------------------------------------------------------------------------------------
define slow_dissolve = Dissolve(1.5)
define slow_fade = Fade(1.0, 0.5, 1.0)
define flash = Fade(0.1, 0.0, 0.5, color="#ffffff")

# -------------------------------------------------------------------------------------------
# MAIN MENU — episode select
# -------------------------------------------------------------------------------------------
label start:
    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Mansion Mysteries{/color}{/size}"

    pause 1.0

    menu:
        "Episode One — Upon Reflection":
            jump episode_one

        "Episode Two — The Cursed Family":
            jump episode_two

        "Episode Three — The Duat's Echo":
            jump episode_three

        "Episode Four — The Jaguar's Shadow":
            jump episode_four

    return

# -------------------------------------------------------------------------------------------
# EPISODE ONE — UPON REFLECTION
# -------------------------------------------------------------------------------------------
label episode_one:
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

# -------------------------------------------------------------------------------------------
# EPISODE TWO — THE CURSED FAMILY
# -------------------------------------------------------------------------------------------
label episode_two:
    # Game State
    $ clue_heirloom = False
    $ clue_ledger2 = False
    $ collector_seen = False

    scene bg mansion_ext
    with slow_fade

    "A fortnight had passed since the mirror was burned. The mansion was quiet, the roses in bloom, and I had begun to think the world had run out of haunted things."

    "I was wrong."

    scene bg hallway
    with slow_dissolve

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Neith. There's a carriage at the gate. A very fine one."

    n "A lord, then. Or a lady with a problem."

    "A moment later, the butler announced our visitor—Lord Marlow, of the Marlow family, whose name I knew from the society pages and little else."

    scene bg library
    with slow_fade

    "Lord Marlow was a tall, grey man with the careful bearing of someone who had spent a lifetime keeping secrets. He did not sit. He stood by the fire, turning a small object over in his hands."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    l "You solved the Ashworth affair. The mirror. I know because I have been watching you, and because I have a problem of my own."

    e "What kind of problem, Lord Marlow?"

    "He held out the object. It was a small, ornate locket of tarnished silver, its face engraved with a crest—a rearing griffin."

    "The same crest as the letter that had brought us the mirror."

    l "This locket has been in my family for three hundred years. It is said to be cursed—that it brings ruin to whoever holds it. I did not believe it. I am a rational man."

    l "But my son is dead, ladies. And my daughter is dying. And the locket is the only thing they both touched."

    "Neith went very still. She reached for the locket, then stopped."

    n "Lord Marlow. Where did your family come by this?"

    l "It has always been ours. It is the Marlow crest."

    n "No. That is not a Marlow crest. That is a Thorne crest."

    "The room went cold. I stared at the locket, and I understood—the griffin, the same as the letter, the same as the mirror's trail."

    e "Neith. The man in the dark coat. He's not collecting random artifacts. He's collecting *Thorne* artifacts."

    n "And this one is the second piece."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPISODE TWO — THE CURSED FAMILY{/color}{/size}"

    pause 1.5

    # --- The investigation ---
    scene bg library
    with slow_fade

    "We examined the locket in the library, the fire crackling, the rain tapping at the windows. Neith held it up to the light, and I saw her frown."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "What is it?"

    n "The locket is not cursed, Eleanor. It is *keyed*. It only responds to the blood of the family it was bound to—the Thorne blood."

    e "But the Marlows have held it for three hundred years."

    n "Which means the Marlows are Thorne. A branch of the family that broke away, long ago, and took the locket with them. They have been carrying a piece of the old curse without knowing it."

    e "And the man in the dark coat wants it back."

    n "He wants all of it. The mirror. The locket. Whatever else is out there. He is assembling something."

    "I looked at the locket, and I felt the weight of it—a piece of my own bloodline, hidden in a stranger's family for three centuries."

    e "Then we have to find out what it does. And we have to stop him from taking it."

    n "There is only one way to know what the locket holds, Eleanor. Someone with Thorne blood must open it."

    "We both looked at the locket. And then we both looked at me."

    e "You want me to open it."

    n "It is the only way. And I will be right here."

    menu:
        "Open the locket — face what it holds":
            jump open_locket

        "Refuse — find another way":
            jump refuse_locket

    return

label open_locket:
    "I took the locket in my hands. It was cold, and it seemed to *know* me—to lean toward my blood like a thing that had been waiting."

    "I pressed the catch, and it sprang open."

    with flash

    "Inside was not a portrait. It was a *name*, engraved in a hand I knew—the hand of the first Thorne."

    "And beneath it, a single word: *Debt.*"

    "The room seemed to darken. I felt a cold hand close around my heart, and I heard—faint, distant—a voice that was not Neith's."

    "You are the blood. You are the debt. You are the one who must pay."

    e "Neith. It's speaking to me."

    n "What is it saying?"

    e "It says I owe a debt. That the bloodline must pay."

    "Neith's face went pale."

    n "Eleanor. The locket is not just a piece of the curse. It is a *claim*. It marks the bearer as the one who must complete the old bargain."

    e "The bargain with the jaguar? That's ended."

    n "Not the jaguar. The *older* hunger. The thing the jaguar was bound to watch. The locket is a piece of *that*."

    "I stared at the name in the locket. The first Thorne. And I understood, with a cold clarity, that the man in the dark coat was not trying to collect the pieces."

    "He was trying to *reunite* them. And the locket had just marked me as the key."

    $ clue_heirloom = True

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE COLLECTOR{/color}{/size}"

    pause 1.5

    jump collector_encounter

label refuse_locket:
    "I set the locket down, my hand steady."

    e "No. I will not open it. I have spent three years refusing to be my name, Neith. I will not let a piece of metal decide who I am."

    n "Then we find another way. But we must be quick—the man in the dark coat will not wait."

    "I looked at the locket, cold and patient on the table. And I felt, more than saw, that it was watching me."

    e "We need to know what it is before he takes it. But we do it on our terms."

    n "Agreed. Let us find out who has been hunting Thorne artifacts—and why."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE COLLECTOR{/color}{/size}"

    pause 1.5

    jump collector_encounter

label collector_encounter:
    scene bg library
    with slow_fade

    "We did not find the man in the dark coat. He found us."

    "He was standing in the library when we returned—a tall, pale figure in a long dark coat, his face half-hidden in shadow. He did not move as we entered. He only watched, patient as the tide."

    show corvus at center
    with dissolve

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Who are you?"

    "His voice was low and calm, like water over old stone."

    cu "I am the one who has been waiting for you, Eleanor Thorne. For a very long time."

    e "You're the one who collects the artifacts. The mirror. The locket."

    cu "I do not collect them. I *reunite* them. They are pieces of a whole—a whole that was stolen from your family, and scattered to the winds."

    n "Stolen? The Thorne bloodline was a curse. You are trying to bring it back."

    cu "I am trying to restore what was *rightfully* theirs. The power your ancestors were robbed of. The power that was meant to be yours."

    "He stepped closer, and I saw his eyes—old, and patient, and certain."

    cu "You are the blood, Eleanor. The locket has marked you. You are the one who can complete the assembly. You can have it all—the power, the name, the legacy your family was denied."

    cu "Or you can let it be scattered forever, and watch the pieces fall into the hands of those who will misuse them."

    "He held out his hand. In it, the locket—and something else. A shard of dark glass, humming with a cold light."

    cu "The mirror is gone. But I have others. Join me, and we will finish what the first Thorne began."

    $ collector_seen = True

    menu:
        "Refuse the collector — stand against him":
            jump refuse_collector

        "Hear him out — ask what he truly wants":
            jump question_collector

    return

label refuse_collector:
    "I did not move. I held his gaze, steady and cold."

    e "I have spent three years refusing to be my name, and I will not start now. The Thorne power was a curse, not a legacy. And I will not help you bring it back."

    "The collector's eyes flickered—not with anger, but with something almost like sorrow."

    cu "You are the first Thorne in a thousand years who could have completed it. And you refuse."

    e "I refuse to become what my ancestors were."

    "He was silent for a long moment. Then he nodded, slowly."

    cu "Then I will find another way. But know this, Eleanor Thorne—the pieces will not stay scattered forever. And when they reunite, with or without you, the old hunger will wake."

    "He turned, and the shadows seemed to swallow him. When I blinked, he was gone."

    "The locket lay on the table, cold and still. He had left it. He did not need it—not yet."

    e "Neith. He's going to keep hunting."

    n "I know. And we are going to keep stopping him."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPILOGUE{/color}{/size}"

    pause 1.5

    jump episode_two_epilogue

label question_collector:
    "I did not refuse. I held his gaze, and I asked the question that had been burning in me since the mirror."

    e "What are you really trying to reunite? The mirror, the locket—what are they pieces of?"

    "The collector was silent for a long moment. Then he spoke, and his voice was heavy."

    cu "Before the jaguar, there was an older hunger. The thing the jaguar was bound to watch. The first Thorne did not only bargain with the jaguar—he *shattered* the older hunger, and bound each piece to an artifact, to keep it from ever reuniting."

    cu "The jaguar was the guard. You ended the guard, Eleanor. And now the pieces are free to come together again."

    e "And you want to reunite them. To bring the older hunger back."

    cu "I want to *finish* what was started. The power was meant to be the Thorne's. It was stolen from them. I am only returning what is rightfully yours."

    "I looked at him, and I saw the certainty in his eyes—the belief that he was doing something just."

    e "You're wrong. The power was never meant to be anyone's. It was a curse, and my family paid for it with their souls."

    "The collector's expression did not change. But something in his eyes went cold."

    cu "Then we are at an impasse, Eleanor Thorne. And I am sorry for it."

    "He turned, and the shadows swallowed him. When I blinked, he was gone."

    e "Neith. He knows what the pieces are. And he's not going to stop."

    n "Neither are we."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}EPILOGUE{/color}{/size}"

    pause 1.5

    jump episode_two_epilogue

label episode_two_epilogue:
    scene bg hallway
    with slow_fade

    "The mansion was quiet that night. The fire crackled, and the rain fell, and I sat with the locket on the table between us."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "He called it the older hunger. The thing the jaguar was bound to watch."

    n "I have heard of it, Eleanor. In the oldest stories of the Duat. A hunger older than the gods themselves, that was broken and scattered so it could never return."

    e "And the first Thorne shattered it. Bound the pieces to artifacts."

    n "And now the pieces are finding their way back together. The mirror. The locket. And there will be more."

    "I looked at the locket, cold and patient on the table."

    e "He said I was the key. That the locket marked me."

    n "It did. But that does not mean you must turn it."

    "She reached across and took my hand."

    n "You are not your name, Eleanor. You never were. And whatever the collector believes, you are the one who will decide what happens to those pieces."

    e "And if he's right? If the older hunger wakes?"

    n "Then we will face it. Together. As we have faced everything."

    "I looked at her, and in the firelight, I felt the weight of it lift, just a little."

    e "Together, then."

    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Mansion Mysteries will return...{/color}{/size}"

    pause 2.0

    centered "{size=+6}{color=#d4a373}END OF EPISODE TWO{/color}{/size}"

    pause 2.0

    return

# -------------------------------------------------------------------------------------------
# EPISODE THREE — THE DUAT'S ECHO
# -------------------------------------------------------------------------------------------
label episode_three:
    # Game State
    $ clue_amulet = False
    $ neith_trial = False

    scene bg hallway
    with slow_fade

    "The letter came from a Professor Ashe, an Egyptologist at the British Museum. It was polite, precise, and faintly worried."

    "'Ladies, I have come into possession of an object that I believe belongs, by right, to the Thorne family. It is a scarab amulet of unusual antiquity. I would be grateful for your counsel.'"

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "A scarab amulet. Another piece?"

    n "I know what it is, Eleanor. I have not seen it in a hundred years, but I know it."

    e "You've seen it before?"

    n "I stood guard over it, in the Duat. It was the seal on the tomb of a Thorne who tried to escape the bargain—who hid a piece of the hunger where he hoped it would never be found."

    n "If it is here, in England, then someone has brought it out. And that means the collector is closer than we thought."

    scene bg library
    with slow_fade

    "Professor Ashe was a thin, earnest man, his rooms cluttered with shards, papyrus, and the smell of old sand. He set the amulet before us with a reverence that bordered on fear."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    pa "It arrived by anonymous post, three days ago, with a note that it 'belonged with the Thorne name.' I did not know what to do. The object—it seems to *watch* me."

    n "It does. It is keyed to the blood, like the others."

    pa "You have seen such things before?"

    n "I have stood in the place where this was made. It is a piece of a greater whole—a hunger that was broken and scattered, to keep it from reuniting."

    "I reached for the amulet, and Neith caught my hand."

    n "Wait. This one is different, Eleanor. It is not merely keyed to Thorne blood. It is keyed to *me*."

    e "To you?"

    n "I guarded it for a century. It knows my touch. And it will show whoever holds it the thing I fear most."

    e "What do you fear, Neith?"

    "She was quiet for a long moment. Then she took the amulet from Ashe, and her voice was steady."

    n "That I did not choose mercy at all. That I chose it because I was afraid of the alternative—and that I am not the good Thorne I believed."

    menu:
        "Let Neith read the amulet — face her fear":
            jump neith_reads_amulet

        "Refuse — protect Neith from the trial":
            jump neith_refused

    return

label neith_reads_amulet:
    "Neith closed her hand around the amulet, and the room went cold."

    with flash

    "For a moment, she stood motionless. And then I saw it—a darkness pass across her face, a shadow of the woman she might have been. The woman who fed the hunger instead of starving it."

    "She gasped, and the amulet fell from her hand, clattering to the floor."

    $ neith_trial = True

    e "Neith!"

    n "I saw it, Eleanor. The thing I could have become. The hunger I could have fed, if I had been weaker."

    "She looked at me, and her eyes were bright."

    n "I did not choose mercy because I was afraid, Eleanor. I chose it because it was *right*. And this amulet cannot take that from me."

    e "Then you've passed its trial."

    n "No. I have passed *my* trial. The amulet only showed me what I already knew."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE COLLECTOR{/color}{/size}"

    pause 1.5

    jump collector_episode

label neith_refused:
    "I took the amulet from Neith's hand and set it back on the desk."

    e "No. I will not let it do to you what the mirror did to me. We are not prisoners of these things, Neith."

    n "You are right. It has waited a century for me to touch it. It can wait a little longer."

    "But I saw it—the flicker in her eyes, the pull of the thing she feared. She was not unaffected."

    scene black
    with slow_fade

    centered "{size=+6}{color=#d4a373}THE COLLECTOR{/color}{/size}"

    pause 1.5

    jump collector_episode

label collector_episode:
    scene bg library
    with slow_fade

    "The collector did not wait long."

    "He was waiting for us at the mansion when we returned, a tall pale figure in the lamplight, the amulet in his hand."

    show corvus at center
    with dissolve

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    "Neith went still. She had not looked at him since we left the Duat."

    cu "You should not have let it slip through your fingers, priestess. It is the third piece. And it has been waiting for you."

    n "You are Corvus. The raven. The last Thorne who believes the power is a birthright."

    cu "You know my name."

    n "I know your line. The ones who broke away, who kept the legends, who never learned what the Thorne power cost."

    cu "What it *cost*? It was stolen from us. You are the one who hid it—you and your chosen heir, this woman who refuses her own name."

    "He looked at me, and for the first time, there was something almost like pleading in his eyes."

    cu "Eleanor. You are the blood. The amulet, the locket, the mirror—they are yours. Not mine, not your ancestors'. *Yours*. Join me, and we will finish what the first Thorne began. We will restore the name. We will be *family*."

    menu:
        "Refuse Corvus — end it here":
            jump refuse_corvus

        "Ask him about the older hunger":
            jump question_corvus

    return

label refuse_corvus:
    "I stood my ground, and I did not flinch."

    e "You think it's a birthright, Corvus. It's a curse. My ancestors fed souls to a hunger for a name. I will not help you raise it again."

    "His expression fell. Not into anger—into sorrow."

    cu "You are the last Thorne who could have completed it. And you refuse to be family."

    "He turned, and the darkness swallowed him, the amulet still in his hand."

    "Neith stood beside me, her hand in mine."

    n "He will not stop. But we will not fall."

    jump episode_three_epilogue

label question_corvus:
    "I held his gaze. I did not refuse—I asked."

    e "Who was the first Thorne to you? Not the legend. The man."

    "Corvus was silent for a long moment. When he spoke, his voice was heavy."

    cu "He was my father's father's father. A man who found a hunger in the dark, and fed it to buy his family power. He thought it was a bargain. It was a *trap*."

    e "Then why do you want to finish it?"

    cu "Because the power was meant to be ours. It was not the first Thorne who was wrong—it was the ones who broke away and hid it. I am not restoring a curse. I am restoring what was stolen."

    "I looked at him, and I understood. He did not see the suffering. He only saw the legacy."

    e "You're wrong, Corvus. But I will not let you pay for it with more souls."

    "He looked at me, sad, and then turned into the dark."

    jump episode_three_epilogue

label episode_three_epilogue:
    scene bg hallway
    with slow_fade

    "The mansion was quiet. Neith sat by the fire, the amulet locked away in a lead box, safe but not forgotten."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "He called it a legacy. He thinks we're family—that we should finish it."

    n "He is family, in a way. He is what we would have been, if we had not learned to choose differently."

    e "And that's what makes him dangerous."

    n "Yes. Because he is not a monster. He is just someone who wants to belong."

    "I looked at her, and I took her hand."

    e "Then we will keep showing him what belonging really means."

    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Mansion Mysteries will return...{/color}{/size}"

    pause 2.0

    centered "{size=+6}{color=#d4a373}END OF EPISODE THREE{/color}{/size}"

    pause 2.0

    return

# -------------------------------------------------------------------------------------------
# EPISODE FOUR — THE JAGUAR'S SHADOW
# -------------------------------------------------------------------------------------------
label episode_four:
    # Game State
    $ jade_awake = False
    $ jaguar_guide = False

    scene bg library
    with slow_fade

    "The letter this time was not a letter. It was a small parcel, left on our doorstep in the night, wrapped in oilcloth and bound with black cord."

    "Inside, on a bed of black velvet, lay the jade jaguar."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    "Neith went very still. She had not seen it since the day she gave it to me in the Duat—the day it led us into the pyramid's heart."

    e "Neith. That's—"

    n "The jaguar. The key. The piece that bound the hunger."

    e "But we ended the bargain. We destroyed the jade jaguar in the temple."

    n "We destroyed the one I gave you, Eleanor. This is a *different* jade jaguar. The collector has been busy."

    "She reached for it, then stopped. In the lamplight, the pendant's eyes seemed to gleam."

    n "It is the fourth piece. And it is keyed to you."

    e "To me?"

    n "To your journey. To the woman who freed the jaguar rather than fed it. It is the piece that remembers *you*."

    "I looked at the pendant, and I felt a pull I could not name—a warmth, and a warning, both at once."

    "It was not a curse. It was a *test*. The same test I had passed in the pyramid."

    menu:
        "Take the jade jaguar — meet the test again":
            jump take_jade

        "Refuse — do not touch it":
            jump refuse_jade

    return

label take_jade:
    "I reached out and took the jade jaguar in my hand."

    with flash

    "The room dissolved, and I was in the jungle again—the green dark, the temple, the jaguar watching me from the dais."

    "But this time, the jaguar was not the hunger. It was the freed spirit—the guardian I had unbound in the pyramid."

    $ jaguar_guide = True

    show jaguar_spirit at center
    with dissolve

    j "You came back, little Thorne. I knew you would."

    e "You're the jaguar. The one I freed in the temple."

    j "I am the echo of it. A piece of the older hunger that was bound into this jade, to watch over the one who ended the bargain. I am your guardian now, Eleanor. Not the hunger—the memory of what you chose."

    e "What do you want?"

    j "To warn you. The raven—Corvus—he does not seek to reunite the older hunger to destroy it. He seeks to *become* it. And the final piece is not an object, Eleanor. It is *you*."

    "The vision flickered. I felt the weight of it—the truth the collector had not spoken."

    e "I'm the last piece."

    j "You are the key that turns the lock. With you, the hunger wakes whole. Without you, it can never be complete. Corvus does not need the artifacts. He needs *you* to accept them."

    "I let the jade jaguar go, and the vision faded. I was in the library again, Neith's hand on my arm."

    jump jaguar_confrontation

label refuse_jade:
    "I drew my hand back. The jade jaguar watched me, and I felt the familiar pull—the voice that had tempted me in the mirror, the hunger that was my name."

    e "No. I will not take it. I have faced this test before, and I will not fail it now."

    "The jade went cold and still. I had refused the invitation."

    n "You are wise, Eleanor. The piece wants you to take it, to complete the set. You have denied it the key."

    "But I knew the collector would not stop. If I would not turn the key, he would find another way."

    jump none

label none:
    "Neith's hand was steady on my arm. The jade jaguar lay cold on the desk, its eyes dark."

    scene bg hallway
    with slow_fade

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "Corvus. He's not trying to collect the artifacts. He's trying to make *me* the key."

    n "And if you refuse, he will try to force you. Or find another Thorne."

    e "There are no other Thornes, Neith. I am the last."

    "She looked at me, and in the firelight, her eyes were heavy."

    n "Then we have one choice left, Eleanor. Face him before he completes the set. And end this."

    jump ep4_finale

label jaguar_confrontation:
    "The vision faded, and I was back in the library—Neith's hand steady on my arm, the jade jaguar cold and still in my palm."

    "The jaguar's warning burned in me: *The final piece is not an object. It is you.*"

    show neith_neutral at right

    e "Neith. The jaguar told me the truth. Corvus doesn't need the artifacts. He needs *me* to accept them. I'm the key that turns the lock."

    n "Then he will come for you, Eleanor. And we must be ready."

    e "No. I will go to him. End this before he can complete the set."

    n "Not alone."

    "She took my hand, and I felt the strength of it."

    n "We face him together. As we have faced everything."

    jump ep4_finale

label ep4_finale:
    scene bg library
    with slow_fade

    "The mansion was still that night. And then, without a sound, Corvus was in the room—the four artifacts laid out on the table before him like an offering."

    show corvus at center
    with dissolve

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    cu "You have refused the key, Eleanor. And yet you come to me. Brave, or foolish."

    e "Both, perhaps. You said you wanted to restore the family name, Corvus. But the truth is you want to *become* the hunger."

    "He was silent. Then he nodded, slowly."

    cu "The hunger is the Thorne destiny. We were meant to be the greatest of all bloodlines. My line was cheated out of it—hidden, scattered, forgotten. I will not let it end in a quiet house and a woman who refuses her own name."

    e "My name was a curse, Corvus. I ended it. And I will end this, too."

    cu "You cannot destroy the pieces. Only a Thorne can. And you will not."

    "He held out his hand. In it, the mirror's shard, the locket, the amulet, the jade jaguar—all four pieces, humming with a cold, hungry light."

    cu "Take them, Eleanor. Complete the set. Be the woman you were always meant to be."

    menu:
        "Take the pieces — accept the power":
            jump ep4_power

        "Refuse the pieces — destroy them":
            jump ep4_destroy

    return

label ep4_power:
    "I looked at the pieces, and I felt the pull—the hunger that was my name, the power that had tempted my ancestors for a thousand years."

    "And I remembered the jaguar's words. The key that turns the lock. The woman I refused to become."

    e "No, Corvus. I will not be the woman you want."

    "I swept my hand across the table, scattering the pieces across the floor. The hunger screamed, and Corvus lunged—but Neith was there, and together we held the line."

    "The pieces lay shattered on the stone, and the older hunger, broken and scattered, could not reunite."

    "Corvus looked at me, and for the first time, there was grief in his eyes."

    cu "You have ended it. You have ended everything."

    e "I have ended the curse, Corvus. Not the family. The family is what I make of it. And I choose to make it a home."

    jump ep4_ending

label ep4_destroy:
    "I reached for the pieces, and instead of taking them, I drove them together—the shard, the locket, the amulet, the jade—and I spoke the words the jaguar had taught me."

    "The words that unmake a hunger."

    with flash

    "The pieces blazed white-hot, then shattered into dust. The older hunger, scattered and broken, could never reunite again."

    "Corvus stared at the dust, his face unreadable. Then he turned, and walked into the dark."

    cu "You have ended it. I hope the quiet house is worth it."

    e "It is. Because it is mine. And it is a home."

    jump ep4_ending

label ep4_ending:
    scene bg hallway
    with slow_fade

    "The mansion was quiet in the dawn. The pieces were dust, the hunger ended, and the shadow that had followed the Thorne name for a thousand years was, at last, gone."

    show eleanor_neutral at left
    show neith_neutral at right
    with dissolve

    e "He's gone, Neith. And the hunger with him. It's finally over."

    n "It is. The Thorne name is just a name now. No power. No curse. No hunger. Just a home."

    "She looked at me, and in the light, her eyes were soft."

    n "You did it, Eleanor. You ended the bloodline's curse, in the end, not by power but by refusal."

    e "I had help. I had you."

    "She took my hand, and we stood together in the quiet house that had once been a house of horrors, and was now a home."

    scene black
    with slow_fade

    centered "{size=+8}{color=#c8a2c8}The Thorne curse is ended. The Mansion Mysteries will continue...{/color}{/size}"

    pause 2.0

    centered "{size=+6}{color=#d4a373}END OF EPISODE FOUR{/color}{/size}"

    pause 2.0

    return
