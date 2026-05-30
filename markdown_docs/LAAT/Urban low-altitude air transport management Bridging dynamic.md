---
source_pdf: Urban low-altitude air transport management Bridging dynamic .pdf
pages: 24
---

# Urban low-altitude air transport management Bridging dynamic 

<!-- page 1 -->

Contents lists available at ScienceDirect Transportation Research Part C journal homepage: www.elsevier.com/locate/trc Urban low-altitude air transport management: Bridging dynamic traffic control and static network equilibrium Canqiang Wenga , Tianlu Panb, Can Chena,c , Renxin Zhonga ,∗ aGuangdong Provincial Key Laboratory of Intelligent Transportation Systems, School of Intelligent Systems Engineering, Sun Yat-Sen University, Shenzhen, China bDepartment of Network Intelligence, Peng Cheng Laboratory, Shenzhen, China cDepartment of Civil and Environmental Engineering, The Hong Kong Polytechnic University, Hong Kong, China

### A R T I C L E I N F O

Keywords: Low-altitude air transport Dynamic air traffic control Static network equilibrium Demand management Macroscopic fundamental diagram A B S T R A C T Urban air mobility is an innovative mode that lifts urban transport to the altitude dimension, giving rise to low-altitude air transport (LAAT) systems. Emerging LAAT systems involve largescale point-to-point operations, which require new management schemes distinct from the centralized flight control used in conventional aviation. In this paper, we explore flow-based traffic modeling for LAAT systems, including the static model of network equilibrium, as well as dynamic models of demand management and air traffic control. The static model aggregates individual UAM trips into traffic flows on the LAAT network, aiming to optimize the network flow pattern in the planning phase. The dynamic models describe regional traffic dynamics based on demand queuing and airspace macroscopic fundamental diagrams (MFDs), aiming to regulate the dynamics to a desired equilibrium in the control phase. Static network planning yields a system-optimal (SO) equilibrium, which is consistent with the desired equilibrium concept in dynamic traffic control. Inspired by this, we establish the interaction between static network planning and dynamic traffic control by deriving the desired equilibrium from the SO network equilibrium. The derived equilibrium is ensured to exist as a stable equilibrium and can be adjusted in response to traffic demand and airspace capacity. We devise a control scheme to implement the planning-control interaction. The proposed scheme, by coupling dynamic traffic control and demand management, can adjust the desired equilibrium according to changes in demand patterns, thus guaranteeing the feasibility of the set-point control problem with respect to varying demand patterns. Numerical examples demonstrate the merits of the integrated dynamic traffic control and demand management scheme. Compared to a fixed equilibrium based on experience, a variable SO equilibrium given by the planning-control interaction can significantly improve network efficiency, especially when demand patterns admit abrupt changes and noise. To the best of our knowledge, this paper is one of the first to bridge dynamic traffic control and static network equilibrium.

## 1. Introduction

Recurrent traffic congestion in metropolises demonstrates that simply expanding roadway infrastructure is no longer a sustainable solution to meet the increasing traffic demand. Recently, interest has surged in low-altitude airspace for its potential to enable pointto-point air travel in congested cities. With a vision to expand the transport supply using low-altitude airspace, urban air mobility ∗Corresponding author. E-mail addresses: wengcq@mail2.sysu.edu.cn (C. Weng) , pantl@pcl.ac.cn (T. Pan), can-caesar.chen@connect.polyu.hk (C. Chen) , zhrenxin@mail.sysu.edu.cn (R. Zhong) . https://doi.org/10.1016/j.trc.2025.105237 Received 24 March 2024; Received in revised form 31 March 2025; Accepted 7 June 2025Transportation Research Part C 178 (2025) 105237 0968-090X/© 2025 Elsevier Ltd. All rights are reserved, including those for text and data mining, AI training, and similar technologies.

<!-- page 2 -->

C. Weng et al.

#### Fig. 1. Different airspace structure designs for future LAAT systems, ordered by degrees of freedom (Sunil et al., 2015 ).

