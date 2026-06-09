++++++++++++++++++++++++++++++++++++
VAMToolbox (Creating Projections)
++++++++++++++++++++++++++++++++++++

Overview
========

Computed Axial Lithography requires a precisely computed set of light projections — a *sinogram* — derived from the 3D geometry of the part to be printed. **VAMToolbox** is the open-source Python package that performs this computation, converting a 3D model into the projection video that the OpenCAL projector plays back during a print.

* `VAMToolbox on GitHub <https://github.com/computed-axial-lithography/VAMToolbox>`__
* `VAMToolbox Documentation (ReadTheDocs) <https://vamtoolbox.readthedocs.io>`__

----

Workflow Overview
=================

The general pipeline for preparing a print file is:

1. **Design your part** — create or obtain a 3D model of the object you want to print, exported as an STL file.

2. **Compute projections with VAMToolbox** — VAMToolbox takes the STL geometry and performs a tomographic optimization to determine the set of angular projections that will deliver the correct cumulative light dose to each voxel of the resin volume. This step encodes the 3D geometry into a sequence of 2D images, one per angular position of the vial.

3. **Export as video** — the computed projections are compiled into an ``.mp4`` video file. Each frame of the video corresponds to one angular position, and the video is played at a frame rate synchronized to the motor's rotation speed.

4. **Transfer to USB** — copy the ``.mp4`` file to a USB storage device.

5. **Print** — insert the USB drive into the Raspberry Pi, navigate to *Print from USB* on the OpenCAL LCD menu, select the file, confirm the rotation speed (RPM), and start the print.

----

**NOTE:** The VAMToolbox user interface is under active development. For current installation instructions and usage details, refer to the `VAMToolbox ReadTheDocs <https://vamtoolbox.readthedocs.io>`__ documentation, which is kept up to date with each release.
