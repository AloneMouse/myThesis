---
source_pdf: Optimal Energy Consumption in Controlled low-altitude Air City Transport Systems.pdf
pages: 25
---

# Optimal Energy Consumption in Controlled low-altitude Air City Transport Systems

<!-- page 1 -->

Optimal Energy Consumption in Controlled 1 Low-altitude Air City Transport Systems 2 Yazan Safadiaand Jack Haddada, aTechnion Israel Institute of Technology, Faculty of Civil and Environmental Engineering, Technion 4 Sustainable Mobility and Robust Transportation (T-SMART) Laboratory 5 Keywords: Traffic Management and Control, Traffic Flow, Feedback Control, Low-Altitude 6 Air City Transport System, Energy Consumption. 7 Abstract 8 Traffic air congestion should be considered in future deployments of Low-Altitude Air city Trans9 port (LAAT) systems. In addition to the congestion concerns, the low-altitude aircraft is being 10 designed with limited energy capacity due to design constraints and battery technologies. Hence, 11 energy consumption concerns should also be considered within LAAT operations. This paper ex12 amines the energy consumption of low-altitude aircraft in air mobility (AM) operations, intending 13 to improve the environmental impact of air mobility in urban and regional areas. To achieve this, 14 the study enhances the LAAT model-based operational framework by integrating an energy con15 sumption model (ECM) for low-altitude aircraft. The framework couples modeling and control of 16 microscopic and macroscopic levels of AM operations. Including the ECM allows us to explore 17 the relationship between macroscopic energy consumption and known macroscopic traffic flow 18 variables. As a result, this paper contributes to the literature with the development of the LAAT 19 Energy Consumption Model (eLMFD). The eLMFD does not only quantify the energy consump20 tion of individual aircraft but also facilitates the aggregation of energy consumption for the entire 21 airspace. The study realizes eLMFD with a simplified hierarchical control design optimizing en22 ergy efficiency and traffic efficiency in LAAT networks. The development of the eLMFD provides 23 a valuable tool for assessing the environmental impact of LAAT systems. eLMFD can be a bench24 mark to diagnose airspace conditions and enhance traffic control strategies for operating efficiently 25 and sustainably of LAAT systems. 26 *Corresponding author. E-mail address: jh@technion.ac.il.

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 2 -->

## 1 Introduction 1

The aviation ecosystem is continually advancing with the development of cutting-edge technolo2 gies. New aircraft designs are being created to enhance air mobility (AM)[1]. These innovations 3 aim to revolutionize commuting possibilities and cargo transport within and between cities, oper4 ating in low-altitude airspace and forming what can be termed the low-altitude air city transport 5 (LAAT) system. 6 The literature highlights a growing interest in deploying low-altitude aircraft in urban airspace 7 Straubinger et al. (2021); Ronald Berger (2020); Doole et al. (2020); Fu et al. (2022). Most of these 8 aircraft are electrically powered, utilizing advanced batteries, and capable of vertical take-off and 9 landing. The success of such designs lies in their ability to be remotely or autonomously controlled, 10 with or without a pilot. This integration of advanced technologies enhances AM operations, en11 suring safety and efficiency and providing a platform for groundbreaking research in this frontier 12 domain. 13 Numerous studies discuss the challenges and opportunities presented by futuristic AM Straub14 inger et al. (2020); Cohen et al. (2021); Cohen and Shaheen (2023); Ahmed et al. (2023). As we 15 have entered the second half of this decade, one of the primary limitations to widespread adoption 16 of futuristic AM operations concerns economic and environmental factors, given the relatively 17 advanced stage of technological developments Kopardekar (2017); FAA NextGen Organization 18 (2023). A recent study PwC (2023) revealed that existing short-distance air travel options (covering 19 distances less than 30 km) are economically less attractive compared to current travel alternatives. 20 Regarding environmental considerations, the literature questions the energy efficiency of new 21 aircraft Pukhova (2018); Kasliwal et al. (2019); Filippone and Barakos (2020); Ahmed et al. 22 (2023). While electric aircraft themselves may not directly impact emissions levels, the source 23 of electricity used to charge these aircraft significantly impacts total emissions. To achieve mean24 ingful emission reductions, this energy must originate from renewable and sustainable sources. 25 Despite challenges in enabling efficient AM operations, the potential for successful large-scale 26 implementation remains promising, with worldwide flight numbers continually increasing. Ad27 dressing environmental concerns, this paper aims to investigate energy consumption patterns of 28 low-altitude aircraft operations. 29 Furthermore, the cost of AM operations and optimization opportunities have been explored 30 in recent literature Brown and Harris (2020); Moore (2012). A conceptual optimization tool, for31 mulated as a geometric program (GP), incorporates vehicle, mission, and cost models for AM. 32 Parameters such as the engine’s energy density, vehicle operational time, battery cycle life, and 33 energy cost are considered in calculating capital and operating expenses. 34 The rapid advancements in unmanned aerial vehicles (UA Vs) and electric vertical takeoff and 35 landing vehicles (VTOLs) have drawn significant attention to the critical issue of energy consump36 tion in aerial transportation systems. As these autonomous aerial vehicles become increasingly 37 prevalent, understanding and optimizing their energy usage have become paramount for sustain38 able and efficient operations. Early research by Thibbotuwawa et al. (2018a,b) identified critical 39 factors influencing energy consumption during UA V missions, paving the way for investigating 40 1In this paper, we use the term air mobility (AM) to refer to the futuristic air mobility industry within urban and regional areas, encompassing both urban air mobility (UAM) andadvanced air mobility (AAM) .

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 3 -->

the relationship between energy consumption and routing decisions. They provided a compre1 hensive overview of energy consumption’s impact on UA V routing, categorizing the influencing 2 parameters and establishing crucial relationships between them and energy usage. Additionally, 3 the study Abeywickrama et al. (2018) introduced a comprehensive energy consumption model for 4 UA Vs based on empirical battery usage data, considering various flight scenarios and conditions 5 to enable accurate prediction of energy consumption during UA V maneuvers. 6 Expanding the scope to VTOLs, the study Kasliwal et al. (2019) conducted an in-depth analy7 sis, comparing their energy usage and greenhouse gas emissions with ground-based vehicles. Their 8 findings revealed that while VTOLs are energy-efficient during cruise phases, significant energy 9 is consumed during takeoff and climb, making their environmental sustainability dependent on 10 trip distances. Nonetheless, fully loaded VTOLs were found to emit fewer greenhouse gases per 11 passenger-kilometer compared to internal combustion engine vehicles (ICEVs) and battery electric 12 vehicles (BEVs), indicating their potential niche role in sustainable mobility. 13 Later on, additional energy consumption models were presented in Yan et al. (2021); Zhang 14 et al. (2021); Beigi et al. (2022); Gong et al. (2023). A simplified energy consumption model 15 for rotary-wing UA Vs was introduced in the study Yan et al. (2021), providing closed-form ex16 pressions as functions of key parameters. This model improves UA V communication designs, 17 optimizing energy usage. To facilitate decision-making for drone delivery operations, the study 18 Zhang et al. (2021) conducted a comprehensive review of drone energy consumption models and 19 their inter-relationships. Their work highlights the importance of accurate modeling for effectively 20 designing and operating delivery drones. The study Beigi et al. (2022) offered insights into critical 21 factors influencing UA V energy usage. Identifying these factors could enhance UA V capabilities, 22 benefiting the different applications. Recently, the study Gong et al. (2023) derived theoretical 23 power consumption models for multi-rotor UA Vs under various flight states, identifying key influ24 encing factors and potential applications. 25 Several studies used energy consumption models to optimize aircraft path planning and 26 scheduling Pradeep and Wei (2019); Qi et al. (2020); Silva and Caillouet (2020); Wang et al. 27 (2022); Takemura et al. (2023). For eVTOL aircraft, Pradeep and Wei (2019) developed a fixed28 final-time optimal control model to achieve energy-efficient arrival trajectories considering con29 straints and battery endurance. Qi et al. (2020) proposed a deep reinforcement learning-based 30 method for optimal UA V communication coverage and service. For UA V trajectory planning, 31 Silva and Caillouet (2020) presented a mixed integer linear program balancing distance and en32 ergy. She et al. (2020) introduced a neural network-based model for accurate energy consumption 33 prediction. Wang et al. (2022) used deep reinforcement learning for energy-efficient path plan34 ning. Takemura et al. (2023) proposed a comprehensive framework for energy-efficient paths and 35 perception quality optimization. 36 Connectivity and digitalization will enable new control measures in aviation operations, fa37 cilitating their integration into real-time urban traffic management. Hence, new control strategies 38 can be designed to regulate LAAT demand and supply, by manipulating aircraft departures, aircraft 39 routings, aircraft speeds, etc. It should be noted that LAAT controlled systems might create system 40 queues, which have a high impact on the system’s efficiency and can lead to environmental and 41 economical challenges Safadi et al. (2024a). Hence, this study focuses on incorporating the energy 42 aspects into the traffic control strategies by: (i) investigating an energy consumption model (ECM) 43

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 4 -->

