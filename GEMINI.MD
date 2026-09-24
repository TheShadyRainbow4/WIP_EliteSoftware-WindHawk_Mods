"explorer-ctrlq-new-folder.wh.cpp" is an upstream official mod so even if name changes FILE NAME must NEVER be changes!

Please track reported issues in corresponding md files with same name as .wh.cpp file it pretains to. always create this file before actually making changes. always mark if an issue was reported as fixed but never delete entries in the file. always append.

EliteSoftware Example Header for Windhawk Mods:

// ==WindhawkMod==
// @id              windhawk-mod-theshadyrainbow4
// @name            Amazing Windhawk Mod
// @description     Description of my amazing mod
// @version         1.2.6.7
// @author          TheShadyRainbow4
// @github          https://github.com/theshadyrainbow4
// @homepage        https://main.elitesoftwaretech.cc
// @include         explorer.exe
// @compilerOptions -lole32 -loleaut32 -lshlwapi -lshell32 -luuid -luser32
// ==/WindhawkMod==

after each edit please copy commited changes to "C:\ProgramData\Windhawk\ModsSource" overwriting existing copies if existing. do this via script to automate it each time. just have the script recurse through all .wh.cpp files located in "C:\Users\Administrator\Desktop\Projects\WindHawk_Mods\WIP_Mods" and sub folders and push all of them to that directory.

Ensure highly detailed organized readme sections are provided for each mod. do not leave comments in the code that indicate that it was done by an ai, that the methods we are using are hacky workarounds or anything like that just clear comments regarding function and purpose of each given section. organize code by spacing out sections with extra blank lines. and follow standard windhawk mod practices strictly. 

Version numbers in windhawk mods should be 4 values eg 1.2.3.4 and you should randomly bump the last 3 each update but dont change the first value unless I say to do so. 


All mods should be configurable in windhawk no hardcoded key combos, or values, User should be able to define everying custom. key combos should allow for 2 modifiers (though 1 of them can be optionally disabled) plus any letter or symbol eg ctrl+shift+q or ctrl+q or Shift+Alt+q 


NEVER CHANGE THE ID OR THE NAME OF ANY EXISTING MOD! The only header info you can change for an existing mod is the Version, Include, CompilerOptions, and (with consideration) appending or slightly changing the description. (This rule does not apply to entirely new mods.)
