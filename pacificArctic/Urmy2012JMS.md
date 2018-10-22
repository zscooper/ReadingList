10/22/18
## Authors:
Urmy, S. S. and Horne, J. K. and Barbee, D. H.
## Title:
Measuring the vertical distributional variability of pelagic fauna
in Monterey Bay
## Keywords:
acoustics, time series, mooring, observatory, biomass, distribution
## Geographic Coverage
Monterey Bay
## Field Dates:
02/27/2009 - 08/18/2010
## Significance:
Use of a moored 38kHz echosounder to look at the vertical distribution of backscatter and temporal variability over an 18-month deployment in Monterey Bay, CA, USA.

## Notes:
*My interest in this paper is the methods (statistic and visual) used to explore moored echosounder time series data*

"Echometrics" paper.

A bottom-mounted 38 kHz EK60 echosounder was deployed at the DEIMOS node in Monterey Bay to collect water column observations.  

Goal was to characterize the distribution of animals in the water column and how it changes through time, but also develop methods/metrics to do so in a quantitative fashion in order to identify the "dominant modes of variability".

 Metrics were designed to describe the backscatter and the spatial structure and variance of the biology:
 - Density (Sv)
 - Abundance (Sa)
 - Center of biomass
 - Inertia
 - Proportion occupied
 - Evenness
 - Aggregation Index (inverse of Evenness)
 - Number of scattering layers
    - locations where the absolute value of the first derivative of Sv was close to zero (wasn't changing significantly) and the second derivative was negative (so the first derivative was at a peak, not a trough)

A sensitivity analysis for acoustic thresholding, blending, derivative slope, bin height, dilation filer, and by file was done for each metric.

PCA was used to explore the time series vs the metrics.  Considerable collinearity exists between multiple metrics (as expected).

The seasonal cycle of backscatter coincides with the upwelling events of the california current, showin ght lag between zooplankton biomass and primary production.

Fourier power spectra were used for each metric to look at coincidence with 12- and 24-hour cycling, and wavelet analysis for magnitude of temporal cycles over the entire time series.

Concluding hypotheses
* "New" metrics effectively capture the vertical distribution over long periods of time and make the datasets quantifiable on such a scale.
* Objective and simple metrics to explore pattern in high-scope datasets can be used for unsupervised monitoring, indicators of data quality, or baseline/anomaly detectors.
