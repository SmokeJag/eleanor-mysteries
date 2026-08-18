################################################################################
## GUI Configuration — Eleanor: The Bloodline Curse
################################################################################

## Resolution
define gui.text_size = 28
define gui.name_text_size = 36
define gui.interface_text_size = 28
define gui.label_text_size = 36
define gui.notify_text_size = 22
define gui.title_text_size = 60

## Fonts — Gothic display fonts (Pirata One) + Victorian interface (Cinzel),
## with readable DejaVu for the dialogue body.
define gui.text_font = "DejaVuSans.ttf"
define gui.name_text_font = "fonts/PirataOne-Regular.ttf"
define gui.interface_text_font = "fonts/Cinzel-Regular.ttf"
define gui.button_text_font = gui.interface_text_font
define gui.choice_button_text_font = gui.text_font
define gui.title_text_font = "fonts/PirataOne-Regular.ttf"

## Colours — Gothic palette
define gui.accent_color = "#c8a2c8"
define gui.idle_color = "#888888"
define gui.idle_small_color = "#aaaaaa"
define gui.hover_color = "#c8a2c8"
define gui.selected_color = "#ffffff"
define gui.insensitive_color = "#55555580"
define gui.muted_color = "#3a3a5a"
define gui.hover_muted_color = "#4a3a6a"

define gui.text_color = "#ffffff"
define gui.choice_button_text_idle_color = "#cccccc"
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = "#55555580"

## Layout
define gui.text_xalign = 0.0
define gui.name_xalign = 0.0

## Dialogue
define gui.textbox_height = 278
define gui.textbox_yalign = 1.0
define gui.name_xpos = 360
define gui.name_ypos = 0
define gui.namebox_width = None
define gui.namebox_height = None
define gui.namebox_borders = Borders(5, 5, 5, 5)
define gui.namebox_tile = False

define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75
define gui.dialogue_width = 1116
define gui.dialogue_text_xalign = 0.0

## Buttons
define gui.button_width = None
define gui.button_height = None
define gui.button_borders = Borders(6, 6, 6, 6)
define gui.button_tile = False
define gui.button_text_size = gui.interface_text_size
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color
define gui.button_text_xalign = 0.0

## Choice buttons
define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_xalign = 0.5

## Slot buttons (save/load)
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color

## Spacing
define gui.page_spacing = 0
define gui.slot_spacing = 15

## Scrollbar
define gui.scrollbar_size = 18
define gui.scrollbar_tile = False
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)

## Bars
define gui.bar_size = 38
define gui.bar_tile = False
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.vbar_borders = Borders(6, 6, 6, 6)

## Slider
define gui.slider_size = 38
define gui.slider_tile = False
define gui.slider_borders = Borders(6, 6, 6, 6)

## Frames
define gui.frame_borders = Borders(6, 6, 6, 6)
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)
define gui.frame_tile = False

## Skip indicator
define gui.skip_ypos = 15
define gui.notify_ypos = 68

## Navigation
define gui.navigation_xpos = 60
define gui.navigation_spacing = 6

## Paging
define gui.page_button_borders = Borders(15, 6, 15, 6)

## Quick buttons
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## NVL
define gui.nvl_borders = Borders(0, 15, 0, 30)
define gui.nvl_height = 173
define gui.nvl_spacing = 15
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0

## History
define config.history_length = 250
define gui.history_height = 210
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0
