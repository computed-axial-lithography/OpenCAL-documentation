Printing Workflow
=================

This page walks through a complete OpenCAL print from start to finish: preparing the print
file, loading resin, running the print, and post-processing the finished part.

.. warning::

   **Resin safety — read before you begin.**

   * Always wear **nitrile gloves** when handling resin or uncured (wet) parts.
   * **Never expose the resin to natural sunlight.** Sunlight (and other strong UV / blue light)
     causes **rapid, uncontrolled curing** that will ruin the resin and can solidify it in its
     container. Keep resin away from windows, work under subdued ambient room light, and keep
     vials **capped** whenever they are not in use.
   * Work in a well-ventilated area and follow the resin's Safety Data Sheet (SDS). See
     :doc:`../materials/overview` for full handling guidance.

Step 1 — Prepare the Print File
-------------------------------

Generate the projection video for your part using :doc:`Tomo <../software/tomo>` (or
:doc:`VAMToolbox <../software/vamtoolbox>` directly). Export it as an ``.mp4`` and name it with
the OpenCAL convention so the printer reads the rotation speed automatically:

.. code-block:: text

   <part_name>_<rpm>rpm.mp4

Then copy the ``.mp4`` onto a USB drive. (See :ref:`naming-convention` for details.)

Step 2 — Load the File onto the Machine
---------------------------------------

#. Insert the USB drive into the Raspberry Pi.
#. On the LCD menu, select **Print from USB** and choose your file
   (see :doc:`Controls & Operation <../software/controls>`).
#. Confirm the **RPM** when prompted.

Step 3 — Prepare and Load the Vial
----------------------------------

.. warning::

   Put on **nitrile gloves** and keep the resin away from sunlight before opening any container.

#. Fill a clean glass vial with the photopolymer resin.
#. **Cap the vial** securely to prevent spills and to limit light and oxygen exposure.
#. Place the capped vial into the machine's rotation stage and make sure it is seated correctly.

Step 4 — Run the Print
----------------------

Start the print from the **Print from USB** menu. The vial rotates while the projector plays the
video, and the part forms volumetrically over the rotation(s). You can monitor progress on the
camera view, and click to stop when the print finishes.

Step 5 — Remove the Part
------------------------

#. When the print is complete, remove the vial from the machine.
#. Wearing gloves, uncap the vial and use **tweezers** to gently lift the cured part out of the
   surrounding uncured resin.
#. Let excess resin drip back into the vial; the remaining uncured resin can be reused (see
   Step 8).

Step 6 — Wash (Post-Process)
----------------------------

Wash the uncured resin off the part using a **Formlabs Form Wash** (or an equivalent solvent
wash). Use the solvent appropriate to your resin, commonly isopropyl alcohol (IPA), and follow
the wash time recommended for your resin.

Step 7 — Post-Cure
------------------

Post-cure the washed part in a **Formlabs Form Cure**, with the part **submerged in water** (or
under **vacuum**). Curing in water or under vacuum excludes oxygen, which would otherwise inhibit
surface curing and leave the part tacky.

Step 8 — Rest Before Reuse
--------------------------

Let the cured part (and any reused resin) **sit for 24 hours before reuse** so the material can
fully stabilize.
