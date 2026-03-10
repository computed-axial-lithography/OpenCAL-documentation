.. OpenCAL documentation master file, created by
   sphinx-quickstart on Wed Oct 15 21:26:09 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.
   Add your content using ``reStructuredText`` syntax. See the
   `reStructuredText <https://www.sphinx-doc.org/en/master/usage/restructuredtext/index.html>`_
   documentation for details.    

OpenCAL: A Comprehensive Guide
-------------------------------
**What is CAL?**

Computed Axial Lithography (CAL) is a recent advancement in volumetric additive manufacturing (VAM) that 
delivers a light dose to a photopolymer volume through tomographic reconstruction. The precursor liquid or gel 
itself generally supports the emerging object, eliminating the need for wasteful dedicated solid supporting structures. 
A challenge, however, is that desired geometry can shrink or expand during solidification and on Earth, if the 
precursor material’s viscosity is low enough. These effects may result in sinking or floating of the component, 
which can blur the geometry.

In principle, CAL is promising for in-space manufacturing because, unlike layer-based processes, CAL does not require a 
flat liquid–gas interface to be maintained during printing. With suitable development, CAL is potentially 
capable of manufacturing parts such as organic tissue, flexible seals, rigid trusses, and microstructures for space exploration, 
as well as repairing existing tools and parts. ‘SpaceCAL’ flew on a microgravity parabolic flight in May 2022 to 
demonstrate the capabilities of CAL and analyse a CAL system in a microgravity. Initial findings show that 0.12 Pa·s 
low viscosity precursor can be printed in microgravity with less geometric distortion than an Earth-based gravity counterpart.

**NOTES:**

This site, and the attached Github, will be used as the **Source-of-Truth** for all things OpenCAL. It is the initial public rendering of the open-source
version for public research. Critique is highly appreciated and the site and information may be updated overtime as more research
is conducted.


.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Engineering Documentation
   
   engineering_documentation/bom
   engineering_documentation/tools
   engineering_documentation/cad

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Step-by-Step Guides 

   step_by_step/frame_stepbystep
   step_by_step/optics_stepbystep
   step_by_step/rotational_element_stepbystep
   step_by_step/electronics_stepbystep
   step_by_step/wiring_stepbystep
   step_by_step/centrifucal_stepbystep
   step_by_step/main_assembly

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Software 

   software/github 
   software/stl_conversion
   software/data_generation

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Resources

   resources/troubleshooting
   resources/research_papers
   resources/photos
   resources/opencal_in_media
   resources/contributors

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Miscellaneous
