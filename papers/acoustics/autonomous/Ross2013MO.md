01/04/19
## Authors:
Ross, Tetjana and Keister, Julie E and Lara-Lopez, Ana
## Title:
On the use of high-frequency broadband sonar to classify biological scattering layers from a cabled observatory in Saanich Inlet, British Columbia
## Keywords:
autonomous, acoustics, moorings, zooplankton, clustering, classification
## Geographic Coverage
Saanich Inlet
## Field Dates:
03/01/2008 - 02/01/2010
## Significance:
Used clustering to reduce the volume and discriminate between species/layers in long-term mooring data via spectral response, normalized spectra, and acoustic color.

## Notes:
While high-frequency acoustics can now be deployed for extended periods, work remains to be done to develop methods for target and layer discrimination and classification for these remote observations, necessary for ecological studies.

Inforation available from a scatterer is frequency dependent, and multi-frequency and broadband approaches increase the data available for identification.  However, these datasets are growing exponentially, and automated methods will be necessary.

Clustering (or blind classification which doesn't require a training set) is well suited for these datasets with sparse biological ground truthing.  It is possible that non-hierarchical classification techniques may be a useful means of the identification of a zooplankton layer in mooring acoustics.

Here, scattering spectra may be used as a descriptor for clustering by providing dimensionality.

Acoustic data were collected from a bottom-moored 855-155kHz echosounder at 100m depth in Saanich Inlet as part of the VENUS observatory, using a 1ms pulse at 1 Hz.

Acoustic Color
- To work with the pulse-compressed dataset, the acoustic data was converted into acoustic color images.
- Sv was thresholded between -40 and -80, which have values of 1 for the color bands
- For each observation, the spectra was mapped onto a 3-color channel.  The Sv value at each frequency across the spectra was multiplied by each of the three color weighting functions.  The values for the entire color channel were summed across the frequency, resulting in a single value for each spectra at each of the 3 bands.
- For the entire time series, 1800 pings (30 mins) were averaged before conversion to acoustic color.

Clustering was done using k-means, where clusters are initially established by nearest mean, then the mean is moved to the centroid of the cluster and the clusters are reestablished until they converged at the same locations.  The number of clusters, k, was one by increasing k until the ratio between the clustered least-squares scatter and the total least-squares scatter were less than 10% (i.e., until variability was not longer significant with additional values of k)

They used forward calculations to predict scattering based on a set of net samples, and show underprediction of Sv compared with observed, likely driven by undersampling (avoidance of larger zooplankton and difficulty retaining/capturing pteropods).  The spectra, however, agree with the net collections, and thus the collections are useful for interpretation of scattering.

Cluster results:
- Three clusters were identified from on-normalized (aka full spectra) targets, with similar slopes and only differentiate based on scattering strength
- The scattering strength dominated the clustering to the point that similar cluster results from simply using the narrow band 120kHz value
- Using the normalized spectra values (normalized to max Sv of scatter), 4 bands were identified
  - 2 that increase with frequency, 1 that was flat across spectra, and one that decreased
- Clustering from acoustic color results in 4 groups
  - 3 with an increasing slope , differentiated by intensity and one that is flat

The absolute difference in Sv drove most of the clustering in non-normalized curves, and instead groups only on intensity.  Many different spectral shapes may be averaged in each cluster, so the mean spectra for the clusters are all similar, and contain no frequency-dependent scattering information (i.e., could be a lot of small or 1 big organism)

Improved differentiation between the groups is achieved by removing the intensity signal and clustering simply based on shape, which allows size of organism to be the distinguishing factor ("A large number of small scatterers can produce the same volume scattering strength as a small number of large scatterers, but they will not have the same spectral shape").  The acoustic color clustering did a better job resolving scattering layers than the normalized spectrum analysis.

Averaging over long periods/many pings will better represent the mix of observations in a layer, comparable with net samples.  Normalized spectra with >2 points are suffiecient to retain the shape of any rayleigh-to-geometric changes, while 2 point would only retain slope.

Over the course of the year, cluster associations were made with more than one potential group, possibly as a consequence of a change in frequency dependence through change in size distribution )animal growth, movement in and out), or species composition.  For example, juvenile euphausiids and pteropods have a similar distribution, so although they may not temporally overlap in situ, they are clustered together and thus the same cluster is applied.  Here, the k-means method cannot distinguish between overlaps in frequency dependence.

Conclusions:
- simplifying the spectra into 3 band color was the most efficient way of distinguishing layers
- normalizing is key to clustering based on response, not intensity
- averaging over larger periods/layers improved consistency of classification within the layers.
- Even with averaging, sometimes clustering would put two distinct groups together or split a single group.  More descriptors (dimensionality) such as depth, time of day will help to sort out organisms with similar size/scatter but different behavior
- Improving bandwidth higher (zoops) or lower (fish) will improve discrimination (get out of the rayleigh region).
- The most effective method may just be to use multi-frequency narrow band sonar since data volume is low but shape can be inferred.
