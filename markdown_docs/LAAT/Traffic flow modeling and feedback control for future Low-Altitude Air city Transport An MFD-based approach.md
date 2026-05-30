---
source_pdf: Traffic flow modeling and feedback control for future Low-Altitude Air city Transport An MFD-based approach.pdf
pages: 20
---

# Traffic flow modeling and feedback control for future Low-Altitude Air city Transport An MFD-based approach

<!-- page 1 -->

Transportation Research Part C 133 (2021) 103380 Available online 17 November 2021 0968-090X/© 2021 Elsevier Ltd. All rights reserved. Contents lists available at ScienceDirect Transportation Research Part C journal homepage: www.elsevier.com/locate/trc Traffic flow modeling and feedback control for future Low-Altitude Air city Transport: An MFD-based approach Jack Haddad∗, Boris Mirkin, Kfir Assor Technion-Israel Institute of Technology, Faculty of Civil and Environmental Engineering, Technion Sustainable Mobility and Robust Transportation (T-SMART) Laboratory, Israel

### A R T I C L E I N F O

Keywords: Air mobility Drones Macroscopic Fundamental Diagram Boundary control Distributed adaptive controlA B S T R A C T The imminent penetration of low-altitude passenger and delivery aircraft into the urban airspace will give rise to new urban air transport systems, which we call low-altitude air city transport (LAAT) systems. As the urban mobility revolution approaches, we must investigate (i) the collective behavior of LAAT aircraft in cities, and (ii) ways of controlling LAAT systems. Future LAAT systems exemplify a new class of modern large scale engineering systems networked control systems. They are spatially distributed, consist of many interconnected elements with control loops through digital communication networks such that the system signals can be exchanged among all components through a common network. Therefore, a decentralized controller design in framework of the unilateral event-driven paradigm is considered. Inspired by controlled urban road networks, in this paper we first establish the concept of Macroscopic Fundamental Diagram (MFD) for LAAT systems and develop a collective and aggregate aircraft traffic flow model. Then, based on that, we design an adaptive boundary feedback flow control which is robust to various anomalies in technical devices and network communication links for LAAT systems.

## 1. Introduction

Low-altitude aircraft are being developed as a new mode of urban transport. The penetration of low-altitude passenger and delivery aircraft into the urban airspace is inevitable in the near future, with estimated 100,000 passenger drones could be in service worldwide by 2050, ( Berger , 2018 ). It will give rise to new urban air transport systems , which we call low-altitude air city transport (LAAT) systems, see Fig. 1(b). Such systems will include aircraft operated with or without pilots, transferring passengers and goods in urban areas. As a result, we will enter the new era of urban air mobility. Similar to road transport systems, increasing numbers of passenger and delivery aircraft will cause urban air traffic congestion, and raise new air traffic control challenges. Therefore, as the urban mobility revolution approaches, we must investigate (i) the collective behavior of LAAT aircraft in cities, and (ii) ways of controlling LAAT systems. The key flow-oriented differences between ground traffic and low-altitude air traffic: (i) direction and dimensionality future aircraft will have multi-directional flows traveling in the 3rd dimension; (ii) interaction aircraft interaction is expected to be structured by new air traffic rules; and (iii) operation the motion dynamics of aircraft are different than cars, and the aircraft are expected to be operated with or without pilots. Current air transportation management schemes are limited to conventional airplane operations, see Fig. 1(a). They are based on centralized control structures for airspace regions, i.e. controllers (human operators) are responsible for ensuring that the air traffic can move safely and efficiently throughout the airspace. This implies rigid individual trajectory-based operations, with fixed routes ∗Correspondence to: Technion-Israel Institute of Technology, Rabin building, Room 726, Haifa, Israel. E-mail address: jh@technion.ac.il (J. Haddad). https://doi.org/10.1016/j.trc.2021.103380 Received 17 December 2020; Received in revised form 5 September 2021; Accepted 5 September 2021

<!-- page 2 -->

Transportation Research Part C 133 (2021) 103380 2J. Haddad et al.

#### Fig. 1. Concept: Controlling flows of aircraft traffic, rather than individual aircraft: (a) conventional airplanes are individually controlled with centralized structure

under rigid individual operations, (b) future urban low-altitude air transport (LAAT) aircraft will be aggregately controlled under flexible aircraft flow operations. and preplanned and approved aircraft schedules, while ensuring conflict detection and resolution in the airspace. On the other hand, the operation of future LAAT systems is expected to be more flexible, allowing e.g. on-demand point-to-point urban travel or delivery, with a higher total number of daily short trips, under a more complex urban environment with energy consumption constraints, in addition to noise and weather considerations. The LAAT aircraft is also expected to be operated under congested traffic conditions , given the large number of passenger and delivery aircraft traveling in a limited allowed urban airspace capacity. Moreover, the future aircraft will have a unique flight dynamic property, i.e. hovering , which is one of the key differences between drones and conventional aircraft or airplanes. In congested airspace regions, hovering drones will introduce aircraft interaction effects and queueing dynamics, e.g. a platoon of drones waiting to enter the parking, which should be efficiently controlled. In addition, LAAT system operations will be carried out combining new physical and network facilities, strong interdependencies between various infrastructures, and use of communication technologies, which will increase the system vulnerability for uncertainties, failures, and cyberattacks. Therefore, large-scale LAAT controlled networks should be robust for various anomalies in technical devices and network communication links. The latter is crucial to increase safety and the community trust and acceptance for such future systems. Given these main operational differences between conventional airplane and LAAT systems, future aircraft cannot be managed by the current or adapted aircraft management schemes, as they will deteriorate the traffic performance of LAAT systems. Therefore, and inspired by controlled urban road networks, we suggest to address future air congestion problems based on a new operational concept :flows of aircraft traffic, rather than individual aircraft, should be controlled , see Fig. 1. In this paper, our solution is to develop traffic flow model and feedback control theory for LAAT systems. Despite the impending advent of LAAT aircraft in the near future, traffic flow models concerning the aggregated behavior of aircraft flows in large-scale networks, e.g. relating average flow to density, have not been developed. Hence, to address this important issue, in this paper we first establish the concept of Macroscopic Fundamental Diagram (MFD), which is widely used for ground urban traffic modeling, for LAAT systems. Over the last decade, substantial contributions have been made in the area of modeling and control of MFD for urban traffic networks, e.g. Daganzo (2007 ), Geroliminis and Daganzo (2008 ), Geroliminis et al. (2013 ), Keyvan-Ekbatani et al. (2012 ), Yildirimoglu et al. (2018 ), Kouvelas et al. (2017 ) and many others. Recent research efforts are devoted to enhance the traffic flow modeling ( Mariotte et al. , 2017 ; Lamotte and Geroliminis , 2018 ; Batista et al. , 2019 ; Fu et al. , 2020 ;

<!-- page 3 -->

Transportation Research Part C 133 (2021) 103380 3J. Haddad et al. Batista et al., 2021; Sirmatel et al., 2021; Sirmatel and Geroliminis, 2021). Other works have also observed MFDs in other transport systems, besides ground urban systems, e.g. ride-sharing systems (Alisoltani et al., 2021) and railway systems (Cuniasse et al., 2015). It should be noted that the MFD concept was also applied for airport surface traffic , as in recent studies (Simaiakis et al., 2014; Yang et al., 2017), and an aggregate curve, which relates the jet take-off rate as a function of the number of departing aircraft on the ground, was shown to exist by empirical data.

### 1.1. A review of using traffic flow models for LAAT systems

### 1.1.1. Urban traffic flow models for low-altitude air transport systems have not been fully explored

There has been very limited exploration of the idea of using traffic flow models in the literature for LAAT systems (Jang et al., 2017; Bulusu et al., 2018; Gharibi et al., 2019; Battista and Ni, 2017). These works introduce elementary traffic flow-oriented models focusing on microscopic or macroscopic levels. Microscopic models: the work (Jang et al., 2017) focuses on the operation of unmanned aerial vehicles (UAVs). It presents several airspace structures with similar road network design. Based on the presented structures, a microscopic traffic flow model with behavioral rules, i.e. separation control, lane change, and turning and exiting ramp, has been introduced for UAVs. By means of numerical simulations, the authors extract a fundamental diagram that relates flow with density. It should be noted that the simulations are very simple as they only consider traffic in one flight lane, under an acceleration from a standstill, followed by cruising and then braking of the leader. A microscopic flow model for small unmanned aircraft systems (sUAS) under external force has been developed in Battista and Ni (2017). The microscopic model presents a ‘‘sense-and-avoid" behavior, taking into account the effects of three different types of winds: headwinds, tailwinds, and consistent winds. Then, the microscopic model was transformed into a macroscopic flow model to describe the group behavior of a platoon of aircraft. Utilizing the macroscopic model in Battista and Ni (2017), a simple simulation was developed to analyze the relationships between density, flow, and speed values under different types of wind. The reference Bulusu et al. (2018) studies an unstructured free-flow traffic of unmanned low-altitude aircraft in an area. The study was based on simulation results, where several conflict detection and resolution algorithms (Kuchar and Yang, 2000) were used. The simulations consider an area of a square of 0.5 km width, and throughput behavior as a function of steady-state air traffic inflow in the representative area was obtained. This is interesting since the results are not restricted to a lane but to a relative large area. The authors state that measuring throughput metric could be used as a tool to evaluate the adequacy of conflict detection and resolution algorithms for large-scale operations. The work (Gharibi et al., 2019) formulates a microscopic traffic flow model in a 3D space with no lanes for UAVs. The paper tries to address the issue that UAVs movements in the 3D space would not be structured by ‘‘lanes", but by space ‘‘channels". A UAV velocity is determined in the 3D space with no lanes according to an aggregated variable, i.e. density, following the concept that a flying UAV in a channel can move forward according to the density in its horizon, as it must be under the capacity of the channel. In other words, the authors integrate aggregated variables (densities) into the microscopic model to address modeling 3D space with no lanes. This results in defining dynamics for ‘‘blocking regime" and ‘‘passing regime", which are respectively analogous to ‘‘car following" model within a lane and ‘‘lane changing" model for multiple lanes road. The presented microscopic traffic flow model in Gharibi et al. (2019) obtained some traffic flow characteristics and properties. Among these properties, the authors extract a fundamental diagram from the presented microscopic traffic flow. The paper (Zhou et al., 2020) tackles a future congestion problem in UAVs traffic system under weather uncertainty. A macroscopic flow model for traffic dynamics was introduced as fluid queues with three basic components: single link, tandem link, and merge link. The effect of weather was captured as uncertainty in the saturation flow rate of fluid queue discharge. The control measure was only presented at the merge link, as proportional capacity allocation control policy was considered. Finally, the paper (Xue and Do, 2019) presents a microscopic behavior of collision avoidance mechanism for UAS. The presented model is utilized to assess the complexity of a given scenario. Macroscopic models: the state-of-the-art shows that most research efforts, except (Zhou et al., 2020), focused only on characterizing macroscopic aircraft flow behavior, without developing macroscopic dynamics flow models. Previous works, e.g. Gharibi et al. (2019), Battista and Ni (2017), Jang et al. (2017), derived fundamental diagrams by relating the macroscopic variables, i.e. flow with density, which are aggregated based on microscopic variables obtained from the developed microscopic models. On the other hand, (Zhou et al., 2020) introduced a first-order macroscopic flow model for traffic dynamics for simple UAV traffic systems.

### 1.1.2. Feedback traffic control strategies for low-altitude air transport systems have not been introduced

Conventional airplane movements in the airspace are managed in a centralized manner by human operators (controllers), (Wensveen, 2018). The operators manage airplanes’ separation by using radar screens to visualize trajectories and make operational judgments, with some automation decision support to help identify and resolve conflicts. However, issues may arise when the operator deals with congested regions, i.e. zones with an increased number of aircraft, and under uncertainty situations, (Neto et al., 2019). Given the expected significant growing of aircraft demand in the future, and the society’s concerns over air quality and climate impacts, and aircraft noise, several next generation air transportation system (NextGen) concepts were developed in Planning and Office (2010). Trajectory-Based Operations (TBO) (Hof, 2018; Ramasamy et al., 2014; Planning and Office, 2010) is one of these concepts, which is related to aircraft flow management, i.e. to dynamically adjust a flight trajectory in space (longitude, latitude, altitude) and time using a known position and intent. The TBO is expected to increase system capacity and achieve efficient flow

<!-- page 4 -->

