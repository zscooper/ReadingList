# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, journal, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.  Upon reading each paper, a new note file is made, an addition is entered into the `.bib` file, and `readingStats.py` is executed to repopulate the below list and update the figures above.


## acoustics 
 

### autonomous 
 
* [Benoit-Bird2018LOM - Equipping an underwater glider with a new echosounder to explore ocean ecosystems](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Benoit-Bird2018LOM.md) 
     * An EK80 (WBT-Mini) was installed on a slocum glider and deployed in Monterey Bay.  This paper documents the instrumentation, installation, and preliminary data from the first deployments. 
* [DeRobertis2018InPrep - Comparison of acoustic backscatter measurements from unmanned sailing vehicles and a noise-reduced research vessel](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/DeRobertis2018InPrep.md) 
     * Currently in preparation manuscript on the 2016 Saildrone deployment in the Bering Sea, investigating vessel avoidance during opportunistic and follow-the-leader ship-saildrone comparisons. 
* [ODriscoll2018AS - Acoustic deployments reveal Antarctic silverfish under ice in the Ross Sea](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/ODriscoll2018AS.md) 
     * This is a proof of concept study using a moored echosounder (ASL AZFP) and discrete observations from ships (acoustic and optical) to determine the abundance and spawning grounds of Antarctic silverfish. 
* [Ross2013MO - On the use of high-frequency broadband sonar to classify biological scattering layers from a cabled observatory in Saanich Inlet, British Columbia](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Ross2013MO.md) 
     * Used clustering to reduce the volume and discriminate between species/layers in long-term mooring data via spectral response, normalized spectra, and acoustic color. 
* [Urmy2012JMS - Measuring the vertical distributional variability of pelagic fauna in Monterey Bay](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/Urmy2012JMS.md) 
     * Use of a moored 38kHz echosounder to look at the vertical distribution of backscatter and temporal variability over an 18-month deployment in Monterey Bay, CA, USA. 
