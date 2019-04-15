04/05/19
## Authors:
De Robertis, Alex and Bassett, Christopher and Andersen, Lars Nonboe and Wangen, Ivar and Furnish, Scott and Levine, Michael
## Title:
Amplifier linearity accounts for discrepancies in echo-integration measurements from two widely used echosounders
## Keywords:
echo-integration, linearity, comparison, survey
## Geographic Coverage
Gulf of Alaska, AK
## Field Dates:
02/07/2018 - 03/22/2018
## Significance:
Found that echo-integration measurements of Ek80 are lower than those of EK60, and the range-dependency of the differences suggested a non-linear amplification in one of the systems which was identified within the EK60.

## Notes:
Previous comparison of EK60 and EK80 systems found range and power-dependent differences between the systems attributed to differences in the noise floor, though there were additional differences found in regions of high backscatter.  The goal of this work is to provide an intercomparison during a fisheries survey.

Methods: All (18, 38, 70, 120 kHz) frequencies were operated on both systems (CW pulse) via multiplexer during three winter pollock surveys in the GoA.  Calibration estimates were bootstrapped, and the data were processed separately using Echoview.  They calculate the ratio of EDSUs, bootstrap the estimates accounting for error in the gains.  The ratio was calculated for 10m bins to look at range dependence.  They corrected the power for the amplifier linearity.

Findings:
- EK80 backscatter was consistently lower than that of the EK60.  Across the survey, it was 2-7% discrepancy.
- Calibration uncertainty increased as a function of frequency.
- There is possible over amplification of weak signals via the EK60 system, which would result in lower ek80/ek60 ratios when the systems are calibrated at high power.  This leads to a range dependence.  After applying a correction, the ek80/ek60 ratios are closer to 1 for all EDSUs and regions.

While the results are within the bounds of error found by Macauley et al., 2018, here they specifically identify the systematic differences.  The range dependence may in part be due to the calibration of the systems at high power and close ranges.

They ruled out:
- transducer differences via multiplexing (and the multiplexer itself)
- calibration error by using multiple and accounting for the error between calibrations
- Processing, they compared echoview and EK80/ER60 and the errors were much smaller
- Cross-channel interference, calibration results from individual frequencies and all frequencies pinging are the same

Ways to address non-linearity:
- characterize amplification it in the laboratory, idealy done by the manufacturer
- Extend calibration over the range of powers over the field, though calibrating over a wide dynamic range on the sphere would not help since it is such a strong signal, rather some sort of inline attenuator to reduce the signal would be more practical.
