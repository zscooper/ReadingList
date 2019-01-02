11/05/18
## Authors:
Benoit-Bird, K. J. and Patrick Welch, T. and Waluk, C. M. and Barth, J. A. and Wangen, I. and McGill, P. and Okuda, C. and Hollinger, G. A. and Sato, M. and McCammon, S.
## Title:
Equipping an underwater glider with a new echosounder to explore ocean ecosystems
## Keywords:
autonomous, glider, acoustics, mesopelagic
## Geographic Coverage
Moneterey Bay, CA, USA
## Field Dates:
09/01/16 - 08/01/17
## Significance:
An EK80 (WBT-Mini) was installed on a slocum glider and deployed in Monterey Bay.  This paper documents the instrumentation, installation, and preliminary data from the first deployments.

## Notes:
The ability to measure both biological and physical components for extended periods of time to complement ship-based efforts would provide opportunities to study bio-physical coupling at lower costs.

Mobile autonomous platforms are capable of extended deployments, access remote locations, and cover large areas.  Moorings, profiler floats, surface vehicles, and gliders all serve different purposes with separate restrictions.  Low power sensor development has improved the science capabilities across platforms.

Echosounders provide multi-taxa information, but are power-hungry instruments.  Low power systems typically have data restrictions (single beam, slow ping rate, limited range) relative to ship echosounders.  Here, they outline the EK80 WBT-Mini configuration off the shelf echosounder integrated into a glider-style AUV.

Integration goals included having the glider self-navigate to and from scattering regions of interest.

Simrad began development of an echosounder  based on EK80 electronics that would collect high-quality data through reduced transducer power input, first deployed by De Robertis et al., 2017.  In order to make the instrument usable on smaller autonomous platforms, the overall system size was reduced to only include the echosounder electronics.

A WBT-mini, and 2 (upward and downward facing) 200kHz ES200-7CDK transducers were installed in a 14" glider hull section, mounted to be oriented vertically during the angle of the glider's dive.  The Instrument was operated in EK80 mode.

The echosounder was controlled by an onboard computer (remote connection for upload/download), and onboard processing was possible in order to transmit reduced data.  Real-time position/IMU data was provided from the navigation computer to EK80 and stored on a ping-by-ping basis.

There was significant platform electrical noise, reduced by adding low-pass filter to the power and additional testing was done to extend the usable data range to ~200m.

The system was deployed in a series of tests in 2016 and 2017 off of the Oregon coast, and environmental variables were compared with the backscatter using linear regressions, finding chlorophyll (39%) and depth (36%) explaining the majority of the backscatter.

The noise level observed in the data was lower than that of a typical research vessel while maintaining the advantages, such as split-beam capabilities, high vertical resolution, making it well suited for integration into autonomous platforms.

Main challenges:
- limiting electrical noise: testing in seawater on the platform is critical as it impacts the strength of the electrical signals, and often the best method is empirical testing until data quality is improved.
- data volume: Onboard data processing was used since the telemetry of raw data is simply not feasible with the data volume produced, but data return for decision making is important
- power consumption: echosounders are power-hungry, and should be considered in platform choice

Primary glider advantage is the bio-physical profile collected, including physical and bio-optical sensors sampling in the entire water column.

There is an advantage to synoptic acquisition of multiple data types, both for cost and science.
