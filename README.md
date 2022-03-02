# Python PLEXOS API
https://github.com/EnergyExemplarNorthAmerica/Python-PLEXOS-API

A repository of simple Python examples for use with the PLEXOS API

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

https://energyexemplar.com/contactus/

# Development Environment
The authors are primarily using Anaconda Python version 3.6.x along with the PythonNet
repository, along with PLEXOS Desktop 8.1R02. The authors also use Visual Studio Code
with the Python and GitExtensions VSCode extensions.

Also .NET Framework 4.7.2 or higher is needed. However, you would have to install 
this to use PLEXOS.

Anaconda --> https://www.anaconda.com/download/

Python for .NET --> https://pythonnet.github.io/

Visual Studio Code --> https://code.visualstudio.com/

Energy Exemplar and PLEXOS --> https://www.energyexemplar.com/

# Method and Enum Listing removal

Many users of this repository have asked why the .txt files that list out the 
enumerations and method signatures in this repository are out of sync with
PLEXOS X.Y R0Z. The short answer is that the information in those files is
version dependent. The best thing to do is to run the scripts that produce
those files against your installation of PLEXOS so that you will get a .txt
file that matches your installation. We provided these as a convenience and 
a quick reference, but their presence is causing some confusion amongst
those reviewing this repo due to the inconsistency between those files and 
what is installed on the actual machine.

# Using Enumerations in Python scripts

The names of the Enumerations rarely change between versions of PLEXOS. Most
commonly (for example) properties are added or removed hence the related 
Enumerations are added or removed. Hence, using the Enumeration symbols (names)
is relatively stable between versions.

The numbers associated with the enumerations is less stable. When scripting in
a way that requires Enumeration information to be passed to an API method, one
***really should*** always use the symbol name instead of the value even if the PLEXOS
API asks for an integer. (It sometimes does this because all Enums can be passed as 
integers, but they are not interchangeable in .NET arguments.) The example scripts 
in this repository demonstrate the strongly preferred way to do this (i.e., everywhere
an enumeration is required, an enumeration symbol is provided) e.g.,
```
results = sol.Query(
    SimulationPhaseEnum.STSchedule, CollectionEnum.SystemGenerators, 
    '', '', PeriodEnum.FiscalYear, SeriesTypeEnum.Values, 
    make_property_list(
        SystemOutGeneratorsEnum.Generation,
        SystemOutGeneratorsEnum.TotalGenerationCost,
        SystemOutGeneratorsEnum.NetRevenue,
        SystemOutGeneratorsEnum.SRMC
        )
    )
```
In the above, one immediately notices that all enumerations are referenced as
symbols. Those symbols are direct imports from .NET of the following type:
```
clr.AddReference('EEUTILITY')
from EEUTILITY.Enums import *
```
PLEXOS Users are (of course) welcome to script the PLEXOS API in the way they
prefer. Our goal is simply to highlight that the above is a risk that is
specific to PLEXOS version variation which is fairly easy to avoid by taking
the approach demonstrated above.
