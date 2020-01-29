01/28/20
## Authors:
Kolmogorov M; Yuan, J; Lin Y; Pevzner, PA
## Title:
Assembly of long, error-prone reads using repeat graphs
## Keywords:
Genomics, assembly, sequencing
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
This paper describes the function of the Flye assembly tool as applied for assembling sequence data produced by long read sequencing techniques.

## Notes:
Flye uses repeat graph construction instead of De Brujin graphs for genome assembly.

These repeats are assembled in an arbitrary and error-riddled path called disjointigs that are then inspected and resolved to solve the proper connections and reduce error.

All repeats in a genome are lined up and then detangled by solving the "Route inspection problem" (aka "Chinese postman problem") to find the shortest path for connecting all sequences

Flye does a good job of making highly contiguous assemblies with minimal error from the sequencing.

Flye assemblies can be polished with Pilon to drive down errors as much as possible (as in the VirION pipeline from the Sullivan Lab)
