01/06/19
## Authors:
Ehrenberg, J. and Torkelson, T. C.
## Title:
Application of dual-beam and split-beam target tracking in fisheries acoustics
## Keywords:
acoustic, tracking, target strength
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Discussion of dual-beam and split-beam fish tracking techniques and their application for fisheries research.  Appendix contains calculations for error/noise in split-beam angular estimates.

## Notes:
When combined with dual-beam or split-beam systems, the usefulness of target tracking is enhanced.  Initial applications were for the removal of beam-pattern discrepecies in the measurements of backscattering cross section (TS) calculations of targets.  By tracking a single targets across multiple pings, lower variance estimates of TS can be collected.  Angular information can also be used for swim speed, location in the water column, and direction.

Two step process:
- Identification of a single target based on pulse shape criteria.
- Use a series of collected single targets to produce a track, formed sequentially, using information a t=[-n to 0] to inform the expected location at t=1.  If criteria are not met, a new track is begun.

1. Single target average strength measurements
- The conversion of TS to length is made complicated by the ping-to-ping variability in TS estimates of individuals.
- Tracks can be used to isolate the estimates from individual fish by producing a single reduced-variance estimate of average TS for each fish.

The number of detections of a single fish can be maximized by accepting targets for a wide range of beam angles, though too large of an angle can insert a bias since small targets are less likely to be detected further off axis.  The higher SNR, the less bias.

As SNR decreases:
- smaller fish in the edge of the beam will result in echo levels comparable to noise level that will not meet a discrimination threshold, which will produce a biased estimate of higher TS
- Additional noise increases the average level of the signal output, which will also bias the estimates too large
- Noise impacts the beam pattern, though split-beam estimates are less biased due to improved beam-pattern and target location mapping.

At high SNR, variations in the TS estimates are due to randomness of backscattering cross section.  This decreases with a larger beam width due to the increased number of detections for a larger beam.

2. Split-beam tracking
- Angular locations from split-beam improve tracking, and make it possible to sort out between multiple scatterers
- TS estimates are relatively insensitive to added noise
- Can be used from a fixed location to monitor fish passage