of the low-altitude aircraft and aggregating the traffic characteristics in the network level; and (ii) 1 designing a feedback control strategy based on the energy consumption in the network, as depicted 2 in Fig. 1. To the authors’ knowledge, integrating a macroscopic energy model within an optimal 3 control problem framework employing a hierarchical control approach for LAAT systems has not 4 been previously investigated. 5 xyz Layer lNetworkRegion i Gi(ni(t)) E(v(t)) i iRegion j Gj(nj(t)) E(v(t)) jj Speed Control Lower Aircraft Max. Speed vm Speed Control Higher Aircraft Max. Speed vm

#### Figure 1: A schematic LAAT network consists of layers ( l2L) divided into regions ( i;j2R), with

modeling and control of the system’s outflow G(n)(as a function of accumulation n) and energy consumption E (V)(as a function of speed V) for each region i;j. The aircraft maximum speed vm can be adjusted to a lower or higher value based on the airspace state. Recent research has increasingly concentrated on Macroscopic Fundamental Diagrams 6 (MFDs) and their use in developing control-oriented strategies for Low-Altitude Air Traffic 7 (LAAT) systems. This emerging research direction builds upon extensive prior studies in urban 8 road networks Johari et al. (2021); Geroliminis and Daganzo (2008); Sirmatel et al. (2021), incor9 porating recent innovations such as perimeter control and route guidance Chen et al. (2024), speed 10 regulation techniques Sirmatel and Yildirimoglu (2023a), and strategies for enhancing resilience 11 against cyber-attacks Wang et al. (2025). These works illustrate how established urban traffic con12 cepts have been effectively adapted to address advanced management challenges in Urban Air Mo13 bility (UAM), including perimeter control Haddad et al. (2021), integrated departure and boundary 14 control Safadi et al. (2024b), and dynamic routing Weng et al. (2024). Adopting an MFD-based 15 framework for LAAT simplifies the inherent complexity through macroscopic aggregation, facili16 tating practical implementation at the microscopic operational level. Comparable studies on road 17 traffic have similarly evaluated environmental implications, specifically carbon emissions associ18 ated with macroscopic traffic dynamics in large-scale networks Zegeye et al. (2013); Fontes et al. 19 (2015); Qi and Zhang (2016); Barmpounakis et al. (2021); Rodriguez-Rey et al. (2021). 20 This paper explores the environmental aspects of AM operations by studying the energy con21 sumption of low-altitude aircraft in the airspace. We extend the LAAT model-based framework 22 Safadi et al. (2023) with an energy consumption model (ECM) Thibbotuwawa et al. (2018a). 23 This integration allows us to study the relationship between macroscopic energy consumption and 24 known macroscopic traffic flow variables, leading to the derivation of the LAAT Energy Con25 sumption Model (eLMFD). eLMFD is utilized to design a simplified feedback control strategy to 26

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 5 -->

optimize the energy efficiency and traffic efficiency in LAAT networks. 1

## 2 Developing LAAT Energy Consumption Model 2

### 2.1 Enhanced LAAT model-based operational framework 3

The LAAT model-based operational framework, which was developed in Safadi et al. (2023, 4 2024a), is extended to include an energy consumption model (ECM) for the low-altitude aircraft, 5 as shown in Fig. 2. The framework couples modeling and control of LAAT systems and integrates 6 the two aggregation levels, i.e., microscopic and macroscopic. In this paper, ECM is applied in 7 the framework to determine the energy consumption of each aircraft simultaneously to the plant 8 model. The aircraft energy consumption can be easily aggregated for the whole airspace, and 9 by then to derive a macroscopic energy consumption model, namely LAAT energy consumption 10 model (eLMFD). The uniqueness of this framework is that eLMFD can straightforwardly diagnose 11 the airspace conditions and enhance traffic control strategies, to efficiently and sustainably operate 12 LAAT systems. 13 t0 tk Plant model •Aircraft dynamics and routet∆tS Aircraft controller

$$
•Collision avoidancepA(t)tk=t+ ∆ tS
$$

vc,A(t) Aircraft energy model •Energy consumption modelvA(t) EA(t) xyzLayerlNetwork G(n(t )) n(t) nc Region iRegion jControl model •Traffic characteristics estimation ◦MFD-based traffic model ◦Aggregated energy model∆tMt∆tC Feedback control Airspace state optimization ◦Model Predictive Controlnij(t) dij(t) . . .Np Aircraft command ◦Departure Time ◦Waypoints ◦Speeduij(t) td,A vc,A(t) ˜pD,AtfMicroscopic level Macroscopic level

#### Figure 2: Enhanced LAAT model-based operational framework that incorporates energy consump-

tion modeling, while combining the microscopic and macroscopic levels of LAAT controlled systems. The framework presented in this study uses a microscopic model as the plant model to de14 scribe aircraft behavior in detail, while a macroscopic model is used as a control model for de15 signing control inputs. The aggregate dynamics of the macroscopic level are steered by the LAAT 16 traffic dynamics of the microscopic level, with the characteristics variables being inserted as an 17 input to the control model. Simultaneously, a feedback control strategy is created to optimize the 18 airspace state operationally, based on airspace dynamics and identification. Finally, the optimal 19

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 6 -->

control inputs are calculated and transferred to the microscopic level through an aircraft command 1 subsystem. This process is illustrated in Fig. 2. 2 Incorporating the Energy Consumption Model (ECM) into the LAAT model-based opera3 tional framework opens up new directions for investigating the energy consumption and traffic 4 characteristics in LAAT networks. The extended framework allows us to identify the relationship 5 between macroscopic energy consumption and known macroscopic traffic flow variables, and to 6 derive eLMFD. As a result, it is possible to optimize the LAAT system’s performance with respect 7 to energy consumption characteristics. In this paper, eLMFD will be utilized with a simplified 8 feedback control strategy to demonstrate the potential of macroscopic energy consumption mod9 els. The control strategy can manipulate aircraft departure time, waypoints, and current speed to 10 optimize the airspace state, achieving energy efficiency and traffic efficiency at the microscopic 11 and macroscopic levels of the system by utilizing a hierarchical control approach and including 12 feedback control and aircraft command subsystems. 13

### 2.2 Plant model for air traffic flow 14

A realistic plant model that captures individual aircraft movements inside the airspace is needed 15 to model LAAT operation sufficiently. We adopt the developed microscopic model in Safadi et al. 16 (2023), which can capture the dynamics of the aircraft while maintaining collision-free flight. A 17 brief description of the microscopic model is given here as follows, while for a detailed description, 18 the interested reader is referred to the original paper. Based on this model, we derive eLMFD to 19 identify and capture the energy consumption characteristics. Moreover, the microscopic model 20 serves as a plant model, i.e., reality, to test traffic control strategies. 21 There are three main parts in the microscopic LAAT model: (1) aircraft dynamics, (2) aircraft 22 route, and (3) collision avoidance. The aircraft dynamics are described by the kinematic equations 23 with states: position pA(t)and velocity vA(t), and the velocity command vc;A(t), which affect 24 the acceleration aA(t), for an aircraft Awith a motion in 3D space. Maximum velocity vm;Aand 25 acceleration am;Abounds are set for each aircraft. The aircraft route determines individual aircraft 26 routes, where each aircraft departs at a predefined time td;Afrom a predefined origin point OAto a 27 predefined destination point DA. A line between the two points is set as the original route ˜ pD;A. It 28 is important to note that the final route depends on the implemented collision avoidance algorithm. 29 A collision avoidance algorithm should control the aircraft to avoid collisions with other aircraft 30 or obstacles. To control LAAT aircraft, two types of space around each aircraft Aare defined: (i) 31 safety space SA, and (ii) avoidance space AA. The safety space SAis determined to avoid a conflict, 32 and the avoidance space AAis determined to start avoidance control. The aircraft avoids a collision 33 with a predefined safety radius rs;Aand avoidance radius ra;A, by determining the aircraft control 34 input vc;Ausing an Artificial Potential Field (APF) approach based on Lyapunov-like functions. In 35 addition, following a decentralized control approach, a detection space for each aircraft is defined. 36 The detection space DAof aircraft Ais centered in its position pA(t)with the detection radius 37 rd;A. The aircraft’s objective is to follow predefined waypoints and avoid collision with moving 38 obstacles. 39 The aircraft model has two properties: (i) conflict-free, i.e., even if an aircraft enters into the 40 safety space of another aircraft, it can keep away from the neighboring aircraft rapidly, and (ii) 41

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 7 -->