(UAM) has emerged as an innovative mode, opening altitude dimensions for future transport. Advances in electric vertical take-off and landing vehicles (eVTOLs) further promote UAM as a safe, affordable, and environmentally friendly mode (Kasliwal et al., 2019 ; Raghunatha et al., 2023 ). With the aid of ride-hailing apps like Lyft or Uber, the viability of large-scale UAM has been evidenced by the test flights of full-size eVTOLs (Dietrich and Wulff , 2020 ; Garrow et al., 2021 ). As reported by Uber Elevate, the service cost of UAM will drop to $1.84 per passenger mile (pax-mile) in the near term and further decrease to $0.44 per pax-mile in the longer term (Holden , 2018 ). Over the coming decade, the UAM market is projected to contribute up to $700 billion (RMB 5 trillion) to the country’s economy of China (Shen et al., 2023 ). The large-scale deployment of UAM would give rise to new transport systems, known as low-altitude air transport (LAAT) systems. In such systems, numerous low-altitude aircraft1 are deployed in urban areas for various missions, such as transferring passengers and goods. Emerging LAAT systems involve large-scale point-to-point operations, necessitating innovation in air traffic management (ATM) schemes. On the one hand, conventional ATM schemes are considered unsuitable for LAAT systems (Haddad et al., 2021 ; Safadi et al., 2024 ). Conventional schemes rely on centralized control of aircraft trajectories, where flights are preplanned and approved with fixed routes and schedules to avoid conflicts. These schemes are designed for low-volume and low-density aviation, focusing on air traffic safety. Recent studies indicate that LAAT systems would face congestion issues similar to roadway traffic, underscoring the need for efficient ATM solutions (Cummings and Mahmassani , 2024a ,b). As the number of aircraft grows, conventional ATM schemes struggle to provide feasible solutions for real-time LAAT management. On the other hand, advanced ATM schemes for high-volume and high-density LAAT systems have yet to be developed. To adapt conventional schemes to LAAT systems, NASA and the FAA initiated research into unmanned aircraft system traffic management (UTM). They proposed the original concept of operations (ConOps) for UTM (Kopardekar et al., 2016 ) and later released an updated version in FAA NextGen Organization (2022 ). In Europe, SESAR Joint Undertaking (2017 ) proposed a similar ATM ConOps, known as urban space (U-space). A detailed discussion and comparison of the UTM and U-space ConOps can be found in Shrestha et al. (2021 ). The proposed concepts envision different technical capability levels, evolving from low to high traffic density. At the early stage, structured airspace is suggested to separate aircraft with different properties, such as direction and mobility capacity. In the literature, the proposed airspace structures can be categorized into four concepts, namely, tube, layer, zone, full mix (see Fig. 1), and their integration. According to Bauranov and Rakas (2021 ), less structured airspace allows aircraft to fly with more degrees of freedom, enabling higher traffic density. Hence, Haddad et al. (2021 ) recently suggested a regional full-mix airspace design for LAAT systems. Nevertheless, further investigation into advanced ATM schemes is needed to manage high-density LAAT systems. Insights gained from roadway transport systems indicate that flow-based traffic control is effective, particularly in oversaturated demand scenarios (Daganzo , 2007 ; Geroliminis and Daganzo , 2008 ; Keyvan-Ekbatani et al., 2012 ; Zhong et al., 2018b ). Flow-based management schemes regulate the operations of the overall traffic network at a macroscopic level by controlling traffic flows on specific network links. Widely used approaches to controlling link traffic flow include boundary control (Geroliminis et al.,

## 2013 ; Haddad and Shraiber , 2014 ; Zhong et al., 2018a , 2020 ; Su et al., 2020 ; Chen et al., 2022 ; Huang et al., 2024 ) and route

guidance (Haddad et al., 2013 ; Sirmatel and Geroliminis , 2018 ; Chen et al., 2024 ). Inspired by this, recent studies suggest flow-based management schemes for future LAAT systems (Haddad et al., 2021 ; Safadi et al., 2023b , 2024 ). Unlike conventional schemes that rely on centralized trajectory control of individual aircraft, flow-based schemes control aircraft traffic flows on the LAAT network . In the literature, flow-based management schemes can be roughly categorized into two paradigms: (i) the static paradigm that concentrates on long-term traffic patterns for network planning2 ; and (ii) the dynamic paradigm that focuses on short-term traffic dynamics for traffic control. The static management paradigm assumes that the traffic system operates at a steady state and aims to identify an optimal steady state for management. A representative approach within the static paradigm is traffic assignment, where the steady state refers to a specific flow pattern on the traffic network. Traffic assignment has been widely investigated in roadway traffic (Gartner , 1980a ,b; Patriksson , 2015 ), but its application in LAAT systems is still in the initial stage. Wang et al. (2022 ) modeled air traffic as flows within a multi-layer tube network and proposed an air traffic assignment framework to optimize the network 1In this paper, the term ‘‘low-altitude aircraft’’ collectively refers to aircraft operating in low-altitude airspace, including different configurations (e.g., fixed-wing or multi-rotor, with or without pilots). 2In this paper, the term ‘‘network planning’’ refers to optimizing the flow pattern on a given network.Transportation Research Part C 178 (2025) 105237

<!-- page 3 -->

C. Weng et al. flow pattern. Wang et al. (2023 ) extended the proposed framework for dynamic management by decomposing the dynamic traffic assignment problem into a series of static traffic assignment problems. Remarkably, optimizing network flow patterns in the above studies can be driven by a common objective, i.e., minimizing the total operational cost. In general, the operational cost for UAM may involve passengers’ waiting time for boarding aircraft (Shrestha et al., 2021 ) and eVTOLs’ cruising time in the air (Wei et al.,

## 2018 ). Wu and Zhang (2021 ) and Wang et al. (2022 , 2023 ) incorporated passengers’ monetary travel cost and network complexity

into the operational cost, respectively. The optimized network flow pattern that minimizes the total operational cost is known as a system-optimal (SO) network equilibrium. In other words, the desired steady state required by the static management paradigm can be identified as an SO network equilibrium. The dynamic management paradigm considers that the traffic system evolves over time and aims to control this evolution, particularly to prevent the system from developing traffic congestion. Along this line, the concept of Macroscopic Fundamental Diagram (MFD) is introduced to characterize different states of a traffic network (Daganzo , 2007 ; Geroliminis and Sun, 2011 ). The MFD3 provides an unimodal, low-scatter relationship between network traffic accumulation and network traffic outflow, enabling aggregated traffic flow modeling and control. Recently, several studies have attempted to extend the MFD concept to LAAT systems. Cummings and Mahmassani (2021 , 2024a ) revealed the existence of airspace MFDs by simulating point-to-point UAM operations in 3D space. Safadi et al. (2023a ) conducted large-scale air traffic simulations and comprehensively investigated the relationships between air traffic flow, density, and speed. A prerequisite for a well-defined MFD in a traffic network is the homogeneous traffic congestion distribution over space with a small variance of link densities (Geroliminis and Sun, 2011 ). In the context of LAAT, this crucial assumption is more likely to be satisfied, as evidenced by the re-routing approach in our latest work (Weng et al., 2024 ). Under the MFD framework, air traffic evolution can be characterized by a traffic flow dynamics model based on flow conservation. Haddad et al. (2021 ) modeled air traffic dynamics within multi-layer LAAT networks and proposed a feedback flow control strategy, where the controller regulates the air traffic dynamics by restricting the cross-boundary flows between airspace regions, known as boundary control. In further work, Safadi et al. (2023b ) developed a simplified air traffic flow model based on MFD, wherein boundary control was applied for air traffic demand management. Flow-based management schemes are promising for efficient LAAT management. However, existing studies are limited to a single management paradigm, rarely considering the interaction between long-term traffic patterns and short-term traffic dynamics (Wang et al., 2022 ; Safadi et al., 2024 ). On the one hand, the static paradigm assumes that the traffic pattern, particularly the demand pattern, remains constant over a long-term time scale. This steady-state traffic assumption makes the traffic network analytically tractable but fails to capture the dynamic variability of traffic congestion, especially the queuing process (Zhong et al., 2020 ). In the static paradigm, the SO network equilibrium is regarded as a holy grail for transportation authorities. Traffic managers always expect the network flow distribution to follow the pattern of SO equilibrium (Wu and Zhang , 2021 ; Wang et al., 2022 , 2023 ). On the other hand, the dynamic paradigm focuses on short-term traffic dynamics and implicitly assumes that the traffic pattern evolves periodically over the long-term time scale. This periodicity assumption of traffic pattern limits traffic dynamics models to take into account the variability in traffic demand and supply induced by the external environment (Cantarella and Watling , 2016 ). In the dynamic paradigm, a common practice is to regulate the traffic dynamics to a desired steady state (Haddad and Geroliminis , 2012 ; Zhong et al., 2018a ; Sirmatel and Geroliminis , 2021 ; Safadi et al., 2024 ). This desired state, also called a desired equilibrium, is often regarded as a preferable network state for management purposes. Under the MFD framework, selecting an appropriate desired equilibrium is as important as achieving it (Zhong et al., 2018b ). However, a systematic way to choose the desired equilibrium is yet to be developed in the literature. On the one hand, traffic demand, acting as a disturbance to MFD systems, is generally not fixed and can be elastic in response to traffic control schemes. Moreover, the implementation of control schemes will influence the shape of the MFD and then the network capacity. Given the dynamic nature of traffic demand and supply, especially for fast time-varying cases, identification of the desired equilibrium is an extremely difficult and unclear task in practice (Zhong et al., 2018b ). Consequently, most existing studies choose the desired equilibrium (e.g., as the critical point) based on experience (Haddad and Shraiber , 2014 ; Zhong et al., 2018a ; Chen et al., 2022 ; Safadi et al., 2024 ). This experiencedriven approach lacks a convincing interpretation and cannot guarantee the feasibility of the control problem in several cases, such as when travel demand is oversaturated or when the travel demand and/or the network fundamental diagram significantly deviate from their nominal values (Zhong et al., 2018b ; Haddad and Geroliminis , 2012 ). On the other hand, various traffic control efforts aim to improve the network performance as close to its best performance as possible. The best network performance corresponds to the well-known SO network equilibrium, which is regarded as a holy grail for transportation authorities. Note that both the static and dynamic paradigms involve the steady state of a traffic network. This observation leads us to speculate that the desired equilibrium can be derived from the SO network equilibrium. Thereby, this paper explores the static paradigm of network planning and the dynamic paradigm of traffic control, along with their interaction, to enable efficient LAAT management. The main objective of this paper is to develop an interpretable mechanism for selecting the desired equilibrium, which can adaptively adjust in response to traffic demand and supply. To achieve this, we derive the desired equilibrium from the SO equilibrium and devise a control scheme to regulate air traffic dynamics accordingly. The main contributions of this paper are summarized as follows: 1.We explore flow-based traffic modeling for LAAT systems, including the static model of network equilibrium, as well as dynamic models of demand management and air traffic control. The static model aggregates individual UAM trips into traffic flows on the 3In this paper, the term ‘‘MFD’’ specifically refers to the accumulation-based MFD model. For a comprehensive comparison of existing MFD models, readers are referred to Huang et al. (2024 ).Transportation Research Part C 178 (2025) 105237

<!-- page 4 -->

C. Weng et al.

#### Table 1

Key notations. Notation Description 𝑔 𝑖Ground region, 𝑖∈ {1,2} 𝑎 𝑗Airspace region, 𝑗∈ {1,2} 𝑘Take-off vertiport, 𝑘∈ {1,2,…, 𝑁}, where 𝑁 is the number of vertiports

𝑓𝑘 𝑙,𝑚The traffic flow of OD pair 𝑚 with take-off vertiport 𝑘 and landing vertiport 𝑙

𝑓𝑘The traffic flow taking off from vertiport 𝑘

𝑡𝑘,𝑙 𝑚The travel time of OD pair 𝑚 with take-off vertiport 𝑘 and landing vertiport 𝑙

𝑖 to region 𝑎 𝑗 at time 𝑡

𝑖 to region 𝑎 𝑗

𝑖 to region 𝑎 𝑗 at time 𝑡

𝑖 at time 𝑡

𝑖, mapping the accumulation 𝑛𝑖(𝑡) to the airspace outflow 𝐺𝑖(⋅)

| 𝑙 | Landing vertiport, 𝑙∈ {1,2,…, 𝑁} |
| --- | --- |
| 𝑚 | Origin-destination (OD) pair of UAM demand, 𝑚∈ {1,2,…, 𝑀}, where 𝑀 is the number of OD pairs |
| 𝑚 | The origin of OD pair 𝑚 |
| 𝑚 | The destination of OD pair 𝑚 |
| 𝑑𝑚 | The travel demand of OD pair 𝑚 |
| 𝑓𝑙 | The traffic flow landing at vertiport 𝑙 |
| 𝑡𝑚 | The generalized travel time of OD pair 𝑚 |
| 𝐷𝑚(𝑡𝑚) | The elastic demand function of OD pair 𝑚 |
| 𝑔𝑖𝑗(𝑡) | The air traffic demand from region 𝑎 |
| 𝑄𝑖𝑗(𝑡) | The length of the queue induced by demand 𝑔𝑖𝑗(𝑡) at time 𝑡 |
| 𝑠𝑖𝑗 | The maximum exit flow rate of queue 𝑄𝑖𝑗 |
| 𝑣𝑖𝑗(𝑡) | The queuing control at time 𝑡, regulating the exit flow of queue 𝑄𝑖𝑗 |
| 𝑞𝑖𝑗(𝑡) | The exit flow of queue 𝑄𝑖𝑗 at time 𝑡, which also represents the inflow of airspace traffic from region 𝑎 |
| 𝑛𝑖𝑗(𝑡) | The accumulation of airspace traffic from region 𝑎 |
| 𝑛𝑖(𝑡) | The number of aircraft in airspace region 𝑎 |
| 𝐺𝑖(𝑛𝑖(𝑡)) | The MFD of airspace region 𝑎 |
| 𝑢𝑖𝑗(𝑡) | The air traffic flow control at time 𝑡, regulating the outflow of airspace traffic from region 𝑎 |

𝑖 to 𝑎 𝑗 LAAT network, aiming to optimize the network flow pattern in the planning phase. The dynamic models characterize regional traffic as dynamics of aircraft accumulation based on demand queuing and airspace MFDs, aiming to regulate the dynamics to a desired equilibrium in the control phase. 2.We establish the interaction between static network planning and dynamic traffic control by deriving the desired equilibrium from the SO network equilibrium. The derived equilibrium is ensured to exist as a stable equilibrium and can be adjusted in response to traffic demand and airspace capacity. We devise a control scheme to implement the planning-control interaction. The proposed scheme, by coupling dynamic traffic control and demand management, can adjust the desired equilibrium according to changes in demand patterns, thus guaranteeing the feasibility of the set-point control problem with respect to varying demand patterns. Numerical examples demonstrate the merits of the integrated dynamic traffic control and demand management scheme. Compared to a fixed equilibrium based on experience, a variable SO equilibrium given by the planning-control interaction can significantly improve network efficiency, especially when demand patterns admit abrupt changes and noise. The remainder of this paper is organized as follows: Section 2 introduces traffic flow models for LAAT systems, including the static network equilibrium model, the queue-based demand management model, and the MFD-based air traffic dynamics model. Section 3 establishes the interaction between static network planning and dynamic traffic control by devising a control scheme to regulate the traffic dynamics to the desired equilibrium derived from the SO equilibrium. Section 4 presents a case study to assess the effectiveness of the proposed control scheme. Section 5 concludes this paper. For convenience, Table 1 collects the key notations used in this paper.

## 2. Traffic flow modeling for LAAT management

This section formulates both static and dynamic traffic flow models for LAAT systems. First, in Section 2.1, we introduce the motivating scenario and problem setting of a two-region LAAT system. Next, in Section 2.2, we aggregate individual UAM trips into traffic flows on the LAAT network, and formulate static SO equilibrium models to optimize flow patterns during the planning phase. Then, in Section 2.3, we employ region-based traffic flow modeling for two-region airspace network, and develop dynamic air traffic flow models, including queue-based demand management and MFD-based air traffic dynamics.

### 2.1. Motivating scenario and problem setting

In February 2024, AutoFlight completed the world’s first public flight of eVTOLs on a cross-sea route between the southern Chinese cities of Shenzhen and Zhuhai (Pritchard , 2024 ). Such cross-sea/river traffic scenarios hold great promise for LAAT applications, as eVTOLs can significantly reduce travel time compared with personal cars (Wei et al., 2018 ). Hence, this paper focuses on cross-region traffic scenarios and proposes a two-region LAAT system design, as illustrated in Fig. 2. The LAAT network comprises a ground network of vertiports and an airspace network. Given natural barriers, such as seas and rivers, the ground network is divided into two regions 𝑔

## 1 and 𝑔

## 2. Correspondingly, the airspace network is considered to consist of two regions 𝑎

and 𝑎 2, which are defined by specific longitude, latitude, and altitude ranges, and are aligned with the two ground regions. In each Transportation Research Part C 178 (2025) 105237

<!-- page 5 -->

C. Weng et al.

#### Fig. 2. The urban low-altitude air transport system consists of two regions separated by natural barriers (e.g., seas and rivers), where UAM demonstrates

advantages for cross-region transport. Individual UAM trips are aggregated into link-level flows for network planning and further aggregated into region-level flows for traffic control. Static planning focuses on steady-state flow patterns on the LAAT network, while dynamic control focuses on the traffic dynamics of the two-region airspace network. ground region, multiple vertiports are deployed at specific locations to meet UAM demand. In each airspace region, the full-mix structure design is adopted, allowing low-altitude aircraft to freely choose their routes (Sunil et al., 2015 ). The proposed system design advances existing studies by integrating both the ground and airspace networks (see e.g., Haddad et al., 2021 ; Safadi et al.,

## 2024 ).

We outline the operational rules for the proposed LAAT system as follows. Given the origin and destination (OD) of UAM demand, a complete UAM trip comprises five stages: accessing (first-mile travel), taking off, cruising, landing, and egressing (last-mile travel). Normally, the take-off and landing vertiports for the same UAM trip are (physically) distinct. Except during the cruising stage, lowaltitude aircraft are not permitted to travel from one region to another. In other words, aircraft taking off from ground region 𝑔 𝑖 directly enter the corresponding airspace region 𝑎 𝑖, 𝑖∈ {1,2}, and a similar rule also applies to aircraft landing. Moreover, we make the following assumptions for LAAT management in this study: (1) An air traffic control center is responsible for the surveillance and management of the entire LAAT system. The control center has the authority to monitor and control individual traffic behaviors, such as the accessing/egressing vertiport selection of passengers and real-time aircraft trajectories, when necessary. (2) Each vertiport is adequately equipped to enable aircraft to take off and land simultaneously, with take-off and landing management operating independently. (3) Each low-altitude aircraft possesses sufficient mobility and intelligence to avoid collisions with other aircraft and to remain within the airspace regions during the cruising stage. Transportation Research Part C 178 (2025) 105237

<!-- page 6 -->

C. Weng et al. Assumption (1) establishes an operable environment for LAAT management, emphasizing the observability and controllability of the system (Zhong et al., 2018a ). Assumption (2) simplifies vertiport management by disregarding the interaction between take-off and landing operations (Rimjha and Trani , 2021 ). Assumption (3) considers low-altitude aircraft with advanced technical capabilities, enabling managers to prioritize system-level management over individual-level control (Kopardekar et al., 2016 ; SESAR Joint Undertaking , 2017 ). Moreover, we assume that the UAM demand can be decomposed into a series of stable patterns over time. This is to consider a periodically constant demand pattern for simplification, which is a common practice in the literature (Zhong et al., 2020 ).

### 2.2. Static SO equilibrium model for LAAT networks

Given the five stages of a complete UAM trip, we model the LAAT network as a directed graph illustrated in Fig. 3. Based on Assumption (2), we distinguish the take-off and landing vertiports in UAM trips using different notations (𝑘 and 𝑙), although they may physically refer to the same vertiport. Traffic flow on the LAAT network is aggregated from individual UAM trips. To be specific, UAM trips sharing the same origin 𝑚, take-off vertiport 𝑘, landing vertiport 𝑙 and destination 𝑚 are aggregated into traffic flow 𝑓𝑘 𝑙,𝑚. Accordingly, we have the flow conservation and non-negative constraints as follows:

$$
𝑑𝑚=𝑁\sum
$$

$$
𝑘=1𝑁\sum
$$

𝑙=1𝑓𝑘 𝑙,𝑚,∀𝑚∈ {1,2,…, 𝑀} (1a)

$$
𝑓𝑘=𝑀\sum
$$

$$
𝑚=1𝑁\sum
$$

𝑙=1𝑓𝑘 𝑙,𝑚,∀𝑘∈ {1,2,…, 𝑁} (1b)

$$
𝑓𝑙=𝑀\sum
$$

$$
𝑚=1𝑁\sum
$$

𝑘=1𝑓𝑘 𝑙,𝑚,∀𝑙∈ {1,2,…, 𝑁} (1c) 𝑓𝑘 𝑙,𝑚\ge 0 ,∀𝑘, 𝑙∈ {1,2,…, 𝑁},∀𝑚∈ {1,2,…, 𝑀} (1d) where 𝑑𝑚 is the travel demand between the origin 𝑚 and destination 𝑚, 𝑓𝑘 is the traffic flow taking off from vertiport 𝑘, 𝑓𝑙 is the traffic flow landing at vertiport 𝑙, 𝑀 is the number of OD pairs and 𝑁 is the number of vertiports. Additionally, we define the travel cost for UAM trips as follows: 𝑡𝑘 𝑙,𝑚=𝜏𝑘 𝑙,𝑚+𝑡𝑘(𝑓𝑘) +𝑡𝑙(𝑓𝑙) (2) where ∙𝑡𝑘 𝑙,𝑚 is the travel time of UAM trips with origin 𝑚, take-off vertiport 𝑘, landing vertiport 𝑙 and destination 𝑚; ∙𝜏𝑘 𝑙,𝑚 denotes the travel time spent on firstand last-mile travel, as well as aircraft cruising; ∙𝑡𝑘(𝑓𝑘) and 𝑡𝑙(𝑓𝑙) represent the waiting time for taking off and landing, respectively. In this study, we treat 𝜏𝑘 𝑙,𝑚 as a constant, while 𝑡𝑘(𝑓𝑘) and 𝑡𝑙(𝑓𝑙) satisfy d𝑡𝑘(𝑓𝑘) d𝑓𝑘>0 and d𝑡𝑙(𝑓𝑙) d𝑓𝑙>0, respectively. The physical interpretation is as follows: The travel time spent on accessing, cruising, and egressing is fixed and primarily depends on the travel distance. The waiting time for taking off (or landing) at a vertiport is variable and depends on the total take-off (or landing) flow at the vertiport. Given the limited capacity of vertiports, the waiting time increases as the total traffic flow increases (Vascik and Hansman , 2019 ). Here, we overlook the increase in aircraft cruising time caused by air traffic congestion. In the network planning phase, the permitted demand is guaranteed not to yield air traffic congestion. Moreover, the increase in aircraft cruising time is not significant compared to the waiting time at vertiports (Rothfeld et al., 2018 ). Different flow patterns on the LAAT network lead to varying total travel costs. The static paradigm of network planning aims to find the optimal flow pattern for management by minimizing the total travel cost, i.e., min 𝑓𝑘

$$
𝑙,𝑚𝑓𝑖𝑥𝑒𝑑 =𝑀\sum
$$

$$
𝑚=1𝑁\sum
$$

$$
𝑘=1𝑁\sum
$$

𝑙=1𝑓𝑘 𝑙,𝑚𝑡𝑘 𝑙,𝑚(3) subject to (1). The model above, which implicitly assumes that each OD demand 𝑑𝑚 is fixed and known in advance, is known as system-optimal traffic assignment with fixed demand. Recent studies emphasize the sensitivity of UAM demand to travel time (Wei et al., 2018 ; Shrestha et al., 2021 ). Hence, we introduce an elastic demand model 𝑑𝑚=𝐷𝑚(𝑡𝑚),∀𝑚∈ {1,2,…, 𝑀}, and rewrite model (3) as follows: min 𝑓𝑘

$$
𝑙,𝑚𝑒𝑙𝑎𝑠𝑡𝑖𝑐 =𝑀\sum
$$

$$
𝑚=1𝑁\sum
$$

$$
𝑘=1𝑁\sum
$$

𝑙=1𝑓𝑘 𝑙,𝑚𝑡𝑘

$$
𝑙,𝑚-𝑀\sum
$$

$$
𝑚=1\int 𝑑𝑚
$$

0𝐷-1 𝑚(𝑠)d𝑠 (4) subject to (1), where 𝐷-1 𝑚(⋅) is the inverse function of 𝐷𝑚(⋅). Transportation Research Part C 178 (2025) 105237

<!-- page 7 -->

C. Weng et al.

#### Fig. 3. Schematics of (a) individual UAM trips; and (b) traffic flows on the LAAT network.

Remark 1. The interpretation of the elastic demand 𝑑𝑚=𝐷𝑚(𝑡𝑚) is that the number of passengers choosing UAM travel (between 𝑚 and 𝑚) is 𝑑𝑚 when the travel time (between 𝑚 and 𝑚) is 𝑡𝑚. Here OD travel time 𝑡𝑚 relies on the corresponding path travel time 𝑡𝑘 𝑙,𝑚. In user equilibrium solutions, the travel time of each path is equal, i.e., 𝑡𝑚=𝑡𝑘 𝑙,𝑚,if𝑓𝑘 𝑙,𝑚>0,∀𝑘, 𝑙∈ {1,2,…, 𝑁} In system optimal solutions, the generalized travel time of each path is equal, i.e., 𝑡𝑚=𝑡𝑘 𝑙,𝑚+𝑓𝑘 𝑙,𝑚𝜕𝑡𝑘 𝑙,𝑚 𝜕𝑓𝑘 𝑙,𝑚,if𝑓𝑘 𝑙,𝑚>0,∀𝑘, 𝑙∈ {1,2,…, 𝑁} where 𝜕𝑡𝑘 𝑙,𝑚 𝜕𝑓𝑘 𝑙,𝑚 represents the partial derivative of the function 𝑡𝑘 𝑙,𝑚 with respect to the variable 𝑓𝑘 𝑙,𝑚. The detailed discussion of the above results can be found in Yang and Huang (2005 ). We denote the solution to model (4) as the set ∗𝐹, which contains the link flows on the LAAT network, i.e., ∗𝐹= {∗𝑓𝑘 𝑙,𝑚},∀𝑘, 𝑙∈ {1,2,…, 𝑁}, 𝑚∈ {1,2,…, 𝑀}. The solution ∗𝐹 is called the SO network equilibrium in the literature. By minimizing the total travel cost, the static paradigm of network planning identifies the optimal state of the LAAT network as the SO equilibrium ∗𝐹. This optimal network state is consistent with the desired equilibrium concept in dynamic traffic control, as discussed in Section 1.

### 2.3. Dynamic traffic flow model for two-region airspace networks

In the planning phase, all potential links on the LAAT network can be considered, as the SO equilibrium remains invariant over a considerable period. However, controlling traffic flows on substantial network links presents great challenges, particularly in dynamic environments. For the LAAT network illustrated in Fig. 3, the connections between vertiports become increasingly complex as the number of vertiports grows, requiring substantial resources for flow control. Additionally, a single vertiport may be connected to multiple others, implying that the management (e.g., queuing) at a vertiport must be handled separately for each link. Recently, some studies have investigated network equilibrium problems at the regional level (e.g., Yildirimoglu and Geroliminis ,

## 2014 ; Batista and Leclercq , 2019 ). Inspired by this, we adopt region-based air traffic flow models in this paper. The approach is to

aggregate traffic flows between vertiports into traffic flows between regions, allowing us to focus on modeling and controlling for regions’ endogenous and exogenous traffic (Haddad et al., 2021 ; Safadi et al., 2024 ). We provide schematics in Fig. 4 to compare link-based and region-based traffic flow modeling. Endogenous traffic, referring to traffic with origin and destination located in the same region, is depicted by blue arrows. Exogenous traffic, referring to traffic with origin and destination located in different regions, is depicted by red arrows. Compared to the link-based model, the region-based model significantly reduces control resource requirements.

### 2.3.1. Demand management based on queuing control

Demand management is an important measure of dynamic traffic control, as widely evidenced in roadway transport systems (Zhong et al., 2018b ; Menelaou et al., 2021 ). Recently, Safadi et al. (2023b , 2024 ) successfully implemented demand management for LAAT systems via aircraft departure control. Inspired by this, we formulate the region-based demand management for dynamic air traffic control in this section. Given the two-region airspace network illustrated in Fig. 2, we denote the traffic demand from region 𝑎 𝑖 to region 𝑎 𝑗 as 𝑔𝑖𝑗(𝑡), 𝑖, 𝑗∈ {1,2}, where 𝑔𝑖𝑗(𝑡)|𝑖=𝑗 and 𝑔𝑖𝑗(𝑡)|𝑖\ne 𝑗 represent endogenous and exogenous demand, respectively. In particular, when the Transportation Research Part C 178 (2025) 105237

<!-- page 8 -->

C. Weng et al.

#### Fig. 4. Schematics of (a) link-based traffic flow modeling; and (b) region-based traffic flow modeling, where the former requires significantly more control

resources (represented by 𝑢) than the latter. LAAT system operates at a steady state, the regional traffic demand is the aggregate of the network traffic demand, i.e.,

$$
𝑔𝑖𝑗=\sum
$$

𝑘∈𝑔 𝑖\sum 𝑙∈𝑔 𝑗𝑀\sum 𝑚=1𝑓𝑘 𝑙.𝑚,∀𝑖, 𝑗∈ {1,2} (5) For dynamic air traffic control, we assume that demand 𝑔𝑖𝑗(𝑡) is managed through a queuing process to gain entry into the airspace. By introducing the queue length as 𝑄𝑖𝑗(𝑡), we formulate the dynamics of demand queue as follows:

$$
.𝑄𝑖𝑗(𝑡) =𝑔𝑖𝑗(𝑡) -𝑞𝑖𝑗(𝑡),∀𝑖, 𝑗∈ {1,2} (6)
$$

where 𝑞𝑖𝑗(𝑡) is the queue’s exit flow, which also represents the traffic flow permitted to enter the airspace. Then we implement the queuing control 𝑣𝑖𝑗(𝑡) ∈ [0 ,1] to manage the queue’s exit flow 𝑞𝑖𝑗(𝑡) as follows

$$
𝑞𝑖𝑗(𝑡) =𝑠𝑖𝑗𝑣𝑖𝑗(𝑡),∀𝑖, 𝑗∈ {1,2} (7)
$$

where 𝑠𝑖𝑗>0 represents the maximum exit flow rate, which is regarded as a parameter that depends on management purposes in this study. Combining (6) and (7), we have

$$
.𝑄𝑖𝑗(𝑡) =𝑔𝑖𝑗(𝑡) -𝑠𝑖𝑗𝑣𝑖𝑗(𝑡),∀𝑖, 𝑗∈ {1,2} (8)
$$

$$
The queue length is typically constrained by 0\le 𝑄𝑖𝑗(𝑡)\le 𝑄𝑚𝑎𝑥
$$

𝑖𝑗, where 𝑄𝑚𝑎𝑥 𝑖𝑗 is the maximum queue length. This constraint implicitly assumes that .𝑄𝑖𝑗(𝑡)\le 0⇒𝑔𝑖𝑗(𝑡)\le 𝑠𝑖𝑗𝑣𝑖𝑗(𝑡)⇒𝑔𝑖𝑗(𝑡)\le 𝑠𝑖𝑗, when 𝑄𝑖𝑗(𝑡) =𝑄𝑚𝑎𝑥 𝑖𝑗. Remark 2. Region-based formulation employs an aggregated queue 𝑄𝑖𝑗(𝑡) to manage the demand from region 𝑖 to region 𝑗, even though the demand may originate from different vertiports. Regional demand management is implemented by coordinating the control of sub-queues at multiple vertiports. For reasons of fairness and efficiency, a widely used approach is to balance the lengths of multiple sub-queues. A detailed discussion on queue balancing can be found in Keyvan-Ekbatani et al. (2021 ). On the other hand, endogenous demand 𝑔𝑖𝑖(𝑡) and exogenous demand 𝑔𝑖𝑗(𝑡)|𝑖\ne 𝑗 are managed separately at each vertiport. To enable this, we consider each vertiport to be well-equipped with (at least) two independent aircraft take-off platforms, one for endogenous demand and the other for exogenous demand. In fact, the mission of endogenous/exogenous travel for an aircraft depends on the boarding passengers’ destination. Hence, we can manage endogenous and exogenous traffic demand separately by regulating passenger boarding, even if the vertiport is equipped with only one aircraft take-off platform.

### 2.3.2. Air traffic dynamics based on MFD

Region-based traffic modeling is a widely used approach in roadway transport systems, especially for large-scale networks (Ramezani et al., 2015 ; Chen et al., 2024 ). Recently, Haddad et al. (2021 ), Safadi et al. (2024 ) introduced the MFD concept to LAAT systems and developed dynamic air traffic flow models for airspace regions. Inspired by this, we formulated two-region air traffic dynamics based on MFD in this section. The MFD concept for an airspace region 𝑎 𝑖 describes the relationship between air traffic accumulation 𝑛𝑖 [veh] and air traffic outflow 𝐺𝑖 [veh/s]. Recently, airspace MFD 𝐺𝑖(𝑛𝑖) has been observed to follow a unimodal distribution, with an initial increasing phase followed by a decreasing phase (Safadi et al., 2023a ; Cummings and Mahmassani , 2024a ). The increasing part characterizes free-flow air traffic, while the decreasing part characterizes congested air traffic. We denote the increasing part and the decreasing part of 𝐺𝑖(𝑛𝑖) as 𝐺𝑖,𝑠(𝑛𝑖), 𝑛𝑖∈ [0, 𝑛𝑐𝑟 𝑖] and 𝐺𝑖,𝑢(𝑛𝑖), 𝑛𝑖∈ (𝑛𝑐𝑟 𝑖, 𝑛𝑗𝑎𝑚 𝑖], respectively, where 𝑛𝑐𝑟 𝑖 represents the critical accumulation and 𝑛𝑗𝑎𝑚 𝑖 represents the jammed accumulation. For mathematical completeness, we assume that 𝐺𝑖,𝑠(𝑛𝑖) and 𝐺𝑖,𝑢(𝑛𝑖) are both strictly Transportation Research Part C 178 (2025) 105237

<!-- page 9 -->

C. Weng et al.

#### Fig. 5. The MFD for airspace region 𝑎

𝑖 links the traffic accumulation 𝑛𝑖 and traffic outflow 𝐺𝑖. monotonic within their respective domains. As illustrated in Fig. 5, a steady-state region traffic outflow 𝑞 < 𝐺𝑖(𝑛𝑐𝑟 𝑖) would correspond to two steady-state traffic accumulations. By introducing the inverse function of 𝐺𝑖,∗(⋅) as 𝐺-1 𝑖,∗(⋅), we can derive the steady-state accumulations corresponding to 𝑞 as follows 𝑛𝑠 𝑖=𝐺-1 𝑖,𝑠(𝑞), 𝑛𝑢 𝑖=𝐺-1 𝑖,𝑢(𝑞) (9) where 𝑛𝑠 𝑖 is a stable equilibrium and 𝑛𝑢 𝑖 is an unstable saddle point (Haddad and Geroliminis , 2012 ; Zhong et al., 2018b ). Suppose that each airspace region 𝑎 𝑖, 𝑖∈ {1 ,2} admits a well-defined MFD. The two-region air traffic can be formulated as the dynamics of aircraft accumulation based on flow conservation. Following Section 2.3.1 , we introduce four state variables 𝑛𝑖𝑗(𝑡), 𝑖, 𝑗 ∈ {1 ,2} corresponding to four airspace inflows 𝑞𝑖𝑗(𝑡), 𝑖, 𝑗 ∈ {1 ,2}. Here state variable 𝑛𝑖𝑗(𝑡) denotes the accumulation of endogenous/exogenous traffic from airspace region 𝑎 𝑖 to region 𝑎 𝑗. By summing up the accumulation of both endogenous and exogenous traffic, we can get the total traffic accumulation within airspace region 𝑎 𝑖 as 𝑛𝑖(𝑡) = 𝑛𝑖𝑖(𝑡) +𝑛𝑖𝑗(𝑡)|𝑖\ne 𝑗. With the aid of airspace MFD, the total airspace outflow for region 𝑎 𝑖 is given by 𝐺𝑖(𝑛𝑖(𝑡)). To distinguish the airspace outflow resulting from endogenous and exogenous traffic, we introduce four control variables 𝑢𝑖𝑗(𝑡) ∈ [0 ,1], 𝑖, 𝑗 ∈ {1 ,2} corresponding to four state variables 𝑛𝑖𝑗(𝑡), 𝑖, 𝑗∈ {1,2}. Then the airspace outflow of endogenous/exogenous traffic from region 𝑎 𝑖 to region 𝑎 𝑗 is regarded as 𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑗(𝑡). By definition, we have 𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑖(𝑡) +𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗\le 𝐺𝑖(𝑛𝑖(𝑡))⇒𝑢𝑖𝑖(𝑡) +𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗\le 1. Based on flow conservation, the two-region air traffic dynamics is formulated as follows .𝑛11(𝑡) =𝑞11(𝑡) +𝐺2(𝑛2(𝑡))𝑢21(𝑡) -𝐺1(𝑛1(𝑡))𝑢11(𝑡) (10a) .𝑛12(𝑡) =𝑞12(𝑡) -𝐺1(𝑛1(𝑡))𝑢12(𝑡) (10b) .𝑛21(𝑡) =𝑞21(𝑡) -𝐺2(𝑛2(𝑡))𝑢21(𝑡) (10c) .𝑛22(𝑡) =𝑞22(𝑡) +𝐺1(𝑛1(𝑡))𝑢12(𝑡) -𝐺2(𝑛2(𝑡))𝑢22(𝑡) (10d)

$$
where state variables are typically constrained by 0\le 𝑛𝑖(𝑡)\le 𝑛𝑗𝑎𝑚
$$

𝑖. Remark 3. In traditional modeling of two-region MFD systems by Geroliminis et al. (2013 ), the traffic outflows resulting from endogenous and exogenous traffic are calculated by 𝑛𝑖𝑖(𝑡) 𝑛𝑖(𝑡)𝐺𝑖(𝑛𝑖(𝑡)) and 𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡)𝐺𝑖(𝑛𝑖(𝑡))|𝑖\ne 𝑗, respectively. Accordingly, traditional boundary control ̂ 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗 is attached to 𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡)𝐺𝑖(𝑛𝑖(𝑡))|𝑖\ne 𝑗 to regulate the exogenous traffic outflow. However, the flow-splitting variable 𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡) is difficult to measure and can be treated as an apriori unknown parameter (Haddad , 2015 ). Hence, we simplify the representation of traffic outflow from region 𝑖 to region 𝑗 as 𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑗(𝑡) in model (10), where control variable 𝑢𝑖𝑗(𝑡) implicitly contains uncertain parameter 𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡). Particularly, when we define 𝑢𝑖𝑖(𝑡) =𝑛𝑖𝑖(𝑡) 𝑛𝑖(𝑡) and 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗=𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡)̂ 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗, model (10) becomes equivalent to the traditional model. Due to the limited observability and controllability of roadway transport systems, traditional boundary control models focus exclusively on the transfer flow between regions. As discussed in Keyvan-Ekbatani et al. (2012 ), Haddad (2017b ), most boundary control measures would induce queues at the boundary and cannot fully utilize the traffic network capacity, i.e., 𝑛𝑖𝑖(𝑡) 𝑛𝑖(𝑡)𝐺𝑖(𝑛𝑖(𝑡)) +𝑛𝑖𝑗(𝑡) 𝑛𝑖(𝑡)𝐺𝑖(𝑛𝑖(𝑡))̂ 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗< 𝐺𝑖(𝑛𝑖(𝑡)),when ̂ 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗\ne 1 The potential of LAAT systems in observability and controllability enables us to overcome the above limitations by revising traditional models. Hence, air traffic flow model (10) is adopted in this paper, and we consider the control inputs for endogenous and exogenous traffic outflow are coupled, i.e., 𝑢𝑖𝑖(𝑡) +𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗= 1,∀𝑖, 𝑗∈ {1,2} (11)Transportation Research Part C 178 (2025) 105237

