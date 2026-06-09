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

Computed Axial Lithography (CAL) is a ground-breaking 3D printing technology that produces parts 
volumetrically in a single step, rather than using a repeated layering process like in traditional 
additive manufacturing (AM). This layerless technique offers numerous advantages over traditional 
AM methods, such as faster print times of complex geometries without the need for supports. In its most basic form, 
CAL consists of a rotating vial of photopolymerizable resin and a light source that displays a projected video. 
As the vial rotates, the resin is selectively cured to form a part. Despite its advantages, CAL has remained largely 
confined to research laboratories due to complex optical setups, high equipment costs, and limited access to materials, 
limiting its potential applications in education, hobbyist manufacturing, and makerspaces.

Historically, open-source hardware (OSH) has played a transformative role in broadening access to AM. 
For CAL to reach the same level of democratized innovation seen in traditional 3D printing, it needs to overcome 
barriers to manufacturability, accessibility, and usability. OpenCAL, the world’s first open-source, 
layerless 3D printer, developed at UC Berkeley by Waddell et al. in 2025, aimed to do just that. 
This second iteration builds upon that foundation by redesigning its hardware, electronics, software, 
and post-processing systems using principles of design for manufacturing and assembly (DFMA). 
Through accessible documentation and an online community, several pilot studies are underway to build OpenCAL, 
accelerating innovation in CAL technologies. Future work will involve a public release and continued refinement 
based on feedback from these pilots. 

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
   :caption: Materials

   materials/overview

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Step-by-Step Guides 

   step_by_step/frame_stepbystep
   step_by_step/optics_stepbystep
   step_by_step/rotational_element_stepbystep
   step_by_step/electronics_stepbystep
   step_by_step/centrifucal_stepbystep
   step_by_step/main_assembly
   step_by_step/wiring_stepbystep

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Software

   software/github
   software/vamtoolbox

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Resources

   resources/research_papers
   resources/opencal_in_media
   resources/contributors

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Miscellaneous