convergence to desired waypoints is guaranteed. Moreover, regarding practicability, the developed 1 control has three features: (i) a practical motion model is used, i.e., a double integrator model with 2 a velocity command as input is proposed for aircraft; (ii) detection of neighboring aircraft IDs of 3 an aircraft is not required by the control; and (iii) control saturation is imposed, i.e., the maximum 4 velocity command in the controller is restricted according to a priori determined requirement. Let 5 us now consider Naircraft in local airspace. Then, the movement dynamic can be described by the 6 following kinematic equations 7

$$
˙pA(t) =vA(t); (1) 8
$$

$$
˙v(t) = LA(vA(t) vc;A(t)); (2) 910
$$

where pA(t)2R3,vA(t)2R3,vc;A(t)2R3, and LA2R330 are the position, the velocity, the 11

$$
velocity command, and the control gain of aircraft A, respectively, A=1;2;:::; M. The control 12
$$

gain LAdepends on the technical properties of aircraft A, which can be obtained through flight 13 experiments, as done in Quan et al. (2021b,a). The velocity command vc;A(t)for aircraft Ashould 14 be constrained by the aircraft speed limit. Hence, a saturation function is defined as follows 15

$$
sat(vA(t);vm;A) =(
$$

vA(t);kvA(t)kvm;A vm;AvA(t) kvA(t)k;kvA(t)k>vm;A) (3) 16 with vm;A>0 is the maximum speed of aircraft A. The velocity command is derived from the 18 Artificial Potential Field (APF) approach; the reader can refer to Safadi et al. (2023) for further 19 descriptions. 20 Additionally, by aggregating the aircraft trajectories in the network, it is possible to iden21 tify the macroscopic level variables, to capture the airspace traffic conditions, and to construct 22 the Macroscopic Fundamental Diagram (MFD). We adopt the spatial structure that divides the 23 airspace into several vertical latitudes and each latitude into different regions, where in this work, 24 the airspace is considered as one layer and one region for simplicity. Furthermore, as shown in 25

#### Fig. 2, the MFD variables are calculated during a specific time interval DtM, i.e., each time interval 26

DtMthe aircraft trajectories are analyzed to determine the macroscopic traffic flow variables. 27 The main traffic characteristics and physics laws of vehicular traffic flow theory can be gener28 alized to aircraft traffic flow by adapting the one-spatial-dimensional flow to twoor three-spatial29 dimensional flow. We follow the generalized definitions of Edie (1963) to calculate the MFD vari30 ables. Using the aircraft trajectories, the travel time and distance of each aircraft for a fixed time 31 period are measured and aggregated, to calculate the main macroscopic traffic flow variables, i.e., 32 flow Q(t), density K(t), and speed V(t). In addition, other macroscopic traffic flow variables are 33 calculated, such as the accumulation n(t), outflow G(t), and production P(t), which are evaluated 34 according to the network borders and the position of aircraft. 35 Moreover, additional factors are estimated to determine the airspace performance, such as: 36 waiting times, queues, and delays. It is known in the literature that when comparing different 37 strategies, it is essential to compare the total traveled distance (TTD), total traveled time (TTT), 38 and total time spent (TTS) in the system, which can accurately reflect the system performance 39 by aggregating the travel distance, travel time, and waiting time of aircraft. By estimating these 40 macroscopic traffic flow variables, one can identify macroscopically the airspace state, i.e., if the 41

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 8 -->

airspace is in free flow or congestion conditions. This estimation allows us to model the airspace 1 dynamics, the outflow Gas a function of accumulation n, and based on that to develop a control 2 model, the accumulation-based MFD model, for the design of a feedback control strategy. 3

### 2.3 Energy consumption model for LAAT networks 4

In this research, we follow the energy consumption model presented in Thibbotuwawa et al. 5 (2018a) and adapt it to low-altitude aircraft, in order to estimate the total energy consumption 6 in the LAAT network. Note that the low-altitude aircraft is assumed to be a multicopter aircraft 7 (without wings), where the aerodynamic factors are minor compared to fixed-wing or tilt-wing 8 aircraft. 9 According to the proposed model in Thibbotuwawa et al. (2018a), while the aircraft is flying, 10 the energy needed to move in horizontal or vertical motion depends on different factors. The 11 aircraft design parameters, such as weight, width, air density, drag coefficient, and surface area of 12 the flying object, influence the aircraft energy consumption model. In recent studies, new models 13 distinguish between vertical motion with or against gravity, see e.g. Gong et al. (2023). It should be 14 stressed that more advanced models which fit different aircraft designs and types can be integrated 15 into the framework without altering the methodology. 16 Given the LAAT model-based operational framework, it is possible to calculate the aircraft 17

$$
energy consumption according to the current aircraft speed. The aircraft speed v= [vx;vy;vz]2R318
$$

can be normalized for the horizontal direction to align with the model in Thibbotuwawa et al. 19 (2018a) as follows 20

$$
Vxy=projxy(v): (4) 21
$$

Then, the power used for horizontal flying p h[W]can be calculated as follows 22 ph(Vxy) =0:5CDADVxy3+W2 DVxyb2; (5) 23 where CD[ ]is the drag coefficient of the aircraft, A[m2]is the front-facing area of the aircraft, 24

$$
D[kg=m3]is the air density in the low-altitude airspace level, W[kg]is the total weight of the 25
$$

aircraft, and b[m]is the rotor radius of the aircraft. The power used for vertical flying p v[W]can 26 be calculated as follows 27

$$
pv=(Wg)3=2
$$

p 2DA; (6) 28

$$
where g[m=s2]is the gravitational acceleration. 29
$$

Finally, the energy consumption of aircraft Afor the travel time tA(t), i.e., E A(t) [Wh], ac30 cording to the horizontal speed Vxy;A(t)at time t, is calculated as follows 31

$$
EA(t) =Zt
$$

t tA(t)  ph(Vxy;A(t))+pv dt: (7) 32

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 9 -->

Let us consider Naircraft in a space S. At the macroscopic level, the time is discretized according 1

$$
to an aggregation time DtM. Let k,k=1;2;:::, be the control time step and DtMthe control 2
$$

sample time. For a time period [(k 1)DtM;kDtM), the energy consumption for the whole 3 network E (k) [aircraftWh]can be aggregated according to the energy consumption of aircraft 4 EA(k);A21;:::; N, as follows, 5 E(k) =å A2SEA(k): (8) 6 The aggregation equation (8) highlights that the energy consumption depends on aircraft speed and 7 flight travel time in the network. Hence, it would be interesting to explore the relationship between 8 the energy consumption E and the average speed Vin the network. 9

### 2.4 eLMFD-centeric speed control methodology 10