<!-- page 10 -->

C. Weng et al. In line with (Haddad , 2017a ), coupled control is an effective approach for simplifying two-region MFD systems. In this paper, we name the control 𝑢𝑖𝑗(𝑡) satisfying (11) as Modified Boundary Control (MBC). The MBC ensures that the total airspace outflow is not diminished by control measures, i.e., 𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑖(𝑡) +𝐺𝑖(𝑛𝑖(𝑡))𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗=𝐺𝑖(𝑛𝑖(𝑡)),∀𝑢𝑖𝑖(𝑡) +𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗= 1. Unlike traditional boundary control, the MBC assumes that managers can regulate the traffic outflow contributed by both endogenous and exogenous traffic. At the microscopic level, the MBC can be implemented through customized motion control (e.g., speed control and route guidance) of aircraft for endogenous and exogenous traffic (Sirmatel and Yildirimoglu , 2023 ). Intuitively, higher speeds or shorter routes for aircraft in endogenous/exogenous traffic would increase the corresponding traffic outflow over a transient control period. An experimental microscopic example is provided in Appendix A, while the detailed mechanism of MBC is left for future work.

## 3. Bridging dynamic traffic control and static network equilibrium

In the literature, most MFD-based traffic flow control aims to regulate the traffic dynamics to the desired equilibrium, which is commonly chosen as the critical point of the MFD function (Haddad and Shraiber , 2014 ; Zhong et al., 2018a ; Chen et al., 2022 ; Safadi et al., 2024 ). Our latest work in microscopic LAAT simulations found that the critical state 𝑛𝑐𝑟 is not an ideal desired equilibrium, as it is likely to cause air traffic congestion (Weng et al., 2024 ). Unlike in theoretical cases, traffic congestion is difficult to eliminate in simulated environments. Selecting an appropriate desired equilibrium is as important as achieving it. However, as discussed in Section 1, the experience-driven choice lacks a convincing interpretation and cannot ensure the existence and stability of the selected equilibrium. To address these challenges, we develop a mechanism to select the desired equilibrium by establishing the interaction between static network planning and dynamic traffic control. The proposed control scheme consists of the planning-control interaction mechanism, the maximum throughput queuing controller, and the steady-state MBC controller. A schematic of the planning-control interaction is shown in Fig. 6. Both static network planning and dynamic traffic control aim to achieve the same steady state in system operations. In the planning phase, the optimal steady state is identified as the SO equilibrium ∗𝐹. To enable region-based traffic control, we rewrite the SO equilibrium ∗𝐹 into the form of regional traffic demand ∗𝑔𝑖𝑗. Based on the SO traffic demand ∗𝑔𝑖𝑗, we derive steady-state conditions for demand management and air traffic dynamics (in Section 3.1). The steady-state conditions yield the optimal parameter ∗𝑠𝑖𝑗 for queuing control and the desired equilibrium 𝑛𝑖 for air traffic control. Since the traffic demand ∗𝑔𝑖𝑗 given by network planning would not result in traffic congestion, we can ensure the existence and stability of the desired equilibrium 𝑛𝑖. Moreover, the desired equilibrium 𝑛𝑖 can be adjusted in response to traffic demand 𝑔𝑖𝑗 and air capacity 𝐺𝑖(⋅), which can affected by route guidance of aircraft and network control policies. To regulate air traffic dynamics to the desired equilibrium, we devise a queuing controller (in Section 3.2) and an MBC controller (in Section 3.3). In this manner, we bridge static network planning and dynamic traffic control by deriving the desired equilibrium from the SO network equilibrium. Suppose the UAM travel demand 𝐷𝑚(⋅), used to activate the planning-control interaction, represents within-day traffic demand. To account for variability in traffic demand and supply, we consider the planning-control interaction in cases where demand pattern switches happen, e.g., workday-to-holiday demand pattern switches and vice versa. The control scheme for air traffic with demand pattern switches is decomposed into a series of within-day traffic control schemes. During each within-day control period, the planning-control interaction is activated to select the desired equilibrium based on demand 𝐷𝑚(⋅) and supply 𝐺𝑖(⋅). In other words, the desired equilibrium is updated dynamically for each within-day control period. The desired equilibrium rises when demand increases or supply decreases, and falls when demand decreases or supply increases. Our aim is to provide proactive responses to the switch of demand patterns. Theoretical results are presented in the remainder of this section. Simulation results will be shown in Section 4 to validate the effectiveness of the proposed approach in efficient UAM.

