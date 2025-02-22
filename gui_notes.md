
- Use TKinter
- Packing the app into an exe (https://www.pythonguis.com/tutorials/packaging-tkinter-applications-windows-pyinstaller/)

# Features

- Game profile
  - Window Name (optional) -> To auto choose profile
  - A list of variables to store the address code that can be change
  - It`s possible to add new variable to the game profile
    - Max HP
    - HP
    - Max Sp
    - SP
    - Buff Array
    - Map name
    - X coord
    - Y coord
    - Weight
  - A list of buff codes
    - This codes will be used in the macros conditions
    - The user can add more buff codes to the game profile
    - 
- Macro Profiles
  - A list of macros (created from template or directly)
  - Has a name
- Macro templates
  - A way to create reusable macros
  - The user can add variables (ex: named_hotkeys, specific delays, etc.)
- Macros
  - Macros will be the main goal of the gui
  - They have a list of actions like: press a button, click with mouse, wait x time, etc.
  - They will have a trigger type:
      - By conditions
        - When some variable reach some condition (ex: hp < 40%, Buff Array has some buff value)
      - Or by user input
        - The user input will be a hotkey
        - This type of trigger can have one of those type
          - Hold - When the user's hold the key, the macro will run
          - Fire - When the user's clicks the key, the macro will run once
          - Toggle - The user can activate/deactivate the macro through a key


overlay: https://www.reddit.com/r/Python/comments/op1tz0/tkinter_was_shockingly_easy_to_write_a_small/
https://github.com/lecrowpus/overlay