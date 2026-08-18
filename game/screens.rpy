################################################################################
## Screens — Eleanor: The Bloodline Curse
##
## Provides all standard Ren'Py screens styled with a dark Gothic theme,
## plus the custom inventory screen.
################################################################################

################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    font gui.button_text_font
    size gui.text_size
    color gui.text_color

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")
    color gui.text_color

style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5

style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")

style bar:
    ysize gui.bar_size
    left_bar Frame("#c8a2c8", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("#3a3a5a", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("#c8a2c8", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("#3a3a5a", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("#3a3a5a", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("#c8a2c8", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("#3a3a5a", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("#c8a2c8", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("#3a3a5a", gui.slider_borders, tile=gui.slider_tile)
    thumb "#c8a2c8"

style vslider:
    xsize gui.slider_size
    base_bar Frame("#3a3a5a", gui.slider_borders, tile=gui.slider_tile)
    thumb "#c8a2c8"

style frame:
    padding gui.frame_borders.padding
    background Frame(Solid("#1a1a2eCC"), gui.frame_borders, tile=gui.frame_tile)


################################################################################
## Say Screen — the dialogue box
################################################################################

screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    ## Side image (character portrait next to dialogue)
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style say_vbox is default

style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height
    background Frame(Solid("#0d0d1aDD"), 0, 0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height
    background Frame(Solid("#2a2a4aCC"), gui.namebox_borders, tile=gui.namebox_tile)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xpos gui.dialogue_xpos
    xanchor gui.dialogue_text_xalign
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos
    text_align gui.dialogue_text_xalign
    layout ("subtitle" if gui.dialogue_text_xalign else "tex")


################################################################################
## Input Screen
################################################################################

screen input(prompt):
    style_prefix "input"
    window:
        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default
style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


################################################################################
## Choice Screen — in-game menus
################################################################################

screen choice(items):
    style_prefix "choice"
    vbox:
        xalign 0.5
        yalign 0.5
        spacing 15
        for i in items:
            textbutton i.caption action i.action:
                style "choice_button"

style choice_vbox is vbox
style choice_button is default
style choice_button_text is default

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5
    spacing 15

style choice_button is default:
    properties gui.button_properties("choice_button")
    xsize gui.choice_button_width
    padding gui.choice_button_borders.padding
    background Frame(Solid("#2a2a4aCC"), gui.choice_button_borders, tile=gui.choice_button_tile)
    hover_background Frame(Solid("#4a3a6aCC"), gui.choice_button_borders, tile=gui.choice_button_tile)

style choice_button_text is default:
    properties gui.text_properties("choice_button")
    xalign gui.choice_button_text_xalign
    idle_color gui.choice_button_text_idle_color
    hover_color gui.choice_button_text_hover_color
    insensitive_color gui.choice_button_text_insensitive_color


################################################################################
## Quick Menu — bottom bar during gameplay
################################################################################

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -10

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu("history")
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu("save")
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu("preferences")
            textbutton _("Inv") action ToggleScreen("inventory")

init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    xalign 0.5
    yalign 0.5
    background Solid("#2a2a4aCC")
    hover_background Solid("#4a3a6aCC")
    selected_background Solid("#4a3a6aCC")
    padding (12, 6)

style quick_button_text:
    size gui.quick_button_text_size
    idle_color gui.quick_button_text_idle_color
    selected_color gui.quick_button_text_selected_color


################################################################################
## Main Menu Screen
################################################################################

screen main_menu():
    tag menu
    # Cinematic title background
    add "bg_title"

    # Dark overlay at the bottom so the menu buttons remain readable
    add Solid("#00000088") yalign 1.0 ysize 0.5

    ## Title
    vbox:
        xalign 0.5
        ypos 90
        text "Eleanor" size 110 color "#e8d8e8" xalign 0.5 bold True font "fonts/PirataOne-Regular.ttf" outlines [(2, "#1a1a2e", 0, 0)]
        text "The Bloodline Curse" size 44 color "#c8a2c8" xalign 0.5 font "fonts/PirataOne-Regular.ttf" outlines [(1, "#1a1a2e", 0, 0)]

    ## Studio credit
    text "SmokeJaguar Studios" size 24 color "#888888" xalign 0.5 ypos 300

    ## Menu buttons
    vbox:
        xalign 0.5
        yalign 0.62
        spacing 14

        textbutton _("Start") action Start() style "main_menu_button"
        textbutton _("Load") action ShowMenu("load") style "main_menu_button"
        textbutton _("Preferences") action ShowMenu("preferences") style "main_menu_button"
        textbutton _("About") action ShowMenu("about") style "main_menu_button"
        textbutton _("Quit") action Quit(confirm=not main_menu) style "main_menu_button"

style main_menu_button is default:
    xsize 400
    xalign 0.5
    padding (20, 8)
    background Frame(Solid("#2a2a4a88"), 4, 4)
    hover_background Frame(Solid("#4a3a6aCC"), 4, 4)

style main_menu_button_text is default:
    xalign 0.5
    size 32
    idle_color "#aaaaaa"
    hover_color "#c8a2c8"
    selected_color "#ffffff"


################################################################################
## Game Menu Base Screen
################################################################################

screen game_menu(title, scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add "#1a1a2e"

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        vbox:
                            transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude

    use navigation

    textbutton _("Return"):
        style "return_button"
        action Return()

    label title:
        style "game_menu_label"
        text_style "game_menu_label_text"

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_label is default
style game_menu_label_text is default

style game_menu_outer_frame:
    bottom_padding 45
    top_padding 180
    background Solid("#1a1a2eEE")

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    left_margin 60
    right_margin 30
    top_margin 15

style game_menu_label:
    xpos 75
    ysize 180

style game_menu_label_text:
    size gui.title_text_size
    color gui.accent_color
    yalign 0.5

style return_button is default:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45
    background None
    padding (10, 5)

style return_button_text is default:
    size gui.interface_text_size
    idle_color gui.idle_color
    hover_color gui.hover_color


################################################################################
## Navigation Screen
################################################################################

screen navigation():
    vbox:
        style_prefix "navigation"
        xpos gui.navigation_xpos
        yalign 0.5
        spacing gui.navigation_spacing

        if main_menu:
            textbutton _("Start") action Start()
        else:
            textbutton _("History") action ShowMenu("history")
            textbutton _("Save") action ShowMenu("save")

        textbutton _("Load") action ShowMenu("load")
        textbutton _("Preferences") action ShowMenu("preferences")

        if _in_replay:
            textbutton _("End Replay") action EndReplay(confirm=True)
        elif not main_menu:
            textbutton _("Main Menu") action MainMenu()

        textbutton _("About") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):
            textbutton _("Quit") action Quit(confirm=not main_menu)

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    background None
    padding (10, 5)

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    size gui.interface_text_size
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color


################################################################################
## About Screen
################################################################################

screen about():
    tag menu
    use game_menu(_("About"), scroll="viewport"):
        style_prefix "about"
        vbox:
            spacing 15
            label "[config.name!t]"
            text _("Version [config.version!t]\n")
            text _("A Gothic visual novel about blood, legacy, and the choices that define us.")
            text _("\nDeveloped by {b}SmokeJaguar Studios{/b}\n")
            text _("\nMade with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text
style about_label_text:
    size gui.label_text_size


################################################################################
## Save / Load Screens
################################################################################

screen save():
    tag menu
    use file_slots(_("Save"))

screen load():
    tag menu
    use file_slots(_("Load"))

screen file_slots(title):
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    use game_menu(title):
        fixed:
            order_reverse True
            button:
                style "page_label"
                key_events True
                xalign 0.5
                action page_name_value.Toggle()
                input:
                    style "page_label_text"
                    value page_name_value

            grid 3 3:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(3 * 3):
                    $ slot = i + 1
                    button:
                        action FileAction(slot)
                        has vbox
                        add FileScreenshot(slot) xalign 0.5
                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                            style "slot_time_text"
                        text FileSaveName(slot):
                            style "slot_name_text"
                        key "save_delete" action FileDelete(slot)

            hbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0
                spacing gui.page_spacing

                textbutton _("<") action FilePagePrevious()

                if config.has_autosave:
                    textbutton _("{#auto_page}A") action FilePage("auto")
                if config.has_quicksave:
                    textbutton _("{#quick_page}Q") action FilePage("quick")

                for page in range(1, 10):
                    textbutton "[page]" action FilePage(page)

                textbutton _(">") action FilePageNext()

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")
    padding (15, 6)

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")
    xsize gui.slot_button_width
    ysize gui.slot_button_height
    padding gui.slot_button_borders.padding
    background Frame(Solid("#2a2a4a88"), gui.slot_button_borders, tile=False)
    hover_background Frame(Solid("#4a3a6aCC"), gui.slot_button_borders, tile=False)

style slot_button_text:
    properties gui.text_properties("slot_button")
    size gui.slot_button_text_size
    xalign gui.slot_button_text_xalign
    idle_color gui.slot_button_text_idle_color


################################################################################
## Preferences Screen
################################################################################

screen preferences():
    tag menu
    use game_menu(_("Preferences"), scroll="viewport"):
        vbox:
            xfill True
            spacing 20

            hbox:
                box_wrap True
                spacing 30

                vbox:
                    style_prefix "radio"
                    label _("Display")
                    textbutton _("Window") action Preference("display", "any window")
                    textbutton _("Fullscreen") action Preference("display", "fullscreen")

                vbox:
                    style_prefix "radio"
                    label _("Rollback Side")
                    textbutton _("Disable") action Preference("rollback side", "disable")
                    textbutton _("Left") action Preference("rollback side", "left")
                    textbutton _("Right") action Preference("rollback side", "right")

                vbox:
                    style_prefix "check"
                    label _("Skip")
                    textbutton _("Unseen Text") action Preference("skip", "toggle")
                    textbutton _("After Choices") action Preference("after choices", "toggle")
                    textbutton _("Transitions") action InvertSelected(Preference("transitions", "toggle"))

            null height 10

            hbox:
                style_prefix "slider"
                box_wrap True
                spacing 20

                vbox:
                    label _("Text Speed")
                    bar value Preference("text speed")

                vbox:
                    label _("Auto-Forward Time")
                    bar value Preference("auto-forward time")

                if config.has_music:
                    vbox:
                        label _("Music Volume")
                        hbox:
                            bar value Preference("music volume")

                if config.has_sound:
                    vbox:
                        label _("Sound Volume")
                        hbox:
                            bar value Preference("sound volume")
                            if config.sample_sound:
                                textbutton _("Test") action Play("sound", config.sample_sound)

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style pref_label is gui_label
style pref_label_text is gui_label_text

style pref_label:
    top_margin 15
    bottom_margin 3

style pref_label_text:
    size gui.label_text_size
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_button:
    properties gui.button_properties("radio_button")
    padding (10, 5)
    background None

style radio_button_text:
    properties gui.text_properties("radio_button")
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style check_button:
    properties gui.button_properties("check_button")
    padding (10, 5)
    background None

style check_button_text:
    properties gui.text_properties("check_button")
    idle_color gui.idle_color
    hover_color gui.hover_color
    selected_color gui.selected_color

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")


################################################################################
## History Screen
################################################################################

screen history():
    tag menu
    predict False
    use game_menu(_("History"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):
        style_prefix "history"
        for h in _history_list:
            window:
                has hbox:
                    spacing 15
                    yfill True
                label (h.who or ""):
                    style "history_name"
                    substitute False
                    if h.who_args.get("color", None):
                        text_color h.who_args["color"]
                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
        if not _history_list:
            label _("The dialogue history is empty.")

define gui.history_allow_tags = { "b", "i", "u", "s", "color", "font", "size", "outlinecolor" }

style history_window is empty
style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text
style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


################################################################################
## Confirm Screen — quit / overwrite prompts (THIS WAS THE CRASH)
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    style_prefix "confirm"

    add Solid("#00000099")

    frame:
        vbox:
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action

    key "game_menu" action no_action

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_button
style confirm_button_text is gui_button_text

style confirm_frame:
    background Frame(Solid("#1a1a2eEE"), gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color "#ffffff"
    size gui.label_text_size

style confirm_button:
    properties gui.button_properties("confirm_button")
    background Frame(Solid("#2a2a4a"), 6, 6)
    hover_background Frame(Solid("#4a3a6a"), 6, 6)
    padding (30, 10)

style confirm_button_text:
    properties gui.text_properties("confirm_button")
    xalign 0.5
    size gui.interface_text_size
    idle_color "#cccccc"
    hover_color "#ffffff"


################################################################################
## Skip Indicator
################################################################################

screen skip_indicator():
    zorder 100
    style_prefix "skip"

    frame:
        hbox:
            spacing 9
            text _("Skipping")
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

transform delayed_blink(delay, cycle):
    alpha .5
    pause delay
    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .6)
        repeat

style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame(Solid("#1a1a2eCC"), 24, 8, 75, 8)
    padding (24, 8, 75, 8)

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    font "DejaVuSans.ttf"


################################################################################
## Notify Screen
################################################################################

screen notify(message):
    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide("notify")

transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0

style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos
    background Frame(Solid("#1a1a2eCC"), 24, 8, 60, 8)
    padding (24, 8, 60, 8)

style notify_text:
    properties gui.text_properties("notify")
    size gui.notify_text_size


################################################################################
## NVL Screen
################################################################################

screen nvl(dialogue, items=None):
    window:
        style "nvl_window"
        has vbox:
            spacing gui.nvl_spacing

        use nvl_dialogue(dialogue)

        for i in items:
            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0

screen nvl_dialogue(dialogue):
    for d in dialogue:
        window:
            id d.window_id
            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:
                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id

style nvl_window is default
style nvl_entry is default
style nvl_label is say_label
style nvl_dialogue is say_dialogue
style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True
    background Solid("#0d0d1aDD")
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_thought_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


################################################################################
## 🎒 Inventory Screen (custom)
################################################################################

screen inventory():
    modal True
    zorder 100

    add Solid("#00000088")

    frame:
        xalign 0.5
        yalign 0.5
        padding (30, 30)
        background Frame(Solid("#1a1a2eEE"), 4, 4)

        vbox:
            spacing 10
            xalign 0.5

            text "🎒 Inventory" size 40 color "#c8a2c8" xalign 0.5

            null height 20

            if not inventory:
                text "Your pockets are empty..." size 24 italic True xalign 0.5 color "#888888"
            else:
                viewport:
                    draggable True
                    mousewheel True
                    scrollbars "vertical"
                    xysize (400, 400)

                    vbox:
                        spacing 8
                        xalign 0.5
                        for item in inventory:
                            hbox:
                                spacing 10
                                text "•" size 28 color "#c8a2c8"
                                text "[item]" size 28 color "#ffffff"

            null height 20

            textbutton "Close" action Hide("inventory") xalign 0.5:
                text_size 24
                text_color "#ffffff"
                text_hover_color "#c8a2c8"
                background Frame(Solid("#2a2a4a"), 4, 4)
                hover_background Frame(Solid("#4a3a6a"), 4, 4)
                padding (20, 8)


################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675
