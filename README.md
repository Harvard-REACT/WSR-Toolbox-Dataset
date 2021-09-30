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
The total testbed area is approx 150 sq. meters and comprises of six separate locations. These include the main testbed with motion capture system and five locations that  are  in  NLOS.  The  locations  are  general  office areas  and include  like  chairs,  tables,  glass  door,  electronics,  metalshelves,  etc. Additional description and details of the setup are available in our paper [**Toolbox  Release:  A  WiFi-Based  Relative  Bearing  Sensor  for  Robotics**](https://arxiv.org/abs/2109.12205)

# Datasets
 This includes data  samples  across  a  total  of  ten positions  of  receiving (RX)  robot  arranged  in  a  grid  which  are at  a  minimum  distance  of  2.5m  from  a  LOS  transmitting (TX) robot  position. For  NLOS, TX robots  are  placed at  different  positions  in  adjacent  office  spaces. A total of about 600 data samples were collected for this dataset.

![Dataset-samples](figs/Dataset-1.png)

## Performance evaluation for 2D Trajectory
![Dataset-AOA-using-t265-displacement](figs/aoa_accuracy_est_disp_with_rejection.png)

### Localization performance for NLOS scenario
The transmitting robot positions are assumed to be know. The receiving robot can localize itself using the bearing angle calculated from our framework. We use the profile variance metric discussed in  to reject outlying measurements. 

Coming soon!!

**Additional results for the dataset are available at our [Wiki Page](https://github.com/Harvard-REACT/WSR-Toolbox/wiki/Experiment-Results)**

## Citation
If this dataset is is useful for your research publications, please cite our work.

- [1] Ninad Jadhav, Weiying Wang, Diana Zhang, Swarun Kumar and Stephanie Gil. [**Toolbox  Release:  A  WiFi-Based  Relative  Bearing  Sensor  for  Robotics**](https://arxiv.org/abs/2109.12205).
 
 ```bibtex
@article{WSR_toolbox,
  title={Toolbox  Release:  A  WiFi-Based  Relative  Bearing  Sensor  for  Robotics},
  author={Ninad Jadhav and Weiying Wang and Diana Zhang and Swarun Kumar and Stephanie Gil},
  journal={},
  year={},
  volume={}
}
```

- [2] Ninad Jadhav*, Weiying Wang*, Diana Zhang, O. Khatib, Swarun Kumar and Stephanie Gil. [**WSR: A WiFi Sensor for Collaborative Robotics**](https://arxiv.org/abs/2012.04174) (* denotes co-primary authors)

```bibtex
@article{Jadhav2020WSRAW,
  title={WSR: A WiFi Sensor for Collaborative Robotics},
  author={Ninad Jadhav and Weiying Wang and Diana Zhang and O. Khatib and Swarun Kumar and Stephanie Gil},
  journal={ArXiv},
  year={2020},
  volume={abs/2012.04174}
}
```