Following the introduced LAAT model-based operational framework, a macroscopic model allows 11 us to capture the airspace conditions and model the aggregate behavior of aircraft flows in LAAT 12 networks. The proposed model can manipulate the maximum allowed speed of aircraft in different 13 regions of the network, e.g. Sirmatel and Yildirimoglu (2023b). The model can be utilized as 14 a control model to implement speed control strategies, aiming to optimize energy efficiency and 15 traffic conditions in LAAT operations. 16 For this reason, an eLMFD-based control model is developed, where the aggregate speed in 17 region iis influenced by a control input, namely the speed control input wi(t) [ ](i2R, where 18 Ris a set containing all regions in the network). The control input wi(t)determines the ratio of 19 the maximum speed limit applied to aircraft in region i, thereby controlling the macroscopic air 20 speed limit conditions, e.g. Sirmatel and Yildirimoglu (2023b). This regulation directly affects 21 the energy consumption and traffic performance of the network. The control input wi(t)modifies 22 the aircraft speed dynamically, according to the proposed framework, by influencing the speed23 dependent energy consumption model in the system. The actuation and implementation of the 24 control inputs will be described later in detail in this section. It should be stressed out that the 25 macroscopic speed control input wi(t)modifies the ratio of the maximum allowable speed in the 26 network, rather than directly setting an exact speed value. This ensures that the aircraft dynamically 27 adjust their velocities in response to changing airspace conditions. 28 In this section, we elaborate on the proposed accumulation-based (MFD-based) model, where: 29 (i) the macroscopic aircraft speed regulation is captured, i.e., a multi-region model for centralized 30 control approach; (ii) the influence of the speed control input wi(t)on macroscopic energy con31 sumption is formulated; (iii) the relationship between macroscopic accumulation ni, average speed 32 Vi, and energy consumption Eiis captured, integrating speed control as a decision variable. 33 The proposed macroscopic control model follows a conservation equation similar to con34 ventional MFD-based frameworks, adapted for speed control. The dynamics of accumulation of 35 traveling aircraft ni(t) [aircraft ]in a given region iis expressed as: 36

$$
˙ni(t) =di(t) Gi(ni(t))wi(t); (9) 37
$$

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 10 -->

$$
where di(t) [aircraft =s]is the aircraft inflow rate (demand) entering the region. Gi(ni(t)) [aircraft =s] 1
$$

is the outflow rate, which depends on the current aircraft accumulation ni(t)and calibrated param2 eters, derived based on the MFD concept as follows: 3

$$
Gi(ni(t)) = (vm
$$

a1)ni(t)exp(( 1 a2)(ni(t) a3)a2 ); (10) 4 where a1;a2;a3are estimated parameters based on eLMFD calibration. It is shown in this research 5 that the outflow is affected by the maximum speed vmin the airspace, see results in Section 3, 6 therefore by multiplying with the speed control input wi(t)can impact the conditions as desired. 7 Moreover, the function Gi(ni(t))includes a critical accumulation point nc;i, which represents the 8 aircraft accumulation level that maximizes the system outflow (throughput). This critical point de9 fines the capacity limit of the system, beyond which congestion effects degrade network efficiency, 10 leading to reduced throughput and increased delays. Thus, maintaining Gi(ni(t))near its maximum 11 value, denoted as Gm;i, is essential for ensuring both efficiency and operational stability. Corre12 spondingly, it is generally desirable to keep the current accumulation below the critical threshold, 13 i.e.,ni(t)nc;i, to prevent the onset of congestion and maintain smooth airspace operations. 14 In order to capture the energy consumption Ei(Vi)at the macroscopic level, first the aircraft 15 average speed Vi(ni)is determined by: 16 Vi(ni) =vm b1exp  ( 1 b2)(ni(t) b3)b2 ; (11) 17 where b1;b2;b3are empirical parameters defining the speed-accumulation relationship, known as 18 the speed-MFD. Then, the energy consumption Ei(Vi)can be determined by: 19 Ei(Vi) =vm c1exp  exp( Vi(t) c2)+c3 ; (12) 20 where c1;c2;c3are calibration parameters based on aircraft energy models. This formulation al21 lows us to establish the relationship between network energy consumption with the accumulation 22 as a function of the speed, i.e. Ei(Vi(ni(t))), which can be controlled in many optimal control prob23 lems such as optimizing aircraft speed to minimize energy consumption while ensuring smooth 24 traffic flow as function of energy-speed Ei(Vi)and speed-accumulation Vi(ni). Furthermore, the 25 energy function E (V)also contains operational critical points, namely E c;iand E OP;i. The criti26 cal energy consumption point E OP;iindicates the speed level at which the energy consumption is 27 efficient relatively to the traffic demand, whereas E c;idefines a threshold separating efficient and 28 non-efficient energy consumption regimes. When Ei(Vi(ni(t)))>Ec;i, the system operates in a 29 non-optimal regime where energy consumption increases disproportionately with respect to speed. 30 Therefore, maintaining Ei(Vi(ni(t)))around E OP;iis crucial for achieving both efficiency and op31 erational stability. Correspondingly, there exist critical speed points, namely Vc;iandVOP;i. The 32 speed VOP;iis associated with E OP;iand represents the optimal speed at which energy consumption 33 is most efficient in relation to the traffic state, while Vc;icorresponds to E cand marks the transition 34 between efficient and inefficient energy regimes. Ensuring that the system operates around VOP;i35 rather than exceeding Vc;iis essential to maintaining sustainable and balanced airspace operations. 36 Following (9), by extending the dynamics to the accumulation of traveling aircraft from region 37 ito region j, i.e. ni j(t) [aircraft ], the control model dynamics can be expressed as: 38

$$
˙ni j(t) =di j(t) bi j(t)Gi(ni(t))wi(t);8i;j2Ri j; (13) 39
$$

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 11 -->

$$
˙nii(t) =dii(t)+å
$$

j2Ri jbji(t)Gj(nj(t))wj(t) bii(t)Gi(ni(t))wi(t);8i2R; (14) 1

$$
˙ni(t) =˙nii(t)+å
$$

j2Ri j˙ni j(t);8i2R; (15) 2

$$
˙n(t) =å
$$

i2R˙ni(t); (16) 3 where ni j(t) [aircraft ]represents the accumulation of aircraft at time tin region iwith a destination 4

$$
in neighboring region j, and its time derivative is denoted by ˙ ni j(t) [aircraft =s]. The inflow rate 5
$$

$$
di j(t) [aircraft =s]accounts for new aircraft entering the region, while the outflow rate is depending 6
$$

on the speed-dependent function Gj(nj(t))wj(t), with the speed control input wi(t) [ ], and 7 adjusted by the weighting factor bi j(t) [ ], as shown in (13). Similarly, the accumulation of 8 aircraft remaining within the same region i, denoted by nii(t), evolves according to (14), where 9 the system accounts for internal inflows dii(t), inter-region transfer flows weighted by bji(t), and 10 internal departures adjusted by bii(t)andwi(t). The total accumulation in a region, denoted by 11 ni(t), aggregates the flows from both internal and external flows, as given in (15). Finally, the 12 total accumulation in the network is obtained by summing over all regions, as described in (16). 13 The control input wi(t)plays a critical role in adjusting the macroscopic aircraft speeds, thereby 14 influencing both the energy efficiency and the airspace throughput. 15 The LAAT system aims to operate efficiently while maintaining sustainability and minimum 16 energy consumption. In this study, the objective function JE(?) [aircraftWh]is chosen to minimize 17 the overall energy consumption in the network by dynamically adjusting aircraft speeds at the 18 macroscopic level. The introduced objective function consists of a single integral term, which can 19 be written as follows: 20 min

$$
wi(t)JE(?) =Ztf
$$

0 å i2RwEiEi  Vi(ni(t)) +å i2Rwwikwr;i wi(t)k2 dt; (17) 21 where E i(Vi(ni(t))) [Wh]represents the estimated macroscopic energy consumption function in 22 each region i2R, which depends on the current accumulation ni(t)and the corresponding speed 23 Vi(ni(t)). The weighting parameter wEi[ ]allows for adjusting the relative importance of energy 24 efficiency across different regions. To achieve this objective, the model optimally determines the 25 speed control input wi(t), which regulates the macroscopic speed of aircraft in each region by 26 modifying the speed-accumulation relationship. This is reflected in the accumulation given by 27 (13)-(16). To ensure feasible aircraft speed control and traffic stability, the optimization problem 28 is subject to the following constraints: 29 0ni j(t)ni j;8i;j2Ri j;0ni(t)ni;8i2R; (18) 30 wi jwi j(t)wi j;8i;j2Ri j; (19) 31 nii(0) =n0;ii;8i2R;ni j(0) =n0;i j;8i;j2Ri j;ni(0) =n0;i;8i2R: (20) 32 The states and control inputs in this problem are bounded as follows: First, the aircraft accu33 mulation ni(t)has a lower bound of zero and an upper bound ni[aircraft ], ensuring that aircraft 34 congestion remains within a feasible range, see (18). Additionally, the speed control input wi(t)is 35 constrained between wi jandwi j, which define the allowable range of macroscopic speed adjust36 ments, see (19). The initial conditions for the accumulation states are set according to (20). 37

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 12 -->