### 3.1. Steady state of dynamic air traffic flow models

We first derive the steady-state conditions for the demand management model presented in Section 2.3.1 . Suppose that the demand management model operates at the steady state corresponding to ∗𝐹, we have the following steady-state conditions

$$
∗𝑔𝑖𝑗=\sum
$$

𝑘∈𝑔 𝑖\sum 𝑙∈𝑔 𝑗𝑀\sum 𝑚=1∗𝑓𝑘 𝑙,𝑚,∀𝑖, 𝑗∈ {1,2} (12a) .𝑄𝑖𝑗(𝑡) = 0 ,∀𝑖, 𝑗∈ {1,2} (12b) where ∗𝑔𝑖𝑗 is the steady-state regional traffic demand corresponding to ∗𝐹. Condition (12a) is derived from Eq. (5) and represents the aggregation of link traffic flows into regional traffic flows. Condition (12b) guarantees a constant queue length, from which we can derive

$$
𝑞𝑖𝑗=𝑠𝑖𝑗𝑣𝑖𝑗=∗𝑔𝑖𝑗,∀𝑖, 𝑗∈ {1,2} (13)
$$

where 𝑞𝑖𝑗 is the queue’s steady-state exit flow and 𝑣𝑖𝑗 is the steady-state queuing control input. We consider the optimal value of parameter 𝑠𝑖𝑗 as the minimum value that enables the demand management model to operate at the steady state corresponding to ∗𝐹. Considering 𝑣𝑖𝑗∈ [0,1], we can easily derive the optimal parameter as ∗𝑠𝑖𝑗=∗𝑔𝑖𝑗 and the corresponding control input as 𝑣𝑖𝑗= 1. In this case, the queuing supply 𝑠𝑖𝑗 can be fully utilized when the system operates at the desired steady state. Transportation Research Part C 178 (2025) 105237

<!-- page 11 -->

C. Weng et al.

#### Fig. 6. The schematic of the planning-control interaction. Both static network planning and dynamic traffic control aim to achieve the same steady state in

system operations. In the planning phase, the optimal steady state is identified as the SO equilibrium ∗𝐹. Based on the SO equilibrium ∗𝐹, steady-state conditions for demand management and air traffic dynamics are derived to determine the desired equilibrium 𝑛𝑖. In the control phase, the queuing controller and MBC controller are devised to regulate the air traffic state to the desired equilibrium derived from the SO equilibrium. Remark 4. The optimal parameter ∗𝑠𝑖𝑗 guarantees that the queue’s exit flow is an admissible inflow for the air traffic flow model (10). As discussed in Zhong et al. (2018b ), the traffic inflows to the MFD system would affect the existence of equilibrium and its convergence and stability properties. By setting 𝑠𝑖𝑗=∗𝑠𝑖𝑗, we impose an upper bound on the airspace inflow, i.e., 𝑞𝑖𝑗(𝑡)\le ∗𝑠𝑖𝑗,∀𝑣𝑖𝑗(𝑡) ∈ [0,1], enabling air traffic equilibrium corresponding to ∗𝐹. Then we derive the steady-state conditions for the air traffic flow model presented in Section 2.3.2 . Given the steady-state airspace traffic inflows as 𝑞𝑖𝑗=∗𝑔𝑖𝑗, the steady state of the air traffic dynamics (10) implies

## 0 =.𝑛11(𝑡) =𝑞11+𝐺2(𝑛2)𝑢21-𝐺1(𝑛1)𝑢11 (14a)

## 0 =.𝑛12(𝑡) =𝑞12-𝐺1(𝑛1)𝑢12 (14b)

## 0 =.𝑛21(𝑡) =𝑞21-𝐺2(𝑛2)𝑢21 (14c)

## 0 =.𝑛22(𝑡) =𝑞22+𝐺1(𝑛1)𝑢12-𝐺2(𝑛2)𝑢22 (14d)

where 𝑛𝑖 is the steady-state traffic accumulation of airspace region 𝑎 𝑖 and 𝑢𝑖𝑗 is the steady-state air traffic control input. Suppose that control inputs are coupled, we combine (11) and (14) to get the following steady-state condition 𝐺1(𝑛1) =𝑞11+𝑞12+𝑞21, 𝐺2(𝑛2) =𝑞22+𝑞12+𝑞21 (15)Transportation Research Part C 178 (2025) 105237

<!-- page 12 -->

C. Weng et al. Eq. (15) always admits a solution because the steady-state demand 𝑞𝑖𝑗 (determined by the SO equilibrium) will not yield air traffic congestion. Mathematically, this implies that 𝑞11+𝑞12+𝑞21< 𝐺1(𝑛𝑐𝑟 1) and 𝑞22+𝑞12+𝑞21< 𝐺2(𝑛𝑐𝑟 2). Following the discussion in Section 2.3.2 , we choose the desired accumulation 𝑛𝑖 as a stable equilibrium. Hence, the coupled desired accumulation and control inputs for the air traffic flow model (10) are derived as follows 𝑛1=𝐺-1

$$
1,𝑠(𝑞11+𝑞12+𝑞21),𝑛2=𝐺-1
$$

2,𝑠(𝑞22+𝑞12+𝑞21)(16a)

$$
𝑢11=𝑞11+𝑞21
$$

$$
𝑞11+𝑞12+𝑞21,𝑢22=𝑞22+𝑞12
$$

𝑞22+𝑞12+𝑞21(16b) 𝑢12=𝑞12

$$
𝑞11+𝑞12+𝑞21,𝑢21=𝑞21
$$

𝑞22+𝑞12+𝑞21(16c) Remark 5. 𝐺-1 𝑖,𝑠(⋅) and 𝑞𝑖𝑗 result from the airspace MFD and the elastic demand setting, respectively. Eq. (16) establishes a mechanism for adjusting the desired equilibrium 𝑛𝑖 in response to traffic demand 𝑞𝑖𝑗 and supply 𝐺𝑖(⋅). Under a fixed demand level, an increase in traffic supply lowers the desired equilibrium, while a decrease in supply raises it. Conversely, under a fixed supply level, an increase in traffic demand raises the desired equilibrium, while a decrease in demand lowers it. This adaptive adjustment of the desired equilibrium coincides with insights from the literature but is established theoretically for the first time.

### 3.2. Maximum throughput queuing controller

In this section, we devise a queuing controller to regulate the air traffic inflow. To improve efficiency, queuing control focuses on minimizing queue length (Keyvan-Ekbatani et al., 2012 , 2021 ). Since the demand management model (6)-(7) is a point queue model, minimizing queue length is equivalent to maximizing the queue’s exit flow.4 Hence, we choose the objective function for queuing control as follows max 𝑣𝑖𝑗(𝑡)𝑄