* [UrmyHorne2016DSRI - Multi-scale responses of scattering layers to environmental variability in Monterey Bay, California](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/autonomous/UrmyHorne2016DSRI.md) 
     * Use of a moored 38kHz echosounder to correlate backscatter with oceanographic variability over an 18-month deployment in Monterey Bay, CA, USA.  Same system used in [Urmy et al, 2012, *J. Mar. Sci.*](https://academic.oup.com/icesjms/article/69/2/184/701699). 

### targets 
 
* [Arrhenius2000FR - Can stationary bottom split-beam hydroacoustics be used to measure fish swimming speed in situ?](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Arrhenius2000FR.md) 
     * Arrhenius et al. deployed an upward facing echosounder in two lakes to determine the ability of a split-beam echosounder to track fish, using a stereo-video system to validate the recorded swim speeds. 
* [Brede1990IMR - Target tracking with a split-beam echo sounder](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Brede1990IMR.md) 
     * Demonstration of the ability to track targets and the ability to determine target strength and directivity in the beam. 
* [EhrenbergTorkelson1996JMS - Application of dual-beam and split-beam target tracking in fisheries acoustics](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/EhrenbergTorkelson1996JMS.md) 
     * Discussion of dual-beam and split-beam fish tracking techniques and their application for fisheries research.  Appendix contains calculations for error/noise in split-beam angular estimates. 
* [Foote1987JASA - Fish target strengths for use in echo integrator surveys](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/Foote1987JASA.md) 
     * An investigation into the backscattering cross section, or target strength, of fish, and the methods for in situ determination of TS and relating it to fish length.  Foote proposes a set of regression analyses from in situ measurements for generalized fish families based on available data. 
* [TorgersenKaartvedt2001JMR - In situ swimming behaviour of individual mesopelagic fish studied by split-beam echo target tracking](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/targets/TorgersenKaartvedt2001JMR.md) 
     * One of the earlier papers presenting the use of target tracking of individual fish to evaluate individual behavior.  Used a 38 kHz EK500 for data collection. 

### unsorted 
 
* [Ona1996JMS - Acoustic sampling and signal processing near the seabed: The deadzone revisited](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/Ona1996JMS.md) 
     * Description and equations for acoustic dead zone and sA correction. 
* [Rose1995JMS - Cod (Gadus morhua L.) migration speeds and transport relative to currents on the north-east Newfoundland Shelf](https://github.com/leviner/ReadingList/tree/master/papers/acoustics/unsorted/Rose1995JMS.md) 
     * Observations of cod migration from spawning to feeding grounds over 3 years using acoustic detection of shoal centroid.  Observations indicate fish use active behavior to remain within the migration route. 

## pacificArctic 
 

### circulation 
 
* [CorlettPickart2017PO - The Chukchi slope current](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/CorlettPickart2017PO.md) 
     * The authors describe the observation of a westward flow that advects a significant portion of Pacific-origin water, predominantly winter water, westward along the slope, as well as a weaker shelfbreak jet moving shallower water to the east. 
* [Danielson2017DSRII - A comparison between late summer 2012 and 2013 water masses, macronutrients, and phytoplankton standing crops in the northern Bering and Chukchi Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Danielson2017DSRII.md) 
     * This paper presents an overview of the physical, chemical, and phytoplankton observations as they relate to winds, flow, and ice conditions as observed during the 2012 and 2013 Arctic EIS program.  First set of "physics to fish" observations covering the whole region. 
* [Gong2015DSRII - Summertime circulation in the eastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Gong2015DSRII.md) 
     * Description of the water masses and transport across the Chukchi as observed in late-summer, focussed on the flow from Bering Strait to Barrow canyon and the implications on the Arctic basin. 
* [Gong2016DSRII - Early summer water mass transformation in the eastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Gong2016DSRII.md) 
     * Detection of a dense Chukchi Sea Water and the description of possible sources due to formation relating tot he modification of water masses as they are transported across the NE Chukchi Shelf via observation during early summer. 
* [Martini2016JGRO - Dependence of subsurface chlorophyll on seasonal water masses in the Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Martini2016JGRO.md) 
     * Mapping of the subsurface chlorophyll maximum in the NE Chukchi Sea in late-summer, and the variability in nutrients and chlorophyll with hydrography and meltwater/summer water fronts.  They show that SCM depth in late summer is sensitive to seasonal changes in hydrography. 
* [Stabeno2018JGRO - Flow Patterns in the Eastern Chukchi Sea: 2010–2015](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Stabeno2018JGRO.md) 
     * A synthesis of mooring, drifter, model, and satellite observations of the flow and physical oceanography in the NE Chukchi Sea. 
* [Weingartner1997AFS - A review of the Physical Oceanography of the Northeastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Weingartner1997AFS.md) 
     * A review of the physical oceanography published in 'Fish Ecology in Arctic North America', AFS symposium proceedings.  Outlines the physical oceanography during the ice-free season in the NE Chukchi. 
* [Woodgate2005DSRII - A year in the physical oceanography of the Chukchi Sea: Moored measurements from autumn 1990-1991](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2005DSRII.md) 
     * Mooring data from a 1-year deployment of CTDs and ADCPs across US and Russian waters of the Chukchi Shelf, to present the seasonality and flow across the entire Chukchi Sea over 1 year. 
* [Woodgate2012GRL - Observed increases in Bering Strait oceanic fluxes from the Pacific to the Arctic from 2001 to 2011 and their impacts on the Arctic Ocean water column](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2012GRL.md) 
     * ## Notes: 
* [Woodgate2015OCN - A Synthesis of Year-Round Interdisciplinary Mooring Measurements in the Bering Strait (1990-2014) and the RUSALCA Years (2004-2011)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/circulation/Woodgate2015OCN.md) 
     * Overview of the ADCP and other moored sensors deployed from 1990-2014 in the Bering Strait.  Stresses the importance of the Bering Strait as the sole conduit of water into the Arctic from the Pacific.  Near-complete 24 year time series of flow through Bering Strait. 

### fishes 
 
* [Aronovich1975AC - Egg incubation and larval rearing of navaga (Eleginus navaga Pall.), polar cod (Boreogadus saida lepechin) and arctic flounder (Liopsetta glacialis Pall.) in the laboratory](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Aronovich1975AC.md) 
     * Early description of Arctic cod egg and larval stages through incubation experiments, with developmental timing and growth rates 
* [Benoit2008JGRO - Hydroacoustic detection of large winter aggregations of Arctic cod (Boreogadus saida) at depth in ice-covered Franklin Bay (Beaufort Sea)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Benoit2008JGRO.md) 
     * This study describes the presence and dispersal of a large, dense aggregation of Arctic cod observed overwinter in Franklin Bay, and aims to explore the physical and behavioral mechanisms responsible for their retention in deep water. 
* [Benoit2014PB - Pre-winter distribution and habitat characteristics of polar cod (Boreogadus saida) in southeastern Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Benoit2014PB.md) 
     * Investigate the distribution of age-0 and age-1+ aggregations of Arctic cod in the Canadian Beaufort in early Winter. 
* [BouchardFortier2011PO - Circum-arctic comparison of the hatching season of polar cod Boreogadus saida: A test of the freshwater winter refuge hypothesis](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/BouchardFortier2011PO.md) 
     * This paper looks at the hatch date frequency distribution in six regions of differing freshwater input, and find evidence to support the winter refuge hypothesis that Arctic cod in lower saline environments have a greater pre-winter size due to faster development and earlier hatching. 
* [Bradstreet1986DFO - Aspects of the Biology of Arctic Cod ( Boreogadus saida ) and its Importance in Arctic Marine Food Chains](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Bradstreet1986DFO.md) 
     * Technical report on the importance of Arctic cod to the Canadian Arctic ecosystem, covers aspects of distribution, physiology, and ecological significance across North American waters.  Includes review of much of the work done prior to the 1980s, and a focus on ringed seal predation of A. cod. 
* [Buckley2016EBF - Variation in the diet of Arctic Cod (Boreogadus saida) in the Pacific Arctic and Bering Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Buckley2016EBF.md) 
     * They look at the summer diet of arctic cod across multiple age classes from opportunistic samples throughout the Chukchi and Bering Sea.  Along a north-south gradient in the ECS, copepods dominate diets at higher latitudes, euphausiids at lower latitudes.  Larger fish have a more diverse diet of larger prey (decapods, fishes).  Arctic cod are highly opportunistic. 
* [Copeman2017MEPS - Temperature impacts on lipid allocation among juvenile gadid species at the Pacific Arctic-Boreal interface: An experimental laboratory approach](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Copeman2017MEPS.md) 
     * Measured temperature dependence of lipid accumulation in juvenile Arctic cod, Saffron cod, Pacific cod, and pollock. 
* [Craig1982CJFAS - Ecological Studies of Arctic Cod (Boreogadus saida) in Beaufort Sea Coastal Waters, Alaska](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Craig1982CJFAS.md) 
     * One of the earlier papers investigating the life history of Arctic cod from samples collected off the north slope of Alaska both nearshore and on the shelf break.  Arctic cod were found to be present in the coastal Beaufort year round. 
* [Crawford2016PB - Occurrence of a gelatinous predator (Cyanea capillata) may affect the distribution of Boreogadus saida, a key Arctic prey fish species](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Crawford2016PB.md) 
     * This paper presents evidence of jellyfish avoidance by Arctic cod in a shallow bay of the Canadian Arctic Archipelago.  The authors describe observations of partitioning which they attribute primarily to avoidance. 
* [DeRobertis2015DSRIIa - Species and size selectivity of two midwater trawls used in an acoustic survey of the Alaska Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/DeRobertis2015DSRIIa.md) 
     * De Robertis et al. conducted a trawl selectivity experiment using recapture nets on a modified-Marinovich trawl to asses the species- and size-specific selectivity.  There is significant escapement, even for the most abundant species, and this analysis is required to properly calculate biomass/abundance estimates for juvenile Arctic cod. 
* [DeRobertis2017DSRIIb - Abundance and distribution of Arctic cod (Boreogadus saida) and other pelagic fishes over the U.S. Continental Shelf of the Northern Bering and Chukchi Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/DeRobertis2017DSRIIb.md) 
     * Two broad-scale baseline acoustic-trawl surveys were conducted in 2012 and 2013. 
* [Drost2016JEB - Acclimation potential of Arctic cod (Boreogadus saida) from the rapidly warming Arctic Ocean](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Drost2016JEB.md) 
     * Laboratory observations of thermal tolerance via measurements of respiration and heart rate to acute changes across various acclimation temperatures.  Shows ability to acclimate to temperatures through changes in aerobic ability and scope after 1-month of exposure. 
* [Geoffroy2011PB - The aggregation of polar cod (Boreogadus saida) in the deep Atlantic layer of ice-covered Amundsen Gulf (Beaufort Sea) in winter](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Geoffroy2011PB.md) 
     * Overwinter observations of vertical distribution of Arctic cod aggregations in the Canadian Beaufort, showing changes in depth distribution with water, light, and prey conditions. 
* [Geoffroy2016PB - Vertical segregation of age-0 and age-1+ polar cod (Boreogadus saida) over the annual cycle in the Canadian Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Geoffroy2016PB.md) 
     * The authors observed two distinct layers of arctic cod, an epipelagic layer of age-0 fish which forms in spring, begins DVM in summer, and settles to depth in late fall, and a mesopelagic layer of age-1+ fish.  They used TS to estimate length at depth to show a stratification and seasonal vaibility in the two layers, as well as estimate biomass. 
* [Kessel2016PB - Distinct patterns of Arctic cod (Boreogadus saida) presence and absence in a shallow high Arctic embayment, revealed across open-water and ice-covered periods through acoustic telemetry](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Kessel2016PB.md) 
     * The authors use acoustic telemetry (tagging) to investigate the spatial distribution of arctic cod in Resolute Bay in ice free and covered periods, and their presence in relation to environmental changes and predator presence. 
* [Laurel2016PB - Temperature-dependent growth and behavior of juvenile Arctic cod (Boreogadus saida) and co-occurring North Pacific gadids](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Laurel2016PB.md) 
     * Laboratory temperature experiments were conducted on gadidae to investigate the importance of temperature on fish growath and survival.  Arctic fishes can grow faster at cooler temperatures, but have a limited range.  Their ability to grow under future climate scenarios is presented. 
* [Loggerwell2015PO - Fish communities across a spectrum of habitats in the western Beaufort Sea and Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Loggerwell2015PO.md) 
     * Synthesized five years of surveys to look at differences in abundance (density) of animals from the lagoon to shelf slope in the Chukchi and Beaufort.  They also looked at icthyoplankton.  Based on Icthyoplankton, they state that the Beaufort Sea shelf is likely a spawning location for Arctic cod. 
* [Marsh2017DSRII - Ontogenetic, spatial and temporal variation in trophic level and diet of Chukchi Sea fishes](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Marsh2017DSRII.md) 
     * Examined the isoscapes and relation to water masses in the Chukchi Sea, looking for diet niches of pelagic fishes, particularly Arctic cod. 
* [Mueter2016PB - The ecology of gadid fishes in the circumpolar Arctic with a special emphasis on the polar cod (Boreogadus saida)](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Mueter2016PB.md) 
     * This is the introduction paper for the 2016 Polar Biology special issue that came out of the 2014 ESSAS annual meeting, focused on Arctic cod and their role in Arctic food webs. 
* [Parker-Stetter2011PB - Distribution of polar cod and age-0 fish in the U.S. Beaufort Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Parker-Stetter2011PB.md) 
     * Investigation of the offshore distribution of Arctic cod in the U.S. Beaufort Sea to examine the density and water property associations. 
* [Ponomarenko2000JI - Eggs, larvae, and juveniles of polar cod Boreogadus saida in the Barents, Kara, and White Seas](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Ponomarenko2000JI.md) 
     * Observations of eggs, larvae, and juveniles from 14 years of sampling Polar cod.  The early life cycle is described, and differences in specimen and development are attributed environmental conditions. 
* [Quast1974FB - Density distribution of juvenile Arctic cod, Boregogadus saida in the Eastern Chukchi Sea in the fall of 1970](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Quast1974FB.md) 
     * This was the first fisheries survey of Arctic cod in the NE Chukchi (as far as I know), and showed that there were primarily young of the year A. cod, with a depth-dependent density.  Quast also speculates about the origin of the juvenile cod. 
* [Vestfals2018 - Distribution of early life stages of Arctic cod and saffron cod in the Pacific Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Vestfals2018.md) 
     * Vestfals et al aim to narrow down the potential spawning grounds for arctic and saffron cod based on the physical oceanography and summer distribution.  It contains a good review in the intro of the current literature on early life history. 
* [Whitehouse2014PB - A trophic mass balance model of the eastern Chukchi Sea with comparisons to other high-latitude systems](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Whitehouse2014PB.md) 
     * This study aimed to describe the trophic structure and function of the Chukchi Sea foodweb using an ecopath model, representing just one of many possible mass-balance solutions.  Fish estimates were taken from beam trawl samples of the Eastern Chukchi shelf. 
* [Wyllie-Echeverria1997AFS - Water masses and transport of age-0 Arctic cod and age-0 Bering flounder into the northeastern Chukchi Sea](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/fishes/Wyllie-Echeverria1997AFS.md) 
     * Describe the abundance and distribution of larval bering flounder in late summer from 1989-1991 in relation to the sampled water masses.  Included collection of age-0 Arctic cod throughout the NE Chukchi to investigate water mass associations. 

### ice 
 
* [Duarte2012NCC - Abrupt climate change in the Arctic](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/ice/Duarte2012NCC.md) 
     * Discussion of the causes and impacts of climate change in the Arctic. 

### zooplankton 
 
* [Ashjian2017DSRII - Mesozooplankton abundance and distribution in association with hydrography on Hanna Shoal, NE Chukchi Sea, during August 2012 and 2013](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/zooplankton/Ashjian2017DSRII.md) 
     * Description of the late-summer zooplankton community composition at Hannah Shoal during August of 2012 and 2013, focusing on copepods and euphausiids of interest for bowhead whales. 
* [Day2013CSR - The offshore northeastern Chukchi Sea, Alaska: A complex high-latitude ecosystem](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/zooplankton/Day2013CSR.md) 
     * Synthesis of the findings from the Chukchi Sea Environmental Studies Program from 2008-2010 at three regions of oil exploration interest near Hanna Shoal. 
* [Kitamura2017CSR - Seasonal dynamics of zooplankton in the southern Chukchi Sea revealed from acoustic backscattering strength](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/zooplankton/Kitamura2017CSR.md) 
     * Use of AZFPs to describe the seasonality of zooplankton biomass, and identify the dominant scatterers in the southern Chukchi Sea, finding a seasonal peak in biomass in autumn and a minimum in early spring, not corresponnding with phytoplankton production.  Zooplpankton communities in the southern Chukchi are largely driven by advection from the Bering. 
* [PinchukEisner2017DSRII - Spatial heterogeneity in zooplankton summer distribution in the eastern Chukchi Sea in 2012–2013 as a result of large-scale interactions of water masses](https://github.com/leviner/ReadingList/tree/master/papers/pacificArctic/zooplankton/PinchukEisner2017DSRII.md) 
     * Describe the differences in zooplankton distribution (focussed on Calanus species of copepods) between 2012 and 2013 as part of the Arctic EIS study.  Zooplankton distribution is wind-driven and a balance between melt water and northward advection of warm Pacific water. 
