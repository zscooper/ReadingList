# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, jounral, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.


## acoustics 
 
* [Arrhenius2000FR - Can stationary bottom split-beam hydroacoustics be used to measure fish swimming speed in situ?](https://github.com/leviner/ReadingList/tree/master/acoustics/Arrhenius2000FR.md) 
     * Arrhenius et al. deployed an upward facing echosounder in two lakes to determine the ability of a split-beam echosounder to track fish, using a stereo-video system to validate the recorded swim speeds. 
* [Foote1987JASA - Fish target strengths for use in echo integrator surveys](https://github.com/leviner/ReadingList/tree/master/acoustics/Foote1987JASA.md) 
     * An investigation into the backscattering cross section, or target strength, of fish, and the methods for in situ determination of TS and relating it to fish length.  Foote proposes a set of regression analyses from in situ measurements for generalized fish families based on available data. 
* [TorgersenKaartvedt2001JMR - In situ swimming behaviour of individual mesopelagic fish studied by split-beam echo target tracking](https://github.com/leviner/ReadingList/tree/master/acoustics/TorgersenKaartvedt2001JMR.md) 
     * One of the earlier papers presenting the use of target tracking of individual fish to evaluate individual behavior.  Used a 38 kHz EK500 for data collection. 
* [Urmy2012JMS - Measuring the vertical distributional variability of pelagic fauna in Monterey Bay](https://github.com/leviner/ReadingList/tree/master/acoustics/Urmy2012JMS.md) 
     * Use of a moored 38kHz echosounder to look at the vertical distribution of backscatter and temporal variability over an 18-month deployment in Monterey Bay, CA, USA. 
* [UrmyHorne2016DSRI - Multi-scale responses of scattering layers to environmental variability in Monterey Bay, California](https://github.com/leviner/ReadingList/tree/master/acoustics/UrmyHorne2016DSRI.md) 
     * Use of a moored 38kHz echosounder to correlate backscatter with oceanographic variability over an 18-month deployment in Monterey Bay, CA, USA.  Same system used in [Urmy et al, 2012, *J. Mar. Sci.*](https://academic.oup.com/icesjms/article/69/2/184/701699). 

## pacificArctic 
 
* [Buckley2016EBF - Variation in the diet of Arctic Cod (Boreogadus saida) in the Pacific Arctic and Bering Sea](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Buckley2016EBF.md) 
     * They look at the summer diet of arctic cod across multiple age classes from opportunistic samples throughout the Chukchi and Bering Sea.  Along a north-south gradient in the ECS, copepods dominate diets at higher latitudes, euphausiids at lower latitudes.  Larger fish have a more diverse diet of larger prey (decapods, fishes).  Arctic cod are highly opportunistic. 
* [CorlettPickart2017PO - The Chukchi slope current](https://github.com/leviner/ReadingList/tree/master/pacificArctic/CorlettPickart2017PO.md) 
     * The authors describe the observation of a westward flow that advects a significant portion of Pacific-origin water, predominantly winter water, westward along the slope, as well as a weaker shelfbreak jet moving shallower water to the east. 
* [DeRobertis2015DSRII - Species and size selectivity of two midwater trawls used in an acoustic survey of the Alaska Arctic](https://github.com/leviner/ReadingList/tree/master/pacificArctic/DeRobertis2015DSRII.md) 
     * De Robertis et al. conducted a trawl selectivity experiment using recapture nets on a modified-Marinovich trawl to asses the species- and size-specific selectivity.  There is significant escapement, even for the most abundant species, and this analysis is required to properly calculate biomass/abundance estimates for juvenile Arctic cod. 
* [Kessel2016PB - Distinct patterns of Arctic cod (Boreogadus saida) presence and absence in a shallow high Arctic embayment, revealed across open-water and ice-covered periods through acoustic telemetry](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Kessel2016PB.md) 
     * The authors use acoustic telemetry (tagging) to investigate the spatial distribution of arctic cod in Resolute Bay in ice free and covered periods, and their presence in relation to environmental changes and predator presence. 
* [Kitamura2017CSR - Seasonal dynamics of zooplankton in the southern Chukchi Sea revealed from acoustic backscattering strength](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Kitamura2017CSR.md) 
     * Use of AZFPs to describe the seasonality of zooplankton biomass, and identify the dominant scatterers in the southern Chukchi Sea, finding a seasonal peak in biomass in autumn and a minimum in early spring, not corresponnding with phytoplankton production.  Zooplpankton communities in the southern Chukchi are largely driven by advection from the Bering. 
* [Laurel2016PB - Temperature-dependent growth and behavior of juvenile Arctic cod (Boreogadus saida) and co-occurring North Pacific gadids](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Laurel2016PB.md) 
     * Laboratory temperature experiments were conducted on gadidae to investigate the importance of temperature on fish growath and survival.  Arctic fishes can grow faster at cooler temperatures, but have a limited range.  Their ability to grow under future climate scenarios is presented. 
* [Loggerwell2015PO - Fish communities across a spectrum of habitats in the western Beaufort Sea and Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Loggerwell2015PO.md) 
     * Synthesized five years of surveys to look at differences in abundance (density) of animals from the lagoon to shelf slope in the Chukchi and Beaufort.  They also looked at icthyoplankton.  Based on Icthyoplankton, they state that the Beaufort Sea shelf is likely a spawning location for Arctic cod. 
* [Quast1974FB - Density distribution of juvenile Arctic cod, Boregogadus saida in the Eastern Chukchi Sea in the fall of 1970](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Quast1974FB.md) 
     * This was the first fisheries survey of Arctic cod in the NE Chukchi (as far as I know), and showed that there were primarily young of the year A. cod, with a depth-dependent density.  Quast also speculates about the origin of the juvenile cod. 
* [Vestfals2018 - Distribution of early life stages of Arctic cod and saffron cod in the Pacific Arctic](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Vestfals2018.md) 
     * Vestfals et al aim to narrow down the potential spawning grounds for arctic and saffron cod based on the physical oceanography and summer distribution.  It contains a good review in the intro of the current literature on early life history. 
* [Woodgate2015OCN - A Synthesis of Year-Round Interdisciplinary Mooring Measurements in the Bering Strait (1990-2014) and the RUSALCA Years (2004-2011)](https://github.com/leviner/ReadingList/tree/master/pacificArctic/Woodgate2015OCN.md) 
     * Overview of the ADCP and other moored sensors deployed from 1990-2014 in the Bering Strait.  Stresses the importance of the Bering Strait as the sole conduit of water into the Arctic from the Pacific.  Near-complete 24 year time series of flow through Bering Strait. 
