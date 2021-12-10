# Python PLEXOS API
https://github.com/EnergyExemplarNorthAmerica/Python-PLEXOS-API

A repository of simple Python examples for use with the PLEXOS API. 

**This branch for PLEXOS 9 is still in progress.** Please note that this repository 
is not a supported product of Energy Exemplar, but rather a help to the user which 
is a free time activity for dedicated fans of the product.

## Some key differences between PLEXOS 9 API and prior versions

### Python's .NET interop components only work with .NET 4. PLEXOS 9 is .NET 5. 
That means you need to install an additional software component to use the PLEXOS 9 API 
with Python. It is available on the Energy Exemplar customer portal (you have to scroll 
nearly to the bottom).
### The primary components to import have changed a bit.
Before
```
sys.path.append('C:/Program Files (x86)/Energy Exemplar/PLEXOS 8.1/')
clr.AddReference('PLEXOS7_NET.Core')
```
After
```
sys.path.append('C:/Program Files/Energy Exemplar/PLEXOS 9.0 API')
clr.AddReference('PLEXOS_NET.Core')
```
**Note** *the new location to add to the ```PATH``` references the install location of
the new software components mentioned above, and the missing ```7``` in the name
of the reference. Also if you are migrating from an older PLEXOS version, ```(x86)```
is no longer in the default installation folder.*
### Likewise, a key ```import``` statement has changed.
Before
```
from PLEXOS7_NET.Core import DatabaseCore
```
After
```
from PLEXOS_NET.Core import DatabaseCore
```
Again a missing ```7```.

### There is a new reference that contains some of the enumerations that used to be in EEUTILITY.
Before
```
clr.AddReference('EEUTILITY')
```
After
```
clr.AddReference('EEUTILITY')
clr.AddReference('EnergyExemplar.PLEXOS.Utility')
```
### There is a corresponding modification to import the enumerations that are in this new component.
Before
```
from EEUTILITY.Enums import *
```
After
```
from EEUTILITY.Enums import *
from EnergyExemplar.PLEXOS.Utility.Enums import *
```
### Some of the scripts are noted in the header as P9 Tested.
Two important points arise from this. First, this notation is not presently attached to 
every script. The scripts have been modified to reflect the above, but they may not all
run successfully for a variety of reasons. Second, the implication that it has been tested
doesn't confer any warrantee of its performance on any environment or infrastructure 
other than that on which it was tested. See below.

# PLEXOS® for Power Systems
PLEXOS® Integrated Energy Model (PLEXOS) is tried-and-true simulation software that
uses state-of-the-art mathematical optimisation combined with the latest data
handling and visualisation and distributed computing methods, to provide a 
high-performance, robust simulation system for electric power, water and gas that is 
leading edge yet open and transparent. PLEXOS meets the demands of energy market
participants, system planners, investors, regulators, consultants and analysts alike 
with a comprehensive range of features seamlessly integrating electric, water, gas 
and heat production, transportation and demand over simulated timeframes from minutes
to 10’s of years, all delivered through a common simulation engine with easy-to-use 
interface and integrated data platform. 

PLEXOS is the fastest and most sophisticated software available today, and also the
most cost-effective.

# PLEXOS Licensing
PLEXOS® licensing is *not* included with the license for these examples. These
scripts are therefore only useful to those with current PLEXOS licensing. 
Furthermore, these scripts are *NOT* a supported part of the PLEXOS software. They
are only illustrative of uses that could be made of the PLEXOS API by PLEXOS
licensees.

For assistance with PLEXOS licensing, please visit

https://www.energyexemplar.com/contact-us

# Development Environment
The authors are primarily using Anaconda Python version 3.6.x along with the PythonNet
repository, along with PLEXOS Desktop 9.0R03. 

*PLEXOS 9 API requires an additional set of software components to interoperate with Python.
In the Energy Exemplar download portal, this is called "API 9.000 R03". This library is 
PLEXOS version specific.*

The authors also use Visual Studio Code with the Python and GitExtensions VSCode extensions.

Also .NET Framework 4.7.2 or higher is needed. However, you would have to install 
this to use PLEXOS.

Anaconda --> https://www.anaconda.com/download/

Python for .NET --> https://pythonnet.github.io/

Visual Studio Code --> https://code.visualstudio.com/

Energy Exemplar and PLEXOS --> https://portal.energyexemplar.com/
