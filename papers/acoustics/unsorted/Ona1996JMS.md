01/03/19
## Authors:
Ona, E. and Mitson, R. B.
## Title:
Acoustic sampling and signal processing near the seabed: The deadzone revisited
## Keywords:
abundance, near-seabed, acoustic, integration
## Geographic Coverage
N/A
## Field Dates:
N/A
## Significance:
Description and equations for acoustic dead zone and sA correction.

## Notes:
Near-seabed estimation has two initial issues:
- fish avoidance
- depth anomaly: discrepancy between the observed and true height of the fish relative to the seabed

The seabed has variable depth and the contour changes on small scales with varying roughness.  Fish echoes are smaller than the bottom echo and will merge when too close.

Fish distribution near the seabed:
- wide beams maximize volume while narrow beams maximize resolution, narrow beams therefore reduce the "depth anomoly"
- Because of the conical shape of the beam, the center axis of the beam will hit the seabed before the edges, thus any fish near the seabed off-axis will not be observed while a fish on-axis will. This shadowing on the flanks is the "acoustic dead zone"
  - This "definite" deadzone was defined by Mitson (1983) as half the wavelength in height off bottom.  This was based off the difficulty of discriminating fish, not integrating/detecting

An echo from a fish is equal to the wavelength of the pulse (c*tau) plus 2x the height of the fish, since the leading edge of the echo will have passed from dorsal to ventral and back to dorsal before returning.

Relative to the seabed, the detection of an infinitely thin fish is possible at height h where h=depth to seabed (1 - cos(angle off axis)).

For the fish echo and bottom echo to form separately, the distance between the two must be > (c*tau/2) + height of the fish

Depth anomoly: the difference in height, relative to the seabed, of targets at the same range from the transducer but at different off-axis angles.  Since the wavefront is spherical, targets close to axis will be encountered first by the beam, seeming closer.  Therefore targets that are encountered at the same time may not be at the same depth (those away from the axis may be shallower).  The wider the beam, the greater the anomaly.

The "final cap" of the samplng volume, where the axis of the beam encounters the seabed, can be determined to describe the limitations of detection near the seabed.  The Acoustic dead zone is the inverse of this cap, where fish can no longer be detected by the echosounder from the point of contact on axis to the edge of the beam in all directions.  This can be quantified in volume as:

ADZ  = (4pi/3)depth^3 * (.5(1-cos(half beam angle))(cos(.5*half beam angle)/cos(half beam angle))-1)

It is equal to the volume defined by the "cap"

Three setting define the deadzone of the echo integration:
- Bottom discrimination level: The amplitude at which the bottom is detected (seabed discrimination/detection)
- Backstep from the seabed: the necessary removal of the entire bottom signal (bottom exclusion line)
- Threshold for signal: Integration Threshold

Total deadzone
- The acoustic deadzone, or area unsampled from the instant the on-axis beam hits the seabed
- The backstep zone, the area excluded above the seafloor within the beam
- Partial integration zone, where only a portion of the echo is detected

This volume can be determined as a function of equivalent beam angles, and the equiavlent lost height off seafloor can be calculated as a function of the effective sampling volume (reference volume) and equivalent lost volume.  This reaches an asymptote as a function of half-beam angle and depth as a function of integration angle

Partial integration zone
- In the pelagic, energy lost in the deepest layers is compensated by energy from the upper portion of the same layer.  Near the seabed, that's not possible since fish detection stops.  for some distance above the backstep (exclusion) zone, echoes are only partially integrated
- The closer a fish is the the range of the backstep, the less fully integrated it is since some portion of it's signal vertically will be cut off.  Assuming random distribution, about 50% of the signal energy is lost.

The accuracy of the IDZ correction depends on the vertical distribution of the fish.  If fish are spread relatively evenly vertically within near-seabed layers, the IDZ will be more accurate.
