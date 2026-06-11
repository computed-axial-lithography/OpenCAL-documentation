.. _wiring-instructions:

Wiring
++++++

.. figure:: ../static/Step_by_Step/Wiring_Images/wiring_diagram.png
   :align: center
   
   General wiring diagram

Introduction
============

Required Materials:
^^^^^^^^^^^^^^^^^^^

* 26 AWG, 22AWG, 18AWG wire
* Heat shrink
* Quick disconnect plugs
* JST connectors
* 2.54mm pitch Dupont Connector Kit
* 4.8mm quick disconnect plugs
* Ring Connectors 5.3mm ID
* Perf board
* 8x1 Header Pins x2
* HDMI 0.5ft
* Zip Ties

Required Tools:
^^^^^^^^^^^^^^^

* Soldering iron & solder
* Dupont crimping tool
* Heat gun

References for wiring techniques:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* `Dupont connectors tutorial <https://www.youtube.com/watch?v=jET1QTP1B7c>`__
* `Fork connector tutorial <https://www.youtube.com/watch?v=goxVeefDpQg>`__

**NOTE: The provided wire lengths are an approximation. For cleaner routing and to account for any differences in your OpenCAL build, measuring wire based on the distances between components in your system.**

This guide assumes Main Assembly Process - Part 1 has been completed.


How to Read Wiring Guide Tables
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

   .. image:: ../static/Step_by_Step/Wiring_Images/Example_for_Wiring_Guide.png
      :align: center

Power Distribution
==================


#. Connect the Power Switch to the 24V Adapter. Use cable clips to secure wire to the 80-20.

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step1_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/table_powerdist_1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/pins_powerdist_1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step1_assem.jpg
      :align: center

   |

#. Connect the 5V Converter to the 24V Adapter. The 5V Converter will need to be removed from the plate to connect wires to the soldering through holes, then reattached.

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step2_cad_diagram.png
      :align: center
   
   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/table_powerdist_2.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/pins_powerdist_2.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step2_assem.jpg
      :align: center

   |

#. Connect 12V Converter to the 24V Adapter. Use cable clips to secure wire to the 80-20.

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step3_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/table_powerdist_3.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/pins_powerdist_3.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step3_assem.png
      :align: center

   |

#. Connect 19V Converter to the 24V Adapter. Use the zip tie cutouts to secure wires in front of the 24V Adapter. **Note:** If you are using a different projector, the voltage requirement may be different from 19V. Check power requirements in the product spec and use a different buck converter if needed.

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step4_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step4_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/table_powerdist_4.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/pins_powerdist_4.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step4_assem.jpg
      :align: center

   |

#. Connect 5V Converter to the Screw Terminal Block, with Vout connected to A and Ground connected to B. This is where all 5V powered components will be connected. It may be easier to remove the Screw Terminal Block from the housing plate while connecting wires. After this step, the 5V Converter requires no more soldering and can be reattached to the housing plate.

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/table_powerdist_5.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/pins_powerdist_5.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Power_Distribution/power_dist_step5_assem.jpg
      :align: center

Top Plate Housing Connections
=============================

#. Remove the motor from the top plate. Attach A+, A-, B+, and B- motor wires to the Tic T249 by trimming the provided cable and stripping the ends. Run wires from the Tic T249 to the 24V adapter using the corresponding cutout.

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step1_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/table_top_plate_step1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step1_vis1.png
      :align: center
   
   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step1_vis2.jpg
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step1_vis3.png
      :align: center
   
   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step1_vis4.png
      :align: center

   |

#. Run a Micro-USB to USB-A cable from the Tic T249 to the RP5 using the designated cutout. Plug the cable into the RP5 using a U-shaped adapter.

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step2_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step2_vis2.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step2_cad_diagram.png
      :align: center
   
   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step2_vis3.png
      :align: center
      
   |

#. Connect wires from a 2 pin JST plug to fork connectors for the 12V Converter output screw terminals. Use a set of 2 pin Dupont connectors in-between for easy fan removal. Run the wires through the corresponding opening in the Top Plate Housing and through the side of the RP5 housing. Use cable clips to secure wire to the 80-20.
   
   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step3_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step3_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/table_top_plate_step3.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Top_Plate/top_plate_step3_vis3.png
      :align: center


.. _lcd-wiring:

LCD Housing
===========

#. Connect the LCD to the Terminal Block and RP5. Run wires through the cutout in the LCD Housing Mount.

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/LCD_step1_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/table_lcd_step1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/LCD_step1_assem.jpg
      :align: center

   |

#. Connect the Encoder to the Terminal Block and RP5. Run wires through the cutout in the LCD Housing Mount.

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/LCD_step2_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/table_lcd_step2.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LCD/LCD_step2_assem.jpg
      :align: center


.. _led-wiring:


LED
===

#. Remove the Bottom Plate of the rotation element from the assembly.

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/LED_step1_vis1.png
      :align: center

   |

#. Solder wires from the LED to a 3 pin Dupont plug. Zip tie the wire in place to keep the Dupont connector exposed.

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/LED_step2_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/table_led_step2.png
      :align: center

   |

#. Connect a 3 pin Dupont receptacle to three wires, running power and ground to the Terminal Block and the data line to the RP5. Add a 300 Ohm resistor to the data line to prevent noise and power leeching. Reconnect the Bottom Plate to the assembly and plug the LED Dupont connectors.

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/LED_step3_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/table_led_step3.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/LED/LED_step3_assem.jpg
      :align: center
      

.. _camera-wiring:

Camera
======

*Note about camera assembly: if CSI to HDMI adapters are not available, a long CSI cable can be used as a substitute.*

#. Remove the camera and CSI to HDMI adapter from the Camera Mount.

   .. image:: ../static/Step_by_Step/Wiring_Images/camera/camera_step1_vis1.png
      :align: center

   |

#. Run the CSI cable from the left side of the camera, behind the camera, and connect it to the adapter. This 22 pin to 22 pin CSI cable comes with the adapter set.

   .. image:: ../static/Step_by_Step/Wiring_Images/camera/camera_step2_vis1.png
      :align: center


   |

#. In the RP5 Housing assembly, connect the CSI to HDMI adapter to the RP5 using a CSI cable. This CSI cable is 22 pin to 15 pin.

   .. image:: ../static/Step_by_Step/Wiring_Images/camera/camera_step3_assem.jpg
      :align: center


   |

#. Connect the adapters using the 0.5 ft HDMI cable.

   .. image:: ../static/Step_by_Step/Wiring_Images/camera/camera_step4_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/camera/camera_step4_assem.jpg
      :align: center

Remaining Connections
=====================

#. Connect the RP5 to 5V power by running a USB cable from the RP5 to the Terminal Block.

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step1_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step1_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/table_remaining_step1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step1_assem.jpg
      :align: center

   |

#. Connect the projector to 19V power by connecting wires from the 19V power output to the corresponding plug for projector power. For the NexiGo Nova Mini, this is a USB-C.

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step2_vis1.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/table_remaining_step2.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step2_assem.jpg
      :align: center


   |

#. Connect the projector to the RP5 using a micro-HDMI to HDMI cable. If using an alternative projector with a different video input method, use a cable for connection from micro-HDMI to the corresponding input plug type.

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step3_cad_diagram.png
      :align: center

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step3_assem.jpg
      :align: center

   |

#. To secure wires on the Inner Housing Plate, use the press-fit clips along the wire routing cutouts.

   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step4_vis1.png
      :align: center


   .. image:: ../static/Step_by_Step/Wiring_Images/Remaining_Connections/remaining_step4_assem.jpg
      :align: center


