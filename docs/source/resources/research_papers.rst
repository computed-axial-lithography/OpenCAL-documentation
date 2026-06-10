Research Papers
===============

A curated list of key publications on Computed Axial Lithography (CAL) and volumetric
additive manufacturing (VAM). The two most important papers — the original CAL paper and
the first OpenCAL paper — are highlighted first.

Foundational Papers
-------------------

.. admonition:: ⭐ The Original CAL Paper — *Science*, 2019
   :class: important

   **Volumetric additive manufacturing via tomographic reconstruction**

   *Brett E. Kelly, Indrasen Bhattacharya, Hossein Heidari, Maxim Shusteff,
   Christopher M. Spadaccini, Hayden K. Taylor* — University of California, Berkeley &
   Lawrence Livermore National Laboratory (LLNL).

   The paper that introduced Computed Axial Lithography. It showed that an entire 3D object
   can be formed *all at once* by illuminating a rotating volume of photosensitive resin with
   a dynamically evolving light pattern — no layers, no support structures, and the ability to
   print around pre-existing objects, with print times of 30–120 seconds. This is the
   foundation that every CAL system, including OpenCAL, is built on.

   `Read the paper <https://www.science.org/doi/10.1126/science.aau7114>`__

.. admonition:: ⭐ The First OpenCAL Paper — arXiv, 2025
   :class: important

   **An Open-Sourced, Community-Driven Volumetric Additive Manufacturing Printer and
   Post-Processor**

   *Taylor Waddell, Erik Broude, Tristan Bourgade, Natalia Fabiana De La Torre,
   Erfan Kohyarnejadfard, Tavleen Kaur, Scarlett Hao, Dylan Motley, Daniel Oslund,
   Evan Percival, Rajdeep Summan, Connor Vidmar, Hayden K. Taylor* —
   University of California, Berkeley.

   The paper that introduces OpenCAL itself — a low-cost, open-source CAL printer and
   post-processor designed to put volumetric additive manufacturing in the hands of
   researchers, educators, and makers. It documents the hardware, software, and resin so the
   system can be reproduced and built upon by the wider community. Start here to understand the
   project this site supports.

   `Read the paper <https://arxiv.org/abs/2509.02865>`__

Additional Reading
------------------

Reconstruction & algorithms
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Deconvolution volumetric additive manufacturing** — *Antony Orth, Daniel Webber, Yujie
  Zhang, Kathleen L. Sampson, Hendrick W. de Haan, Taylor Waddell, Hayden K. Taylor, et al.*
  (*Nature Communications*, 2023). National Research Council Canada & UC Berkeley.
  Shows that light-dose spread from chemical diffusion and optical blur becomes significant for
  features below ~0.5 mm, then introduces a deconvolution method to correct for it and sharpen
  fine features. `View paper <https://www.nature.com/articles/s41467-023-39886-4>`__

* **OSMO — Object-Space Optimization of Tomographic Reconstructions for Additive Manufacturing**
  — *Charles M. Rackson, Kyle M. Champley, Joseph T. Toombs, Erika J. Fong, Vishal Bansal,
  Hayden K. Taylor, Maxim Shusteff, Robert R. McLeod* (*Additive Manufacturing*, 2021).
  University of Colorado Boulder, UC Berkeley & LLNL.
  Rather than optimizing the projected images, OSMO iteratively optimizes the digital *model*
  itself — forward/back-projecting the part, finding regions of excess or missing dose, and
  adjusting the model accordingly. Simple to implement and improves accuracy of complex parts
  even with imperfect optics and materials.
  `View paper <https://www.sciencedirect.com/science/article/abs/pii/S2214860421005212>`__

* **BCLP — Tomographic projection optimization with general band-constraint Lp-norm
  minimization** — *Chi Chung Li, Joseph Toombs, Hayden K. Taylor, Thomas J. Wallin*
  (*Additive Manufacturing*, 2024). UC Berkeley.
  Optimizes the computed light patterns using a band-constrained Lp-norm minimization, producing
  sharper dose contrast between the part and surrounding resin and improving resolution and
  fidelity. `View paper <https://www.sciencedirect.com/science/article/pii/S2214860424004937>`__

Process monitoring & control
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Automatic Exposure Volumetric Additive Manufacturing** — *Antony Orth, et al.*
  (*Advanced Materials Technologies*, 2025). National Research Council Canada.
  Introduces automatic exposure control for VAM: instead of guessing the dose and time, the
  system uses real-time optical feedback to determine the correct light dose and stop the print
  at the optimal moment, improving consistency and removing trial-and-error.
  `View paper <https://advanced.onlinelibrary.wiley.com/doi/10.1002/admt.202402168>`__

* **On-the-fly 3D metrology of volumetric additive manufacturing** — *Antony Orth,
  Kathleen L. Sampson, Yujie Zhang, Kayley Ting, Derek Aranguren van Egmond, Kurtis Laqua,
  Thomas Lacelle, Daniel Webber, Dorothy Fathi, Jonathan Boisvert, Chantal Paquet*
  (arXiv, 2022). National Research Council Canada.
  Demonstrates in-situ optical monitoring of a part *as it forms* during printing, measuring the
  emerging geometry in real time to enable closed-loop feedback rather than after-the-fact
  evaluation. `View paper <https://arxiv.org/pdf/2202.04644>`__

Materials & chemistry
~~~~~~~~~~~~~~~~~~~~~~~

* **Advancing Tomographic Volumetric Printing via Oxygen Inhibition Control** — *Yujie Zhang,
  Katherine Houlahan, Daniel Webber, Nicolas Milliken, Kathleen L. Sampson, Hendrick W. de Haan,
  Hao Li, Robynne Vlaming, Liliana Gaburici, Antony Orth, Chantal Paquet* (*Advanced Materials*,
  2025). National Research Council Canada.
  Turns oxygen inhibition into a tool rather than a nuisance: using **N-methyldiethanolamine
  (MDEA)** — the same additive in the OpenCAL resin — to regenerate radicals, the authors achieve
  high-resolution, large-volume prints (up to 60 mm, a 16× increase in print volume).
  `View paper <https://advanced.onlinelibrary.wiley.com/doi/10.1002/adma.202508729>`__

* **A review of materials used in tomographic volumetric additive manufacturing** —
  *Jorge Madrid-Wolff, Joseph Toombs, … Christophe Moser* (19 authors) (*MRS Communications*,
  2023). EPFL, with UC Berkeley, Harvard, Utrecht, LLNL, CU Boulder, Freiburg, ETH Zürich and
  others. A broad survey of the photopolymer resins and material systems used across VAM,
  summarizing their properties, trade-offs, and current limitations — a good orientation to the
  materials side of the field. `View paper <https://pubmed.ncbi.nlm.nih.gov/37901477/>`__

In-space manufacturing
~~~~~~~~~~~~~~~~~~~~~~~~

* **Demonstration and Analysis of Volumetric Additive Manufacturing via Sub-Orbital Spaceflight
  Testing** — *UC Berkeley SpaceCAL team* (*Acta Astronautica*, 2026). University of California,
  Berkeley. Reports SpaceCAL Mission 3, which autonomously manufactured and post-processed four
  parts during ~140 seconds of microgravity on a suborbital flight — the first integrated CAL
  workflow demonstrated in space, with analysis of the distortions encountered.
  `View paper <https://www.sciencedirect.com/science/article/pii/S0094576526003395>`__