Transportation Research Part C 133 (2021) 103380 4J. Haddad et al. management. The TBO concept was recently adopted for future urban air mobility , as trajectory-based urban air mobility operations simulator was developed in Neto et al. (2019). The developed simulator can be utilized to evaluate future planning methods and operational schemes. However, currently the simulation tool includes simplified take-off and landing procedures and cruise trajectories, without considering complex operations, and without including small aircraft, e.g. package delivery drones. Because of the centralized control structure, and corresponding difficulties that may arise when the operator deals with congested aircraft traffic, the current traffic management schemes for conventional air transportation systems are not suitable for future LAAT control systems. Hence, NASA recently dedicates intensive research to adapt the control structure of conventional air transportation systems to future LAAT systems, in particular for unmanned aircraft systems (UAS). The main operational concept in NASA’s UAS traffic management project is that future UAS traffic management systems would not require human operators to continuously monitor every aircraft, (UAS Traffic Management (UTM) Project, 2018; Kopardekar et al., 2016; Kopardekar, 2014). While in conventional systems, a human pilot communicates with a human air traffic controller to provide the airplane clearance, this would be a major obstacle in LAAT control systems in the future where an increased number of LAAT aircraft will closely utilize the airspace. Therefore, NASA aims to introduce a new management system that has a centralized control structure, but operates differently than the conventional system, as LAAT aircraft will share their planned flight details with the management system that communicates all aircraft together and determines in real time airspace areas over which aircraft are not permitted to fly. Based on this concept, NASA’s UAS traffic management project develops new methods to manage the scheduling, i.e. departure and arrival times, and routing of small unmanned aircraft to enable safer and more efficient operations. NASA’s project also includes testing new various technologies for collision and obstacle avoidance (Belcastro et al., 2017), remote identification, while operating beyond visual line of sight (Johnson et al., 2017; Balachandran et al., 2017). It is clear from the state of the art that very limited research efforts are currently dedicated towards developing traffic management for small unmanned aircraft systems only, and do not consider future LAAT aircraft traffic of passenger drones, operated with or without pilots. The state of the art considers early stages of unmanned aircraft operation, focusing on aircraft collision and obstacle avoidance, and aircraft separation rules mainly under uncongested conditions. However, the fact that a large number of LAAT aircraft is expected, and for future complex operations of intermediate or mature states having medium or high density (Hackenberg, 2019), one has to consider congested traffic conditions in airspace regions and closely environment. Therefore, the concept of developing flow-based traffic control, instead of individual-based control, should be adopted. Considering the macroscopic-link flow level, urban traffic management and feedback control strategies for ground vehicles have a long history, which are presented in e.g. Papageorgiou et al. (2003), Zegeye et al. (2013), Zhou et al. (2015), Hunt et al. (1982), Skabardonis and Geroliminis (2008), Aboudolas et al. (2009), D’Ans and Gazis (1976), Diakaki et al. (2002), Gartner (1983), Gartner et al. (2002), Herman and Prigogine (1979), Diakaki et al. (2003), Daganzo (1994), Lin et al. (2011), Little et al. (1981) and literature therein. However, research on feedback traffic control for drones is very limited. Only preliminary concepts of adopting traffic control measures for ground vehicles to LAAT systems are presented in Jang et al. (2017). Similarly, considering the network flow level, feedback traffic control concerning the aggregated behavior of vehicle flows in large-scale networks for ground vehicles have been also investigated intensively, in e.g. Daganzo (2007), Godfrey (1969), Geroliminis and Daganzo (2008), Buisson and Ladier (2009), Ji et al. (2010), Mazloumian et al. (2010), Daganzo et al. (2011), Gayah and Daganzo (2011), Zhang et al. (2013), Mahmassani et al. (1987), Olszewski et al. (1995). Among the different proposed control architectures based on MFD, the perimeter feedback control paradigm is one of the most promising and rapidly developing. In perimeter control (Daganzo, 2007; Geroliminis and Daganzo, 2008; Geroliminis et al., 2013; Keyvan-Ekbatani et al., 2012; Yildirimoglu et al., 2018; Kouvelas et al., 2017), the idea is to manipulate the transfer flows at the perimeter borders of the urban regions. In recent studies (Simaiakis et al., 2014; Yang et al., 2017), the perimeter control concept was utilized in airport surface traffic to design off-block control, i.e. metering (or holding at gates) the airplane flow rate entering the airport surface. However, feedback control strategies considering the aggregated behavior of aircraft flows in large-scale LAAT systems have never been designed to the authors’ knowledge. Moreover, the future LAAT systems are a typical example of a new class of modern large scale engineering systems networked control systems. They are spatially distributed, consist of many interconnected elements in which the control loops are closed through digital communication networks such that the systems’ signals (control and feedback signals) can be exchanged among all components (sensors, controllers, and actuators) through a common network. However, on the other hand, using networks introduces new great challenges, due to the network-induced uncertainties such as: signal’s sampling, varying network induced (communication) delays, information constraints due to spatial distribution, etc.

### 1.1.3. Summary

Given the general trend towards increasing significantly the amount of LAAT operations in the city’s airspace with possible congestion problems and other issues, it is difficult to overestimate the importance of efficient modeling and feedback control strategies development, focusing on aggregated behavior of aircraft traffic flows by using advanced technologies and modern network control techniques. This is emphasized by the success of ground urban transport networks using such aggregated modeling approach with perimeter control , as follows from the above literature review. In the context of LAAT city’s setting, these problems are still in their early stages, in what promises to be an important and fertile field of research with many open research challenges. Therefore, a comprehensive understanding of traffic flow dynamics and characteristics in traffic flow theory, and a systematic understanding of uncertainties and operational anomalies role in feedback control theory for urban LAAT network management are thus required. Novel aggregated mode modeling and air traffic feedback boundary control paradigm is needed.

<!-- page 5 -->

Transportation Research Part C 133 (2021) 103380 5J. Haddad et al.

#### Fig. 2. (a) Four aircraft, traveling from east to west, west to east, north to south, and south to north, detect possible violations and coordinately maneuver to

minimize the deviation from their original trajectories. (b) Scenario of 1 aircraft per minute flow, as each aircraft emerges from a point ‘O’ and heads towards point ‘X’. Solid lines are the planned trajectories. Dashed curves indicate maneuvered routes.

### 1.2. Contributions

The main contributions of the current paper are summarized as follows: (i) the concept of aggregated macroscopic dynamical modeling and control using MFD is introduced; (ii) based on this concept, an aggregate flow model with boundary control, i.e. manipulation of flows on conditional boundaries, for large-scale multilayer air transport city networks is developed; and (iii) within the framework of event-driven control design, a new design approach to the solution of the boundary adaptive feedback flow control is developed to cope with different kinds of non-constant input and state delays in the dynamics description, under information constraints and uncertainties due to both the traditional and the network-induced phenomena in LAAT systems.

## 2. Problem setting and developing airspace structure for LAAT networks

Inspired by the ground transportation systems and their traffic management schemes, we assume that the airspace structure of future LAAT networks would be similar to the one of the road transport networks. Yet, future LAAT systems will be different from ground transportation systems, and conventional air transportation systems, because the LAAT systems have substantial differences in traffic flow characteristics and dynamics compared with the other systems.

### 2.1. Macroscopic fundamental diagram for large-scale LAAT networks

Theconjecture in this paper is that an MFD linking space-mean flow, density, and speed exists on a large-scale LAAT network. The results presented below, see Fig. 3, support our conjecture. It should be stressed that (Bulusu et al., 2018) have also presented results that link throughput and inflow in air traffic. Let us consider an airspace volume. We define accumulation as the number of aircraft in an airspace volume, and aircraft traffic flow as the number of aircraft traversing the airspace per unit time. Then, intuitively and based on the MFD concept, as the accumulation increases, the aircraft traffic flow (and correspondingly the aircraft trip completion flow) increases as well up to a peak flow. This regime is the uncongested regime, where beyond that regime the congested regime starts as the traffic becomes congested and flow decreases. In the congested regime, the aircraft impede each other, as they slow down and/or deviate from their planned paths to avoid losses of separation. The flow reaches its minimum steady-state value at a maximum aircraft accumulation that maintains safety. An MFD curve is observed based on simulated data. In this paper, we follow the microscopic model presented in Xue and Do (2019) to construct the MFD. The microscopic traffic model of each LAAT aircraft considers a double integrator dynamic with inter-aircraft interactions based on the description in Xue and Do (2019).1The main flow characteristic of the microscopic model is summarized here as follows, while for a detailed description, the interested reader is referred to Xue and Do (2019). The main traffic flow safety condition is that a well clear distance must be kept between aircraft at all time. Therefore, a lookahead time is used to define for each aircraft which other aircraft might potentially violate the well clear distance soon. Using mesh communication, each aircraft reports its future trajectory (up to the look-ahead time) to every other aircraft. If no future violation is detected in the look-ahead time, the aircraft is free to accelerate up to the maximal velocity toward its destination. If one or more future distance violations are detected, a well-coordinated maneuver is planned and executed to minimize the deviation of each aircraft from its initial trajectory. This is calculated using a nonlinear integer programming, see equations (1)-(10) in Xue and Do (2019), which is solved in this paper by the BARON solver (Kılınç and Sahinidis, 2018). Fig. 2(a) shows microscopic results of four 1Other microscopic models can be used to construct the MFD shapes. This will not alter the aggregate modeling and control methodology presented in this paper.

<!-- page 6 -->

Transportation Research Part C 133 (2021) 103380 6J. Haddad et al.

#### Fig. 3. MFD results for LAAT flow operation, relating aircraft trip completion flow and accumulation in an urban airspace.

aircraft trajectories, traveling from east to west, west to east, north to south, and south to north. The four aircraft detect possible conflicts and violations, and coordinately maneuver to minimize their deviations from the original trajectories. In this paper, we present only one of the case studies that we investigated to extract an MFD shape for LAAT systems. It includes a squared area where each aircraft starts and ends on different edges of the squared area. An aircraft lifts-off only if it will not violate other aircraft (already traveling or about to lift) safety the well clear distance; otherwise it will hover outside the area and randomly choose another lift-off time several seconds later. We examine a case-study where the area’s edge is 100meters, the well clear distance is 15meters and the look-ahead time is 30seconds. We allow aircraft to accelerate up to 5 [m∕s2], and the maximal speed is 20 [m∕s] . Fig. 2(b) shows trajectory results for a scenario of 1 aircraft per minute flow, as each aircraft emerges from a point ‘O’ and heads towards point ‘X’. The solid lines are the planned trajectories, while the dashed curves indicate maneuvered routes. To extract the MFD, we simulate 30minutes of different levels of constant flows up to 65aircraft per minutes. For each simulation with constant inflow, we calculate the Generalized Edie’s definitions, see e.g. Hoogendoorn et al. (2011), over 30 s of measurements along the simulation to finally average them to a single measurement on the MFD curve. The MFD results for LAAT flow operation, relating aircraft trip completion flow and accumulation in an urban airspace, are shown in Fig. 3. The nominal MFD is approximated following the form in Ioannou and Fidan (2006, p. 123), see more details in Section 5.

### 2.2. Developing an airspace structural design for LAAT networks

Urban road networks are well structured, where roads are split into one or multiple lanes, and intersections are formed by at least two roads. This structure helps the traffic flow modeling task, i.e. describing the movement of aircraft in two-dimensional space. Only a few papers have recently proposed different airspace structural designs, following the concept that the airspace can be similarly structured to the roads network in the cities (Jang et al., 2017; Gharibi et al., 2016). In Jang et al. (2017), the airspace above an urban street is used for aircraft movement and is divided into multiple layers by altitude, corresponding to the land physical features. Along the street, each layer is designed to have a certain airspace structure that guides and constrains aircraft flights in it. Three types of airspace design concepts are presented: (i) sky-lane, (ii) sky-tube, and (iii) sky-corridor systems. Each design concept has a different level of freedom for flight trajectory. Sky-lane system is the most restrictive, whereas sky-corridor allows the most free non-collision flights. Note that similar architecture was proposed in Gharibi et al. (2016), as there are three main elements, i.e.airways which act similarly as roads, and intersections which are formed by airways, while nodes are intermediate points through a sequence of airways. However, each airway is considered as a single lane to reduce technological burden on drones to safely execute a passing maneuver. Moreover, the intersections are guaranteed to be collision free, as they are assumed to act as diverging intersection flow only (without including merging). While a few works (Jang et al., 2017; Gharibi et al., 2016) consider the airspace structure at micro and macro (link or lane) levels, we aim to tackle this challenge at the network level. Hence, in this paper, we propose the following airspace structural design, taking into account the special elements of aggregate-network flow modeling and future possible control measures at the network level.

### 2.2.1. Proposed multi-layer structure of the controlled urban airspace volume

To provide effective and safe operating urban aircraft traffic, the following urban airspace structure is proposed. The city’s controlled airspace is decomposed into 𝐿vertical layers, labeled by 1, ... , L as depicted in Fig. 4. Layering makes it easier to solve the control problems by separation of concerns. Each layer’s region is managed by one of the air traffic control centers located on the ground. In such multi layer network architecture, each horizontal 𝑙th layer, similar to the urban road infrastructure (Haddad and

<!-- page 7 -->

Transportation Research Part C 133 (2021) 103380 7J. Haddad et al.

#### Fig. 4. A multi-layer-region urban LAAT system where the traffic LAAT flow generated in a virtual region of a layer can be distributed both horizontally and

vertically. Mirkin , 2017a ), is partitioned into 𝑍𝑙(𝑙= 1,…,𝐿)virtual regions (zones) with conditional borders, virtual aero traffic gateways, intersections, etc. Following the ground urban traffic notations, we define accumulation 𝑛(𝑡)as the number of aircraft in volume of an airspace region, and aircraft traffic flow 𝐻(𝑡) (𝑉(𝑡))as the number of aircraft traversing per unit time in the horizontal (vertical) direction. To manage the LAAT flows, i.e. both inter horizontal regions of the same layer and inter vertical layers, a group of virtual distributing gateways with virtual devices for inflow and outflow (control) manipulation, i.e. boundary virtual actuators, are located at the conditional region or layer border of any region. We will use the symbol IRG to denote the horizontal interregional group and the symbol ILG for vertical interlayers group. The number of individual aero traffic gateways in any IRG and ILG are m and g, respectively. The traffic LAAT flow 𝐴𝐹𝑙 𝑖(𝑡)generated in a given virtual region 𝑖(𝑖= 1,…,𝑍𝑙) of any arbitrary layer 𝑙(𝑙= 1,…,𝐿) can be distributed both (i)horizontally between different regions of a given layer and (ii)upright between different regions of the other vertical layers. Hence, it can be represented as the sum of different directional flows 𝐴𝐹𝑙 𝑖(𝑡) =𝐻𝑙

$$
𝑖𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑙 𝐻𝑖𝐻𝑙

$$
𝑖𝑗(𝑡) +\sum
$$

𝑝∈𝑆𝑙 𝑉𝑖𝑉𝑙

$$
𝑖𝑝(𝑡), 𝑖 = 1,…,𝑍𝑙;𝑙= 1,…,𝐿, (1)
$$

