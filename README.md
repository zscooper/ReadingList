# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/zscooper/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/zscooper/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, journal, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.  Upon reading each paper, a new note file is made, an addition is entered into the `.bib` file, and `readingStats.py` is executed to repopulate the below list and update the figures above.


## Cryosphere 
 

### Permafrost 
 
* [Shietal1996 - Characterization of viable bacteria from siberian permafrost by 16S rDNA sequencing](https://github.com/zscooper/ReadingList/tree/master/papers/Cryosphere/Permafrost/Shietal1996.md) 
     * This study isolated and identified viable bacteria from permafrost using 16S sequencing. 

## Bacterial-genera 
 

### Psychrobacter 
 
* [AyaladelRioetal2010 - The Genome Sequence of *Psychrobacter arcticus* 273-4, a Psychroactive Siberian Permafrost Bacterium, Reveals Mechanisms for Adaptation to Low-Temperature Growth](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Psychrobacter/AyaladelRioetal2010.md) 
     * First genome sequence of a cold-adapted, terrestrial bacterium *Psychrobacter arcticus* 273-4 

### Marinobacter 
 
* [HandleyandLloyd2013 - Biogeochemical implications of the ubiquitous colonization of marine habitats and redox gradients by *Marinobacter* species](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Marinobacter/HandleyandLloyd2013.md) 
     * Major review of *Marinobacter* spp. 
* [Chuaetal2018 - Genomic and physiological characterization and description of *Marinobacter gelidimuriae* sp. nov., a psychrophilic, moderate halophile from Blood Falls, an antarctic subglacial brine](https://github.com/zscooper/ReadingList/tree/master/papers/Bacterial-genera/Marinobacter/Chuaetal2018.md) 
     * Isolation of *Marinobacter gelidimuriae* sp. nov. from Antarctic subglacial brine 

## Metagenomics 
 

### Population Genetics 
 
* [DeLong2002 - Microbial population genomics and ecology](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population Genetics/DeLong2002.md) 
     * This is an early review of culture-independent studies of bacterial diversity/populations in the environment. 
* [Truongnetal2017 - Microbial strain-level population structure and genetic diversity from metagenomes](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population Genetics/Truongnetal2017.md) 
     * Development and application of StrainPhlAn, a tool for differentiating prokaryotic strains from metagenomes 
* [Karstetal - Enabling high-accuracy long-read amplicon sequences using unique molecular identifiers and Nanopore sequencing (pre-print)](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population Genetics/Karstetal.md) 
     * Pre-print of a methods development for producing high accuracy consensus sequences from amplicons generated using Oxford Nanopore MinION sequencing. 
* [WarwickDugdaleetal2019 - Long-read viral metagenomics captures abundant and microdiverse viral populations and their niche-defining genomic islands](https://github.com/zscooper/ReadingList/tree/master/papers/Metagenomics/Population Genetics/WarwickDugdaleetal2019.md) 
     * First use of combined long and short read metaviromics to produce data useful for understanding microdiversity within a viral population 

### Community-assembly 
 
