
## Keyboard
### Hotkeys
- When a hotkey is triggered, the name of the hotkey is passed as its first parameter named `ThisHotkey`

#### Modifier Symbols
- `#` Win
- `!` Alt
- `^` Ctrl
- `+` Shift
- `&` Used between any two keys or mouse buttons to combine them into a custom hotkey
- `<` Use the left key of the pair
- `>` Use the right key of the pair


### Hotstrings


### Varibles
- `A_ThisHotkey` The most recently executed hotkey or non-auto-replace hotstring
    - This value will change if the current thread is interrupted by another hotkey or hotstring, so it is generally better to use the parameter *ThisHotkey* when available.
- `A_PriorHotkey` Same as above except for the previous hotkey.
- `A_TimeSinceThisHotkey` The number of milliseconds that have elapsed since *A_ThisHotkey* was pressed.
- `A_TimeSincePriorHotkey` The number of milliseconds that have elapsed since *A_PriorHotkey* was pressed.
- `A_EndChar` The ending character that was pressed by the user to trigger the most recent non-auto-replace hotstrin
    - If no ending character was required (due to the * option), this variable will be blank.

### Functions
- `Suspend [Mode]` Disables or enables all or selected hotkeys and hotstrings.
    - `1` or `True`: Suspends all hotkeys and hotstrings except those explained the Remarks section.
    - `0` or `False`: Re-enables the hotkeys and hotstrings that were disable above.
    - `-1` (default): Changes to the opposite of its previous state (On or Off).


### Directives
- `#HotIf [Expression]` Creates context-sensitive hotkeys and hotstrings.
    - The expression is evaluated when the key, mouse button or combination is pressed, or at other times when the program needs to know whether the hotkey is active.
    - It affects all hotkeys and hotstrings physically beneath it in the script, until the next #HotIf directive, and braces have no effect. So we can specify #HotIf without any expression to turn off context sensitivity.
    - A particular hotkey or hotstring can be defined more than once in the script if each definition has different #HotIf criteria. These are known as **hotkey variants**.







## Flow of Control
### If Statements
```C
if Expression
{
    Statements
} else if Expression {
    Statements
} else {
    Statements
}
```

### Loop Statements
- `SetTimer [Function, Period, Priority]` Causes a function to be called automatically and repeatedly at a specified time interval.
    - `Period` The approximate number of milliseconds






## Threads
- The **current thread** is defined as the flow of execution invoked by the most recent event; examples include hotkeys, SetTimer subroutines, custom menu items, and GUI events.
- If a second thread is started, the current thread will be interrupted (temporarily halted) to allow the new thread to become current.
- When the current thread finishes, the one most recently interrupted will be resumed.



