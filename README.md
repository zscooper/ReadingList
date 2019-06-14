# ReadingList

I am attempting to keep track of reading journal articles by maintaining a git repository that contains notes and .bib files specific to certain projects/themes/manuscripts.

The goal is that these .md files will be able to be indexed by python based on things like author, keywords, and dates.  An example file, `noteTemplate.md` is available in the current directory.  Indexing can be done with `readingStats.py` which will be updated as needed.

# Paper Folders
![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingCloud.png)![readingTimeline](https://github.com/leviner/ReadingList/blob/master/readingTimeline.png)

Notes (author, year, journal in file header) on readings.  Top of each note document has authors, year, journal, title, and keywords as subsections that can be used to later index through files if needed. Each folder contains a `.bib` file updated with each new `.md` note file for use in compiling references in LaTeX.  Upon reading each paper, a new note file is made, an addition is entered into the `.bib` file, and `readingStats.py` is executed to repopulate the below list and update the figures above.


## example 
 

### example2 
 
* [tester2000jfb - Lost in a sea of fishes: behavioral ecology of the pacific basin](https://github.com/leviner/ReadingList/tree/master/papers/example/example2/tester2000jfb.md) 
     * This is the first documented case of blue-tang (*Paracanthurus hepatus*) and blue whale (*Balaenoptera musculus*) auditory communication. 

## example0 
 

### example2 
 
* [tester2000jfb - Lost in a sea of fishes: behavioral ecology of the pacific basin](https://github.com/leviner/ReadingList/tree/master/papers/example0/example2/tester2000jfb.md) 
     * This is the first documented case of blue-tang (*Paracanthurus hepatus*) and blue whale (*Balaenoptera musculus*) auditory communication. 