Thus, the objective function (17) is minimized subject to the system dynamics (13)-(16), the 1 constraints (18)-(19), and the initial conditions (20). The optimization problem is solved using 2 an MPC approach, where an optimal control sequence is determined over a prediction horizon Np 3 and applied in a feedback loop. The MPC controller continuously updates the speed control inputs 4 wi(t)based on real-time airspace conditions to minimize energy consumption while maintaining 5 efficient traffic flow. 6 The optimal control problem (13)-(16) and (17)-(20) is solved using a Model Predictive Con7 trol (MPC) approach. These macroscopic optimal control actions must be translated into individual 8 speed adjustments at the microscopic level using aircraft command and control subsystem. At each 9 simulation time step, once the optimal control inputs wi(t)are computed at the macroscopic level, 10 they are applied to the individual aircraft in the network. Specifically, for each aircraft present in 11 region iat time t, the commanded speed is updated as a function of the control input wi(t). This 12 is implemented by scaling the aircraft’s dynamic maximum speed v mwith the macroscopic speed 13 control ratio wi(t)and the original maximum speed vm 14 The speed update is performed in a loop over all aircraft in each region at every control step 15 DtC. Since the macroscopic MPC operates on a larger time scale than the microscopic updates, 16 the control inputs wi(t)are held constant between updates, ensuring consistent and smooth tran17 sitions in aircraft speed profiles. The algorithm for microscopic speed adjustments is described in 18 Algorithm 1. Algorithm 1 Description of the microscopic speed control algorithm Require: tkCurrent time step tk2[t0;tf],t0initial time, tffinal time , DtCcontrol step. Require: AAircraft index. Require: MactActive aircraft index set. Definition: wi(tk)Optimal macroscopic speed control input. Definition: Aircraft.rit Aircraft properties with current region index. Definition: vm;AAssigned aircraft maximum speed. Definition: v m;A(tk)Dynamic aircraft maximum speed. Definition: Aircraft.vm Aircraft properties with maximum speed value. 1:iftkmodDtCthen 2: wi(tk) MPC (?); 3:end if 4:for all A2fMactgdo 5: i Aircraft[ A].rit 6: v m;A(tk) wi(tk)vm;A; 7: Aircraft[ A].vm v A(tk); 8:end for To investigate and evaluate the performance of the MPC controller, we compare it with a 20 Greedy Control (GC) strategy. GC is a state-feedback control mechanism, where the control action 21 is determined based on the current accumulation ni(t)in region i. The strategy follows a threshold22 based policy relying on the critical accumulation nc;i, namely GC-G , and the critical speed Vc;i, 23 namely GC-E. The control input wi(t), which regulates the macroscopic speed in the network, 24 is adjusted based on these parameters. If the region is in a low-traffic regime, i.e., ni(t)<nc;i, 25

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 13 -->

the controller allows maximum speed utilization, meaning that the speed control input is set to its 1

$$
upper bound wi(t) =wi. Accordingly, if the region approaches congestion, i.e., ni(t)nc;i, the 2
$$

controller restricts the speed, reducing the control input for the incoming traffic from region jto 3

$$
region i, i.e., wj(t) =wj. Similarly, the control input can also be derived based on the critical speed 4
$$

threshold Vc;i. The critical speed Vc;irepresents the transition point between efficient and inefficient 5 energy consumption regimes. If the current average speed in the region is sufficiently high, i.e., 6

$$
Vi(t)Vc;i, the controller maintains maximum speed allocation, i.e., wi(t) =wi. However, if 7
$$

the region experiences a speed drop below the critical threshold, i.e., Vi(t)<Vc;i, the controller 8

$$
restricts the speed for incoming traffic by setting wj(t) =wjto prevent further deterioration of 9
$$

network conditions. This strategy ensures that speed adjustments are dynamically regulated to 10 prevent both excessive congestion and inefficient energy consumption, maintaining a stable and 11 sustainable LAAT network. 12 This methodology ensures that the aircraft movements remain consistent with the macroscopic 13 control strategy while preserving the flexibility needed for real-time dynamic adjustments. The 14 ability to modify aircraft speeds at each time step allows for fine-grained control over energy 15 consumption and traffic flow efficiency in LAAT operations. 16

## 3 Simulation results 17

To diagnose energy consumption in the LAAT network and examine the proposed eLMFD method18 ology, the LAAT-Flow simulation environment is extended to include aircraft energy consumption 19 model . The additional settings are described in Section 3.1. To estimate the relationship between 20 network energy consumption and average speed, one needs first to identify the airspace behavior 21 via traffic characteristics estimation. The identification methodology and results are presented in 22 Section 3.2. Furthermore, to demonstrate the potential behind eLMFD, a simplified case study 23 with the application of a hierarchical speed control strategy is presented in Section 3.3. In the 24 following, we focus on describing the inputs only; a detailed description of the framework and its 25 components is provided in Safadi et al. (2023, 2024c); Safadi and Haddad (2024). 26

### 3.1 Simulation setup 27

Different settings and inputs are required to configure the simulations for the traffic analysis, such 28 as aircraft, airspace, and traffic and simulation settings. These inputs are fed to the plant model, the 29 control model, and the controllers. It is possible to conduct a wide range of analyzes and studies of 30 the plant model’s outputs, but in this study, our main interest is the aircraft trajectories and speeds. 31 The aircraft trajectories construct the MFD variables, and the aircraft speeds construct the eLMFD 32 variables. Additional information from the plant model is used for the aircraft command system, 33 such as the aircraft state (departing, traveling, arriving, and queuing) and the aircraft entrance time. 34 It is noteworthy that the LAAT-Flow simulation can effectively simulate the traffic characteristics 35 of LAAT systems using different algorithms, aircraft settings, and airspace settings. Hence, the 36 simulation settings for the following case study are resolved to explore ECM and eLMFD for low37 altitude airspace; where flight is permitted with the X-Y-Z space and the network area is set to 38

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 14 -->

be 1:5[km]by 1:5[km]by 120 [m]. For the identification results, the airspace is considered as 1 a single-layer, single-region 3D network. For the control results, the airspace is divided into two 2 regions within a single layer: the city center (region 1) and the periphery (region 2). 3 Additionally, the aircraft energy consumption model described in Section 2.3 requires ad4 ditional settings related to the aircraft parameters along with the environment coefficients. In 5 this study, the following values are chosen based on Qi et al. (2020): the drag coefficient CDis 6 0:025[ ], the rotor radius bis 0:25[m], the front-facing area Ais 0:2[m2], and the total weight of 7 the aircraft (including the battery, payload, and frame) Wis 3:5[kg]. Additionally, the air density 8

$$
can be approximated as D=1:2[kg=m3]and the gravitational acceleration as g=9:8[m=s2]. 9
$$

### 3.2 Identification results 10

Several case study examples are presented to construct eLMFD curves for a LAAT system. The 11 traffic behavior of each LAAT aircraft is is described by the microscopic model presented in Sec12 tion 2.2 and Safadi et al. (2023). Based on the simulated data results, the MFD is constructed by 13 using the Generalized Edie’s definitions, see Edie (1963), to estimate the MFD variables, accord14 ing to Section 2.2 and Safadi et al. (2023). Additionally, the eLMFD is constructed by utilizing the 15 ECM presented in Section 2.3. 16 Following the setup in Section 3.1, where the airspace is considered as a single-layer single17 region 3D network, we investigate the effect of aircraft maximum speed on the eLMFD curves, 18 where the analysis is conducted for different aircraft maximum speeds. This section presents 19 four case studies to introduce the eLMFD curves. First, the following three different values are 20

$$
analyzed: (Ex.1) vm=20[m=s], (Ex.2) vm=10[m=s], and (Ex.3) vm=30[m=s]. Additionally, 21
$$

it is essential to investigate the effect of heterogeneous traffic on eLMFD; therefore, we relax the 22 assumption that all aircraft have the same maximum speed value, as they are randomly chosen, 23

$$
and in (Ex.4), the aircraft maximum velocity is varied for each aircraft within the range of vm= 24
$$

$$
f10;30g[m=s]. 25
$$

Each case study example is evaluated from different simulation scenarios (up to 36 scenarios), 26 as each scenario has a different maximum inflow rate in the traffic inflow q(t)profile, where the 27

$$
maximum inflow rate value qmvaries from 0 :5[aircraft =s]to 40 [aircraft =s]. Each point is an 28
$$

