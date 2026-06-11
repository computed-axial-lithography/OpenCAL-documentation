Lab Directions (Experts Only)
=============================

.. danger::

   **This page is intended for trained professionals only.** Resin mixing is hazardous and
   must only be performed by qualified personnel in a laboratory fume hood. If you are not
   equipped to mix photopolymer chemistry safely, do **not** attempt this; instead, purchase
   the pre-mixed resin (see :doc:`overview`).

The OpenCAL resin is a UDMA-based photopolymer tuned for Computed Axial Lithography.
This page covers the resin recipe, where to source each component, and the lab procedure
used to mix it.

.. danger::

   **Resin mixing is hazardous and must only be performed by trained professionals in a
   laboratory fume hood.**

   The components are reactive methacrylate monomers and amines that are skin/eye irritants,
   sensitizers, and harmful if inhaled or ingested. Before handling anything:

   - Work **only** inside a certified chemical fume hood.
   - Wear appropriate PPE: nitrile gloves, safety goggles, and a lab coat.
   - Read and follow the **Safety Data Sheet (SDS)** for every chemical below.
   - Never mix outside of a properly equipped lab. This is **not** a home or hobbyist procedure.

Resin Recipe
------------

The final recipe, by concentration in the UDMA base resin:

.. list-table::
   :widths: 30 20 50
   :header-rows: 1

   * - Component
     - Concentration
     - Role
   * - CQ (camphorquinone)
     - 2.5 mM
     - Photoinitiator
   * - EDAB (ethyl 4-dimethylaminobenzoate)
     - 5 mM
     - Co-initiator
   * - MDEA (N-methyldiethanolamine)
     - 200 mM
     - Co-initiator (oxygen scavenger)
   * - UDMA (urethane dimethacrylate)
     - Base resin
     - Monomer

Suppliers
---------

.. list-table::
   :widths: 35 15 50
   :header-rows: 1

   * - Component
     - Size
     - Link
   * - CQ (camphorquinone)
     - 5 g
     - `TCI C0014 <https://www.tcichemicals.com/US/en/p/C0014>`_
   * - EDAB
     - 25 g
     - `TCI D1744 <https://www.tcichemicals.com/US/en/p/D1744>`_
   * - MDEA
     - 250 mL
     - `Sigma-Aldrich 471828 <https://www.sigmaaldrich.com/US/en/product/aldrich/471828>`_
   * - UDMA (Esstech X-850)
     - 4 kg
     - `Esstech X-850 <https://catalog.esstechinc.com/item/oligomers/urethane-methacrylates/x-850-0000-2>`_

Mixing Procedure
----------------

This is the procedure currently used in our lab. It is constrained by lab-scale equipment
(small hot plates and magnetic stir bars rather than industrial mixers), so the mixing times
below are conservative and could be shortened significantly with better equipment.

#. Heat the UDMA base resin to **60 °C** in a water bath, in a **sealed container**.
#. Add the **CQ** and **EDAB** to the resin. Mix on a stir plate at **70 °C** and **200 rpm**.
   Wait approximately **12 hours**, until fully dissolved.
#. Turn the temperature down to **40 °C**.
#. Add the **MDEA**. Wait **1–2 days**, until fully mixed.

.. important::

   Two things are critical to a good batch:

   - **Do not heat the resin while mixing in the MDEA.** Cool to 40 °C first.
   - **MDEA readily reacts with atmospheric oxygen and degrades itself.** Always mix in a
     **sealed or semi-sealed container** to limit air exposure.