where: (i)𝐻𝑙 𝑖𝑗(𝑡)is the horizontal LAAT traffic flow generated in virtual region 𝑖of the𝑙th layer with direct destination to region 𝑗 (𝑗∈𝑆𝑙 𝐻𝑖) at the same level. Here 𝑆𝑙 𝐻𝑖defines the set of the horizontal virtual regions, with which the region 𝑖can communicate, i.e. the set of virtual regions that are directly reachable from region 𝑖. Each of𝑆𝑙 𝐻𝑖is a set of integers corresponding to the virtual region’s index number; (ii) 𝑉𝑙 𝑖𝑝(𝑡)is the vertical LAAT traffic flow generated in virtual region 𝑖of the𝑙th layer with direct destination to the region 𝑝(𝑝∈𝑆𝑙 𝑉𝑖) of the vertical layer 𝑙. Here𝑆𝑙 𝑉𝑖defines the set of the layers, with which the region 𝑖can communicate, i.e. the set of vertical layers that are directly reachable from virtual region 𝑖. Each of𝑆𝑙 𝑉𝑖is a set of integers corresponding to the virtual region’s index number; and (iii) 𝐻𝑙 𝑖𝑖(𝑡)is the flow portion with destination to inside the region. In view that the LAAT flows 𝐴𝐹𝑙 𝑖(𝑡)in any virtual region 𝑖will be distributed through appropriate gateways groups 𝐼𝑅𝐺𝑖,𝑗 (𝑗∈𝑆𝑙 𝐻𝑖) and𝐼𝐿𝐺𝑖,𝑝(𝑝∈𝑆𝑙 𝑉𝑖), where in each group 𝐼𝑅𝐺𝑖,𝑗and𝐼𝐿𝐺𝑖,𝑝there are𝑚𝑙 𝑖𝑗and𝑔𝑙 𝑖𝑝individual gateways, then instead of (1) we have 𝐴𝐹𝑙 𝑖(𝑡) =𝐻𝑙

$$
𝑖𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑙 𝐻𝑖𝑚𝑙 𝑖𝑗\sum 𝑘=1𝐻𝑙

$$
𝑖𝑗𝑘(𝑡) +\sum
$$

𝑝∈𝑆𝑙 𝑉𝑖𝑔𝑙 𝑖𝑝\sum 𝑠=1𝑉𝑙

$$
𝑖𝑝𝑠(𝑡), 𝑖= 1,…,𝑍𝑙;𝑙= 1,…,𝐿, (2)
$$

where𝐻𝑙 𝑖𝑗𝑘(𝑡)and𝑉𝑙 𝑖𝑝𝑠(𝑡)are the LAAT’s flow portions passing through the individual gateways 𝑘,𝑠with the corresponding directions.

## 3. General dynamic model of multi-layer urban airspace network

### 3.1. An aggregated network dynamical model for feedback boundary flow control

An aggregated macroscopic dynamical model for feedback control of large-scale LAAT systems composed of several layer networks is developed in several steps.

<!-- page 8 -->

Transportation Research Part C 133 (2021) 103380 8J. Haddad et al. Step 1. Similar to the ground urban road infrastructure (Haddad and Shraiber, 2014; Haddad, 2015), to design the boundary flow control policy into the MFD framework, we postulate that each region of every layer has a partial uncertainty MFD. The MFD provides a unimodal, low-scatter relationship between network aircraft density (aircraft/ km2) and network space-mean flow or outflow (aircraft/h) for different network regions. In other words, it links accumulation, defined as the number of aircraft in the region, and trip completion flow, defined as the output flow of the region. The MFD allows us to formalize the dynamic flow model for urban LAAT networks at a macro level. Step 2 . To derive LAAT traffic flow dynamic, we take into account that the regional accumulation of the 𝑙th layer includes: (i)the portion of aircraft with destination to inside the region 𝑛𝑙 𝑖𝑖;(ii)the portion of aircraft to outside the region, with destination from the region𝑖to the region 𝑗-𝑛𝑙 𝑖𝑗,𝑗∈𝑆𝑙 𝐻𝑖; and (iii)the portion of aircraft to outside the region, with destination from the region 𝑖 to the vertical layer 𝑝-𝑛𝑙 𝑖𝑝,𝑝∈𝑆𝑙 𝑉𝑖. Hence, considering the case of inter-regional and inter-layered gateways , the integral aircraft accumulation of 𝑖th region at the 𝑙th layer, in view of (2), has the form for 𝑖= 1,…,𝑍𝑙;𝑙= 1,…,𝐿 𝑛𝑙 𝑖(𝑡) =𝑛𝑙

$$
𝑖𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑙 𝐻𝑖𝑚𝑙 𝑖𝑗\sum 𝑘=1𝑛𝑙

$$
𝑖𝑗𝑘(𝑡) +\sum
$$

𝑝∈𝑆𝑙 𝑉𝑖𝑔𝑙 𝑖𝑝\sum 𝑠=1𝑛𝑙 𝑖𝑝𝑠(𝑡), (3) then, referring to Haddad and Mirkin (2017a) and utilizing (2), the aircraft conservation equation can be written as follows ̇ 𝑛𝑙 𝑖(𝑡) = -𝐻𝑙

$$
𝑖𝑛𝑠𝑖𝑖(𝑡) -\sum
$$

𝑗∈𝑆𝑙 𝐻𝑖𝑚𝑙 𝑖𝑗\sum 𝑘=1𝐻𝑙

$$
𝑜𝑢𝑡𝑖𝑗𝑘(𝑡) -\sum
$$

𝑝∈𝑆𝑙 𝑉𝑖𝑔𝑙 𝑖𝑝\sum 𝑠=1𝑉𝑙 𝑜𝑢𝑡𝑖𝑝𝑠(𝑡), +\sum 𝑗∈𝑆𝑙 𝐻𝑖𝑚𝑙 𝑗𝑖\sum 𝑘=1𝐻𝑙

$$
𝑖𝑛𝑗𝑖𝑘(𝑡) +\sum
$$

𝑝∈𝑆𝑙 𝑉𝑖𝑔𝑙 𝑝𝑖\sum 𝑠=1𝑉𝑙

$$
𝑖𝑛𝑝𝑖𝑠(𝑡) +𝑑𝑖(𝑡),𝑖= 1,…,𝑍𝑙,𝑙= 1,…,𝐿 (4)
$$

where the variables 𝐻𝑙 𝑜𝑢𝑡𝑖𝑗𝑘(𝑡),𝐻𝑙 𝑖𝑛𝑗𝑖𝑘(𝑡) (𝑘= 1,…,𝑚𝑙 𝑗𝑖)and𝑉𝑙 𝑜𝑢𝑡𝑖𝑝𝑠(𝑡),𝑉𝑙 𝑖𝑛𝑝𝑖𝑠(𝑡) (𝑠= 1,…,𝑔𝑙 𝑝𝑖)denote the controlled input and output aircraft flows through individual inter-regional and inter-layered gateways with the corresponding directions. 𝑑𝑖(𝑡)is the uncontrolled traffic aircraft demand (disturbances). Step 3 . Based on the MFD concept, the internal and input-output adjustable traffic flows of any region can be calculated corresponding to some relationships between accumulations (Geroliminis et al., 2013; Hajiahmadi et al., 2015; Ramezani et al.,

$$
2015; Haddad and Mirkin, 2017a), namely in the form of the following weighted nonlinear relations 𝐻(𝑡) =\sum 𝑚
$$

𝑘=1𝐺(⋆)𝑏𝑅𝑘(⋆)𝑈𝑅𝑘(𝑡) = 𝐺(⋆)𝐵𝑇

$$
𝑅𝑈𝑅(𝑡)(𝑉(𝑡) =\sum 𝑔
$$

𝑠=1𝐺(⋆)𝑏𝑉𝑠(⋆)𝑈𝑉𝑠(𝑡) =𝐺(⋆)𝐵𝑇 𝑉𝑈𝑉(𝑡)), where𝑏𝑅𝑘(⋆)and𝑏𝑉𝑠(⋆)are some weighting factors, 𝐺denotes the appropriate state delayed MFD parametrization, refer to Haddad and Zheng (2018), and 𝑈𝑅𝑘∈R(𝑈𝑉𝑠∈R) are the control commands of relevant individual traffic gateways. Note that the weighting factors are assumed to have general nonlinear forms, and they can be constant or time-varying. 𝑈𝑅∈R𝑚(𝑈𝑉∈R𝑔) are the vector variables with components 𝑈𝑅𝑘(𝑈𝑉𝑠). Step 4 . As a result, bearing in mind the aircraft conservation Eq. (4), we can write the following general nonlinear dynamic model, operating in the nominal mode, i.e. model that is designed for the nominal MFD, ̇ 𝑛𝑙 𝑖𝑖(𝑡) = -𝑏𝑙 𝑅𝑖𝑖𝐺𝑙

$$
𝑖(𝑛𝑖(𝑡)) +\sum
$$

𝑗∈𝑆𝑙 𝐻𝑖𝐺𝑙 𝑗(𝑛𝑗(𝑡-𝜏𝑗(𝑛𝑗)))𝐵𝑙𝑇 𝑅𝑗𝑖𝐷𝑗𝑖(𝑈𝑙 𝑅𝑗𝑖(𝑡)) +\sum 𝑝∈𝑆𝑙 𝑉𝑖𝐺𝑙 𝑝(𝑛𝑝(𝑡-𝜏𝑝(𝑛𝑝)))𝐵𝑙𝑇 𝑉𝑝𝑖𝐷𝑝𝑖(𝑈𝑙 𝑉𝑝𝑖(𝑡))+𝑑𝑖𝑖, ̇ 𝑛𝑙 𝑖𝑗(𝑡) = -𝐺𝑙 𝑖(𝑛𝑖(𝑡))𝐵𝑙𝑇 𝑅𝑖𝑗𝐷𝑖𝑗(𝑈𝑙 𝑅𝑖𝑗(𝑡))+𝑑𝑖𝑗, ̇ 𝑛𝑙 𝑖𝑝(𝑡) = -𝐺𝑙 𝑖(𝑛𝑖(𝑡))𝐵𝑙𝑇 𝑉𝑖𝑝𝐷𝑖𝑝(𝑈𝑙 𝑉𝑖𝑝(𝑡))+𝑑𝑖𝑝, (5) and (3), where the operator 𝐷𝑖𝑗(𝑢𝑖𝑗(𝑡))denotes delay function, which is defined by 𝐷𝑖𝑗(𝑢𝑖𝑗(𝑡))=𝑢𝑖𝑗(𝑡-ℎ𝑖(𝑛𝑖)),𝐷𝑖𝑗(𝑢𝑖𝑗(𝑡))=𝑢𝑖𝑗(𝑡-ℎ𝑖(𝑡))and 𝐷𝑖𝑗(𝑢𝑖𝑗(𝑡))=𝑢𝑖𝑗(𝑡-ℎ𝑖)for the state-dependent ℎ𝑖(𝑛𝑖), time-varying ℎ𝑖(𝑡)or constant ℎ𝑖cases of time delay, respectively. Similarly, for the case of 𝐷𝑝𝑖(𝑢𝑝𝑖(𝑡))etc.𝜏𝑗(𝑛𝑗)denotes state delay in region 𝑗. Principal observations. Inspection of (4) and (5) allows to detect the first fundamental feature of the introduced multi-layer-region LAAT system model (5), namely the presence of input accumulation dependent time delays ℎ𝑖(𝑛𝑖)into the control channels of each region. For urban ground networks composed of some interconnected aggregate regions, to reflect the travel times needed for vehicles to reach the region’s border, dynamic models based on MFDs and time delays as key units have been proposed, motivated and tested in Haddad and Mirkin (2016b). For future urban LAAT systems, future research should investigate how to reflect physical aspects. In addition, a further particular problem that should be treated in a future research is how to determine formal analytical mathematical relationships for various ℎ𝑖(𝑛𝑖)and MFD. The second underlying observation is that in the developed model, we have the so called input redundant or over-actuated system, i.e. there are more control inputs than strictly needed to meet the control objectives. This significant feature of proposed dynamic model opens up wide possibilities to succeed in designing practical control laws, when abnormal conditions in measurement and control channels or in equipment occur, i.e. actuation redundancy can be used

<!-- page 9 -->

Transportation Research Part C 133 (2021) 103380 9J. Haddad et al. forfault-tolerant control (safety control) in LAAT traffic systems. A nice feature here is that we can realize adaptive fault-tolerant control without the addition of new technical devices, as is done for example in the control of individual flying aircraft. The fault tolerant control problems have attracted attention of the control community over the past half-century, for many safety critical control systems. A large body of literature currently exists for building such systems under several different directions and in most cases redundancy is the key element. One of significant trend here is direct adaptive control approach, in which yet at the synthesis stage the controller is being designed to be robust against the technical failures and potential cyber-attack problems in addition to other system and dynamics uncertainties. It does not require on-line fault detection, as the fault effects are continuously and adaptively compensated. When abnormal conditions (damage or attacks) occur, desired stability and tracking performance can still be achieved with adaptive cooperation of the remaining (non-failed) actuation elements, see e.g. Haddad and Mirkin (2017b, 2019b), where there is a necessary literature review.

### 3.2. Partially linearized boundary flow control oriented dynamic model

Based by the model from the previous section, defining new states 𝑥𝑖(𝑡)and control inputs 𝑢𝑖𝑗(𝑡)as deviations from equilibrium points𝑋𝑒𝑞𝑖and𝑈𝑒𝑞𝑖𝑗, and assuming the time delay ℎ𝑖𝑗=ℎ𝑖𝑗(𝑋𝑒𝑞𝑖), then the locally linearized uncertain dynamics of each virtual region (i.e. when we linearize only the local part of the general nonlinear model ) with multi-input delayed control, nonlinear interconnections, in the presence of unknown external disturbances, parametric uncertainties and suitably initialized, has the following form:

$$
̇ 𝑥𝑖(𝑡) =𝐴𝑖𝑥𝑖(𝑡) +\sum
$$

$$
𝑗∈𝑆𝑖𝑏𝑖𝑗𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(𝑛𝑖)) +\sum
$$

