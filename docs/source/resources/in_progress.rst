In-Progress
===========

This page tracks parts of OpenCAL that are **actively being worked on but are not yet fully
functional**. They are documented here so the community knows what is still in flux and where
help is welcome.

Have experience, ideas, or a fix? Reach out on the
`OpenCAL Discord <https://discord.com/invite/patduYdnSN>`__ — contributions are very welcome.

Cheaper Motor Controller (TMC5160T)
-----------------------------------

The current OpenCAL build drives the stepper motor with a **Pololu Tic T249**. We would like to
support **cheaper motor controllers** wherever possible to lower the overall build cost.

One candidate we are evaluating is the **TMC5160T**:

* `TMC5160T stepper motor driver (Amazon) <https://www.amazon.com/dp/B0B8HZXWPP>`__

So far we have **not been able to get it working reliably**, so it is not yet part of the
official build. If you have experience running the TMC5160T — or another low-cost driver —
dependably with OpenCAL, we would love to hear from you.

Large Vial (Screw-On)
---------------------

The large, **screw-on glass vial** assembly is still being finalized and is **not yet fully
working**. Everything related to the large vial is considered in-progress for now, and the build
instructions for it will be moved into this section as the design is sorted out.

In the meantime, use the small vial for printing. (The Large Vial subassembly in the
:doc:`Rotational Element guide <../step_by_step/rotational_element_stepbystep>` is still a work in
progress.)

Vial Light-Protection Covers
----------------------------

Photopolymer resin cures on exposure to stray light (see the resin-handling warnings in the
:doc:`Materials overview <../materials/overview>`). We are working on **covers for the vials** to
shield them from ambient and stray light **when they are not actively being printed** — protecting
the resin between prints and during storage. A reliable, easy-to-use cover design is still in
progress.

Centrifugal Spinning (CentrifuCAL)
----------------------------------

A centrifugal spinning approach — **CentrifuCAL** — is being explored to help counteract sinking
or floating of the part in low-viscosity resin. It is a **hand-cranked, planetary-gear spinner**
that holds and rotates the vial.

The design is **not yet finalized**, so CentrifuCAL is not part of the official build. An early
prototype and its assembly steps are recorded below for reference and to invite contributions.

.. note::

   The steps below describe an early prototype. Step images are not yet included — they will be
   added as the design is finalized.

Tools
~~~~~

* Soldering iron (for heat-set inserts)
* 3D printer — PETG capable, minimum bed size 256 × 256 mm (prototype printed on a Prusa)
* 3 mm hex key
* Superglue
* Scissors / box cutter

Parts
~~~~~

**3D-printed parts** (print quantity in parentheses):

* Lower Base (3 parts), Upper Base (3 parts), Lid (3 parts)
* Vial Holder, Spinner, Tab
* Sun Gear, Ring Gear, Planet Gear (×3)
* Gearbox Crank Top, Gearbox Cover, Gearbox Bottom, Crank Handle
* Door, Door Handle, Handle (×2), Handle Cap (×4)
* Hinge Bottom, Hinge Top, Hinge Pin
* Foot (×4), Drain Plug

**Other materials:**

* 2 × polycarbonate sheets, cut to 145 × 135 mm
* 28 mm bearing
* M3 heat-set inserts
* M3 bolts: M3×6, M3×10, M3×25, M3×40, M3×50

(See the :doc:`BOM <../engineering_documentation/bom>` for quantities and sourcing.)

Assembly (prototype)
~~~~~~~~~~~~~~~~~~~~~~

#. 3D print all parts.
#. Cut 2 polycarbonate sheets to **145 × 135 mm**.
#. Place the polycarbonate sheets into their respective slots in the **Lower Base**.
#. Using the soldering iron, place **3× M3 heat-set inserts** into the holes on the top of the Lower Base.
#. Place the remaining M3 heat-set inserts: **7 on the Lid** and **4 on the Upper Base**.
#. Assemble the Lower and Upper Base in thirds, placing the Upper Base onto the polycarbonate sheets and fastening with an **M3×40 bolt**.
#. Fasten the three pieces of the Lower Base, Upper Base, and Lid together with superglue.
#. Place the final **3× M3 heat-set inserts** into the holes on the Door.
#. On the Lower Base, press-fit a **28 mm bearing** into the middle section.
#. Superglue the **Vial Holder** to the **Spinner**.
#. Secure the **Tab** to the Vial Holder with an **M3×6 bolt**.
#. Place the Vial Holder and Spinner onto the bearing in the Lower Base.
#. Affix the Lid and handles with **4× M3×50 bolts**.
#. Affix the **Ring Gear** with **4× M3×25 bolts**.
#. Assemble the remaining gears (3 planet gears + 1 sun gear), passing the Sun Gear through the hole and fastening it into the slot on the Vial Holder.
#. Assemble the gearbox: stack the Gearbox Bottom, Cover, and Top; flip it over and drive **3× M3×10 bolts** into the holes.
#. Place the assembled gearbox on top of the gears, fitting its pegs into each planet gear.
#. Secure the gearbox to the Lid with **4× M3×25 bolts**.
#. Superglue the **4 feet** to the bottom of the assembly.
#. Place the handles on top of the box and secure with **4× M3×50 bolts**.
#. Place the handle caps on the handles and secure with superglue.