aggregated value of 60 [s]of simulated data. 29 From a traffic control perspective, it is interesting to estimate the relation between the 30 accumulation nand outflow G(n), as observed in Fig. 3(a), we estimate the following re31

$$
lation: G(n) = (20
$$

430)nexp  ( 1:40((n 177)0:49)) , with the critical point (nc;Gm)equals to 32

$$
(372[aircraft ];2:3[aircraft =s]). Additionally, the relation between the accumulation nand speed 33
$$

V(n)is essential for deriving the eLMFD. As observed in Fig. 3(b), we estimate the following rela34

$$
tion: V(n) = (20
$$

1:44)exp  ( 0:89((n 336)1:12))+0:03 . The goal of this study is to explore how the 35 aggregate energy consumption in the network E is related to the speed V, as it is the main factor 36 affecting the energy consumption in ECM. The relation is presented in Fig. 3(c). As expected, 37 the results show an inverse relationship: as speed decreases, energy consumption increases. The 38 key contribution of this research is the ability to determine the relationship between speed V, and 39 energy consumption E (V). We have derived the following equation to describe this relationship: 40

$$
E(V) = (20
$$

0:0011)exp  ( V 0:73)+0:01 , where the steady-state energy consumption E ssis identified 41

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 15 -->

as 243 :1[aircraftWh]. 1

## 0 1000 2000 3000 4000 500000.511.522.533.5

## 0 1000 2000 3000 4000 5000051015202530

## 0 5 10 15 20 25 3000.511.522.5104

(a) (b) (c)

#### Figure 3: (Ex.1) Simulation results for VTOL aircraft with a maximum speed vm=20[m=s]: (a)

Outflow Gvs. Accumulation n, (b) Speed Vvs. Accumulation n, and (c) Energy E vs. Speed V. It is important to note that the energy consumption of an aircraft depends on both its travel 2 distance and travel time. At the network level, it is also affected by the number of aircraft present. 3 Recall that E [aircraftWh]is defined as the aggregated energy consumption in the network. Con4 sequently, it is worthwhile to investigate the values of E that are normalized by the following 5 factors within a given time period: (i) Accumulation, which is denoted as E n[Wh]; (ii) total travel 6

$$
time (TTT), which is denoted as E t[Wh=s]; (iii) total travel distance (TTD), which is denoted as 7
$$

$$
Ed[Wh=m]. The findings are illustrated in Fig. 4(a), (b), and (c), respectively. 8
$$

## 0 5 10 15 20 25 300.511.522.533.54

## 0 5 10 15 20 25 300.020.0250.030.0350.040.0450.050.0550.060.065

## 0 5 10 15 20 25 3000.10.20.30.40.50.60.70.80.91

(a) (b) (c)

#### Figure 4: (Ex.1) Simulation results for VTOL aircraft with a maximum speed vm=20[m=s]: (a)

Energy normalized by accumulation E n[Wh]vs. Speed V, (b) Energy normalized by total travel

$$
time E t[Wh=s]vs. Speed V, and (c) Energy normalized by total travel distance E d[Wh=m]vs.
$$

Speed V. The MFD and eLMFD curves and relations are also valid for different maximum speeds. The 9

$$
results for aircraft maximum speed vm=10[m=s]are presented in Fig. 5, and for aircraft maximum 10
$$

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 16 -->

$$
speed vm=30[m=s]are presented in Fig. 6. Note that for high maximum speed the aircraft finish 1
$$

their flight faster, and therefore, the network capacity increases. 2

## 0 1000 2000 3000 4000 5000 600000.20.40.60.811.21.41.61.8

## 0 1000 2000 3000 4000 5000 6000051015202530

## 0 5 10 15 20 25 3000.511.522.533.5104

(a) (b) (c)

#### Figure 5: (Ex.2) Simulation results for VTOL aircraft with a maximum speed vm=10[m=s]: (a)

Outflow Gvs. Accumulation n, (b) Speed Vvs. Accumulation n, and (c) Energy E vs. Speed V.

## 0 1000 2000 3000 4000 5000 600000.511.522.533.544.5

## 0 1000 2000 3000 4000 5000 6000051015202530

## 0 5 10 15 20 25 3000.511.522.53104

(a) (b) (c)

#### Figure 6: (Ex.3) Simulation results for VTOL aircraft with a maximum speed vm=30[m=s]: (a)

Outflow Gvs. Accumulation n, (b) Speed Vvs. Accumulation n, and (c) Energy E vs. Speed V.

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 17 -->

## 0 1000 2000 3000 4000 500000.511.522.53

## 0 1000 2000 3000 4000 5000051015202530

## 0 5 10 15 20 25 3000.511.522.5104(a) (b) (c)

#### Figure 7: (Ex.4) Simulation results for VTOL aircraft with varied maximum speed vm=

$$
f10;30g[m=s]: (a) Outflow Gvs. Accumulation n, (b) Speed Vvs. Accumulation n, and (c)
$$

Energy E vs. Speed V.

### 3.3 eLMFD-centric control strategies results 1

The performance of the LAAT system is significantly influenced by the implementation of speed 2 control strategies. In this section, the results for different control strategies No Control (NC), 3 Greedy Controller with nc;i(GCG), Greedy Controller with Vc;i(GC-E), and Model Predictive 4 Controller (MPC) are analyzed and compared in terms of energy efficiency and airspace perfor5 mance. 6 The results were obtained for a single-layer two-region 3D airspace network, where aircraft 7 speed adjustments were applied at the macroscopic level and translated into individual speed mod8 ifications at the microscopic level. The system parameters, including critical accumulation points 9 nc;iand critical speed thresholds Vc;i, were determined based on the estimated energy-speed re10 lationship. The developed control strategies are tested and simulated with the same setting with 11

$$
inflow rate qm=2:5[aircraft =s]. Note that according to the airspace identification, the estimated 12
$$

$$
maximum outflow (capacity) is Gm=2:3[aircraft =s], therefore the conditions in the system are 13
$$

over-saturated. Additionally, the following information is needed for the implementation: the 14

$$
accumulation lower bounds are set to zero, and the upper bounds are n1=135[aircraft ];n2= 15
$$

$$
577[aircraft ]; the speed control input lower bounds are w1=0:62[ ];w2=0:76[ ]and the upper 16
$$

$$
bounds are wi=1[ ]; the critical accumulations are nc;1=45[aircraft ];nc;2=192[aircraft ]; the 17
$$

$$
critical speeds are Vc;1=7:1667 [m=s];Vc;2=8:7500 [m=s]; the control reference values are wr;i= 18
$$

$$
1[ ]; the weighting factors are calibrated as follows: wEi=1[ ],ww1=35:5155 [aircraftWh] 19
$$

$$
andww2=122:6110 [aircraftWh]. 20
$$

The total time spent (TTS) and the total energy consumption across the network for different 21 control strategies are presented in Fig. 8. The TTS metric captures the overall efficiency of the 22 airspace network with respect to travel delays, while the total energy consumption reflects the 23 effectiveness of speed control strategies in optimizing energy use. The results demonstrate that the 24 MPC-based strategy achieves the lowest energy consumption while maintaining efficient traffic 25 performance. The greedy control strategies (GCGand GC-E) perform better than the no-control 26

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 18 -->

case but lack the adaptability of the MPC approach. 1 NC GC-GGC-E MPC01 0.87 0.660% -12%-15% -34% Percentage compared to NC NC GC-GGC-E MPC08.11 7.01

#### 5.329.74 * 105TTS [aircraft * s]

NC GC-GGC-E MPC01 0.830.77 0.570% -17%-23% -43% Percentage compared to NC NC GC-GGC-E MPC04.38 3.653.37

#### 2.485.26 * 104E [aircraft * Wh]

(a) (b)

#### Figure 8: Simulation results for comparing different control strategies - No Control (NC), Greedy

Controller with nc;i(GCG), Greedy Controller with Vc;i(GC-E), and Model Predictive Controller (MPC): (a) Total Time Spent (TTS), (b) Total energy consumption in the network. The macroscopic traffic flow characteristics under different control strategies are illustrated in 2

#### Fig. 9. The relationship between outflow Gand accumulation n(Fig. 9(a)) reveals that the MPC 3

