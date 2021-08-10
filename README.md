# WSR-Toolbox-Dataset

<div align="center">
  <a href="https://react.seas.harvard.edu//">
    <img align="left" src="https://github.com/Harvard-REACT/WSR-Toolbox/blob/main/figs/lab_logo.png?raw=true" width="180" alt="REACT Lab and WiTech Lab">
  </a>
  <a href="https://react.seas.harvard.edu/communication-sensor">
    <img align="center" src="https://github.com/Harvard-REACT/WSR-Toolbox/blob/main/figs/toolbox_logo.png?raw=true" width="350" alt="WSR Toolbox">
  </a>
  <a href="https://www.seas.harvard.edu/">
    <img align="right" src="https://github.com/Harvard-REACT/WSR-Toolbox/blob/main/figs/univ_logo.png?raw=true" width="160" alt="SEAS Harvard and CMU">
  </a>
</div>
<p>&nbsp;</p>

# Testbed area
The total testbed area is approx 150 sq. meters and comprises of six separate locations. These include the main testbed with motion capture system and five locations that  are  in  NLOS.  The  locations  are  general  office areas  and include  like  chairs,  tables,  glass  door,  electronics,  metalshelves,  etc.


# Dataset-1
 This includes data  samples  across  a  total  of  ten positions  of  receiving (RX)  robot  arranged  in  a  grid  which  are at  a  minimum  distance  of  2.5m  from  a  LOS  transmitting (TX) robot  position. For  NLOS, TX robots  are  placed at  different  positions  in  adjacent  office  spaces. A total of 600 data samples were collected for this dataset.

![Dataset-1-samples](figs/Dataset-1.png)

### AOA accuracy for 2D Trajectory
![Dataset-1-AOA-accuracy-plot1](figs/Dataset_1_AOA_accuracy_plot_1.png)
![Dataset-1-AOA-accuracy-plot1](figs/Dataset_1_AOA_accuracy_plot_2.png)


### Localization performance for NLOS scenario
The transmitting robot positions are assumed to be know. The receiving robot can localize itself using the bearing angle calculated from our framework. We use the profile variance metric discussed in [**Toolbox  Release:  A  WiFi-Based  Relative  Bearing  Sensor  for  Robotics**]() to reject outlying measurements. 

The localization accuracy for non-line-of-sight by directly using the data

<div align="center">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_gt_traj.png" width="400" alt="Localization NLOS accuracy gt">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_camera_traj.png" width="400" alt="Localization NLOS accuracy">
</div>
<p>&nbsp;</p>

The profile variance metric conveys the confidence in AOA estimation. We filter out "noisy" AOA estimates (highly impacted by signal multipath) using a variance threshold, which can be used to improve localization accuracy. About **x% of samples are rejected by this simple filtering method**

<div align="center">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_using_thresholding_gt_traj.png" width="400" alt="Localization NLOS accuracy gt with thresholding">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_using_thresholding_camera_traj.png" width="400" alt="Localization NLOS accuracy with thresholding">
</div>
<p>&nbsp;</p>







# Dataset-2
![Dataset-1-samples](https://github.com/Harvard-REACT/WSR-Toolbox/blob/main/figs/test_area_map.png?raw=true)

The 2D motion would be corresponding to commonmotion  for  normal  ground  robots;  3D  hand-held  arbitrary motion  reflects  the  mobility  of  a  UAV. The  experiment  is  performed  in  two  scenarios:  Line-of-sight  (LOS)  and  Non-line-of-sight  (NLOS).  The  LOS experiments are all conducted on the right half of the test bed including positions 1 to 10. The NLOS ex-periments are carried out by putting the RX robot  in  the  testbed  with  TX  robots  in  other  rooms, occluded  by  a  wall,  at  positions  14,  15  and  16.


Note: Additional data samples in gitlab repo
