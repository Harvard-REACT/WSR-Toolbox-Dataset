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

## Performance evaluation for 2D Trajectory
![Dataset-1-AOA-accuracy-plot1](figs/Dataset_1_AOA_accuracy_plot_1.png)
![Dataset-1-AOA-accuracy-plot1](figs/Dataset_1_AOA_accuracy_plot_2.png)

### Location-wise AOA accuracy for NLOS scenario
The bearing angle i.e Angle-of-Arrival accuracy in NLOS using groundtruth and T265 Tracking camera trajectory:
![NLOS_Set_B_AOA](figs/NLOS_Set_A_B_2D_Trajectory_AOA_Accuracy_Results.png)

### Localization performance for NLOS scenario
The transmitting robot positions are assumed to be know. The receiving robot can localize itself using the bearing angle calculated from our framework. We use the profile variance metric discussed in [**Toolbox  Release:  A  WiFi-Based  Relative  Bearing  Sensor  for  Robotics**]() to reject outlying measurements. 

The localization accuracy for non-line-of-sight by directly using the data

<div align="center">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_gt_traj.png" width="400" alt="Localization NLOS accuracy gt">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_camera_traj.png" width="400" alt="Localization NLOS accuracy">
</div>
<p>&nbsp;</p>

The profile variance metric conveys the confidence in AOA estimation. We filter out "noisy" AOA estimates (highly impacted by signal multipath) using a variance threshold, which can be used to improve localization accuracy.

<div align="center">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_using_thresholding_gt_traj.png" width="400" alt="Localization NLOS accuracy gt with thresholding">
  <img align="center" src="figs/Dataset-1-NLOS_accuracy_using_thresholding_camera_traj.png" width="400" alt="Localization NLOS accuracy with thresholding">
</div>
<p>&nbsp;</p>


## Performance - Runtime tradeoff using different config parameters
To achieve better online runtime, different parameters in the config file can be tweaked with minimal impact on AOA accuracy. The following plots compare the AOA accuracy for all onboard sensing using a) lower resolution of profile and b) Subsampling - using alternate data packets. The defult config parameters use all the data packets to generate a profile with resolution 360 x 180.

![Performance - Runtime tradeoff](figs/Dataset-1-performance-runtime-tradeoff-1.png)