controller effectively maintains accumulations below critical levels, preventing congestion and en4 suring high throughput. Similarly, the speed Vvs. accumulation nrelationship (Fig. 9(b)) shows 5 that MPC maintains higher speed profiles across different accumulation levels. The energy con6 sumption E vs. speed Vrelationship (Fig. 9(c)) indicates that the MPC strategy optimally regulates 7 speeds to operate in the energy-efficient range, avoiding excessive energy use at suboptimal speed 8 levels. 9

## 0 100 200 300 40000.511.522.533.54

## 0 100 200 300 40002468101214161820

## 0 5 10 15 200200400600800100012001400160018002000

(a) (b) (c)

#### Figure 9: Simulation results for comparing different control strategies - No Control (NC), Greedy

Controller with nc;i(GCG), Greedy Controller with Vc;i(GC-E), and Model Predictive Controller (MPC): (a) Outflow Gvs. Accumulation n, (b) Speed Vvs. Accumulation n, and (c) Energy E vs. Speed V.

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 19 -->

Further analysis of the control inputs, state evolution, and airspace performance is presented 1 in Fig. 10. The simulation results show how the speed control inputs widynamically adjust aircraft 2 speeds in response to changing accumulation levels, ensuring efficient outflow Giwhile minimiz3 ing energy consumption E i. The MPC strategy outperforms the greedy controllers by proactively 4 adapting to dynamic traffic conditions. In contrast, the GCGand GC-E strategies rely solely on 5 predefined thresholds, limiting their optimality under varying demand. 6 These findings emphasize the importance of speed control in managing airspace energy effi7 ciency and traffic performance. The results confirm that an MPC-based control strategy effectively 8 balances speed adjustments to optimize energy consumption while maintaining efficient through9 put. The comparison with greedy control strategies highlights the advantage of predictive control 10 in mitigating congestion and avoiding excessive energy use. 11 Overall, the study suggests that integrating speed control into the LAAT system through 12 eLMFD-based strategies can significantly improve both operational efficiency and sustainability. 13 The MPC strategy proves to be the most effective in reducing energy consumption while ensuring 14 smooth traffic conditions, making it a promising approach for future air traffic management. 15

## 4 Summary and Concluding Remarks 16

This paper investigates the energy efficiency of LAAT networks by integrating an aircraft energy 17 consumption model (ECM) into the LAAT model-based operational framework. By incorporating 18 macroscopic energy modeling, the study derives the eLMFD, which enables a systematic evalu19 ation of the relationship between energy consumption, aircraft speed, and accumulation in urban 20 airspace networks. The results highlight that energy consumption follows a structured macro21 scopic pattern, allowing the identification of critical operational points such as Ec(critical energy 22 threshold), EOP(optimal energy level), Vc(critical speed), and VOP(optimal speed). These findings 23 offer a new perspective on managing energy consumption in air mobility operations and establish 24 a foundation for developing energy-efficient traffic control strategies. 25 To optimize energy efficiency and airspace performance, this study proposes eLMFD-centric 26 speed control strategies, including No Control (NC), Greedy Controller based on nc;i(GCG), 27 Greedy Controller based on Vc;i(GC-E), and Model Predictive Controller (MPC). Simulation re28 sults demonstrate that MPC significantly outperforms other strategies by achieving the lowest en29 ergy consumption, maintaining efficient throughput, and minimizing congestion effects. MPC’s 30 ability to dynamically adjust aircraft speeds in response to real-time airspace conditions enables 31 operation within energy-optimal regions, reducing unnecessary power usage and ensuring sustain32 able LAAT operations. The results confirm that macroscopic speed control plays a critical role 33 in balancing energy efficiency and network capacity, and highlight the advantages of predictive 34 control over static threshold-based approaches. 35 The findings of this study underscore the potential of energy-aware macroscopic traffic control 36 for improving the sustainability of air mobility systems. The eLMFD framework provides a scal37 able and computationally efficient method for integrating energy consumption considerations into 38 traffic management strategies, paving the way for more efficient and environmentally responsible 39 urban airspace operations. Overall, the presented results highlight that energy-conscious airspace 40

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 20 -->

05001000150020002500300035000.70.80.91 050010001500200025003000350005010015020005001000150020002500300035000.70.80.91 0500100015002000250030003500050100150200Figure 10: Simulation results of the control inputs, states, and airspace performance: Speed Control Inputs wi, Accumulation ni, Outflow Gi, Speed Vi, Energy E i, in regions 1 ;2 obtained from different strategies: No Control (NC), Greedy Controller with nc;i(GCG), Greedy Controller with Vc;i(GC-E), and Model Predictive Controller (MPC).

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 21 -->

management is essential for the successful deployment and operation of future urban air mobility 1 networks. 2 Acknowledgment 3 The research presented in this paper was partially funded by the Technion, the ISTRC, and the 4 EuroTech Alliance. 5 Data and Code Availability 6 Supporting data, code, and the simulation software are available from the authors upon reasonable 7 request via the website T-SMART (2023). 8 References 9 Abeywickrama, H. V ., Jayawickrama, B. A., He, Y ., and Dutkiewicz, E. (2018). Comprehensive 10 energy consumption model for unmanned aerial vehicles, based on empirical studies of battery 11 performance. IEEE Access , 6:58383-58394. 12 Ahmed, S. S., Fountas, G., Lurkin, V ., Anastasopoulos, P. C., Bierlaire, M., and Mannering, F. L. 13 (2023). The state of urban air mobility research: An assessment of challenges and opportunities. 14 Barmpounakis, E., Montesinos-Ferrer, M., Gonzales, E. J., and Geroliminis, N. (2021). Empirical 15 investigation of the emission-macroscopic fundamental diagram. Transportation Research Part 16 D: Transport and Environment , 101:103090. 17 Beigi, P., Rajabi, M. S., and Aghakhani, S. (2022). An overview of drone energy consumption 18 factors and models. In Handbook of Smart Energy Systems , pages 1-20. Springer International 19 Publishing. 20 Brown, A. and Harris, W. L. (2020). Vehicle design and optimization model for urban air mobility. 21 Journal of Aircraft , 57(6):1003-1013. 22 Chen, C., Geroliminis, N., and Zhong, R. (2024). An iterative adaptive dynamic programming 23 approach for macroscopic fundamental diagram-based perimeter control and route guidance. 24 Transportation Science , 58(4):896-918. 25 Cohen, A. and Shaheen, S. (2023). Future of aviation: Advancing aerial mobility through technol26 ogy, sustainability, and on-demand flight. 27 Cohen, A. P., Shaheen, S. A., and Farrar, E. M. (2021). Urban air mobility: History, ecosystem, 28 market potential, and challenges. IEEE Transactions on Intelligent Transportation Systems , 29 22(9):6074-6087. 30

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 22 -->

Doole, M., Ellerbroek, J., and Hoekstra, J. (2020). Estimation of traffic density from drone-based 1 delivery in very low level urban airspace. Journal of Air Transport Management , 88:101862. 2 Edie, L. (1963). Discussion of traffic stream measurements and definitions. In Almond, J. (Ed.). 3 Proceedings of the 2nd International Symposium on the Theory of Traffic Flow , pages 139-154, 4 OECD, Paris, France. 5 FAA NextGen Organization (2023). Urban Air Mobility (UAM) Concept of Operations v2.0. 6 Filippone, A. and Barakos, G. (2020). Rotorcraft systems for urban air mobility: A reality check. 7 The Aeronautical Journal , 125(1283):3-21. 8 Fontes, T., Pereira, S., Fernandes, P., Bandeira, J., and Coelho, M. (2015). How to combine 9 different microsimulation tools to assess the environmental impacts of road traffic? lessons and 10 directions. Transportation Research Part D: Transport and Environment , 34:293-306. 11 Fu, M., Straubinger, A., and Schaumeier, J. (2022). Scenario-based demand assessment of urban 12 air mobility in the greater munich area. Journal of Air Transportation , 30(4):125-136. 13 Geroliminis, N. and Daganzo, C. F. (2008). Existence of urban-scale macroscopic fundamental 14 diagrams: some experimental findings. Transportation Research Part B , 42(9):759-770. 15 Gong, H., Huang, B., Jia, B., and Dai, H. (2023). Modelling power consumptions for multi-rotor 16 UA Vs. IEEE Transactions on Aerospace and Electronic Systems , pages 1-14. 17 Haddad, J., Mirkin, B., and Assor, K. (2021). Traffic flow modeling and feedback control for 18 future low-altitude air city transport: An MFD-based approach. Transportation Research Part 19 C: Emerging Technologies , 133:103380. 20 Johari, M., Keyvan-Ekbatani, M., Leclercq, L., Ngoduy, D., and Mahmassani, H. S. (2021). 21 Macroscopic network-level traffic models: Bridging fifty years of development toward the next 22 era.Transportation Research Part C: Emerging Technologies , 131:103334. 23 Kasliwal, A., Furbush, N., Gawron, J., McBride, J., Wallington, T., De Kleine, R., Kim, H., and 24 Keoleian, G. (2019). Role of flying cars in sustainable mobility. Nature Communications , 10(1). 25 Kopardekar, P. (2017). Safely enabling uas operations in low-altitude airspace. 26 Moore, M. D. (2012). Concept of operations for highly autonomous electric zip aviation. In 27 12th AIAA Aviation Technology, Integration, and Operations (ATIO) Conference and 14th 28 AIAA/ISSMO Multidisciplinary Analysis and Optimization Conference . American Institute of 29 Aeronautics and Astronautics. 30 Pradeep, P. and Wei, P. (2019). Energy-efficient arrival with RTA constraint for multirotor eVTOL 31 in urban air mobility. Journal of Aerospace Information Systems , 16(7):263-277. 32 Pukhova, A. (2018). Environmental evaluation of urban air mobility operation . PhD thesis, Tech33 nical University of Munich (TUM) Munich, Germany. 34 PwC (2023). Advanced air mobility uk economic impact study. 35

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 23 -->

