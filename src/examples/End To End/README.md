# End to End
This folder contains scripts that will be useful in end-to-end
automation. For example, one might desire to do the following
as part of an automated process.

* Update PLEXOS .csv files
* Update PLEXOS input data in .xml
* Update the horizon for the next 7 days
* Run one or more simulations (either in PLEXOS Connect or on a PLEXOS Desktop)
* Query PLEXOS outputs
* Construct output reports

Scripts in other parts of this repository can be run in sequence
to obtain this fully automated effect.

# 1. Edit_Execute_Query.py
This script shows an example of simple end-to-end automation. If using
Visual Studio Code as your Python IDE, one should run this script with 
an external console, which may be configured in ```launch.json``` as follows:

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "externalTerminal"
        }
    ]
}
```
# 2. launch.py

This script shows one way to launch a PLEXOS simulation on a licensed
PLEXOS Desktop machine. This process does not use the PLEXOS API, but
rather the Command Line Interface (CLI) of the PLEXOS Engine.

# 3. modify_setup.py

This script shows how to update the Horizon of a model.

# 4. update_inputs.py

This script shows how to update PLEXOS inputs, which may include attaching
data that is in a PLEXOS formatted data file, and formatting a stream of
time series data into a PLEXOS formatted data file.
