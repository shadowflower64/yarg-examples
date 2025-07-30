# Localization

**Note: localization is not fully supported by YARG yet!**

The `generate_placeholders.py` script reads the `en-US.json` file from the current working directory, changes all strings to simple placeholder strings, and saves the results to `PLACEHOLDERS_LONG.json` and `PLACEHOLDERS_SHORT.json` in the current working directory. The `PLACEHOLDERS_LONG.json` file replaces everything with the full translation key, surrounded by two dollar signs on each side (for example: `$$Enum.Difficulty.ExpertPlus$$`). The `PLACEHOLDERS_SHORT.json` file replaces everything with only the top-most key, surrounded by one dollar sign on each side (for example: `$ExpertPlus$`)

The `en-US.json` file is not included in this repository. You can get the newest version of the en-US language file from the official YARG repo: 
* Stable: https://github.com/YARC-Official/YARG/blob/master/Assets/StreamingAssets/lang/en-US.json
* Nightly: https://github.com/YARC-Official/YARG/blob/dev/Assets/StreamingAssets/lang/en-US.json

These files can be helpful to quickly check which in-game strings are translatable, and which are hard-coded. They can also help with debugging certain localization features, such as practice mode sections.

To use these files, you have to place them into your YARG installation directory at: `.../installation/YARG_Data/StreamingAssets/lang/`, and then add a custom command-line argument with the launcher:
* `-lang PLACEHOLDERS_SHORT` to load the short placeholder file
* `-lang PLACEHOLDERS_LONG` to load the long placeholder file

**Warning: the contents of the `lang/` directory will be deleted every time the game updates!**

More info on localization is available on the YARG wiki: https://yarg.miraheze.org/wiki/Localization