𝑗∈𝑆𝑖𝑝𝑗𝑖(𝑥𝑗(𝑡),𝑥𝑗(𝑡-𝜏𝑗𝑖)) +𝑏𝑖𝑑𝑖(𝑡), 𝑦𝑖(𝑡) =𝑐𝑇 𝑖𝑥𝑖(𝑡) (6) where𝑥𝑖∈Rcard(𝑆𝑖)+1,𝑛𝑖(𝑡) ∈R,𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(𝑛𝑖)) ∈Rand𝑑𝑖(𝑡) ∈Rare the state, output (regional accumulation), state delayed control inputs𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(𝑛𝑖)), which are introduced between the regions 𝑖and𝑗to control the transfer flows, and an equivalent external disturbance of the 𝑖th region, respectively. The constant matrix 𝐴𝑖∈R(card(𝑆𝑖)+1)×(card(𝑆𝑖)+1)and vector 𝑏𝑖,𝑏𝑖𝑗∈Rcard(𝑆𝑖)+1are defined by appropriate Jacobian matrices, whose values in the control synthesis are assumed to be unknown. The input delays ℎ𝑖𝑗(𝑛𝑖) ∈𝑅+are known and the state time-delays 𝜏𝑖𝑗(𝑡) ∈𝑅are nonnegative differentiable functions, satisfying

$$
0\le 𝜏𝑖𝑗(𝑡)\le 𝜏𝑖𝑗max\le 𝜏max, ̇ 𝜏𝑖𝑗(𝑡)\le 𝜏∗
$$

$$
𝑖𝑗\le 𝜏∗<1 (7)
$$

where𝜏𝑖𝑗max,𝜏∗ 𝑖𝑗,𝜏max, and𝜏∗are some unknown positive constants. Hence, 𝜏𝑖𝑗(𝑡)are uncertain within unknown upper bounds. The variable𝑆𝑖stands for the set of the regions, with which the region 𝑖can communicate. Each of 𝑆𝑖is a set of integers corresponding to the region’s index number. The symbol 𝑐𝑎𝑟𝑑(𝑆𝑖)denotes the cardinality (size) of 𝑆𝑖. The unknown term 𝑝𝑗𝑖(⋆)brings together as: (i) the bounded nonlinear interconnections; (ii) a bounded nonlinear offset introduced by the non-equilibrium operating points; (iii) higher-order terms after local region linearization approximation errors, and also captures (iv) the potential unreliable communication between regions (e.g. denial-of-service (DoS)) which is modeled by inclusion unknown time dependent delays 𝜏𝑗𝑖in the region to region communication channels in addition to existing delays in interconnections of system model.

## 4. Design adaptive feedback control strategies under anomalies

The future LAAT systems are a class of modern networked control systems. The question is how the adaptive boundary flow control strategies for such networked control systems can be designed and analyzed to reduce the effect of uncertainties and to cope with the volatile time-delay phenomena as a key factor in the dynamics description. The hitherto achieved results constitute only the primary steps toward theory and practice of adaptive feedback control of such systems, especially taking into account the network realization specifics, especially, when the air-traffic control performed in a distributed control framework under variable time-delays in control transfer channels. The presence of such delays introduces fundamental difficulties in the design adaptive controllers.

### 4.1. Literature overview on input delays in adaptive control framework

The problem of handling uncertain systems under input delays is one of the challenges of adaptive feedback control theory nowadays, mainly because of the plant state prediction over the input delay value under uncertainties. Comparatively few results are available here, especially for cases of non-constant (time varying, state dependent, time and state dependent) . We will mention only some substantive early and more recent contributions. In context of infinite-dimensional predictor based feedback laws, a globally stable MRAC solution for SISO input delayed plants was developed in Ortega and Lozano (1988), and later in Niculescu and Annaswamy (2003), Yildiz et al. (2010). Recently, within the backstepping framework, a new approach was developed for the case when the uncertain plant has unknown input delays, see e.g. Krstić (2009). The input delay is treated as a transport partial differential equation (PDE), and the dynamic system is represented as a PDE-ODE cascaded system with boundary control. Works (Zhou et al., 2009; Liua et al., 2017) should be indicated, where they also studied adaptive control of systems with input delays based on backstepping technique. However, the papers deal only with models where there is delayed unmodeled dynamic acting on the input, and the main weakness of the proposed control schemes is the restrictive assumption that in the considered systems there are also parallel not delayed (direct) channels in the control action.

<!-- page 10 -->

Transportation Research Part C 133 (2021) 103380 10J. Haddad et al.

#### Fig. 5. Controlled system.

However, the applicability of the cited results is limited because all the proposed adaptive control laws are infinite-dimensional control laws , i.e. utilizing finite-time integrals of the delayed control signals, so-called distributed-delay (DD) blocks. The impractical DD element is irrational (infinite-dimensional), and its precise implementation does not appear to be feasible. Note that a design procedure based on a reference trajectory prediction, which does not use DD blocks in the control law, was developed for a class of delayed linear systems with constant delays and parametric uncertainty in Mirkin et al. (2009 ). Alternative control architecture options, which also do not use DD blocks in the feedback control laws, in a centralized setting under unknown nonlinear perturbation, input constraints, modeling errors, and external disturbance based only on the lumped-delays were developed in our recent papers ( Haddad and Mirkin , 2016b ; Mirkin et al. , 2016 ; Haddad and Mirkin , 2016a ). To overcome the difficulty in predicting directly the plant state, a control synthesis is proposed which relies on a decomposition of the adaptive control design procedure, where a ‘‘generalized error’’ and auxiliary linear Smith-like dynamic units with adjustable gains are introduced. It should be noted that all papers mentioned above, that deal with input delays, studied mainly centralized problems with a single constant delay. It is well known that the presence of non-constant input delays significantly complicates the determination of the control, and to our knowledge, there are no papers that apply the MRAC design technique for uncertain systems with non-constant input delays especially within framework of information constraints (decentralized control structure).

### 4.2. Control setup

In this paper, we consider the decentralized controller design in framework of the unilateral event-driven paradigm, specifically the case of an event driven sample-and-hold implementation only of the local control signals 𝑢𝑖𝑗(𝑡)over an actuation network. The control signal 𝑢𝑖𝑗(𝑡), which is designed by a continuous-time adaptive controller without taking into account the implementation problems, is not continuously implemented but it is transformed to the plant and actuated only at certain event instants 𝑡𝑖 𝑘(𝑖= 1,…,𝑅;𝑘= 0,1,2,…). An event occurs when control variables deviate ‘‘too much’’ from their required or expected values. To identify this deviation, an additional solution element (an event detector) is included in the control architecture as shown in Fig. 5. The event detector continuously monitors the control 𝑢𝑖𝑗(𝑡)and checks a pre-specified logic rule. The transmission of a new control action 𝑢𝑖𝑗(𝑡) =𝑢𝑖𝑗(𝑡𝑖 𝑘)is carried out and will be applied to the plant as 𝑢𝑖𝑗(𝑡𝑖 𝑘-ℎ𝑖𝑗)if this rule is violated. The control action is supposed to be held constant between two successive sampling instants 𝑡𝑖 𝑘and𝑡𝑖 𝑘+1, i.e. during the time 𝑡∈ [𝑡𝑖 𝑘,𝑡𝑖 𝑘+1), the control signal holds as a constant, namely 𝑢𝑖𝑗(𝑡𝑖 𝑘).

### 4.3. Underlying design idea

Before proceeding to design the adaptive controller, the main design idea is presented in this subsection. To overcome the difficulty of directly predicting the plant state, and be able to uniformly treat the various types of input delays in multichannel feedback control design, the underlying idea is based on a suitable equivalent reformulation of the plant model desired for control law designs. We introduce the non-delayed control inputs 𝑢𝑖𝑗(𝑡), which must be synthesized, and relocate the actual (valid) delayed control inputs 𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(∙))as a component into some service signals . Different scenarios can be considered depending on the used event detector rule. Let us e.g. define the event detector rule for subsystem 𝑖in the form with fixed thresholds as follows: ‖‖‖𝑢𝑖𝑗(𝑡) -𝑢𝑖𝑗(𝑡𝑖 𝑘)‖‖‖\le 𝑢𝑇𝑖𝑗and‖‖‖𝑢𝑖𝑗(𝑡𝑖

$$
𝑘) -𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(∙))‖‖‖\le 𝑢𝑇ℎ𝑖𝑗, (8)
$$

for𝑡∈ [𝑡𝑖 𝑘,𝑡𝑖 𝑘+1), 𝑢𝑇𝑖𝑗,𝑢𝑇ℎ𝑖𝑗>0. The transmission of a new control action 𝑢𝑖𝑗(𝑡) =𝑢𝑖𝑗(𝑡𝑖 𝑘)is carried out and will be applied to the plant as𝑢𝑖𝑗(𝑡𝑖 𝑘-ℎ𝑖𝑗(∙))if the above inequality is violated. Further the non-delayed control input 𝑢𝑖𝑗(𝑡)is introduced, and the actual (valid) delayed control input 𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(∙))is relocated as a component into some service signal 𝛥𝑢ℎ𝑖𝑗by adding and subtracting to

<!-- page 11 -->

Transportation Research Part C 133 (2021) 103380 11J. Haddad et al.

$$
the right side of (6) terms\sum
$$

$$
𝑗∈𝑆𝑖𝑏𝑖𝑗𝑢𝑖𝑗(𝑡)and\sum
$$

𝑗∈𝑆𝑖𝑏𝑖𝑗𝑢𝑖𝑗(𝑡𝑖 𝑘), transforming (6) into the following equivalent equations

$$
̇ 𝑥𝑖(𝑡) =𝐴𝑖𝑥𝑖(𝑡) +\sum
$$

$$
𝑗∈𝑆𝑖𝑏𝑖𝑗𝑢𝑖𝑗(𝑡) +\sum
$$

$$
𝑗∈𝑆𝑖𝑝𝑗𝑖(∙) +𝑏𝑖𝑑𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖𝑏𝑖𝑗𝑑𝑎𝑔𝑟𝑖𝑗(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗(∙)), 𝑦𝑖(𝑡) =𝑐𝑇 𝑖𝑥𝑖(𝑡), (9) where 𝑑𝑎𝑔𝑟𝑖𝑗(∙) =𝛥𝑢𝑖𝑗(𝑡,𝑡𝑖 𝑘) +𝛥𝑢ℎ𝑖𝑗(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗(∙)) 𝛥𝑢𝑖𝑗(𝑡,𝑡𝑖 𝑘) =𝑢𝑖𝑗(𝑡) -𝑢𝑖𝑗(𝑡𝑖 𝑘), 𝛥𝑢ℎ𝑖𝑗(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗(∙)) =𝑢𝑖𝑗(𝑡𝑖 𝑘) -𝑢𝑖𝑗(𝑡-ℎ𝑖𝑗(∙)). (10) Principal observation. In view of the assigned detector rule (8), we can make the following key observation by inspection of (9). The entered auxiliary signal components due to input delay 𝛥𝑢ℎ𝑖𝑗(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗)can be further treated as certain additive external measurable disturbances similarly as the plant disturbance 𝑑(𝑡). That is for the control synthesis problem we have the input delay free case of a controlled system, since the input delay is present only into the measurable signals𝛥ℎ𝑗(𝑡,𝑡𝑘). Moreover, in view of (8), these signals are also bounded . Hence, in this way it is possible to pull the input delay out of the design control law . As a result, we can seek various procedures of control design based on the equivalent plant equations of such a type, by using various known control synthesis techniques with the different control objectives. It should be stress that such procedure is independent of the delay type. That is the time delay can be constant, time-varying and state or input dependent. Remark 1. Note, that other formalisms of the detector’s rule setting can be proposed. Obviously, we need in prospect to investigate, clarify, and compare various alternatives in the specification of such rules that are popular in event based control literature, viz. not fixed thresholds, which depends on the size of the control signal, relative, adaptive, switching etc., threshold strategies (Heemels et al., 2012; Miskowich, ed).

### 4.4. Decentralized adaptive tracking control

In the framework of the proposed concept, now we consider the adaptive state feedback trajectory tracking problem for the system (6). Our control objective is to design local feedback decentralized controllers for system (6) such that the closed-loop system is stable and the states 𝑥𝑖(𝑡)asymptotically exact track the states 𝑥𝑟𝑖of𝑅non-delayed stable local reference models

$$
̇ 𝑥𝑟𝑖(𝑡) =𝐴𝑟𝑖𝑥𝑟𝑖(𝑡) +𝑏𝑟𝑖𝑟𝑖(𝑡), 𝑖 = 1,…,𝑀 (11)
$$

where for the 𝑖th model,𝑥𝑟𝑖(𝑡)is the state vector postulated to belong to R𝑛𝑖,𝑟𝑖∈Ris the reference input which is assumed to be a uniformly bounded and piecewise continuous function of time. The matrices 𝐴𝑟𝑖,𝑏𝑟𝑖are known constant matrices of appropriate dimensions. To develop an adaptive controller, as it is generally done in traditional model reference adaptive control (MRAC), see e.g. Ioannou and Sun (1996), Tao (2003), the following assumptions are made on the system model (6) and the reference models (11): (A1) There exist unknown constant vectors 𝜃∗ 𝑥𝑖𝑗∈R𝑛𝑖and nonzero constant scalars 𝜃∗ 𝑟𝑖𝑗,𝜃∗ 𝑑𝑖𝑗such that the following equations are satisfied, 𝐴𝑖+\sum 𝑗∈𝑆𝑖𝑏𝑖𝑗𝜃∗𝑇 𝑥𝑖𝑗=𝐴𝑟𝑖, 𝑏𝑖𝑗=𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗for all𝑗∈𝑆𝑖, 𝑏𝑖=𝑏𝑟𝑖𝜃∗ 𝑑𝑖(12) (A2) The sign of 𝜃𝑟𝑖𝑗is known. (A3) The external disturbance 𝑑𝑖(𝑡)is bounded by an unknown constant ||𝑑𝑖(𝑡)||<𝑑∗ 𝑖.(A4) The nonlinear interconnections 𝑝𝑖𝑗(𝑥𝑗(𝑡),𝑥𝑗(𝑡-𝜏𝑖𝑗(𝑡)),𝑡)satisfy the conditions that there exist nonnegative, but unknown , numbers𝜉∗ 𝑖,𝜉∗ 1𝑖𝑗and𝜉∗ 2𝑖𝑗 such that \sum 𝑗∈𝑆𝑖|𝑝𝑗𝑖(𝑥𝑗(𝑡),𝑥𝑗(𝑡-𝜏𝑖𝑗(𝑡)),𝑡)|\le 𝜉∗ 𝑖+\sum 𝑗∈𝑆𝑖𝜉∗

