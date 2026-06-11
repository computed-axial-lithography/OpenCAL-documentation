+++++++++++++++++++++++++
OpenCAL Device Software
+++++++++++++++++++++++++

Overview
========

The OpenCAL device software runs headless on a **Raspberry Pi 5** and orchestrates all printer hardware: the stepper motor, LED array, projector, camera, and 20×4 LCD display. The user interacts entirely through a rotary encoder and the LCD menu — no external monitor is needed during normal operation.

Source code and releases are hosted on GitHub:
`OpenCAL on GitHub <https://github.com/computed-axial-lithography/OpenCAL>`__

----

Installation
============

There are two ways to get the OpenCAL software onto your Raspberry Pi 5. Both produce a bootable SD card image; choose the pathway that fits your needs.

----

Pathway 1: Pre-Built Image (Provided)
--------------------------------------

A curated, fully-tested image is available for download here:

`OpenCAL Pi 5 image (opencal_pi5.img.gz) <https://drive.google.com/file/d/1HBJ7cH8QSTCckkTwJ3i0WToUSsLiP4YX/view?usp=sharing>`__

This image has been validated against the OpenCAL V2 hardware and includes all configuration needed to run out of the box.

**Steps:**

1. Download the ``opencal_pi5.img.gz`` file from the link above.
2. Flash it to a microSD card (16 GB or larger) using `Raspberry Pi Imager <https://www.raspberrypi.com/software/>`__ or `Balena Etcher <https://etcher.balena.io/>`__.
3. Insert the card into the Raspberry Pi 5 and power on.

The system will boot directly into the OpenCAL interface. On first login you will be prompted to change the default password (``OpenCAL1!``).

----

Pathway 2: GitHub Releases (Automated Images)
-----------------------------------------------

**NOTE: These images are in the experimental stage. Hardware and software configuration may differ from the provided image above, and some features may not behave identically.**

Automated images are built by a GitHub Actions workflow and published to the `Releases tab <https://github.com/computed-axial-lithography/OpenCAL/releases>`__ of the OpenCAL repository whenever a new version tag is pushed.

Key characteristics of automated images:

* **Lightweight** — built on a bare-minimum Debian Bookworm base (``bookworm-minbase``) with only the packages strictly required to run OpenCAL. No desktop environment or extra utilities are included.
* **Auto-configured boot sequence** — greetd autologs in as the ``opencal`` user, launches the Wayfire Wayland compositor, and a ``systemd`` user service starts ``python -m opencal`` automatically once the Wayland socket is available.
* **Difference from the provided image** — because the automated image strips the OS to essentials, certain Pi configuration tweaks or additional tools present in the hand-provided image may be absent.

**Steps:**

1. Navigate to the `Releases <https://github.com/computed-axial-lithography/OpenCAL/releases>`__ page and download the latest ``.img.zst`` asset.
2. Flash it to a microSD card using Raspberry Pi Imager or Balena Etcher (same as Pathway 1).
3. Insert the card and power on the Raspberry Pi 5.

----

FAQ / Troubleshooting
======================

This section covers common configuration and debugging questions. Additional Q&A pairs will be added as they arise.

----

**Q: How do I change GPIO pin assignments or I2C addresses to match my hardware?**

All hardware configuration lives in ``opencal/utils/config.json`` inside the OpenCAL repository (located at ``/home/opencal/OpenCAL/opencal/utils/config.json`` on a flashed image). Edit this file to update GPIO pin numbers, the I2C port and address for the LCD, LED count, stepper driver settings, and similar low-level parameters. After saving, restart the service for changes to take effect:

.. code-block:: bash

   sudo systemctl restart opencal.service

----

**Q: How do I adjust OpenCAL defaults such as rotation speed, LED color, or projector print size?**

These values are also stored in ``opencal/utils/config.json``. Key parameters include:

* ``stepper.default_rpm`` — default motor speed in RPM (factory default: ``9``).
* ``led_array.default_color`` — RGB color array for the LED ring during printing (factory default: ``[0, 255, 0]``).
* ``projector.default_print_size`` — initial print size as a percentage of full projector width (factory default: ``100``).

After editing, restart the service as shown above.

----

**Q: How do I view logs or debug software and hardware issues?**

To follow live OpenCAL logs on a running image:

.. code-block:: bash

   journalctl --user -u opencal.service -f

For hardware-specific debugging, the OpenCAL repository ships several standalone test scripts that exercise individual subsystems without starting the full application:

* ``camera_test.py`` — verifies the PiCamera2 is detected and can capture frames.
* ``stepper_test.py`` — runs the stepper motor through basic movements.
* ``lcd_test.py`` — writes test strings to the LCD display.

Run any of these directly with:

.. code-block:: bash

   cd /home/opencal/OpenCAL
   source .venv/bin/activate
   python camera_test.py
