# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/zscooper/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/zscooper/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, journal, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.  Upon reading each paper, a new note file is made, an addition is entered into the `.bib` file, and `readingStats.py` is executed to repopulate the below list and update the figures above.


## Lab_methods 
 

## Cryosphere 
 

### Sea_ice 
 
* [NiemiandMichel2015 - Temporal and spatial variability in sea-ice carbon:nitrogen ratios on Canadian Arctic shelves](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Sea_ice/NiemiandMichel2015.md) 
     * This study conducts a temporal and spatial survey of C:N ratios in sea ice. 

### Permafrost 
 
* [Shietal1996 - Characterization of viable bacteria from siberian permafrost by 16S rDNA sequencing](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Permafrost/Shietal1996.md) 
     * This study isolated and identified viable bacteria from permafrost using 16S sequencing. 
* [Katayamaetal2007 - Phylogenetic Analysis of Bacteria Preserved in a Permafrost Ice Wedge for 25,000 Years](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Permafrost/Katayamaetal2007.md) 
     * Phylogenetic analysis of microbes preserved in an ice wedge for 25,000 years 
* [Lizukaetal2019 - Ion concentrations in ice wedges: An innovative approach to reconstruct past climate variability](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Permafrost/Lizukaetal2019.md) 
     * This study investigates ionic composition of the Barrow Ice Wedge System (massive ice in my paper) as a proxy for paleoclimate and geography records 

### Cold_brines 
 
* [Bakermans2015 - Extreme environments as model systems for the study of microbial evolution](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Cold_brines/Bakermans2015.md) 
     * This is a book chapter Life in Extreme Environments (ed. Dirk Wagner) discussing the study of microbial evolution in extreme environments. 

## Bacterial-genera 
 

### Psychrobacter 
 
* [Bowman2006 - The genus *Psychrobacter*](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Psychrobacter/Bowman2006.md) 
     * This book chapter discusses the understanding of the dominant phenotypes associated with the genus *Psychrobacter* as of 2006. 
* [AyaladelRioetal2010 - The Genome Sequence of *Psychrobacter arcticus* 273-4, a Psychroactive Siberian Permafrost Bacterium, Reveals Mechanisms for Adaptation to Low-Temperature Growth](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Psychrobacter/AyaladelRioetal2010.md) 
     * First genome sequence of a cold-adapted, terrestrial bacterium *Psychrobacter arcticus* 273-4 

### Marinobacter 
 
* [HandleyandLloyd2013 - Biogeochemical implications of the ubiquitous colonization of marine habitats and redox gradients by *Marinobacter* species](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Marinobacter/HandleyandLloyd2013.md) 
     * Major review of *Marinobacter* spp. 
* [Chuaetal2018 - Genomic and physiological characterization and description of *Marinobacter gelidimuriae* sp. nov., a psychrophilic, moderate halophile from Blood Falls, an antarctic subglacial brine](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Marinobacter/Chuaetal2018.md) 
     * Isolation of *Marinobacter gelidimuriae* sp. nov. from Antarctic subglacial brine 

## Metagenomics 
 

### Methods 
 
* [McMurdieandHolmes2014 - Waste Not, Want Not: Why Rarefying Microbiome Data Is Inadmissible](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Methods/McMurdieandHolmes2014.md) 
     * This paper refutes the common practice of rarefying compositional amplicon data and suggests a more appropriate method for comparing amplicon data across samples. 
* [Glooretal2017 - Microbiome Datasets Are Compositional: And This Is Not Optional](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Methods/Glooretal2017.md) 
     * This paper reviews the issues and approaches to dealing with compositional data. 
* [Falush2016 - Microbial GWAS coming of age](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Methods/Falush2016.md) 
     * This is a Nature News and Reviews article on GWAS for bacteria, an uncommon practice. 
* [TsilimigrasandFodor2016 - Compositional data analysis of the microbiome: fundamentals, tools, and challenges](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Methods/TsilimigrasandFodor2016.md) 
     * This is a minireview of compositional data analyses. 

### Community_assembly 
 

### Population_genetics 
 
* [DeLong2002 - Microbial population genomics and ecology](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/DeLong2002.md) 
     * This is an early review of culture-independent studies of bacterial diversity/populations in the environment. 
* [Greenbaumetal2016 - Inference and Analysis of Population Structure Using Genetic Data and Network Theory](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/Greenbaumetal2016.md) 
     * This paper describes a method for analyzing population structure using network analyses based on distance-based clustering. 
* [Truongnetal2017 - Microbial strain-level population structure and genetic diversity from metagenomes](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/Truongnetal2017.md) 
     * Development and application of StrainPhlAn, a tool for differentiating prokaryotic strains from metagenomes 
* [Karstetal - Enabling high-accuracy long-read amplicon sequences using unique molecular identifiers and Nanopore sequencing (pre-print)](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/Karstetal.md) 
     * Pre-print of a methods development for producing high accuracy consensus sequences from amplicons generated using Oxford Nanopore MinION sequencing. 
* [Andersonetal2017 - Genomic variation in microbial populations inhabiting the marine subseafloor at deep-sea hydrothermal vents](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/Andersonetal2017.md) 
     * This study explores evolution in hydrothermal vent microbial populations using population genetics to investigate genomic variation in MAGs. 
* [WarwickDugdaleetal2019 - Long-read viral metagenomics captures abundant and microdiverse viral populations and their niche-defining genomic islands](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/WarwickDugdaleetal2019.md) 
     * First use of combined long and short read metaviromics to produce data useful for understanding microdiversity within a viral population 
* [CorderoandPolz2014 - Explaining microbial genomic diversity in light of evolutionary ecology](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population_genetics/CorderoandPolz2014.md) 
     * This review discusses how the frequency of a gene present in a population can result from ecological and evolutionary dynamics. 