$$
1𝑖𝑗‖𝑥𝑗(𝑡)‖+\sum
$$

𝑗∈𝑆𝑖𝜉∗ 2𝑖𝑗‖𝑥𝑗(𝑡-𝜏𝑗𝑖(𝑡))‖. (13)

### 4.4.1. Controller parametrization

Motivated by our previous works, see e.g. Haddad and Mirkin (2019a, 2017c, 2020), we look for parametrization of an 𝑖th local region control law 𝑢𝑖𝑗(𝑡)(which is based only on the local signals of the 𝑖th region ) with the form of summation of two components 𝑢𝑖𝑗(𝑡) =𝑢1𝑖𝑗(𝑡) +𝑢2𝑖𝑗(𝑡) 𝑢1𝑖𝑗(𝑡) =𝜃𝑇 𝑖𝑗(𝑡)𝜔𝑖(𝑡), 𝜔𝑖(𝑡) = [𝑒𝑥𝑖(𝑡)𝑥𝑟𝑖(𝑡)𝑟𝑖(𝑡)]𝑇 ̇𝜃𝑖𝑗(𝑡) = sgn(𝜃𝑟𝑖𝑗)𝛤𝐼𝑖𝑗𝑧𝑖-sgn(𝜃𝑟𝑖𝑗)𝛤𝑃𝑖𝑗̇ 𝑧𝑖(𝑡), 𝑧𝑖(𝑡) =𝜔𝑖(𝑡)𝐸𝑖(𝑒𝑥𝑖)

$$
𝑢2𝑖𝑗(𝑡) = - sgn(𝜃𝑟𝑖𝑗)𝛾𝑖𝑗\int 𝑡
$$

0𝐸𝑖(𝑒𝑥𝑖(𝑡))𝑑𝑡 (14) where𝑒𝑥𝑖(𝑡) =𝑥𝑖(𝑡) -𝑥𝑟𝑖(𝑡)is the tracking error, 𝜃𝑖𝑗(𝑡)is the vector adaptation gain, the constant matrices 𝛤𝑇 𝐼𝑖𝑗=𝛤𝐼𝑖𝑗>0, 𝛤𝑇 𝑃𝑖𝑗=𝛤𝑃𝑖𝑗>0and the scalar 𝛾𝑖𝑗>0are some design parameters of corresponding dimensions, respectively. The signal 𝐸𝑖(𝑒𝑥𝑖) is defined as 𝐸𝑖(𝑒𝑥𝑖) =𝑏𝑇 𝑟𝑖𝑃𝑖𝑒𝑥𝑖(𝑡), where the matrix 𝑃𝑖=𝑃𝑇 𝑖>0, 𝑖= 1,…,𝑅is computed from the Lyapunov equation 𝐴𝑇

$$
𝑟𝑖𝑃𝑖+𝑃𝑖𝐴𝑟𝑖+𝑄𝑖= 0 (15)
$$

for any chosen constant matrix 𝑄𝑖∈R𝑛𝑖×𝑛𝑖such that𝑄𝑇 𝑖=𝑄𝑖>0.

<!-- page 12 -->

Transportation Research Part C 133 (2021) 103380 12J. Haddad et al.

### 4.4.2. Basic tracking error equation

To develop an adaptive control law, we need to express, as usual in adaptive control theory, the closed-loop system in terms of the tracking error 𝑒𝑖𝑗(𝑡), and some parameter errors. It is well-known that such error models form the basis for most adaptive systems as discussed in numerous articles and books, see e.g. the textbooks (Ioannou and Sun, 1996; Tao, 2003). Using (9), (11) and (12) we obtain for any 𝑢𝑖𝑗(𝑡)

$$
̇ 𝑒𝑥𝑖(𝑡) =𝐴𝑟𝑖𝑒𝑥𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗[ 𝑢𝑖𝑗(𝑡) -𝜃∗𝑇 𝑖𝑗𝜔𝑖(𝑡) -𝑑𝑎𝑔𝑟𝑖𝑗(∙) +𝜃∗-1 𝑟𝑖𝑗𝜃∗ 𝑑𝑖1 𝑐𝑎𝑟𝑑(𝑆𝑖)𝑑𝑖(𝑡)] +\sum 𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑑𝑖𝑝𝑗𝑖(∙), 𝜃∗ 𝑖𝑗= [𝜃∗ 𝑥𝑖𝑗𝜃∗ 𝑥𝑖𝑗1 𝑐𝑎𝑟𝑑(𝑆𝑖)𝜃∗-1 𝑟𝑖𝑗]𝑇. (16) Let us define the vector parameter error ̃𝜃𝑖𝑗(𝑡) =𝜃𝑖𝑗(𝑡) -𝜃∗ 𝑖𝑗with the unknown vector 𝜃∗ 𝑖𝑗from (16). Then, after some manipulations the following basic tracking error equation for stability analysis is derived

$$
̇ 𝑒𝑥𝑖(𝑡) =𝐴𝑟𝑖𝑒𝑥𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝜔𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗𝑢2𝑖𝑗(𝑡) +\sum 𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗[ -𝑑𝑎𝑔𝑟𝑖𝑗(∙) +𝜃∗-1 𝑟𝑖𝑗𝜃∗ 𝑑𝑖1 𝑐𝑎𝑟𝑑(𝑆𝑖)𝑑𝑖(𝑡)] +\sum 𝑗∈𝑆𝑖𝑏𝑟𝑖𝜃∗ 𝑟𝑖𝑗𝜃∗-1 𝑟𝑖𝑗𝜃∗ 𝑑𝑖𝑝𝑗𝑖(∙) (17)

### 4.4.3. Main control design result

We now state the main control design result of this paper, showing that, the proposed completely distributed adaptive tracking controller (14) makes all signals in the closed-loop system bounded, and the signals 𝑥𝑖(𝑡)tracking the given reference signals 𝑥𝑟𝑖(𝑡), generated from the stable reference models. Theorem 1. For the system given by (6) and (11) , the completely decentralized adaptive tracking controller (14) guarantees that all closed-loop signals are bounded, and the tracking errors 𝑒𝑥𝑖(𝑡) =𝑥𝑖(𝑡) -𝑥𝑟𝑖(𝑡)go to zero asymptotically. Proof See Appendix. Remark 2. It is important to note principal statements here, compared to our previous decomposition approach (Mirkin and Gutman, 2009; Mirkin et al., 2016; Haddad and Mirkin, 2016b) of direct continuous adaptive control for a centralized system with input delays, where to overcome the difficulty to directly predict the plant state, a ‘‘generalized error’’ in conjunction with auxiliary linear Smith-like dynamic units with adjustable gains were introduced. In this paper, the synthesis is based on: (S1) the actual and not on the generalized error; (S2) the auxiliary Smith-like filters are removed; (S3) the requirement of plant stability or stabilizable with memoryless state feedback or with so-called ‘‘delayed feedback control’’ is eliminated, which is very attractive; (S4) the important property the controller is based only on the lumped-delays is retained, and as a result, we will get a much simpler controller structure; (S5) the formalism fits addressing the issues under communication constraints (S6) and most importantly, the developed approach opens up perspectives for solving the input delay compensation problems under (decentralized framework) information structure constraints. Remark 3. In this section, we have restricted our attention to a case of state feedback-Lyapunov design. However, note that the structure of the unified tracking error Eq. (17) makes it possible to write in a similar way the basic tracking error equation for the output feedback case. Then, one can synthesize various modifications of adaptive controllers by following e.g. Mirkin and Gutman (2009), Mirkin et al. (2016), Haddad and Mirkin (2016b).

## 5. Simulation results

In this simulation study, an urban LAAT network that includes 3 aggregated regions one on the second layer and two on the first layer, as shown in Fig. 6 is tested. It is assumed that each region has its own MFD. The nominal MFDs are approximated following the form in Ioannou and Fidan (2006, p. 123) as follows: 𝐺1(𝑛1) =𝑣𝑓1𝑛1 𝐴1𝑒𝑥𝑝[-1 𝑎1(𝑛1

$$
𝑛𝑐𝑟1)𝑎1],𝐺2= 0.8𝐺1and𝐺3= 1.2𝐺1.𝐴1is the area
$$

of region 1. The critical accumulations 𝑛𝑐𝑟1corresponds to an optimum regional accumulation at which a maximum flow is reached.

$$
In this simulation 𝑛𝑐𝑟1= 80 [aircraft] and 𝑎1= 0.73. The MFDs are normalized by 𝑛1maxand𝐺1maxas shown in Fig. 7. The
$$

partially linearized model (6) for this example has the form: ̇ 𝑛1(𝑡) =𝐴1𝑛1(𝑡) +𝑏12𝑢12(𝑡-ℎ12) +𝑏13𝑢13(𝑡-ℎ13) +𝑑1(𝑡) +𝑝21(𝑛2) +𝑝31(𝑛3) ̇ 𝑛2(𝑡) =𝐴2𝑛2(𝑡) +𝑏21𝑢21(𝑡-ℎ21) +𝑏23𝑢23(𝑡-ℎ23) +𝑑2(𝑡) +𝑝12(𝑛1) +𝑝32(𝑛3)

$$
̇ 𝑛3(𝑡) =𝐴3𝑛3(𝑡) +𝑏31𝑢31(𝑡-ℎ31) +𝑏32𝑢32(𝑡-ℎ32) +𝑑3(𝑡) +𝑝13(𝑛1) +𝑝23(𝑛2) (18)
$$

where𝑝𝑗𝑖(𝑛𝑗) =𝑣𝑓𝑗𝑛𝑗∕𝐴𝑗𝑒𝑥𝑝[-1 𝑎𝑗(𝑛𝑖

$$
𝑛𝑐𝑟𝑗)𝑎𝑗], 𝑖,𝑗 = 1,2,3and the values of 𝑣𝑓𝑗are𝑣𝑓1= 3.714,𝑣𝑓2= 2.9712,𝑣𝑓3= 4.4568.
$$

<!-- page 13 -->

Transportation Research Part C 133 (2021) 103380 13J. Haddad et al.

#### Fig. 6. A two-layer-region urban LAAT system with three regions.

#### Fig. 7. Macroscopic fundamental diagram approximations.

The parameter values of the partially linearized model (18) around the given operation point 𝑛𝑜= 0.85𝑛𝑐𝑟, after normalization and time scaling, are: 𝐴1𝐴2𝐴3𝑏12𝑏13𝑏21𝑏23𝑏31𝑏32 -4.0139 -3.2111 -4.8166 11.7129 8.7847 3.5139 3.5139 5.6222 4.2167

$$
ℎ12= 3,ℎ13= 0.1,ℎ21= 3,ℎ23= 0.2,ℎ31= 1,ℎ32= 0.7.
$$

The equivalent external bounded disturbances (unknown time-varying demands), which can include both internal inflow and external non-controlled inflows are chosen in the following different variants: 𝑑𝑖(𝑡) =𝑑𝑖+𝑎𝑑𝑖Square (𝑓𝑑𝑖𝑡)(𝑟𝑎𝑑∕𝑠) (𝑖= 1,2,3), with 𝑑1𝑑2𝑑3𝑎𝑑1𝑎𝑑2𝑎𝑑3𝑓𝑑1𝑓𝑑2𝑓𝑑3

### 0.13 0.2 0.3 -0.1 0.1 0.13 0.29 0.25 0.21

The desired trajectories 𝑥𝑟𝑖(𝑖= 1,2,3)are generated by the reference model (11). The reference model parameters are chosen as

$$
𝐴𝑟1=𝐴𝑟2=𝐴𝑟3= -1 and𝑏𝑟1=𝑏𝑟3=𝑏𝑟3= 1, while the input model’s signals are chosen as 𝑟1= 1,𝑟2= 1.2and𝑟3= 1.3.
$$

In this simulation study, we apply the adaptive controller from (14). The design parameter values of the controller are chosen as:

$$
𝛤𝐼𝑖𝑗= 0.001𝐼3×3,𝛤𝑃𝑖𝑗= 0.001𝐼3×3,𝛾12= 0.1,𝛾21= 0.1,𝛾13= 0.5,𝛾31= 0.1,𝛾23= 0.1,𝛾32= 0.5.
$$

<!-- page 14 -->

Transportation Research Part C 133 (2021) 103380 14J. Haddad et al.

#### Fig. 8. Simulation of the distributed adaptive control for two-layer aero urban network with three interacting regions. The left and right graphs show the time

history of the corresponding tracking error 𝑒(𝑡), controls𝑢𝑖𝑗(𝑡)and unknown equivalent external disturbance 𝑑(𝑡)signals for Region 1. Difference between left and right graphs the different values of detector’s rule threshold parameters 𝑢𝑇𝑖𝑗.

#### Fig. 9. Simulation of the distributed adaptive control for two-layer aero urban network with three interacting regions. The left and right graphs show the time

history of the corresponding tracking error 𝑒(𝑡), controls𝑢𝑖𝑗(𝑡)and unknown equivalent external disturbance 𝑑(𝑡)signals for Region 2. Difference between left and right graphs the different values of detector’s rule threshold parameters 𝑢𝑇𝑖𝑗.

#### Fig. 10. Simulation of the distributed adaptive control for two-layer aero urban network with three interacting regions. The left and right graphs show the time