$$
𝑖𝑗=\int 𝑡𝑓
$$

0𝑞𝑖𝑗(𝑡) d𝑡,∀𝑖, 𝑗∈ {1,2} (17) where 𝑡𝑓>0 is the control horizon and 𝑄 𝑖𝑗 represents the queue’s throughput during the control period [0, 𝑡𝑓]. We design the queuing controller to maximize the queue’s throughput as follows 𝑣𝑖𝑗(𝑡) = min{ (𝑄𝑖𝑗)+𝑔𝑖𝑗(𝑡) ∗𝑠𝑖𝑗,1} ,∀𝑖, 𝑗∈ {1,2} (18) where (𝑥) ={1,if 𝑥 >0 0,else is an indicator function, and ‘‘min{ 𝑥, 𝑦}’’ is the minimum value of the set {𝑥, 𝑦}. Proposition 1. The controller given by (18) achieves the objective defined in (17). Proof. See Appendix B. □ Proposition 1 demonstrates that the proposed controller (18) is a feasible solution for maximizing the queue’s throughput. The maximum queue’s exit flow rate 𝑠𝑖𝑗=∗𝑠𝑖𝑗 strikes a balance between maximizing the queue’s throughput and limiting air traffic inflow, as discussed in Section 3.1. When the demand side is undersaturated, i.e., 𝑄𝑖𝑗(𝑡) = 0 and 𝑔𝑖𝑗(𝑡)<∗𝑠𝑖𝑗, the queuing control becomes inactive, leading to 𝑣𝑖𝑗(𝑡) = 1⇒𝑞𝑖𝑗(𝑡) =𝑔𝑖𝑗(𝑡). Typically, traffic managers are interested in scenarios of demand oversaturation, i.e., 𝑄𝑖𝑗(𝑡)>0 or 𝑔𝑖𝑗(𝑡)>∗𝑠𝑖𝑗. In this case, the queuing controller (18) guarantees a steady-state exit flow 𝑞𝑖𝑗(𝑡) = 𝑞𝑖𝑗, which corresponds to the SO network equilibrium ∗𝐹, as discussed in Section 3.1.

### 3.3. Steady-state MBC controller

In this section, we devise an MBC controller to regulate the air traffic dynamics to the desired equilibrium. Given the desired equilibrium (16) derived from the SO network equilibrium, we choose the objective function for air traffic control as follows: min

$$
𝒖(𝑡)=\int 𝑡𝑓
$$

0𝜔𝑛(𝒏-𝒏)𝑇(𝒏-𝒏) +𝜔𝑢(𝒖-𝒖)𝑇(𝒖-𝒖) d𝑡 (19) where 𝒏= [𝑛1(𝑡), 𝑛2(𝑡)]𝑇, 𝒏= [𝑛1,𝑛2]𝑇, 𝒖= [𝑢11(𝑡), 𝑢12(𝑡), 𝑢21(𝑡), 𝑢22(𝑡)]𝑇, 𝒖= [𝑢11,𝑢12,𝑢21,𝑢22]𝑇 and 𝜔𝑛, 𝜔𝑢>0 are weight factors. Referring to Zhong et al. (2018a ), the objective  contains a regularization term of control inputs. We design the MBC controller to regulate air traffic dynamics as follows: 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗= min{𝑞𝑖𝑗(𝑡) 𝐺𝑖(𝑛𝑖(𝑡)),1}

$$
, 𝑢𝑖𝑖(𝑡) = 1 - 𝑢𝑖𝑗(𝑡)|𝑖\ne 𝑗,∀𝑖, 𝑗∈ {1,2} (20)
$$

4Intuitively, a point queue can be imagined as a water reservoir with a valve. To quickly lower the water level, the valve should be opened as wide as possible.Transportation Research Part C 178 (2025) 105237

<!-- page 13 -->

C. Weng et al. Proposition 2. Given oversaturated demand 𝑔𝑖𝑗(𝑡)>∗𝑠𝑖𝑗,∀𝑖, 𝑗∈ {1 ,2} and the controller (20), the air traffic dynamics (10) with an uncongested initial state asymptotically converges the desired equilibrium defined in (16). Proof. See Appendix C. □ Proposition 2 demonstrates that the proposed controller (20) is a feasible solution for regulating traffic dynamics to the desired equilibrium. In this paper, we focus on the convergence of air traffic dynamics under conditions of demand oversaturation. When the demand side is undersaturated, it is not necessary to enforce the convergence of traffic dynamics to the desired equilibrium, as discussed in Zhong et al. (2018a ). The proposed controller is simple yet ensures the convergence of air traffic dynamics. If necessary, we can replace the MBC controller (20) with more advanced controllers, such as Model Predictive Control, to improve control performance during the transient period (Geroliminis et al., 2013 ; Safadi et al., 2024 ). At the end of this section, Algorithm 1 summarizes the proposed planning-control interaction. Algorithm 1: The planning-control interaction input : Steady-state pattern 𝐷𝑚(⋅); Network travel cost 𝑡𝑘 𝑙,𝑚(⋅); Time horizon [𝑡0, 𝑡𝑓]; Time-varying demand 𝑔𝑖𝑗(𝑡); Airspace MFD 𝐺𝑖(𝑛𝑖); Initial queue length 𝑄𝑖𝑗(0); Initial air traffic accumulation 𝑛𝑖𝑗(0); output: Queuing control 𝑣𝑖𝑗(𝑡), Air traffic control 𝑢𝑖𝑗(𝑡),∀𝑡∈ [𝑡0, 𝑡𝑓] 1Create symbolic variables 𝑓𝑘 𝑙,𝑚; 2Define constraints in (1) and objective 𝑒𝑙𝑎𝑠𝑡𝑖𝑐 in (4); 3Minimize 𝑒𝑙𝑎𝑠𝑡𝑖𝑐 to obtain the solution ∗𝐹= {∗𝑓𝑘 𝑙,𝑚}; 4Derive ∗𝑠𝑖𝑗 and 𝑛𝑖 from ∗𝑓𝑘 𝑙,𝑚 by steady-state equations (12)-(16); 5Initialize 𝑄𝑖𝑗(𝑡0) =𝑄𝑖𝑗(0) and 𝑛𝑖𝑗(𝑡0) =𝑛𝑖𝑗(0); 6for 𝑡∈ [𝑡0, 𝑡𝑓] do

## 7 if 𝐷𝑚(⋅)←𝐷𝑛𝑒𝑤

𝑚(⋅) then

## 8 Run step 1-4;

## 9 Update ∗𝑠𝑖𝑗 and 𝑛𝑖;

## 10 end

## 11 Calculate the queuing control 𝑣𝑖𝑗(𝑡) in (18);

## 12 Calculate queue’s exit flow 𝑞𝑖𝑗(𝑡) in (7);

## 13 Calculate the air traffic control 𝑢𝑖𝑗(𝑡) in (20);

## 14 Update demand queuing length 𝑄𝑖𝑗(𝑡) based on dynamics (6);

## 15 Update air traffic accumulation 𝑛𝑖𝑗(𝑡) based on dynamics (10);

16end 17Export data 𝑣𝑖𝑗(𝑡) and 𝑢𝑖𝑗(𝑡).

## 4. Simulation of two-region LAAT systems

In this section, we present case studies to assess the effectiveness of the proposed control scheme under time-varying demand profiles. Section 4.1 introduces the settings of the simulation environment. Then in Section 4.2, two numerical experiments are presented. For comparison, we introduce a baseline scheme that relies on a fixed desired equilibrium selected based on experience. For the time-varying demand that can yield variable equilibria, we consider two demand switching patterns: the workday-toholiday pattern, which simulates demand variability from low to high, and the holiday-to-workday pattern, which simulates demand variability from high to low.

### 4.1. Simulation settings

In our case studies, the LAAT network consists of 4 OD pairs and 8 vertiports, where vertiports 𝑘∕𝑙, 𝑘, 𝑙 ∈ {1,2,3,4} located in region 𝑔

## 1 and vertiports 𝑘∕𝑙, 𝑘, 𝑙 ∈ {5 ,6,7,8} located in region 𝑔

## 2. Accordingly, the LAAT network can be divided into 4

sub-networks for regional traffic, as illustrated in Fig. 7. The parameters of fixed travel cost 𝜏𝑘 𝑙,𝑚 [min] are chosen as follows 𝜏1

$$
3= 48, 𝜏1
$$

$$
4= 41, 𝜏2
$$

$$
3= 42, 𝜏2
$$

$$
4= 44, 𝜏3
$$

$$
5= 62, 𝜏3
$$

$$
6= 56, 𝜏4
$$

$$
5= 64, 𝜏4
$$

6= 57, 𝜏5

$$
7= 41, 𝜏5
$$

$$
8= 47, 𝜏6
$$

$$
7= 42, 𝜏6
$$

$$
8= 41, 𝜏7
$$

$$
1= 58, 𝜏7
$$

$$
2= 61, 𝜏8
$$

$$
1= 57, 𝜏8
$$

2= 56 The variable travel costs are set as 𝑡𝑘(𝑓𝑘) =𝜌(𝑓𝑘 𝑐𝑘)𝜎 [min] and 𝑡𝑙(𝑓𝑙) =𝜌(𝑓𝑙 𝑐𝑙)𝜎 [min], where 𝜌= 60 , 𝜎= 4. Parameters 𝑐𝑘 and 𝑐𝑙, representing the capacities of vertiports, are chosen as 𝑐𝑘=𝑐𝑙= 30 [veh/min] ,∀𝑘, 𝑙∈ {1,2,3,4,5,6,7,8}. In addition, airspace region 𝑎

## 1 and 𝑎

## 2 are set to be airspace cubes with the same size of 2 [km] by 2 [km] by 1 [km]. Then

we need to calibrate the airspace MFD for each airspace region. In our latest work (Weng et al., 2024 ), we conduct microscopic simulations for large-scale UAM, considering both aircraft collision avoidance and route guidance. Using collision-free aircraft trajectories, we can calculate macroscopic traffic variables, such as density and flow, referring to Safadi et al. (2023a ). Within Transportation Research Part C 178 (2025) 105237

<!-- page 14 -->

C. Weng et al.

#### Fig. 7. Settings of the LAAT network, where color red indicates region 𝑔

## 1 and color blue indicates region 𝑔

2.

#### Fig. 8. The relationship between air traffic flow and density, obtained from microscopic simulations (Weng et al., 2024 ).

an airspace cube of size 1 [km] by 1 [km] by 1 [km], the result of traffic flow and density is obtained, as illustrated in Fig. 8. Inspired by Haddad et al. (2021 ), we fit the flow-density relationship with a curve ̃𝑄(𝐾) =𝛼⋅𝐾⋅exp( -1 𝛽( 𝐾 𝐾𝑐𝑟)𝛽)

$$
,0\le 𝑘\le 𝐾𝑗𝑎𝑚
$$

where the parameters are estimated as 𝛼= 0.016, 𝛽= 1.136, 𝐾𝑐𝑟= 27 .6, 𝐾𝑗𝑎𝑚= 200 . Hence, we derive the airspace MFD for each airspace region in the case study as follows 𝐺(𝑛) =𝛼⋅𝑛⋅exp( -1 𝛽( 𝑛 𝑛𝑐𝑟)𝛽)

$$
[veh/s] ,0\le 𝑛\le 𝑛𝑗𝑎𝑚
$$

where 𝑛𝑐𝑟= 4𝐾𝑐𝑟= 110 .4 [veh] , 𝑛𝑗𝑎𝑚= 4𝐾𝑗𝑎𝑚= 800 [veh].

### 4.2. Simulation results

In our case studies, we simulate air traffic with demand variability between two levels: a low demand level 𝐷𝑤 𝑚(⋅), 𝑚∈ {1,2,3,4} for workdays and a high demand level 𝐷ℎ 𝑚(⋅), 𝑚∈ {1 ,2,3,4} for holidays. The elastic demand follows a linear model 𝐷𝑚(𝑡) = 𝑎𝑚𝑡+𝑏𝑚 [veh/min], which allows us to explicitly calculate the objective function (4). As a result, the state-of-the-art CasADi Transportation Research Part C 178 (2025) 105237

<!-- page 15 -->

C. Weng et al.

#### Fig. 9. Time-varying demand pattern subject to Gaussian noises.

toolbox (Andersson et al., 2019 ) integrated with the IPOPT solver is employed to solve the static network planning problem. The parameters of the workday and holiday demand are chosen as follows 𝐷𝑤 1(𝑡) = -0 .75𝑡+ 38, 𝐷𝑤 2(𝑡) = -0 .68𝑡+ 58, 𝐷𝑤 3(𝑡) = -0 .71𝑡+ 32, 𝐷𝑤 4(𝑡) = -0 .73𝑡+ 52, 𝐷ℎ 1(𝑡) = -0 .75𝑡+ 41, 𝐷ℎ 2(𝑡) = -0 .68𝑡+ 63, 𝐷ℎ 3(𝑡) = -0 .71𝑡+ 36, 𝐷ℎ 4(𝑡) = -0 .73𝑡+ 58 The solutions for the workdays and holidays are obtained as follows ∗𝐹𝑤=⎡ ⎢ ⎢ ⎢ ⎢⎣∗𝑓1 3∗𝑓1 4∗𝑓2 3∗𝑓2 ∗𝑓3 5∗𝑓3 6∗𝑓4 5∗𝑓4 ∗𝑓5 7∗𝑓5 8∗𝑓6 7∗𝑓6 ∗𝑓7 1∗𝑓7 2∗𝑓8 1∗𝑓8 2⎤ ⎥ ⎥ ⎥ ⎥⎦=⎡ ⎢ ⎢ ⎢ ⎢⎣0 6 .06 0 .44 0

### 3.37 4 .81 0 6 .50

### 1.44 0 0 1 .44

### 2.41 0 0 7 .23⎤

⎥ ⎥ ⎥ ⎥⎦[veh/min] , ∗𝐹ℎ=⎡ ⎢ ⎢ ⎢ ⎢⎣∗𝑓1 3∗𝑓1 4∗𝑓2 3∗𝑓2 ∗𝑓3 5∗𝑓3 6∗𝑓4 5∗𝑓4 ∗𝑓5 7∗𝑓5 8∗𝑓6 7∗𝑓6 ∗𝑓7 1∗𝑓7 2∗𝑓8 1∗𝑓8 2⎤ ⎥ ⎥ ⎥ ⎥⎦=⎡ ⎢ ⎢ ⎢ ⎢⎣0 6 .18 3 .25 0

### 6.64 2 .93 0 8 .68

### 3.41 0 0 3 .41

### 6.51 0 0 8 .17⎤

⎥ ⎥ ⎥ ⎥⎦[veh/min] Remarkably, the SO network equilibrium ∗𝐹𝑤 and ∗𝐹ℎ are sparse, indicating that not all potential network links are necessary for optimal traffic assignment. In practice, most passengers prefer the shortest path with minimal fixed travel time. On the other hand, the variable travel costs only depend on the total traffic flow of vertiports, allowing the all-or-nothing traffic assignment to be optimal. As discussed in Section 3, the proposed management scheme uses the SO network equilibrium ∗𝐹𝑤 and ∗𝐹ℎ as the benchmark for demand management and air traffic control. Hence, we get the parameters of the demand management model as [∗𝑠𝑤 11,∗𝑠𝑤 12,∗𝑠𝑤 21,∗𝑠𝑤 22] = [0 .108,0.245,0.160,0.048] [veh/s] ,[∗𝑠ℎ 11,∗𝑠ℎ 12,∗𝑠ℎ 21,∗𝑠ℎ 22] = [0 .157,0.30,0.245,0.114] [veh/s] , and the desired equilibrium of the air traffic flow model as [𝑛𝑤 1,𝑛𝑤 2] = [43 .6,36.3][veh] ,[𝑛ℎ 1,𝑛ℎ 2] = [82 .8,69.0][veh] . Based on the equilibrium ∗𝐹𝑤 and ∗𝐹ℎ, we introduce the corresponding time-varying demand for dynamic traffic control, as illustrated in Fig. 9. Both workday and holiday demands follow a trapezoidal profile consisting of the congestion on-set, peak, and congestion dissolving periods. During the congestion on-set and dissolving periods, the demand 𝑔𝑖𝑗(𝑡) is lower than the desired demand level ∗𝑔𝑖𝑗=∗𝑠𝑖𝑗. To compensate, we let the demand exceed the desired level (by 20%) during the peak period. In addition, the trapezoidal demand is subject to a 0.5% Gaussian Noise, to simulate the uncertainty in demand induced by a minority of passengers.

### 4.2.1. Example 1: simulation for workday-to-holiday traffic

Example 1 considers workday-to-holiday traffic, simulating demand variability from low to high. The time-varying demand 𝑔𝑖𝑗(𝑡), 𝑡∈ [0 ,120] [min] is constructed by concatenating the workday and holiday demands. In this example, the proposed management scheme aims to achieve the equilibrium ∗𝐹𝑤 during the period 𝑡∈ [0,60] [min], and ∗𝐹ℎ during the period 𝑡∈ [60 ,120] [min]. The baseline management scheme aims to achieve the equilibrium ∗𝐹𝑤 throughout the entire period 𝑡∈ [0,120] [min]. For a fair comparison, both the proposed scheme and the baseline scheme apply the same controllers for demand management and air traffic control, as proposed in Section 3.Transportation Research Part C 178 (2025) 105237

<!-- page 16 -->

C. Weng et al.

#### Fig. 10. Results of the baseline scheme under workday-to-holiday demand.

The results of the baseline and proposed schemes are illustrated in Figs. 10and 11, respectively. The maximum throughput queuing controller is effective in controlling air traffic inflow. When the time-varying demand 𝑔𝑖𝑗(𝑡) exceeds the desired level ∗𝑠𝑖𝑗, queuing control is activated to limit air traffic inflow. In this way, demand management ensures steady-state inflow for air traffic while filtering out demand noise caused by uncertainty. The baseline scheme uses the fixed benchmark ∗𝑠𝑖𝑗=∗𝑠𝑤 𝑖𝑗 to regulate the air traffic inflow to the same level during both the workday and holiday periods. The benchmark ∗𝑠𝑖𝑗=∗𝑠𝑤 𝑖𝑗 is preferred for workday demand, but it is insufficient to meet holiday demand. To address the increased demand during the holiday period, the proposed scheme uses a higher benchmark ∗𝑠𝑖𝑗=∗𝑠ℎ 𝑖𝑗 for queuing control. By allowing higher queuing exit flows, the proposed scheme performs better at reducing demand queues. Compared to the baseline scheme, the proposed scheme reduces the average queuing time by 42.3% and the maximum queue length by 52.6%, respectively. On the other hand, the steady-state MBC controller can effectively regulate the air traffic dynamics to the desired equilibrium. Benefiting from the bounded inflow provided by demand management, air traffic remains in free-flow states, i.e., 𝑛𝑖(𝑡)< 𝑛𝑐𝑟 𝑖. The baseline scheme achieves a fixed equilibrium [𝑛𝑤 1,𝑛𝑤 2], while the proposed scheme allows a variable equilibrium evolving from [𝑛𝑤 1,𝑛𝑤 2] to [𝑛ℎ 1,𝑛ℎ 2]. Notably, the equilibrium [𝑛𝑤 1,𝑛𝑤 2] is lower than [𝑛ℎ 1,𝑛ℎ 2]. Under the MFD framework, a low equilibrium helps improve air traffic safety (by reducing potential aircraft conflicts) but harms air traffic efficiency (due to the reduction in trip completion). Choosing an appropriate desired equilibrium is important for managers to balance the requirements of air traffic safety and efficiency. A consensus in the literature is that the desired equilibrium is related to the demand level (Zhong et al., 2018b ). Hence, it is reasonable for the proposed scheme to achieve a higher equilibrium to meet the increased demand during the holiday period. Compared to the baseline scheme, the proposed scheme increases the maximum trip completion flow by 26.9%. In Example 1, the baseline scheme is designed based on prior knowledge of workday demand. This knowledge can have a lasting influence on traffic managers’ decisions, especially in practical applications. Alternatively, traffic managers may lack systematic Transportation Research Part C 178 (2025) 105237

<!-- page 17 -->

C. Weng et al.

#### Fig. 11. Results of the proposed scheme under workday-to-holiday demand.

methods to update the control scheme when the demand pattern changes. As a result, the baseline scheme attempts to handle holiday demand using the knowledge of workday demand, e.g., ∗𝑠𝑤 𝑖𝑗 and [𝑛𝑤 1,𝑛𝑤 2]. The results demonstrate the limitations of the baseline scheme. In contrast, the proposed scheme can effectively respond to variability in traffic demand by implementing the planning-control interaction for both workday and holiday demand. More importantly, the integration of static network planning and dynamic traffic control provides an interpretable method for traffic managers to design new traffic control measures.

### 4.2.2. Example 2: simulation for holiday-to-workday traffic

Example 2 investigates holiday-to-work traffic, simulating demand variability from high to low. We construct the time-varying demand 𝑔𝑖𝑗(𝑡), 𝑡∈ [0,120] [min] by concatenating the holiday and workday demands. In this example, the proposed management scheme aims to achieve the equilibrium ∗𝐹ℎ during the period 𝑡∈ [0,60] [min], and ∗𝐹𝑤 during the period 𝑡∈ [60 ,120] [min]. The baseline management scheme aims to achieve the equilibrium ∗𝐹ℎ throughout the entire period 𝑡∈ [0,120] [min]. The other settings of Example 2 are identical to those of Example 1. The results of the baseline and proposed schemes are illustrated in Figs. 12and 13, respectively. As explained, the demand management mechanism aims to regulate air traffic inflow based on queuing. The baseline scheme uses the fixed benchmark ∗𝑠𝑖𝑗=∗𝑠ℎ 𝑖𝑗 for demand management during both the workday and holiday periods. The benchmark ∗𝑠𝑖𝑗=∗𝑠ℎ 𝑖𝑗 adapts to workday demand but becomes oversupplied for holiday demand. As the demand decreases during the workday period, the queuing control becomes inactive. Consequently, the air traffic inflow is the same as the origin demand, i.e., 𝑞𝑖𝑗(𝑡) =𝑔𝑖𝑗(𝑡), without filtering the demand noise. To save control resources during the workday period, the proposed scheme lowers the benchmark from ∗𝑠ℎ 𝑖𝑗 to ∗𝑠𝑤 𝑖𝑗. Accordingly, the air traffic inflow is regulated to the corresponding desired level with demand noise being filtered out. On the other hand, the air traffic control mechanism aims to regulate the air traffic dynamics to the desired equilibrium. Unlike Example 1, the Transportation Research Part C 178 (2025) 105237

<!-- page 18 -->

C. Weng et al.

#### Fig. 12. Results of the baseline scheme under holiday-to-workday demand.

fixed equilibrium [𝑛ℎ 1,𝑛ℎ 2] becomes unreachable for the baseline scheme during the workday period. Here, we do not enforce the air traffic dynamics to reach the equilibrium [𝑛ℎ 1,𝑛ℎ 2], by employing more extreme policies, such as concentrating air traffic inflow within a small time window. As discussed in Zhong et al. (2018a ), achieving a high equilibrium under low-demand conditions is meaningless because the control objective is to make the network denser than it should be without any control. Responding to the decrease in demand during the workday period, the proposed scheme achieves a lower equilibrium [𝑛𝑤 1,𝑛𝑤 2]. In this example, the baseline scheme follows the holiday management policy to handle workday demand. This aggressive policy often leads to resource wastage in practice. Resources are required to maintain the maximum queue exit capacity ∗𝑠𝑖𝑗, regardless of whether the capacity is fully utilized. An unreasonable choice of a high desired equilibrium under low-demand conditions results in wasted air traffic capacity. In contrast, the proposed scheme implements different management policies for different demand patterns, balancing the requirements of control resources and air traffic efficiency. To close the discussion, under time-varying demand profiles, numerical results demonstrate that the proposed scheme can effectively regulate the air traffic dynamics to the desired equilibrium derived from the SO equilibrium, which prevents air traffic congestion. Compared to a fixed equilibrium, a variable SO equilibrium given by the planning-control interaction is shown to be more effective in improving traffic efficiency, particularly when demand increases.

## 5. Conclusion

The rapid development of urban air mobility gives rise to low-altitude air transport (LAAT) systems. Flow-based traffic management schemes are promising solutions for achieving efficient LAAT management. In this paper, we explore flow-based traffic modeling for LAAT systems, including the static model of network equilibrium, as well as dynamic models of demand Transportation Research Part C 178 (2025) 105237

<!-- page 19 -->

C. Weng et al.

#### Fig. 13. Results of the proposed scheme under holiday-to-workday demand.

management and air traffic control. The static model aggregates individual UAM trips into traffic flows on the LAAT network, aiming to optimize the network flow pattern in the planning phase. The dynamic models characterize regional traffic as dynamics of aircraft accumulation based on demand queuing and airspace MFDs, aiming to regulate the dynamics to a desired equilibrium in the control phase. Static network planning yields a system-optimal (SO) equilibrium, which is consistent with the desired equilibrium concept in dynamic traffic control. Inspired by this, we establish the interaction between static network planning and dynamic traffic control by deriving the desired equilibrium from the SO network equilibrium. The derived equilibrium is ensured to exist as a stable equilibrium and can be adjusted in response to traffic demand and airspace capacity. We devise a control scheme to implement the planning-control interaction. The proposed scheme, by coupling dynamic traffic control and demand management, can adjust the desired equilibrium according to changes in demand patterns, thus guaranteeing the feasibility of the set-point control problem with respect to varying demand patterns. Numerical examples demonstrate the merits of the integrated dynamic traffic control and demand management scheme. Compared to a fixed equilibrium based on experience, a variable SO equilibrium given by the planning-control interaction can significantly improve network efficiency, especially when demand patterns admit abrupt changes and noise. CRediT authorship contribution statement Canqiang Weng: Writing review & editing, Writing original draft, Visualization, Validation, Methodology, Formal analysis, Conceptualization. Tianlu Pan: Writing review & editing, Writing original draft, Methodology, Formal analysis, Conceptualization. Can Chen: Writing review & editing, Visualization, Methodology, Formal analysis. Renxin Zhong: Writing review & editing, Writing original draft, Methodology, Formal analysis, Conceptualization.Transportation Research Part C 178 (2025) 105237

<!-- page 20 -->

C. Weng et al. Acknowledgments The work in this paper was supported by research grants from the National Natural Science Foundation of China (Nos. 72071214 & 62203239). Appendix A In this appendix, we provide an experimental example to explore the microscopic implementation of the coupled air traffic control MBC. As illustrated in Fig. 14, the test airspace is divided into two regions: the left region labeled as 𝑎 1, and the right region labeled as 𝑎

## 2. Each region consists of 9 hexagonal cells, with each cell having a side length of 250 [m] and a height of 100 [m]. We load

an endogenous traffic inflow of 𝑞11(𝑡) = 0 .5 [veh/s] and an exogenous traffic inflow of 𝑞12(𝑡) = 0 .5 [veh/s] into airspace region 𝑎 1. The origins and destinations of air traffic flow are randomly distributed across the test airspace. We use the simulation framework proposed by Weng et al. (2024 ) to generate aircraft trajectories between origins and destinations. The simulation framework, which integrates aircraft collision avoidance and route guidance, can effectively ensure air traffic homogeneity. In this example, all aircraft follow the same settings as follows: the detection radius 𝑟𝑑= 200 [m], safety radius 𝑟𝑠= 50 [m]. Fig. 14 shows the trajectories of some aircraft for an intuitive understanding. Inspired by Sirmatel and Yildirimoglu (2023 ), we consider that aircraft travel speed can potentially influence regional traffic flow. Hence, we regulate aircraft travel speed for endogenous/exogenous traffic. To be specific, we divide the microscopic simulation into two phases 𝑡∈ [0,450] [s] and 𝑡∈ [450 ,900] [s]. During the first phase 𝑡∈ [0,450] [s], the maximum speed of aircraft is set to be 𝑣𝑚= 20 [m/s]. During the second phase 𝑡∈ [0,900] [s], the maximum speed of aircraft with endogenous travel demand is set to be 𝑣𝑚

$$
11= 10 [m/s], while the maximum speed of aircraft with exogenous travel demand is set to be 𝑣𝑚
$$

$$
12= 30 [m/s]. The average
$$

speed of aircraft during both phases is approximately equal. The adjustment in the maximum speed of aircraft is expected to reduce endogenous traffic flow while increasing exogenous traffic flow. We measure the trip completion flow for both endogenous and exogenous traffic. The results are illustrated in Fig. 15. During 𝑡∈ [300 ,450] [s], both the endogenous and exogenous traffic flows remain at a relatively stable level. During 𝑡∈ [450 ,600] [s], the endogenous traffic flow is observed to decrease, while the exogenous traffic flow is observed to increase. The results demonstrate

#### Fig. 14. The experimental example of microscopic air traffic simulation, where ‘O’ marks the origin, ‘X’ marks the destination, and the color of the dotted line

represents the travel time.Transportation Research Part C 178 (2025) 105237

<!-- page 21 -->

C. Weng et al.

#### Fig. 15. Changes in trip completion flow induced by aircraft speed adjustment.

the correlation between aircraft travel speed and air traffic flow. In other words, it is possible to regulate macroscopic traffic flow through microscopic aircraft speed control. If we can map the MBC 𝑢𝑖𝑗 to speed limit 𝑣𝑚 𝑖𝑗, we can implement macroscopic air traffic control at the microscopic level. Appendix B Proof of Proposition 1. Combining Eqs. (6) and (17), we have

$$
𝑄𝑖𝑗(𝑡𝑓) =𝑄𝑖𝑗(0) +\int 𝑡𝑓
$$

0.𝑄𝑖𝑗(𝑡) d𝑡 (B.1)

$$
=𝑄𝑖𝑗(0) +\int 𝑡𝑓
$$

0𝑔𝑖𝑗(𝑡) -𝑞𝑖𝑗(𝑡) d𝑡

$$
=𝑄𝑖𝑗(0) +\int 𝑡𝑓
$$

0𝑔𝑖𝑗(𝑡) d𝑡-𝑄 𝑖𝑗

$$
Noting that 𝑄𝑖𝑗(0) +\int 𝑡𝑓
$$

0𝑔𝑖𝑗(𝑡) d𝑡 is a control-independent constant, we have max 𝑣𝑖𝑗(𝑡)𝑄 𝑖𝑗⇔ min 𝑣𝑖𝑗(𝑡)𝑄𝑖𝑗(𝑡𝑓) Then we denote the queue length induced by controller (18) as ∗𝑄𝑖𝑗(𝑡), 𝑡∈ [0, 𝑡𝑓] and divide the discussion into the following cases: (1)If ∗𝑄𝑖𝑗(𝑡𝑓) = 0 : Noting that ∀𝑡∈ [0 , 𝑡𝑓], 𝑄𝑖𝑗(𝑡)\ge 0, we can easily find that ∗𝑄𝑖𝑗(𝑡𝑓) = 0 is minimal, which implies that 𝑄 𝑖𝑗 is maximal for 𝑡∈ [0, 𝑡𝑓]. (2)If ∗𝑄𝑖𝑗(𝑡𝑓)>0 and ∀𝑡∈ [0, 𝑡𝑓],∗𝑄𝑖𝑗(𝑡)>0 : The controller (18) is simplified as 𝑣𝑖𝑗(𝑡) = 1 ,∀𝑡∈ [0, 𝑡𝑓]. Hence, we have ∗𝑄

$$
𝑖𝑗=\int 𝑡𝑓
$$

$$
0𝑞𝑖𝑗(𝑡) d𝑡=\int 𝑡𝑓
$$

0∗𝑠𝑖𝑗𝑣𝑖𝑗(𝑡) d𝑡=∗𝑠𝑖𝑗⋅𝑡𝑓 Obviously, ∗𝑄 𝑖𝑗 is maximal for 𝑡∈ [0, 𝑡𝑓]. (3)If ∗𝑄𝑖𝑗(𝑡𝑓)>0 and ∃̂𝑡∈ [0, 𝑡𝑓],∗𝑄𝑖𝑗(̂𝑡) = 0 : Considering that there may be more than one ̂𝑡 satisfying ∗𝑄𝑖𝑗(̂𝑡) = 0 , here we regard ̂𝑡 as the one closest to 𝑡𝑓. Accordingly, we partition the control period [0, 𝑡𝑓] into two intervals [0,̂𝑡] and (̂𝑡, 𝑡𝑓], where ∗𝑄𝑖𝑗(̂𝑡) = 0 and ∀𝑡∈ (̂𝑡, 𝑡𝑓],∗𝑄𝑖𝑗(𝑡)>0. From Eq. (B.1), we have

$$
∗𝑄𝑖𝑗(𝑡𝑓) =∗𝑄𝑖𝑗(̂𝑡) +\int 𝑡𝑓
$$

$$
̂𝑡𝑔𝑖𝑗(𝑡) d𝑡-\int 𝑡𝑓
$$

̂𝑡𝑞𝑖𝑗(𝑡) d𝑡Transportation Research Part C 178 (2025) 105237

<!-- page 22 -->

C. Weng et al.

$$
According to Case (1), ∗𝑄𝑖𝑗(̂𝑡) = 0 is minimal. According to Case (2), \int 𝑡𝑓
$$

$$
̂𝑡𝑞𝑖𝑗(𝑡) d𝑡=∗𝑠𝑖𝑗⋅(𝑡𝑓-̂𝑡) is maximal. Besides, \int 𝑡𝑓
$$

̂𝑡𝑔𝑖𝑗(𝑡) d𝑡 is a control-independent constant. Hence, we have ∗𝑄𝑖𝑗(𝑡𝑓) is minimal, which implies that 𝑄 𝑖𝑗 is maximal for 𝑡∈ [0, 𝑡𝑓] To conclude, the controller given by (18) achieves the objective defined in (17). □ Appendix C Proof of Proposition 2. Given oversaturated demand 𝑔𝑖𝑗(𝑡)>∗𝑠𝑖𝑗,∀𝑖, 𝑗∈ {1 ,2}, the airspace inflows are regulated as 𝑞𝑖𝑗(𝑡) =𝑞𝑖𝑗, which are defined in Section 3.1. Combing Eqs. (10) and (20), we have .𝑛11(𝑡) =𝑞11+𝐺2(𝑛2(𝑡))𝑢21(𝑡) -𝐺1(𝑛1(𝑡))(1 𝑢12(𝑡)) (C.1a) .𝑛12(𝑡) =𝑞12-𝐺1(𝑛1(𝑡))𝑢12(𝑡) (C.1b) .𝑛21(𝑡) =𝑞21-𝐺2(𝑛2(𝑡))𝑢21(𝑡) (C.1c) .𝑛22(𝑡) =𝑞22+𝐺1(𝑛1(𝑡))𝑢12(𝑡) -𝐺2(𝑛2(𝑡))(1 𝑢21(𝑡)) (C.1d) By summing (C.1a)-(C.1b) and (C.1c)-(C.1d), respectively, we have .𝑛1(𝑡) =𝑞11+𝑞12+𝐺2(𝑛2(𝑡))𝑢21(𝑡) -𝐺1(𝑛1(𝑡)) (C.2a) .𝑛2(𝑡) =𝑞21+𝑞22+𝐺1(𝑛1(𝑡))𝑢12(𝑡) -𝐺2(𝑛2(𝑡)) (C.2b) By introducing the inverse MFD function, we have 𝑛1(𝑡)\le 𝐺-1 1,𝑠(𝑞12)⇒𝐺1(𝑛1(𝑡))\le 𝑞12 (C.3) Combing (C.3) and (C.2a), we have ∀𝑛1(𝑡)\le 𝐺-1 1,𝑠(𝑞12),.𝑛1(𝑡)\ge 𝑞11 (C.4) Proposition 3. Given 𝑛1(0) ∈ [0 , 𝑛𝑐𝑟 1) and condition (C.4), it holds that ∀𝑡\ge 𝜏1, 𝑛1(𝑡)\ge 𝐺-1

$$
1,𝑠(𝑞12), where 𝜏1=𝐺-1
$$

1,𝑠(𝑞12) 𝑞11. Proof. We divide the discussion into the following cases: (1)If 𝐺-1 1,𝑠(𝑞12)\le 𝑛1(0)< 𝑛𝑐𝑟 1, we use proof by contradiction and assume that ∃𝑡𝑒>0, 𝑛1(𝑡𝑒)< 𝐺-1 1,𝑠(𝑞12): Note that 𝑛1(0)\ge 𝐺-1 1,𝑠(𝑞12)> 𝑛1(𝑡𝑒) and 𝑛1(𝑡) is a continuous function. Hence, there exists a 𝑡𝑠∈ [0, 𝑡𝑒) such that 𝑛1(𝑡𝑠) =𝐺-1 1,𝑠(𝑞12) and ∀𝑡∈ (𝑡𝑠, 𝑡𝑒), 𝑛1(𝑡)< 𝐺-1 1,𝑠(𝑞12). Combining condition (C.4) and the Mean Value Theorem, we have 𝑛1(𝑡𝑒) -𝑛1(𝑡𝑠) 𝑡𝑒-𝑡𝑠=.𝑛1(̂𝑡)|̂𝑡∈(𝑡𝑠,𝑡𝑒)⋅(𝑡𝑒-𝑡𝑠)\ge 𝑞11⋅(𝑡𝑒-𝑡𝑠)>0 This implies that 𝑛1(𝑡𝑒)> 𝑛1(𝑡𝑠) =𝐺-1 1,𝑠(𝑞12), which contradicts the assumption. In this case, i.e., 𝐺-1 1,𝑠(𝑞12)\le 𝑛1(0)< 𝑛𝑐𝑟 1, the conclusion is that ∀𝑡 >0, 𝑛1(𝑡)\ge 𝐺-1 1,𝑠(𝑞12).

$$
(2)If 0\le 𝑛1(0)< 𝐺-1
$$

1,𝑠(𝑞12), we use proof by contradiction and assume that ∃̂𝑡\ge 𝜏1, 𝑛1(̂𝑡)< 𝐺-1 1,𝑠(𝑞12): According to the conclusion of Case (1), it requires that ∀𝑡∈ [0,̂𝑡], 𝑛1(𝑡)< 𝐺-1 1,𝑠(𝑞12) to ensure 𝑛1(̂𝑡)< 𝐺-1 1,𝑠(𝑞12). Note that

$$
𝑛1(̂𝑡) =𝑛1(0) +\int ̂𝑡
$$

$$
0.𝑛1(𝑡) d𝑡\ge \int ̂𝑡
$$

0𝑞11d𝑡=𝑞11⋅̂𝑡 Hence, we have 𝑛1(̂𝑡) =𝑞11⋅̂𝑡 < 𝐺-1 1,𝑠(𝑞12) and ̂𝑡 <𝐺-1 1,𝑠(𝑞12)

$$
𝑞11=𝜏1, which contradicts the assumption.
$$

$$
In this case, i.e., 0\le 𝑛1(0)< 𝐺-1
$$

1,𝑠(𝑞12), the conclusion is that ∀𝑡 > 𝜏1, 𝑛1(𝑡)\ge 𝐺-1 1,𝑠(𝑞12). □ Similar conclusions hold for state 𝑛2(𝑡). Hence, given uncongested initial state 𝑛1(0) ∈ [0 , 𝑛𝑐𝑟 1) and 𝑛2(0) ∈ [0 , 𝑛𝑐𝑟 2), it holds that ∀𝑡\ge 𝜏1, 𝑛1(𝑡)\ge 𝐺-1 1,𝑠(𝑞12) and ∀𝑡\ge 𝜏2, 𝑛2(𝑡)\ge 𝐺-1

$$
2,𝑠(𝑞21), where 𝜏1=𝐺-1
$$

1,𝑠(𝑞12)

$$
𝑞11 and 𝜏2=𝐺-1
$$

2,𝑠(𝑞21) 𝑞22. Noting that 𝜏1 and 𝜏2 are constants, we simplify the proof by regarding ∀𝑡 >0, 𝑛1(𝑡)\ge 𝐺-1 1,𝑠(𝑞12), 𝑛2(𝑡)\ge 𝐺-1 2,𝑠(𝑞21). Consequently, controller (20) is rewritten as follows:

$$
𝑢12=𝑞12(𝑡)
$$

$$
𝐺1(𝑛1(𝑡)), 𝑢12=𝑞21(𝑡)
$$

𝐺1(𝑛2(𝑡))(C.5) Combining (C.2) and (C.5), we have .𝑛1(𝑡) =𝑞11+𝑞12+𝑞21-𝐺1(𝑛1(𝑡)) .𝑛2(𝑡) =𝑞21+𝑞22+𝑞12-𝐺2(𝑛2(𝑡))Transportation Research Part C 178 (2025) 105237

<!-- page 23 -->

C. Weng et al.

$$
By introducing 𝑛1=𝐺-1
$$

1,𝑠(𝑞11+𝑞12+𝑞21), we have 𝑛1<𝑛1⇒𝐺1(𝑛1)<𝑞11+𝑞12+𝑞21⇒.𝑛1(𝑡)>0 𝑛1>𝑛1⇒𝐺1(𝑛1)>𝑞11+𝑞12+𝑞21⇒.𝑛1(𝑡)<0 Considering the Lyapunov function 𝑉(̃ 𝑛1) =1

$$
2̃ 𝑛1⋅̃ 𝑛1, where ̃ 𝑛1=𝑛1(𝑡) -𝑛1, we have
$$

d𝑉 d𝑡=𝜕𝑉 𝜕̃ 𝑛1⋅d̃ 𝑛1 d𝑡= (𝑛1-𝑛1)⋅d(𝑛1-𝑛1) d𝑡= (𝑛1-𝑛1)⋅.𝑛1(𝑡)<0 Similar conclusions hold for state 𝑛2(𝑡). Hence, based on the Lyapunov Stability Theorem, the air traffic dynamics (10) asymptotically converges the equilibrium [𝑛1,𝑛2]𝑇 defined in (16). □

## References

Andersson, J.A.E., Gillis, J., Horn, G., Rawlings, J.B., Diehl, M., 2019. CasADi A software framework for nonlinear optimization and optimal control. Math. Program. Comput. 11 (1), 1-36. http://dx.doi.org/10.1007/s12532-018-0139-4 . Batista, S.F., Leclercq, L., 2019. Regional dynamic traffic assignment framework for macroscopic fundamental diagram multi-regions models. Transp. Sci. 53 (6), 1563-1590. Bauranov, A., Rakas, J., 2021. Designing airspace for urban air mobility: A review of concepts and approaches. Prog. Aerosp. Sci. 125, 100726. Cantarella, G.E., Watling, D.P., 2016. A general stochastic process for day-to-day dynamic traffic assignment: Formulation, asymptotic behaviour, and stability analysis. Transp. Res. Part B: Methodol. 92, 3-21. Chen, C., Geroliminis, N., Zhong, R., 2024. An iterative adaptive dynamic programming approach for macroscopic fundamental diagram-based perimeter control and route guidance. Transp. Sci. 58 (4), 896-918. Chen, C., Huang, Y., Lam, W., Pan, T., Hsu, S., Sumalee, A., Zhong, R., 2022. Data efficient reinforcement learning and adaptive optimal perimeter control of network traffic dynamics. Transp. Res. Part C: Emerg. Technol. 142, 103759. Cummings, C., Mahmassani, H., 2021. Emergence of 4-D system fundamental diagram in urban air mobility traffic flow. Transp. Res. Rec. 2675 (11), 841-850. Cummings, C., Mahmassani, H., 2024a. Airspace congestion, flow relations, and 4-D fundamental diagrams for advanced urban air mobility. Transp. Res. Part C: Emerg. Technol. 159, 104467. Cummings, C., Mahmassani, H., 2024b. Comparing urban air mobility network airspaces: Experiments and insights. Transp. Res. Rec. 2678 (4), 440-454. Daganzo, C.F., 2007. Urban gridlock: Macroscopic modeling and mitigation approaches. Transp. Res. Part B: Methodol. 41 (1), 49-62. Dietrich, A., Wulff, Y., 2020. Urban air mobility: Adding the third dimension to urban and regional transportation. In: Presentation for: An Introduction To Urban Air Mobility for State and Local Decision Makers: A Virtual Workshop, Sponsored By the Community Air Mobility Initiative (CAMI). Available Online At https://www.communityairmobility.org/uam101 . FAA NextGen Organization, 2022. Unmanned aircraft system (UAS) traffic management (UTM) concept of operations v2.0. Available at: https://www.faa.gov/ sites/faa.gov/files/2022-08/UTM_ConOps_v2.pdf . Garrow, L.A., German, B.J., Leonard, C.E., et al., 2021. Urban air mobility: A comprehensive review and comparative analysis with autonomous and electric ground transportation for informing future research. Transp. Res. Part C: Emerg. Technol. 132, 103377. Gartner, N.H., 1980a. Optimal traffic assignment with elastic demands: A review part I. analysis framework. Transp. Sci. 14 (2), 174-191. Gartner, N.H., 1980b. Optimal traffic assignment with elastic demands: a review part II. algorithmic approaches. Transp. Sci. 14 (2), 192-208. Geroliminis, N., Daganzo, C.F., 2008. Existence of urban-scale macroscopic fundamental diagrams: Some experimental findings. Transp. Res. Part B: Methodol.

## 42 (9), 759-770.

Geroliminis, N., Haddad, J., Ramezani, M., et al., 2013. Optimal perimeter control for Two Urban Regions with macroscopic fundamental diagrams: A model predictive approach. IEEE Trans. Intell. Transp. Syst. 14 (1), 348-359. http://dx.doi.org/10.1109/TITS.2012.2216877 . Geroliminis, N., Sun, J., 2011. Properties of a well-defined macroscopic fundamental diagram for urban traffic. Transp. Res. Part B: Methodol. 45 (3), 605-617. Haddad, J., 2015. Robust constrained control of uncertain macroscopic fundamental diagram networks. Transp. Res. Part C: Emerg. Technol. 59, 323-339. Haddad, J., 2017a. Optimal coupled and decoupled perimeter control in one-region cities. Control Eng. Pract. 61, 134-148. Haddad, J., 2017b. Optimal perimeter control synthesis for two urban regions with aggregate boundary queue dynamics. Transp. Res. Part B: Methodol. 96, 1-25. Haddad, J., Geroliminis, N., 2012. On the stability of traffic perimeter control in two-region urban cities. Transp. Res. Part B: Methodol. 46 (9), 1159-1176. Haddad, J., Mirkin, B., Assor, K., et al., 2021. Traffic flow modeling and feedback control for future low-altitude air city transport: An MFD-based approach. Transp. Res. Part C: Emerg. Technol. 133, 103380. Haddad, J., Ramezani, M., Geroliminis, N., 2013. Cooperative traffic control of a mixed network with two urban regions and a freeway. Transp. Res. Part B: Methodol. 54, 17-36. Haddad, J., Shraiber, A., 2014. Robust perimeter control design for an urban region. Transp. Res. Part B: Methodol. 68, 315-332. Holden, J., 2018. Uber Keynote: Scaling Uber Air. Uber Elevate Summit, Los Angeles, CA, May 8. Huang, Y., Xiong, J., Hsu, S.C., Sumalee, A., Lam, W., Zhong, R., 2024. A comparison of the accumulation-based, trip-based and time delay macroscopic fundamental diagram models. Transp. A: Transp. Sci. 1-37. Kasliwal, A., Furbush, N.J., Gawron, J.H., McBride, J.R., Wallington, T.J., De Kleine, R.D., Kim, H.C., Keoleian, G.A., 2019. Role of flying cars in sustainable mobility. Nat. Commun. 10 (1), 1555. Keyvan-Ekbatani, M., Carlson, R.C., Knoop, V.L., Papageorgiou, M., 2021. Optimizing distribution of metered traffic flow in perimeter control: Queue and delay balancing approaches. Control Eng. Pract. 110, 104762. Keyvan-Ekbatani, M., Kouvelas, A., Papamichail, I., Papageorgiou, M., 2012. Exploiting the fundamental diagram of urban networks for feedback-based gating. Transp. Res. Part B: Methodol. 46 (10), 1393-1403. Kopardekar, P., Rios, J., Prevot, T., Johnson, M., Jung, J., Robinson, J.E., 2016. Unmanned aircraft system traffic management (UTM) concept of operations. In: AIAA Aviation and Aeronautics Forum (Aviation 2016). Menelaou, C., Timotheou, S., Kolios, P., Panayiotou, C.G., 2021. Joint route guidance and demand management for real-time control of multi-regional traffic networks. IEEE Trans. Intell. Transp. Syst. 23 (7), 8302-8315. Patriksson, M., 2015. The traffic assignment problem: models and methods. Courier Dover Publications. Pritchard, J., 2024. AutoFlight completes world’s first inter-city eVTOL aircraft flight between Shenzhen and Zhuhai in China. Available at: https://evtolinsights. com/2024/02/autoflight-completes-worlds-first-inter-city-evtol-aircraft-flight-between-shenzhen-and-zhuhai/ . Raghunatha, A., Lindkvist, E., Thollander, P., Hansson, E., Jonsson, G., 2023. Critical assessment of emissions, costs, and time for last-mile goods delivery by drones versus trucks. Sci. Rep. 13 (1), 11814.Transportation Research Part C 178 (2025) 105237

<!-- page 24 -->

C. Weng et al. Ramezani, M., Haddad, J., Geroliminis, N., 2015. Dynamics of heterogeneity in urban networks: aggregated traffic modeling and hierarchical control. Transp. Res. Part B: Methodol. 74, 1-19. Rimjha, M., Trani, A., 2021. Urban air mobility: Factors affecting vertiport capacity. In: 2021 Integrated Communications Navigation and Surveillance Conference. ICNS, IEEE, pp. 1-14. Rothfeld, R., Balac, M., Ploetner, K.O., Antoniou, C., 2018. Initial analysis of urban air mobility’s transport performance in sioux falls. In: 2018 Aviation Technology, Integration, and Operations Conference. p. 2886. Safadi, Y., Fu, R., Quan, Q., Haddad, J., 2023a. Macroscopic fundamental diagrams for low-altitude air city transport. Transp. Res. Part C: Emerg. Technol. 152, 104141. Safadi, Y., Geroliminis, N., Haddad, J., 2024. Integrated departure and boundary control for low-altitude air city transport systems. Transp. Res. Part B: Methodol. 103020. Safadi, Y., Geroliminis, N., Haddad, J., et al., 2023b. Aircraft departures management for low altitude air city transport based on macroscopic fundamental diagram. In: 2023 American Control Conference. ACC, IEEE, pp. 4393-4398. SESAR Joint Undertaking, 2017. U-space: Blueprint. Available at: https://www.sesarju.eu/sites/default/files/documents/reports/U-space%20Blueprint% 20brochure%20final.PDF . Shen, X., Li, S., Li, M., Tang, Y., Chen, F., Sun, J., Xu, C., 2023. Low altitude economy development white paper (2.0) all digital solutions. Available at: https://doc.weixin.qq.com/forms/ALIAUwdzAA8AMcA4wb7ABYUzKzwpn8Txf#/fill . Shrestha, R., Oh, I., Kim, S., et al., 2021. A survey on operation concept, advancements, and challenging issues of urban air traffic management. Front. Futur. Transp. 2, 626935. Sirmatel, I.I., Geroliminis, N., 2018. Economic model predictive control of large-scale urban road networks via perimeter control and regional route guidance. IEEE Trans. Intell. Transp. Syst. 19 (4), 1112-1121. Sirmatel, I.I., Geroliminis, N., 2021. Stabilization of city-scale road traffic networks via macroscopic fundamental diagram-based model predictive perimeter control. Control Eng. Pract. 109, 104750. Sirmatel, I.I., Yildirimoglu, M., 2023. Nonlinear model predictive control of large-scale urban road networks via average speed control. Transp. Res. Part C: Emerg. Technol. 156, 104338. Su, Z., Chow, A.H., Zheng, N., Huang, Y., Liang, E., Zhong, R., 2020. Neuro-dynamic programming for optimal control of macroscopic fundamental diagram systems. Transp. Res. Part C: Emerg. Technol. 116, 102628. Sunil, E., Hoekstra, J., Ellerbroek, J., Bussink, F., Nieuwenhuisen, D., Vidosavljevic, A., Kern, S., 2015. Metropolis: Relating airspace structure and capacity for extreme traffic densities. In: ATM Seminar 2015, 11th USA/EUROPE Air Traffic Management R&D Seminar. Vascik, P.D., Hansman, R.J., 2019. Development of vertiport capacity envelopes and analysis of their sensitivity to topological and operational factors. In: AIAA Scitech 2019 Forum. p. 0526. Wang, Z., Delahaye, D., Farges, J.-L., Alam, S., 2022. Complexity optimal air traffic assignment in multi-layer transport network for urban air mobility operations. Transp. Res. Part C: Emerg. Technol. 142, 103776. Wang, Z., Delahaye, D., Farges, J.-L., Alam, S., 2023. A quasi-dynamic air traffic assignment model for mitigating air traffic complexity and congestion for high-density UAM operations. Transp. Res. Part C: Emerg. Technol. 154, 104279. Wei, L., Justin, C.Y., Briceno, S.I., Mavris, D.N., 2018. Door-to-door travel time comparative assessment for conventional transportation methods and short takeoff and landing on demand mobility concepts. In: 2018 Aviation Technology, Integration, and Operations Conference. p. 3055. Weng, C., Chen, C., Tan, J., Pan, T., Zhong, R., 2024. Real-time traffic simulation and management for large-scale urban air mobility: Integrating route guidance and collision avoidance. Prepr. Submitt. Transp. Res. Part C: Emerg. Technol. Available at: https://arxiv.org/abs/2412.01235 . Wu, Z., Zhang, Y., 2021. Integrated network design and demand forecast for on-demand urban air mobility. Engineering 7 (4), 473-487. Yang, H., Huang, H.J., 2005. Mathematical and Economic Theory of Road Pricing. Emerald Group Publishing Limited, pp. 48-49. Yildirimoglu, M., Geroliminis, N., 2014. Approximating dynamic equilibrium conditions with macroscopic fundamental diagrams. Transp. Res. Part B: Methodol. 70, 186-200. Zhong, R., Chen, C., Huang, Y., Sumalee, A., Lam, W., Xu, D., 2018a. Robust perimeter control for two urban regions with macroscopic fundamental diagrams: A control-Lyapunov function approach. Transp. Res. Part B: Methodol. 117, 687-707. Zhong, R., Huang, Y., Chen, C., Lam, W., Xu, D., Sumalee, A., 2018b. Boundary conditions and behavior of the macroscopic fundamental diagram based network traffic dynamics: A control systems perspective. Transp. Res. Part B: Methodol. 111, 327-355. Zhong, R., Xie, X., Luo, J., Pan, T., Lam, W., Sumalee, A., 2020. Modeling double time-scale travel time processes with application to assessing the resilience of transportation systems. Transp. Res. Part B: Methodol. 132, 228-248.Transportation Research Part C 178 (2025) 105237