Qi, H., Hu, Z., Huang, H., Wen, X., and Lu, Z. (2020). Energy efficient 3-d UA V control for 1 persistent communication service and fairness: A deep reinforcement learning approach. IEEE 2 Access , 8:53172-53184. 3 Qi, X. and Zhang, Y . (2016). Data-driven macroscopic energy consumption estimation for electric 4 vehicles with different information availability. In 2016 International Conference on Computa5 tional Science and Computational Intelligence (CSCI) . IEEE. 6 Quan, Q., Fu, R., and Cai, K.-Y . (2021a). Practical control for multicopters to avoid non7 cooperative moving obstacles. IEEE Transactions on Intelligent Transportation Systems , pages 8 1-19. 9 Quan, Q., Fu, R., Li, M., Wei, D., Gao, Y ., and Cai, K.-Y . (2021b). Practical distributed control for 10 VTOL UA Vs to pass a virtual tube. IEEE Transactions on Intelligent Vehicles , pages 1-1. 11 Rodriguez-Rey, D., Guevara, M., Linares, M. P., Casanovas, J., Salmer ´on, J., Soret, A., Jorba, O., 12 Tena, C., and Garc ´ıa-Pando, C. P. (2021). A coupled macroscopic traffic and pollutant emission 13 modelling system for barcelona. Transportation Research Part D: Transport and Environment , 14 92:102725. 15 Ronald Berger (2020). Urban air mobility. 16 Safadi, Y ., Fu, R., Quan, Q., and Haddad, J. (2023). Macroscopic fundamental diagrams for low17 altitude air city transport. Transportation Research Part C: Emerging Technologies , 152:104141. 18 Safadi, Y ., Geroliminis, N., and Haddad, J. (2024a). Integrated departure and boundary control 19 for low-altitude air city transport systems. Transportation Research Part B: Methodological , 20 189:103020. 21 Safadi, Y ., Geroliminis, N., and Haddad, J. (2024b). Integrated departure and boundary control 22 for low-altitude air city transport systems. Transportation Research Part B: Methodological , 23 189:103020. 24 Safadi, Y ., Geroliminis, N., and Haddad, J. (2024c). Integrated departure and boundary control for 25 low-altitude air city transport systems. under review. 26 Safadi, Y . and Haddad, J. (2024). Overview and perspectives of air mobility operations and simu27 lation tools. IFAC-PapersOnLine , 58(10):296-301. 28 She, X. T. P., Lin, X., and Lang, H. (2020). A data-driven power consumption model for electric 29 UA Vs. In 2020 American Control Conference (ACC) . IEEE. 30 Silva, I. D. D. and Caillouet, C. (2020). Optimizing the trajectory of drones: trade-off between 31 distance and energy. In 2020 IEEE International Conference on Sensing, Communication and 32 Networking (SECON Workshops) . IEEE. 33 Sirmatel, I. I., Tsitsokas, D., Kouvelas, A., and Geroliminis, N. (2021). Modeling, estimation, 34 and control in large-scale urban road networks with remaining travel distance dynamics. Trans35 portation Research Part C: Emerging Technologies , 128:103157. 36

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 24 -->

Sirmatel, I. I. and Yildirimoglu, M. (2023a). Nonlinear model predictive control of large-scale 1 urban road networks via average speed control. Transportation research part C: emerging tech2 nologies , 156:104338. 3 Sirmatel, I. I. and Yildirimoglu, M. (2023b). Nonlinear model predictive control of large-scale 4 urban road networks via average speed control. Transportation Research Part C: Emerging 5 Technologies , 156:104338. 6 Straubinger, A., Rothfeld, R., Shamiyeh, M., Bchter, K.-D., Kaiser, J., and Pltner, K. O. (2020). 7 An overview of current research and developments in urban air mobility setting the scene for 8 UAM introduction. Journal of Air Transport Management , 87:101852. 9 Straubinger, A., Verhoef, E. T., and de Groot, H. L. (2021). Will urban air mobility fly? the effi10 ciency and distributional impacts of UAM in different urban spatial structures. Transportation 11 Research Part C: Emerging Technologies , 127:103124. 12 T-SMART (2023). LAAT-Flow project, website: https://sites.google.com/view/laat-flow/. 13 Takemura, R., Aoki, N., and Ishigami, G. (2023). Energy-and-perception-aware planning and 14 navigation framework for unmanned aerial vehicles. Advances in Mechanical Engineering , 15 15(4):168781322311696. 16 Thibbotuwawa, A., Nielsen, P., Zbigniew, B., and Bocewicz, G. (2018a). Energy consumption 17 in unmanned aerial vehicles: A review of energy consumption models and their relation to the 18 UA V routing. In Advances in Intelligent Systems and Computing , pages 173-184. Springer 19 International Publishing. 20 Thibbotuwawa, A., Nielsen, P., Zbigniew, B., and Bocewicz, G. (2018b). Factors affecting energy 21 consumption of unmanned aerial vehicles: An analysis of how energy consumption changes in 22 relation to UA V routing. In Advances in Intelligent Systems and Computing , pages 228-238. 23 Springer International Publishing. 24 Wang, L., Ding, H., Zheng, N., and Zheng, X. (2025). Two-layer control strategy response to 25 regional cyberattacks on large-scale road networks in a connected vehicle environment. Trans26 portation Research Part C: Emerging Technologies , 174:105116. 27 Wang, Y ., Biswas, K., Zhang, L., Ghazzai, H., and Massoud, Y . (2022). 3d autonomous navigation 28 of UA Vs: An energy-efficient and collision-free deep reinforcement learning approach. In 2022 29 IEEE Asia Pacific Conference on Circuits and Systems (APCCAS) . IEEE. 30 Weng, C., Chen, C., Tan, J., Pan, T., and Zhong, R. (2024). Real-time traffic simulation and man31 agement for large-scale urban air mobility: Integrating route guidance and collision avoidance. 32 arXiv preprint arXiv:2412.01235 . 33 Yan, H., Chen, Y ., and Yang, S.-H. (2021). New energy consumption model for rotary-wing UA V 34 propulsion. IEEE Wireless Communications Letters , 10(9):2009-2012. 35

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$

<!-- page 25 -->

Zegeye, S., Schutter, B. D., Hellendoorn, J., Breunesse, E., and Hegyi, A. (2013). Integrated 1 macroscopic traffic flow, emission, and fuel consumption model for control purposes. Trans2 portation Research Part C: Emerging Technologies , 31:158-171. 3 Zhang, N., Zhang, M., and Low, K. H. (2021). 3d path planning and real-time collision resolution 4 of multirotor drone operations in complex urban low-altitude airspace. Transportation Research 5 Part C: Emerging Technologies , 129:103123. 6

$$
This preprint research paper has not been peer reviewed. Electronic copy available at: https://ssrn.com/abstract=5237517Preprint not peer reviewed
$$