history of the corresponding tracking error 𝑒(𝑡), controls𝑢𝑖𝑗(𝑡)and unknown equivalent external disturbance 𝑑(𝑡)signals for Region 3. Difference between left and right graphs the different values of detector’s rule threshold parameters 𝑢𝑇𝑖𝑗. Remark 4. Note that the plant parameter values and the value of the disturbances 𝑑𝑖(𝑡)are assumed to be unknown for the controller . The only information available to the controller is the structural information given in assumptions (A1)-(A4). Furthermore, the reference model and the controller’s design parameter values are the same for all investigated cases (without retuning).

<!-- page 15 -->

Transportation Research Part C 133 (2021) 103380 15J. Haddad et al.

#### Fig. 11. Simulation of the distributed adaptive control for two-layer aero urban network with three interacting regions. The graphs show the time history of

$$
the regional tracing errors 𝑒𝑖(𝑡)of the interconnected aero city system, unknown equivalent external disturbances 𝑑𝑖(𝑡)signals (i=1, 2, 3) and the aggregated
$$

disturbance signals 𝑑𝑎𝑔𝑖(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗). Simulation results of the closed-loop system specifically: command signal tracking errors, unknown time-varying demands and control signals for the three interacting aero-urban regions system model are depicted in Figs. 8-11. The graphs are presented for different values of thresholds 𝑢𝑇𝑖𝑗and𝑢𝑇ℎ𝑖𝑗in the detector rule (8). The left-hand plots correspond to the following values of parameters 𝑢𝑇𝑖𝑗and𝑢𝑇ℎ𝑖𝑗

$$
𝑢𝑇12= 0.01, 𝑢𝑇ℎ12= 0.01, 𝑢𝑇13= 0.009, 𝑢𝑇ℎ13= 0.009,
$$

$$
𝑢𝑇21= 0.013, 𝑢𝑇ℎ21= 0.013, 𝑢𝑇23= 0.018, 𝑢𝑇ℎ23= 0.018,
$$

$$
𝑢𝑇31= 0.02, 𝑢𝑇ℎ31= 0.02, 𝑢𝑇32= 0.05, 𝑢𝑇ℎ32= 0.05. (19)
$$

and the right-hand plots correspond to the following values

$$
𝑢𝑇12= 0.02, 𝑢𝑇ℎ12= 0.02, 𝑢𝑇13= 0.01, 𝑢𝑇ℎ13= 0.01,
$$

$$
𝑢𝑇21= 0.016, 𝑢𝑇ℎ21= 0.016, 𝑢𝑇23= 0.02, 𝑢𝑇ℎ23= 0.02,
$$

$$
𝑢𝑇31= 0.03, 𝑢𝑇ℎ31= 0.03, 𝑢𝑇32= 0.06, 𝑢𝑇ℎ32= 0.06. (20)
$$

#### Fig. 11 shows the time history of the regional tracing errors 𝑒𝑖(𝑡), unknown external disturbances 𝑑𝑖(𝑡)signals (i=1, 2, 3), and

the aggregated equivalent disturbance signals 𝑑𝑎𝑔𝑖(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗) 𝑑𝑎𝑔𝑖(𝑡,𝑡𝑖

$$
𝑘,ℎ𝑖𝑗) =𝑑𝑖-\sum
$$

$$
𝑖∈𝑆𝑖𝑏𝑖𝑗𝑑𝑎𝑔𝑟𝑖𝑗(∙) =𝑑𝑖-\sum
$$

𝑖∈𝑆𝑖𝑏𝑖𝑗[ 𝛥𝑢𝑖𝑗(𝑡,𝑡𝑖 𝑘) +𝛥𝑢ℎ𝑖𝑗(𝑡,𝑡𝑖 𝑘,ℎ𝑖𝑗(∙))] with𝑑𝑎𝑔𝑟𝑖𝑗(∙)from (10).

## 6. Concluding remarks

This paper constitutes the first primary steps towards theory and practice of both aggregate traffic flow modeling and adaptive feedback control design for LAAT systems. With respect to traffic flow modeling, a multi-region multi-layer aggregate model for LAAT systems is developed utilizing the MFD concept. With respect to feedback control design, and taking into account the network realization specifics, an adaptive decentralized boundary control in an event-driven paradigm framework is designed with robust properties against different uncertainty with non-constant input delays. The case of an event driven sample-and-hold implementation only of the local control signals 𝑢𝑖𝑗(𝑡)over an actuation network is considered. Simulation results for an urban LAAT network that

<!-- page 16 -->

Transportation Research Part C 133 (2021) 103380 16J. Haddad et al. includes 3 aggregated regions, one on the second layer and two on the first layer, are presented to analyze the adaptive boundary flow control. The results verify the developed theory. To the best of the authors’ knowledge, developing the MRAC design technique for uncertain systems with non-constant input delays especially with information constraints, i.e. decentralized control structure, is new in the literature. Such technique can be applied to other networked control systems as well. In this paper, only one case study for extracting an MFD shape for LAAT systems was presented. The MFD was derived from simulation observations related to different stationary network loadings. Future research should focus on investigating the MFD properties for different settings of drone and operational parameters under different control algorithms at the micro level. Moreover, it would be interesting to investigate dynamic loading with time-dependent demand profiles, analyzing the corresponding MFD shapes and inspecting the hysteresis phenomena. This is an ongoing research. Finally, inspired from the multi-region framework for urban road networks, integrating inflow supply functions and investigating how to share the capacity between upstream regions are important modeling elements that can be added in a future research. Acknowledgment This research was supported by the ISRAEL SCIENCE FOUNDATION (grant No. 2353/20). Appendix. Proof of Theorem 1 For the stability analysis using the following Lyapunov-Krasovskii like functional is proposed

$$
𝑉(⋆) =3\sum
$$

$$
𝑖=1𝑉𝑖+𝑉𝜏, 𝑉1=𝑅\sum
$$

𝑖=1𝑉1𝑖, 𝑉1𝑖=𝑒𝑇 𝑥𝑖(𝑡)𝑃𝑖𝑒𝑥𝑖(𝑡),

$$
𝑉2=𝑅\sum
$$

$$
𝑖=1𝑉2𝑖, 𝑉2𝑖=\sum
$$

𝑗∈𝑆𝑖|𝜃𝑟𝑖𝑗|̃ 𝑧𝑇 𝑖𝑗(𝑡)𝛤-1 𝐼𝑖̃ 𝑧𝑖𝑗(𝑡)

$$
𝑉3=𝑅\sum
$$

$$
𝑖=1𝑉3𝑖, 𝑉3𝑖=\sum
$$

𝑗∈𝑆𝑖|||𝜃𝑟𝑖𝑗|||𝛾-1 𝑖𝑗̃𝜃2 2𝑖𝑗(𝑡)

$$
𝑉𝜏=𝑅\sum
$$

𝑖=1\sum

$$
𝑗∈𝑆𝑖𝑉𝜏𝑖𝑗, 𝑉𝜏𝑖𝑗=𝑞𝑜\int 𝑡
$$

𝑡-𝜏𝑗𝑖(𝑡)‖𝑒𝑥𝑖(𝑠)‖2𝑑𝑠 (A.1) where ̃ 𝑧𝑖𝑗(𝑡) =̃𝜃𝑖𝑗(𝑡) +𝑧𝑜𝑖+sgn(𝜃𝑟𝑖𝑗)𝛤𝑃𝑖𝑧𝑖(𝑡), 𝑧𝑖(𝑡) =𝜔𝑖(𝑡)𝐸𝑖(𝑒𝑥𝑖) (A.2) ̃𝜃2𝑖𝑗(𝑡) =𝜃2𝑖𝑗(𝑡) +sign(𝐸𝑖(𝑒𝑥𝑖))𝜃∗ 2𝑖𝑗, 𝜃∗ 2𝑖𝑗=𝜃∗-1 𝑟𝑖𝑗𝜒∗ 𝑖𝑗(A.3) and𝛤𝐼𝑖,𝛤𝑃𝑖,𝛾𝑃𝑖𝑗and𝛾𝑖𝑗are from (14) 𝑧𝑇 𝑜𝑖=[ -𝑟𝑜 2𝑐𝑎𝑟𝑑(𝑆𝑖)𝑏𝑇 𝑟𝑖𝑃𝑖0 0] , 𝑟𝑜>0. (A.4) The vector 𝑧𝑜𝑖with the chosen scalar 𝑟𝑜>0is ‘‘artificial’’ and used only in the process of the stability proof. The sign function is defined as sgn (⋆) = 1,if(⋆)>0;sgn(⋆) = 0,if(⋆) = 0; sgn(⋆) = -1,if(⋆)<0. The ‘‘virtual’’ scalar adaptation gain 𝜃2𝑖𝑗(𝑡)and unknown parameters 𝜒∗ 𝑖𝑗will be defined later. The time derivative of the Lyapunov-krasovskii functional components. Using (15) and 𝐸𝑖(𝑒𝑥𝑖)from (14), the time derivatives of the component 𝑉1𝑖along (17) can be written as ̇𝑉1𝑖|(17)= -𝑒𝑇

$$
𝑥𝑖(𝑡)𝑄𝑖𝑒𝑥𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇 𝑖𝑗(𝑡)𝜔𝑖(𝑡) +\sum 𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗

$$
𝑟𝑖𝑗𝑢2𝑖𝑗(𝑡) +\sum
$$

𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗

$$
𝑟𝑖𝑗𝑑𝑒𝑞𝑖𝑗(∙) +\sum
$$

𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗ 𝑑𝑖𝑝𝑗𝑖(∙) (A.5) where𝑑𝑒𝑞𝑖𝑗(∙) = -𝑑𝑎𝑔𝑟𝑖𝑗(∙) +𝜃∗-1 𝑟𝑖𝑗𝜃∗ 𝑑𝑖1 𝑐𝑎𝑟𝑑(𝑆𝑖)𝑑𝑖(𝑡). In view of (13) and using boundedness of the reference signals‖‖‖𝑥𝑟𝑗(𝑡)‖‖‖\le 𝑥∗ 𝑟𝑗,|||𝑟𝑗(𝑡)|||\le 𝑟∗ 𝑗, the following estimate of the last term of (A.5) can be calculated \sum 𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗

$$
𝑑𝑖𝑝𝑗𝑖(∙)\le \sum
$$

𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖||||||𝑝𝑗𝑖(∙)|||(A.6)

$$
\le \sum
$$

𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 𝑖𝑗+\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗

$$
1𝑖𝑗‖𝑒𝑥𝑗(𝑡)‖+\sum
$$

𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 2𝑖𝑗‖𝑒𝑥𝑗(𝑡-𝜏𝑗𝑖(𝑡))‖ Then, using (A.6) into (A.5) gives ̇𝑉1𝑖|(17)\le -𝑒𝑇

$$
𝑥𝑖(𝑡)𝑄𝑖𝑒𝑥𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝜔𝑖(𝑡) +\sum
$$

𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 1𝑖𝑗‖𝑒𝑥𝑗(𝑡)‖

<!-- page 17 -->

Transportation Research Part C 133 (2021) 103380 17J. Haddad et al. +\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 2𝑖𝑗‖𝑒𝑥𝑗(𝑡-𝜏𝑗𝑖(𝑡))‖ +\sum 𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗

$$
𝑟𝑖𝑗𝑢2𝑖𝑗(𝑡) +\sum
$$

𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 𝑖𝑗+\sum 𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗ 𝑟𝑖𝑗𝑑𝑒𝑞𝑖𝑗(∙) (A.7) Estimations for the last two terms of (A.7) are \sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 𝑖𝑗+\sum 𝑗∈𝑆𝑖2𝐸𝑖(𝑒𝑥𝑖)𝜃∗

$$
𝑟𝑖𝑗𝑑𝑒𝑞𝑖𝑗(∙)\le 𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)||𝜒∗ 𝑖𝑗(A.8) where the unknown constant 𝜒∗ 𝑖𝑗=|||𝜃∗ 𝑑𝑖|||𝜉∗ 𝑖𝑗+|||𝜃∗ 𝑟𝑖𝑗|||𝑑∗ 𝑒𝑞𝑖𝑗. By using (A.8), (A.7), and 𝑢2𝑖𝑗(𝑡)from (14) we have

$$
̇𝑉1|(17)\le -𝑅\sum
$$

𝑖=1𝑒𝑇

$$
𝑥𝑖(𝑡)𝑄𝑖𝑒𝑥𝑖(𝑡) +𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝜔𝑖(𝑡)𝐸𝑖(𝑒𝑥𝑖)𝑧𝑖(𝑡)+𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)||𝜒∗ 𝑖𝑗 -𝑅\sum 𝑖=1\sum 𝑗∈𝑆𝑖2|||𝜃∗

$$
𝑟𝑖𝑗|||𝛾𝑖𝑗𝐸𝑖(𝑒𝑥𝑖)\int 𝑡
$$

$$
0𝐸𝑖(𝑒𝑥𝑖(𝑡))𝑑𝑡+𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 1𝑖𝑗‖𝑒𝑥𝑗(𝑡)‖ +𝑅\sum 𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗ 2𝑖𝑗‖𝑒𝑥𝑗(𝑡-𝜏𝑗𝑖(𝑡))‖. (A.9) The time derivative of 𝑉2𝑖satisfies

$$
̇𝑉2𝑖=\sum
$$

𝑗∈𝑆𝑖2|𝜃𝑟𝑖𝑗|-1̃ 𝑧𝑇 𝑖𝑗(𝑡)𝛤-1 𝐼𝑖̇̃ 𝑧𝑖𝑗(𝑡). (A.10) In view of the adaptation algorithm from (14) it follows that ̇̃ 𝑧𝑖𝑗(𝑡) = sgn(𝜃𝑟𝑖𝑗)𝛤𝐼𝑖𝑧𝑖(𝑡), and we get from (A.10)

$$
̇𝑉2𝑖= - 2\sum
$$

𝑗∈𝑆𝑖𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝑧𝑖(𝑡) - 2\sum
$$

𝑗∈𝑆𝑖|||𝜃𝑟𝑖𝑗|||𝑧𝑇

$$
𝑖(𝑡)𝛤𝑃𝑖𝑧𝑖(𝑡) - 2\sum
$$

𝑗∈𝑆𝑖𝑧𝑇 𝑜𝑖𝑧𝑖(𝑡)

