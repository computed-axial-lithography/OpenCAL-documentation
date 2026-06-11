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

Centrifugal Spinning (CentrifuCAL)
----------------------------------

A centrifugal spinning approach — **CentrifuCAL** — is being explored to help counteract sinking
or floating of the part in low-viscosity resin during a print. The hardware and procedure are
**not yet finalized**, so the CentrifuCAL build section is currently hidden. It will be brought
back here as the design matures.

Vial Light-Protection Covers
----------------------------

Photopolymer resin cures on exposure to stray light (see the resin-handling warnings in the
:doc:`Materials overview <../materials/overview>`). We are working on **covers for the vials** to
shield them from ambient and stray light **when they are not actively being printed** — protecting
the resin between prints and during storage. A reliable, easy-to-use cover design is still in
progress.
