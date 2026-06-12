Controls & Operation
====================

Once the software is installed, the entire printer is operated through the **rotary
encoder** on the LCD display; there is no keyboard or mouse during normal use.

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Input
     - Action
   * - **Rotate**
     - Scroll through menu items, or adjust a value
   * - **Click (press)**
     - Select an item, confirm a value, or exit a mode

Main Menu
---------

On boot, OpenCAL displays the main menu:

.. code-block:: text

   > Print from USB
     Manual Control
     Settings
     Power Options
     About

Each option is described below.

Print from USB
--------------

Lists all ``.mp4`` print files found on the inserted USB drive. Selecting a file:

#. If the filename encodes an RPM (e.g. ``part_9rpm.mp4``), the motor speed is pre-set
   automatically (see :ref:`naming-convention`).
#. An **RPM adjustment screen** appears: rotate to change, click to confirm and start
   the print.
#. While in this menu the projector shows a **black image**; this is intentional, to
   avoid accidentally curing resin while browsing.
#. A **Print Status screen** is shown while the print runs. Click to stop.
#. If **USB video prompt** is enabled (see :ref:`settings-menu`), you are asked whether
   to save the camera recording to USB after stopping.

.. note::

   Files with ``recording`` in the filename are hidden from this list (they are camera
   output files). Avoid using "recording" in your print filenames.

.. tip::

   The camera saves recordings as ``.h264`` (raw H.264 bitstream), not ``.mp4``. To
   convert for playback on a computer:

   .. code-block:: bash

      ffmpeg -i recording.h264 -c copy recording.mp4

Manual Control
--------------

Direct hardware control without running a full print job.

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Item
     - Action
   * - **Turn on LEDs**
     - Turns the LED array on to the default red colour.
   * - **Turn off LEDs**
     - Turns the LED array off.
   * - **Start stepper**
     - Starts the stepper motor rotating (uses the last-set RPM).
   * - **Stop stepper**
     - Stops the stepper motor.
   * - **Capture image**
     - Takes a still image with the camera. Saved to USB with a timestamp filename if a
       USB drive is mounted, otherwise saved locally. The LCD shows "Image Captured" or
       "Image error".

.. _settings-menu:

Settings
--------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Item
     - Action
   * - **Calibration Images**
     - Browse and display calibration images from the ``opencal/utils/calibration/``
       directory on the projector.
   * - **Show Alignment**
     - Displays the cross-strut alignment tool image on the projector. Rotate the encoder
       to shift the image up/down for transverse alignment. Click to return.
   * - **USB video prompt**
     - Toggles whether you are asked to save the camera recording to USB after each print.
       Shows the current state ("USB prompt: On/Off").

Power Options
-------------

.. list-table::
   :header-rows: 1
   :widths: 28 72

   * - Item
     - Action
   * - **Kill GUI**
     - Stops the OpenCAL application without rebooting.
   * - **Restart**
     - Reboots the Raspberry Pi.
   * - **Power Off**
     - Shuts down the Raspberry Pi.

About
-----

Displays an animated scrolling credits screen with the project contributors. The LED
array runs a blue/gold checkerboard animation while credits are shown. Click to exit at
any time.

.. _naming-convention:

Video File Naming Convention
----------------------------

OpenCAL reads the RPM value directly from the video filename. Name your print files as:

.. code-block:: text

   <part_name>_<rpm>rpm.mp4

**Examples:**

* ``cylinder_9rpm.mp4`` → motor set to 9 RPM automatically
* ``part_v2_12rpm.mp4`` → motor set to 12 RPM automatically

If no RPM is found in the filename, the menu opens with the last-used RPM value.

.. note::

   Print files (``.mp4`` videos) are generated from your 3D model using **Tomo** (or
   **VAMToolbox** directly). See :doc:`tomo` and :doc:`vamtoolbox` for how to create them.