$$
\le - 2\sum
$$

𝑗∈𝑆𝑖𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝑧𝑖(𝑡) - 2\sum
$$

𝑗∈𝑆𝑖𝑧𝑇 𝑜𝑖𝑧𝑖(𝑡). (A.11)

$$
Invoking the constant vector 𝑧𝑜𝑖from (A.4) for the last term of (A.11), it follows -2\sum
$$

𝑗∈𝑆𝑖𝑧𝑇 𝑜𝑖𝑧𝑖(𝑡) = -𝑟𝑜𝐸2 𝑖(𝑒𝑥𝑖).Then, using (A.11) we can write

$$
̇𝑉2\le -𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2𝜃∗ 𝑟𝑖𝑗̃𝜃𝑇

$$
𝑖𝑗(𝑡)𝑧𝑖(𝑡) -𝑅\sum
$$

𝑖=1𝑟𝑜𝐸2 𝑖(𝑒𝑥𝑖). (A.12) Invoking (7) the time derivative of 𝑉𝜏can be written in the following form

$$
̇𝑉𝜏|(17)\le 𝑅\sum
$$

$$
𝑖=1𝑞𝑜1‖‖𝑒𝑥𝑖(𝑡)‖‖2-𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖𝑞𝑜2‖‖‖𝑒𝑥𝑖(𝑡-𝜏𝑗𝑖(𝑡))‖‖‖2, (A.13)

$$
where𝑞𝑜2=𝑞𝑜1(1 -𝜏∗). The time derivative of 𝑉3is calculated for two cases - when 𝐸𝑖(𝑒𝑥𝑖)\ne 0and𝐸𝑖(𝑒𝑥𝑖) = 0 , (Mirkin and
$$

Gutman, 2010; Mirkin et al., 2012). Now, the ‘‘virtual" adaptation gain 𝜃2𝑖𝑗(𝑡)in (A.3) is defined as ̇𝜃2𝑖𝑗(𝑡) = sgn(𝜃𝑟𝑖𝑗)𝛾𝑖𝑗𝐸𝑖(𝑒𝑥𝑖), 𝜃2𝑖𝑗(0) = 0. (A.14) Applyinġ𝜃2𝑖𝑗(𝑡)from (A.14) for the time derivative ̇𝑉3𝑖(𝑡)we obtain ̇𝑉3𝑖|(17)=2|||𝜃𝑟𝑖𝑗|||𝛾-1 𝑖𝑗𝜃2𝑖𝑗(𝑡)̇𝜃2𝑖𝑗(𝑡) +|||𝜃𝑟𝑖𝑗|||𝛾-1 𝑖𝑗sign𝐸𝑖(𝑒𝑥𝑖)𝜃∗ 2𝑖𝑗̇𝜃2𝑖𝑗(𝑡) = 2𝜃𝑟𝑖𝑗𝜃2𝑖𝑗(𝑡)𝐸𝑖(𝑒𝑥𝑖) -𝜃𝑟𝑖𝑗𝜃∗ 2𝑖𝑗||𝐸𝑖(𝑒𝑥𝑖)||

$$
=2|||𝜃𝑟𝑖𝑗|||𝛾𝑖𝑗𝐸𝑖(𝑒𝑥𝑖)\int 𝑡
$$

0𝐸𝑖(𝑒𝑥𝑖)𝑑𝑡2𝜒∗ 𝑖𝑗||𝐸𝑖(𝑒𝑥𝑖)||. (A.15)

$$
For convenience, let us define 𝑄𝑖from (15),𝑟𝑜from (A.12) and 𝑞𝑜2from (A.13) as 𝑄𝑖=𝑞1𝑖𝐼+𝑞2𝑖𝐼,𝑞1𝑖,𝑟𝑜=𝑟𝑜1+𝑟𝑜2and𝑞𝑜2=𝑞𝑜3+𝑞𝑜4,
$$

respectively, where 𝑞1𝑖>0,𝑞2𝑖>0,𝑟𝑜1>0,𝑟𝑜2>0and𝑞𝑜3>0,𝑞𝑜4>0are positive constants, and 𝐼is the identity matrix. Combining the last two terms of (A.9) with the second terms of (A.12) and (A.13), respectively, completing the squares and dropping negative terms, after simplifications one gets 𝑅\sum 𝑖=1\sum 𝑗∈𝑆𝑖-𝑟𝑜1 𝑐𝑎𝑟𝑑(𝑆𝑖)𝐸2

$$
𝑖(𝑒𝑥𝑖) +𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗

$$
1𝑖𝑗‖𝑒𝑥𝑗(𝑡)‖\le 𝑅\sum
$$

𝑖=1𝑐𝑖1 𝑟𝑜1‖𝑒𝑥𝑖(𝑡)‖2(A.16) and -𝑅\sum 𝑖=1\sum

$$
𝑗∈𝑆𝑖𝑞𝑜4‖‖‖𝑒𝑥𝑖(𝑡-𝜏𝑗𝑖(𝑡))‖‖‖2+𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖2||𝐸𝑖(𝑒𝑥𝑖)|||||𝜃∗ 𝑑𝑖|||𝜉∗

$$
2𝑖𝑗‖𝑒𝑥𝑗(𝑡-𝜏𝑗𝑖(𝑡))‖\le 𝑅\sum
$$

𝑖=1𝑐2𝑖 𝑞𝑜4𝐸2 𝑖(𝑒𝑥𝑖) (A.17)

<!-- page 18 -->

Transportation Research Part C 133 (2021) 103380 18J. Haddad et al.

$$
where𝑐𝑖1=\sum
$$

𝑗∈𝑆𝑖(𝑐𝑎𝑟𝑑(𝑆𝑖)|||𝜃∗ 𝑑𝑗|||𝜉∗

$$
1𝑗𝑖)2and𝑐2𝑖=\sum
$$

𝑗∈𝑆𝑖(|||𝜃∗ 𝑑𝑖|||𝜉∗ 2𝑖𝑗)2are unknown constants. Further, grouping (A.9), (A.12), (A.16) (A.13), (A.15) and (A.17) results in

$$
̇𝑉|(17)\le -𝑅\sum
$$

$$
𝑖=1𝑞1‖‖𝑒𝑥𝑖(𝑡)‖‖2-𝑅\sum
$$

𝑖=1\sum 𝑗∈𝑆𝑖𝑞𝑜3‖‖‖𝑒𝑥𝑖(𝑡-𝜏𝑗𝑖(𝑡))‖‖‖2 -𝑅\sum 𝑖=1[ 𝑟𝑜2-𝑐2𝑖 𝑞𝑜2] 𝐸2

$$
𝑖(𝑒𝑥𝑖) -𝑅\sum
$$

𝑖=1[ 𝑞2-𝑐𝑖1 𝑟𝑜1-𝑞𝑜1] ‖‖𝑒𝑥𝑖(𝑡)‖‖2. (A.18) Now, if selective parameters 𝑟𝑜1,𝑟𝑜2and𝑞𝑜1,𝑞𝑜2are chosen from the inequalities 𝑟𝑜1>𝑐1𝑖 𝑞2-𝑞𝑜1and𝑟𝑜2>𝑐2𝑖 𝑞𝑜2, one obtains from (A.18)

$$
̇𝑉|(17)\le -𝑅\sum
$$

$$
𝑖=1𝑞1‖‖𝑒𝑥𝑖(𝑡)‖‖2-𝑅\sum
$$

𝑖=1\sum

$$
𝑗∈𝑆𝑖𝑞𝑜2‖‖‖𝑒𝑥𝑖(𝑡-𝜏𝑗𝑖(𝑡))‖‖‖2\le 0, (A.19)
$$

$$
Thus, we have proved that 𝑉and, therefore 𝑒𝑥𝑖(𝑡),̃𝜃𝑖𝑗(𝑡),𝜃𝑖𝑗(𝑡) ∈𝐿\infty , (i=1,. .. ,R, 𝑗∈𝑆𝑖) and𝑒𝑥𝑖(𝑡) ∈𝐿2by following the
$$

usual arguments (Ioannou and Sun, 1996; Tao, 2003). The remainder of the stability analysis follows directly using the steps in (Ioannou and Sun, 1996; Tao, 2003). Because 𝑒𝑥𝑖(𝑡),𝜃𝑖𝑗(𝑡)are bounded, it follows that 𝑢𝑖𝑗(𝑡) ∈𝐿\infty . So all signals are bounded. With 𝑒𝑥𝑖(𝑡) ∈𝐿2⋂𝐿\infty anḋ 𝑒𝑥𝑖(𝑡) ∈𝐿\infty , applying, e.g. Corollary 2.8. in (Tao, 2003, p. 81), we conclude that lim𝑡→\infty 𝑒𝑥𝑖(𝑡) = 0 for all 𝑖= 1,…,𝑅and𝑗∈𝑆𝑖. Remark 5. In addition to the boundness of all signals and go to zero tracking error now we also show that the proposed design meets the requirement of avoiding the Zeno behavior, i.e. the phenomenon that the event is triggered for infinite times in a finite time interval. The standard way to avoid Zeno behavior see e.g. Miskowich (ed) is to derive a lower bound for the interevent time {𝑡𝑘+1-𝑡𝑘}, namely under the event detector rule (EVDR), the length of the interevent interval is bounded from below by a positive constant. We provide a proof sketch of this result that highlights its key components and refer to e.g. works (Miskowich, ed) for details. Denoting 𝜖𝑖(𝑡) =𝑢𝑖𝑗(𝑡) -𝑢𝑖𝑗(𝑡𝑖 𝑘)errors induced by the event-triggered implementation, the time-derivative of 𝜖𝑖(𝑡) between the time instants 𝑡𝑖 𝑘and𝑡𝑖 𝑘+1, computed as ̇ 𝜖𝑖(𝑡) =̇𝑢𝑖𝑗(𝑡). For ∀𝑡∈ [𝑡𝑖 𝑘,𝑡𝑖 𝑘+1),𝑘= 0,1,…, integrating this expression result in

$$
||𝜖𝑖(𝑡)||\le \int 𝑡
$$

𝑡𝑖 𝑘|||̇𝑢𝑖𝑗(𝑡)|||. Since𝑢𝑖𝑗(𝑡)is a function of the signals 𝜃𝑖(𝑡),𝜔𝑖(𝑡)and𝐸𝑖(𝑒𝑥𝑖(𝑡))(see (14)), and the boundedness of all the closed-loop signals has been ensured in Theorem 1, there must exist a set of positive constants 𝜅𝑖such that|||̇𝑢𝑖𝑗|||\le 𝜅𝑖. So (𝑡-𝑡𝑖 𝑘)𝜅𝑖\ge ||𝜖𝑖||, which invoking EVDR (8) guarantees a lower bound for the inter-event times.

## References

Aboudolas, K., Papageorgiou, M., Kosmatopoulos, E., 2009. Store-and-forward based methods for the signal control problem in large-scale congested urban road networks. Transp. Res. C 17, 163-174. Alisoltani, N., Leclercq, L., Zargayouna, M., 2021. Can dynamic ride-sharing reduce traffic congestion? Transp. Res. B 145, 212-246. Balachandran, S., Narkawicz, A., Muñoz, C., Consiglio, M., 2017. A path planning algorithm to enable well-clear low altitude UAS operation beyond visual line of sight. In: Twelfth USA/Europe Air Traffic Management Research and Development Seminar (ATM2017). Batista, S., Leclercq, L., Geroliminis, N., 2019. Estimation of regional trip length distributions for the calibration of the aggregated network traffic models. Transp. Res. B 122, 192-217. Batista, S., Seppecher, M., Leclercq, L., 2021. Identification and characterizing of the prevailing paths on a urban network for mfd-based applications. Transp. Res. C 127, 102953. Battista, A., Ni, D., 2017. Modeling small unmanned aircraft system traffic flow under external force. Transp. Res. Rec. 2626 (1), 74-84. Belcastro, C.M., Klyde, D.H., Logan, M.J., Newman, R.L., Foster, J.V., 2017. Experimental flight testing for assessing the safety of unmanned aircraft system safety-critical operations. In: 17th AIAA Aviation Technology, Integration, and Operations Conference, p. 3274. Berger, Ronald, 2018. Urban air mobility the rise of a new mode of transportation. Buisson, C., Ladier, C., 2009. Exploring the impact of homogeneity of traffic measurements on the existence of macroscopic fundamental diagrams. Transp. Res. Rec. 2124, 127-136. Bulusu, V., Sengupta, R., Mueller, E.R., Xue, M., 2018. A throughput based capacity metric for low-altitude airspace. In: 2018 Aviation Technology, Integration, and Operations Conference. p. 3032. Cuniasse, P.-A., Buisson, C., Rodriguez, J., Teboul, E., De Almeida, D., 2015. Analyzing railroad congestion in a dense urban network through the use of a road traffic network fundamental diagram concept. Publ. Transp. 7 (3), 355-367. Daganzo, C.F., 1994. The cell transmission model: A dynamic representation of highway traffic consistent with the hydrodynamic theory. Transp. Res. B 28 (4), 269-287. Daganzo, C.F., 2007. Urban gridlock: Macroscopic modeling and mitigation approaches. Transp. Res. B 41 (1), 49-62. Daganzo, C.F., Gayah, V.V., Gonzales, E.J., 2011. Macroscopic relations of urban traffic variables: Bifurcations, multivaluedness and instability. Transp. Res. B

## 45 (1), 278-288.

