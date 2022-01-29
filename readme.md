# Resistor Picker
This small Python script is designed to help pick resistors to achieve as little deviation from a desired value as possible. The script is designed for hobbiests or students who need a quick set of options to continue their projects.

## Use
Open `settings.txt` and adjust:
`#desired_resistance_in_ohms#` to the desired total resistor value.
`#available_resistors_in_ohms#` to a list of available resistors.

In the given `settings.txt`, small measured deviations are added with plus and/or minus signs next to the labeled value of the resistors. This allows to increase precision when the available resistors are not perfect.

Run `resistor_picker.py` or `resistor_picker.exe` to obtain a list of possible resistor combinations in series that will approach the desired resistance. The number in front of each output line indicates the number of resistors needed for that possibility, and the `delta` at the end indicates the absolute deviation from the desired resistance.

## To Do

- Add parallel options
- Remove possibility duplicates
- Add further customisation for limited resistor sets