D’Ans, G., Gazis, D., 1976. Optimal control of oversaturated store-and forward transportation networks. Transp. Sci. 10 (1), 1-19. Diakaki, C., Dinopoulou, V., Aboudolas, K., Papageorgiou, M., Ben-Shabat, E., Seider, E., Leibov, A., 2003. Extensions and new applications of the traffic-responsive urban control strategy: Coordinated signal control for urban networks. Transp. Res. Rec. 1856 (1), 202-211. Diakaki, C., Papageorgiou, M., Aboudolas, K., 2002. A multivariable regulator approach to traffic-responsive network-wide signal control. Control Eng. Pract. 10 (13), 183-195. Fu, H., Wang, Y., Tang, X., Zheng, N., Geroliminis, N., 2020. Empirical analysis of large-scale multimodal traffic with multi-sensor data. Transp. Res. C 118, 102725. Gartner, N.H., 1983. OPAC: A demand responsive strategy for traffic signal control. Transp. Res. Rec. 906, 75-81. Gartner, N.H., Pooran, F.J., Andrews, C.M., 2002. Optimized policies for adaptive control strategy in real-time traffic adaptive control systems, implementation and field testing. Transp. Res. Rec. 1811, 148-156.

<!-- page 19 -->

Transportation Research Part C 133 (2021) 103380 19J. Haddad et al. Gayah, V.V., Daganzo, C.F., 2011. Clockwise hysteresis loops in the macroscopic fundamental diagram: An effect of network instability. Transp. Res. B 45 (4), 643-655. Geroliminis, N., Daganzo, C.F., 2008. Existence of urban-scale macroscopic fundamental diagrams: some experimental findings. Transp. Res. B 42 (9), 759-770. Geroliminis, N., Haddad, J., Ramezani, M., 2013. Optimal perimeter control for two urban regions with macroscopic fundamental diagrams: A model predictive approach. IEEE Trans. Intell. Transp. Syst. 14 (1), 348-359. Gharibi, M., Boutaba, R., Waslander, S.L., 2016. Internet of drones. IEEE Access 4, 1148-1162. Gharibi, M., Boutaba, R., Waslander, S.L., 2019. 3D traffic flow model for uavs. Godfrey, J.W., 1969. The mechanism of a road network. Traff. Eng. Control 11 (7), 323-327. Hackenberg, D., 2019. Nasa grand challenge update for vfs. Haddad, J., 2015. Robust constrained control of uncertain macroscopic fundamental diagram networks. Transp. Res. C 59, 323-339. Haddad, J., Mirkin, B., 2016a. Adaptive multiple input delays compensation under input constraints applied to perimeter traffic control. In: Proceedings of the 14-th IFAC Symposium on Control in Transportation Systems (CTS). Istanbul, Turkey. Haddad, J., Mirkin, B., 2016b. Adaptive perimeter traffic control of urban road networks based on MFD model with time delays. Int. J. Robust Nonlinear Control 26, 1267-1285. Haddad, J., Mirkin, B., 2017a. Coordinated distributed adaptive perimeter control for large-scale urban road networks. Transp. Res. C 77, 495-515. Haddad, J., Mirkin, B., 2017b. Distributed fault tolerant perimeter control for urban road networks. In: The 20th World Congress of the International Federation of Automatic Control. Toulouse, France. Haddad, J., Mirkin, B., 2017c. Distributed fault tolerant perimeter control for urban road networks. In: 20th IFAC World Congress, (IFAC WC 2017). Toulouse, France, July 9-14, pp. 4318-4323. Haddad, J., Mirkin, B., 2019a. Coordinated distributed adaptive perimeter control for large-scale urban road networks. Transp. Res. C 77, 495-515. Haddad, J., Mirkin, B., 2019b. Resilient perimeter control of macroscopic fundamental diagram networks under cyberattacks. Transp. Res. B. Haddad, J., Mirkin, B., 2020. Resilient perimeter control of macroscopic fundamental diagram networks under cyberattacks. Transp. Res. B 132, 44-59. Haddad, J., Shraiber, A., 2014. Robust perimeter control design for an urban region. Transp. Res. B 68, 315-332. Haddad, J., Zheng, Z., 2018. Adaptive perimeter control for multi-region accumulation-based models with state delays. Transp. Res. B http://dx.doi.org/10.1016/ j.trb.2018.05.019. Hajiahmadi, M., Haddad, J., Schutter, B.D., Geroliminis, N., 2015. Optimal hybrid perimeter and switching plans control for urban traffic networks. IEEE Trans. Control Syst. Technol. 23 (2), 464-478. Heemels, W.P.M.H., Johansson, K.H., Tabuada, P., 2012. An introduction to event-triggered and self-triggered control. In: Proc. IEEE Conf. Decis. Contr. Maui, HW, pp. 3270-3285. Herman, R., Prigogine, I., 1979. A two-fluid approach to town traffic. Science 204 (4389), 148-151. Hof, H.J., 2018. Trajectory based operations will deliver atm enhancements. Hoogendoorn, S., Campanella, M., Daamen, W., 2011. Fundamental diagrams for pedestrian networks. In: Peacock, R.D., Kuligowski, E.D., Averill, J.D. (Eds.), Pedestrian and Evacuation Dynamics. Springer US, Boston, MA, pp. 255-264. Hunt, P.B., Roberston, D.L., Bretherton, R.D., 1982. The SCOOT on-line traffic signal optimization technique. Traffic Eng. Control 23, 190-192. Ioannou, P.A., Fidan, B., 2006. Adaptive Control Tutorial. SIAM, USA. Ioannou, P.A., Sun, J., 1996. Robust Adaptive Control. Prentice Hall, New Jersey. Jang, D.-S., Ippolito, C.A., Sankararaman, S., Stepanyan, V., 2017. Concepts of airspace structures and system analysis for UAS traffic flows for urban areas. In: AIAA Information Systems-AIAA Infotech@ Aerospace. p. 0449. Ji, Y., Daamen, W., Hoogendoorn, S., Hoogendoorn-Lanser, S., Qian, X., 2010. Macroscopic fundamental diagram: Investigating its shape using simulation data. Transp. Res. Rec. 2161, 42-48. Johnson, M., Jung, J., Rios, J., Mercer, J., Homola, J., Prevot, T., Mulfinger, D., Kopardekar, P., 2017. Flight test evaluation of an unmanned aircraft system traffic management (UTM) concept for multiple beyond-visual-line-of-sight operations. Keyvan-Ekbatani, M., Kouvelas, A., Papamichail, I., Papageorgiou, M., 2012. Exploiting the fundamental diagram of urban networks for feedback-based gating. Transp. Res. B 46 (10), 1393-1403. Kılınç, M.R., Sahinidis, N.V., 2018. Exploiting integrality in the global optimization of mixed-integer nonlinear programming problems with baron. Optim. Methods Softw. 33 (3), 540-562. Kopardekar, P.H., 2014. Unmanned aerial system (uas) traffic management (utm): Enabling low-altitude airspace and uas operations. Kopardekar, P., Rios, J., Prevot, T., Johnson, M., Jung, J., Robinson, J.E., 2016. Unmanned aircraft system traffic management (utm) concept of operations. Kouvelas, A., Saeedmanesh, M., Geroliminis, N., 2017. Enhancing model-based feedback perimeter control with data-driven online adaptive optimization. Transp. Res. B 96, 26-45. Krstić, M., 2009. Delay Compensation for Nonlinear, Adaptive, and PDE Systems. Birkhauser, Boston. Kuchar, J.K., Yang, L.C., 2000. A review of conflict detection and resolution modeling methods. IEEE Trans. Intell. Transp. Syst. 1 (4), 179-189. Lamotte, Raphaël, Geroliminis, Nikolas, 2018. The morning commute in urban areas with heterogeneous trip lengths. Transp. Res. B 117, 794-810. Lin, S., De Schutter, B., Xi, Y., Hellendoorn, H., 2011. Fast model predictive control for urban road networks via milp. IEEE Trans. Intell. Transp. Syst. 12 (3), 846-856. Little, J.D.C., Kelson, M.D., Gartner, N.H., 1981. MAXBAND: A program for setting signals on arteries and triangular networks. Transp. Res. Rec. 795. Liua, L., Zhou, J., Wen, C., Zhao, X., 2017. Robust adaptive tracking control of uncertain systems with time-varying input delays. Int. J. Syst. Sci. 48 (16), 3440-3449. Mahmassani, H., Williams, J., Herman, R., 1987. Performance of urban traffic networks. In: Gartner, N., Wilson, N. (Eds.), Proceedings of the 10th International Symposium on Transportation and Traffic Theory. Elsevier, Amsterdam, The Netherlands. Mariotte, G., Leclercq, L., Laval, J.A., 2017. Macroscopic urban dynamics: Analytical and numerical comparisons of existing models. Transp. Res. B 101, 245-267. Mazloumian, A., Geroliminis, N., Helbing, D., 2010. The spatial variability of vehicle densities as determinant of urban network capacity. Phil. Trans. R. Soc. A

## 368 (1928), 4627-4647.

Mirkin, B.M., Gutman, P.-O., 2009. Adaptive output-feedback tracking: the case of MIMO plants with unknown, time-varying state delay. Systems Control Lett.

## 58 (1), 62-68.

Mirkin, B.M., Gutman, P.-O., 2010. Robust adaptive output-feedback tracking for a class of nonlinear time-delayed plants. IEEE Trans. Automat. Control 55 (10), 2418-2424. Mirkin, B., Gutman, P.-O., Shtessel, Y., 2012. Asymptotic sliding mode control approach to adaptive distributed tracking problem for multi-agent nonlinear delayed systems. Internat. J. Control 85 (11), 1671-1682. Mirkin, B., Haddad, J., Shtessel, Y., 2016. Tracking with asymptotic sliding mode and adaptive input delay effect compensation of nonlinear delayed systems applied to traffic feedback control. Internat. J. Control. Mirkin, B.M., Mirkin, E.L., Gutman, P.-O., 2009. State-feedback adaptive tracking of linear systems with input and state delays. Internat. J. Adapt. Control Signal Process. 23 (6), 567-580. Miskowich(ed), M., 2016. Event-Based Control and Signal Processing. CRS Press, New Jersey.

<!-- page 20 -->

Transportation Research Part C 133 (2021) 103380 20J. Haddad et al. Neto, E.C.P., Baum, D.M., Junior, J. R. d. A., Junior, J.B.C., Cugnasca, P.S., 2019. Trajectory-based urban air mobility (UAM) operations simulator (tus). arXiv preprint arXiv:1908.08651. Niculescu, S.I., Annaswamy, A.M., 2003. An adaptive smith-controller for time-delay systems with relative degree 𝑛∗\le 2. Syst. Control Lett. 49 (5), 347-358. Olszewski, P., Fan, H.S.L., Tan, Y.-W., 1995. Area-wide traffic speed-flow model for the Singapore CBD. Transp. Res. A 29A (4), 273-281. Ortega, R., Lozano, R., 1988. Globally stable adaptive controller for systems with delay. Internat. J. Control 47 (1), 17-23. Papageorgiou, M., Diakaki, C., Dinopoulou, V., Kotsialos, A., Wang, Y., 2003. Review of road traffic control strategies. Proc. IEEE 91 (12), 2043-2067. Planning, J., Office, D., 2010. Concept of operations for the next generation air transportation system. Version 3.2. Ramasamy, S., Sabatini, R., Gardi, A., Kistan, T., 2014. Next generation flight management system for real-time trajectory based operations. In: Applied Mechanics and Materials, vol. 629. Trans Tech Publ, pp. 344-349. Ramezani, M., Haddad, J., Geroliminis, N., 2015. Dynamics of heterogeneity in urban networks: aggregated traffic modeling and hierarchical control. Transp. Res. B 74, 1-19. Simaiakis, I., Khadilkar, H., Balakrishnan, H., Reynolds, T.G., Hansman, R.J., 2014. Demonstration of reduced airport congestion through pushback rate control. Transp. Res. A 66, 251-267. Sirmatel, I.I., Geroliminis, N., 2021. Stabilization of city-scale road traffic networks via macroscopic fundamental diagram-based model predictive perimeter control. Control Eng. Pract. 109, 104750. Sirmatel, I.I., Tsitsokas, D., Kouvelas, A., Geroliminis, N., 2021. Modeling, estimation, and control in large-scale urban road networks with remaining travel distance dynamics. Transp. Res. C 128, 103157. Skabardonis, A., Geroliminis, N., 2008. Real-time monitoring and control on signalized arterials. J. Intell. Transp. Syst. 12 (2), 64-74. Tao, G., 2003. Adaptive Control Design and Analysis. John Wiley & Sons, New York. UAS Traffic Management (UTM) Project, 2018. National Aeronautics and Space Administration. Wensveen, J., 2018. Air Transportation: A Management Perspective. Routledge. Xue, M., Do, M., 2019. Scenario complexity for unmanned aircraft system traffic. In: AIAA Aviation 2019 Forum. p. 3513. Yang, L., Yin, S., Han, K., Haddad, J., Hu, M., 2017. Fundamental diagrams of airport surface traffic: Models and applications. Transp. Res. B 106, 29-51. Yildirimoglu, M., Sirmatel, I.I., Geroliminis, N., 2018. Hierarchical control of heterogeneous large-scale urban road networks via path assignment and regional route guidance. Transp. Res. B 118, 106-123. Yildiz, Y., Annaswamy, A., Kolmanovsky, I., Yanakiev, D., 2010. Adaptive posicast controller for time-delay systems with relative degree 𝑛∗\le 2. Automatica 46, 279-289. Zegeye, S., Schutter, B.D., Hellendoorn, J., Breunesse, E., Hegyi, A., 2013. Integrated macroscopic traffic flow, emission, and fuel consumption model for control purposes. Transp. Res. C 31, 158-171. Zhang, L., Garoni, T., de Gier, J., 2013. A comparative study of macroscopic fundamental diagrams of arterial road networks governed by adaptive traffic signal systems. Transp. Res. B 49, 1-23. Zhou, H., Bouyekhf, R., Moudni, A.EL., 2015. Constrained 𝐻\infty control of urban transportation network. J. Adv. Transp. 49, 434-456. Zhou, J., Jin, L., Wang, X., Sun, D., 2020. Resilient uav traffic congestion control using fluid queuing models. IEEE Trans. Intell. Transp. Syst. Zhou, J., Wen, C., Wang, W., 2009. Adaptive backstepping control of uncertain systems with unknown input time-delay. Automatica 45, 1415-1422.
