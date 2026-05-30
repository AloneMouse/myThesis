---
source_pdf: Lei 等 - 2020 - Data-Driven Model Free Adaptive Perimeter Control for Multi-Region Urban Traffic Networks With Route.pdf
pages: 12
---

# Lei 等 - 2020 - Data-Driven Model Free Adaptive Perimeter Control for Multi-Region Urban Traffic Networks With Route

<!-- page 1 -->

## 2894 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

Data-Driven Model Free Adaptive Perimeter Control for Multi-Region Urban Traffic Networks With Route Choice Ting Lei , Zhongsheng Hou ,Senior Member, IEEE ,a n dY eR e n Abstract Recent studies have shown that a homogenous urban road network exists a well-defined macroscopic funda-mental diagram (MFD), which can be used for perimeter controlconveniently. Most of the existing perimeter control strategiesare model-based control methods, leading to the result that thecontrol effect may be not good enough if the traffic model is notaccurate. In this paper, a novel data-driven strategy called modelfree adaptive control (MFAC) method is proposed for multi-region perimeter control in order to get rid of the dependency ofthe aforementioned model-based MFD-based perimeter controlmethods. Due to the fact that th e multi-region urban traffic system (MRUTS) is a complex interconnected system, a decentral-ized estimation and decentralized MFAC (DED-MFAC) methodis utilized to deal with the strong-coupled characteristic of thetraffic system. In this framework, MFD is used to determinethe desired accumulations in each region and generate thethroughput data of the urban traffic system, since the acquisitionof trip completion flow is more difficult than accumulations.In addition, route choice is also integrated in the proposed policyto further improve the performance of the urban traffic system.A key advantage of the proposed approach is that it can only use the traffic data instead of the traffic model for real-time perimeter control. The effectiveness of the proposed perimetercontrol scheme is tested in simulation for a multi-region system,and the results show that it is superior to some other commonlyused perimeter control methods. Index Terms Macroscopic fundamental diagram (MFD), decentralized estimation and decentralized model free adaptivecontrol (DED-MFAC), route choice, real-time perimeter control.

## I. I NTRODUCTION

URBAN traffic system is indispensable to people’s life. With the expansion of cities and the improvement of people’s living standard, the vehicles travelling on the urban road increase dramatically. Meanwhile, the contradiction between the growing number of vehicles and limited infrastructure Manuscript received January 23, 2018; revised September 14, 2018 and March 15, 2019; accepted May 31, 2019. Date of publication June 18, 2019; date of current version June 29, 2020. This work was supported in part by the National Natural Science F oundation of China under Grant 61433002 and Grant 61833001, and in part by the Beijing Natural Science Foundation under Grant W17E000020. The Associate Ed itor for this paper was A. Hegyi. (Corresponding author: Ting Lei.) T. Lei and Y . Ren are with the Advanced Control Systems Laboratory, School of Electronic and Informatio n Engineering, Beijing Jiaotong University, Beijing 100044, China (e-mail: 14111049@bjtu.edu.cn; 14111048@ bjtu.edu.cn). Z. Hou was with the Advanced Control Systems Lab, School of Electronic and Information Engineering, Beijin g Jiaotong University, Beijing 100044, China. He is now with the School of Automation, Qingdao University,Qingdao 266071, China (e-mail: zshou@qdu.edu.cn). Digital Object Identifier 10.1109/TITS.2019.2921381becomes progressively prominent. Since the expansion of urban roads and other infrastructures is costly and the available space is limited, traffic control has attracted great interest of researchers and engineers. Up to present, there are alr eady a number of urban traffic control strategies, such as SCOOT [1], SCATS [1], [2], OPAC [3], TUC [4], [5], MPC [6], [7], etc. Most of the existing traffic control methods are based on minimizing the traffic delay, which is not easy to be obtained in practice. Meanwhile,they are difficult to handle the problem of the imbalanced traffic load, which often appears in reality. In recent years, some perimeter control methods are presented to balance the urbantraffic load using macroscopic fundamental diagram (MFD). MFD describes a unimodal, low-scatter relationship between the accumulation and the trip completion flow in homogeneous urban traffic networks. The original idea of MFD was provided in [8], and s imilar approaches were also introduced in [9], [10]. The existence of MFD was verified in the downtown of Yokohama, Japan [11], while a derivation of MFD via traffic flow is presented in [12]. These worksindicated that MFD has the following three properties: (i) some homogeneous urban regions with suitable size approximately exhibit an MFD relating accu mulation to space-mean flow, (ii) there is a robust linear rela tion between the region’s spacemean flow and its trip completion flow (the rate that vehiclesreaching their destinations, inc luding leaving the region and finishing their trips in it), and (iii) although MFD is affected by the infrastructure and control strategies of the regions(see [13], [14]), it is not sensitive to the change of traffic demands. Property (i) is important for modeling purpose as detailed dynamics of individual links and intersections are no longer required. Property (ii) is helpful for monitoring purpose because the average flow can be measured more easilythan the trip completion flow. Property (iii) is applicable for control purpose since the traffic administration can formulate traffic control and management measures without detailedinformation of O-D table. Based on MFD, the perimeter control methods have been designed where the MFD is used to provide the desired volume of traffic accumulation. Perimeter control for single region can be found in [15]-[19]. S tability analysis of perimeter control for two-region networks is treated in [20], [21], and perimeter control for two urban regions is presented in [20], [22], [23]. For a multi-region urban traffic system (MRUTS), a perime-ter feedback regulator with online adaptive optimization is 1524-9050 © 2019 I EEE. Personal u se is perm itted, but republication/redistri bution requires IEEE permission. See https://www.ieee.org/publications/rights/index.html for more information.

<!-- page 2 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2895 presented in [24], a Linear-Quadratic-Integral (LQI) based feedback perimeter control strategy is introduced in [25], and a transfer function based perimeter control scheme can be found in [26]. Some other perimeter control methods for multi-region systems are shown in [27]-[29]. In order to improve the performance of perimeter control for the large-scale urban road network systems, the route guidance is also introduced intoperimeter control [13], [30], and some other route guidance strategies can be found in [31], [32]. The above perimeter control methods are all based on the MFD-based traffic model, in which the homogeneity of each region is required. However, if the urban road network or theregion is heterogeneous, the MFD will be not well-defined, especially under congested condition. It will have high scatter and hysteresis phenomena during the process of formation anddissipation of congestion [33]-[36], and further the inaccurate MFD-based traffic model will lead to the deterioration of the control effects of the above mode l-based perimeter control methods. In order to deal with this issue, some partitioning methods are presented in [37]-[41] to homogenize the het-erogeneous urban road network s. Nonetheless, homogeneous regions are difficult to be partitioned perfectly, and the modeling process of MFD is also arduous, which makes the model-based perimeter control methods hard to be used. Another factor that could lead to the inaccuracy of traffic model is that vehicles always not fully comply with the route guidance. Furthermore, all the traffic information is required to be known to implement the above existing perimeter control methods,such as time-varying traffic demands, route choice ratios, and regional O-D tables, etc., which are difficult to be obtained. Finally, most of the above perimeter control strategies arecentralized control methods, and the internal coupling of multiple-input and multiple-out put (MIMO) nonlinear systems needs to be mathematically described accurately, which is difficult to deal with. Nowadays, the urban transportation system produces numerous traffic data every day, and it will be of great significance to make use of traffic data instead of traffic model to deal with urban traffic problems, which can be realizedby taking advantage of computer and network technology. Thus, the data-driven approaches has been promoted. The data-driven methods have been applied in many aspects of urban traffic field in the last decade, such as traffic flow prediction [42]-[44] and traffic control [45], [46], etc. Forperimeter control, using traffic data for controller designing can avoid all the drawbacks of the model-based methods, such as modeling difficulty, robustness less, etc., so that the trafficcontrol performance can be improved. In recent years, model free adaptive control (MFAC) has been investigated extensively in the data-driven control com-munity. MFAC is originally proposed in [47], and the systematic framework has been shaped and the stability of the closed-loop system has been proved in [48], [49]. MFAC scheme for MIMO systems is also presented and it has been successfully applied in many practical plants, such as freewayramp metering [45], AC/DC microgrids [50], networked nonlinear systems [51], computer communication networks [52], and so on. A key advantage of MFAC is that the modelinformation of the controlled system is no longer needed. Instead, it merely needs the input and output data of the system to design the controller. As the MRUTS is essentially a MIMO nonlinear system, inspired by the above discussion,in this paper the decentralized estimation and decentralized MFAC (DED-MFAC) method [49] is utilized for perimeter control to deal with the coupling of the MRUTS. The main contributions of this paper are as follows. 1) A novel description of coupled MIMO system and a system decomposition scheme for MRUTS are proposed for macroscopic traffic flow perimeter control of the heterogeneous urban road networks. 2) A novel data driven control method called DED-MFAC is first applied to perimeter control for large-scale multiregion complex connected urban traffic system. It only usethe input and output data of the urban road network system to design the perimeter controller. Different from the existing centralized MFAC for MIMO systems, it is implemented with the decentralized estimation and decentralized control manner. The advantages of this method are as below:1) Comparing with the existing MFD-based perimeter control methods, the time-consuming and laborious work of MFD modeling, the precise partitioning of the urban traffic network,and the regional O-D tables, are all avoided in the proposed DED-MFAC perimeter control scheme. Instead, a sketchy partitioning according to geometrical location and other factors for the urban traffic network is enough, since the precise model is not necessity. 2) Comparing with the model-based MIMO perimeter control strategies, the difficulty of urban traffic modeling, the accurate description and treatment for the coupling of complex nonlinear systems for the MRUTS are also avoided. Instead, in this work, the coupling interactions among the different regions are only required to be measurable. In the MRUTS, the physical meaning of the coupling is that the transfer flows among the adjacent regions, which is easyto be measured with the advanced sensors, such as magnetic induction coil, traffic video detector, etc. 3) Additionally, route choice is combined with the proposed perimeter control strategy in order to make it more in line with the actual traffic situation and further enhance the efficiency of the urban traffic system, while the precise route choice ratios are not needed in the process of p erimeter controller design. The rest of this paper is organized as follows. The dynamics for MRUTS is formulated in Section II. In Section III, the DED-MFAC strategy for perimeter control of the MRUTS is described. Section IV depicts the numerical simulationresults of the proposed DED-MFAC method compared with some other commonly used perimeter control strategies. The main conclusions and future works are summarized inSection V . II. T RAFFIC DYNAMICS FOR MULTI -REGION URBAN TRAFFIC NETWORK SYSTEM Assume that there is an urban traffic network Npartitioned

$$
into Nregions, i.e., N={1,2,..., N}, which is diagrammed
$$

in Fig. 1, and that each region has an MFD with trip

<!-- page 3 -->

## 2896 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

#### Fig. 1. An urban road network partitioned into Nregions.

completion flow Gi(ni(k)). In this section, the traffic dynamics for the MRUTS is given here. A. Dynamics of Multi-Region Urban Traffic Networks In order to save space, the first order Eulerian discretization of the urban traffic dynamics is directly given in the following. The traffic dynamics is similar to [13], [30]. It is noteworthy that the traffic model here is only utilized to generate traffic data instead of perimeter controller design. The dynamicsof the multi-region urban traffic network is presented as follows: nf ij(k+1)=⎧ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎪⎩n f ij(k)+T * (qij(k) +\sum g∈Ni,g/∈Nj i∈Vgjugi(k) * Mgij(k) -uij(k) * Mf ij(k)), j∈Ni nf ij(k)+T * (qij(k) +\sum g∈Ni,g/∈Nj i∈Vgjugi(k) * Mgij(k) -\sum h∈Vij,uih(k) * Mihj(k)), j/∈Ni (1)

$$
nij(k)=⎧
$$

⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎩n f

$$
ij(k)+\sum
$$

h∈N\Ni j∈Vihnijh(k), j∈Ni \sum h∈Vijnihj(k), j/∈Ni (2)

$$
Mij(k)=nij(k)
$$

ni(k) * Gi(ni(k)),j∈Ni (3) Mf

$$
ij(k)=nf
$$

ij(k) ni(k) * Gi(ni(k)),j∈Ni (4)

$$
Mijh(k)=nijh(k)
$$

ni(k) * Gi(ni(k)), j∈Ni,h/∈Ni,j∈Vih (5)

$$
Mii(k)=nii(k)
$$

$$
ni(k) * Gi(ni(k)) (6)Mij(k)=Mf
$$

$$
ij(k)+\sum
$$

h/∈Ni j∈VihMijh(k),j∈Ni (7)

$$
nij(k)=nf
$$

ij(k),j/∈Ni (8)

$$
nihj(k)=bihj(k) * nij(k),j/∈Ni,h∈Vij (9)
$$

$$
nii(k)=nf
$$

ii(k) (10)

$$
nii(k+1)=nii(k)+T * (qii(k)
$$

+\sum

$$
j\ne =i,j∈Niuji(k) * Mf
$$

ji(k)-Mii(k)) (11)

$$
ni(k)=nii(k)+\sum
$$

$$
j\ne =inf
$$

ij(k) (12) where the variables are defined as follows: i,j,h,g Symbols representing regions and subsystems, Ni The set of regions neighboring region i, Vij The set of regions that vehicles from region ito region jcan go through next immediately, ni(k) The total number of vehicles travelling in region iat time step k, nij(k) Number of vehicles in region itravelling to region jat time step k, nf ij(k) Number of vehicles in region iwith final destination to region jat time step k, nii(k) Number of vehicles in region iwith destination to itself at time step k, nihj(k) Number of vehicles in region itravelling to t h en e x ti m m e d i a t er e g i o n hwith destination to region jat time step k, qij(k) Exogenous traffic demands generated in region iwith destination to region jat time step k, qii(k) Endogenous traffic demands in region iat time step k, Mij(k) Transfer flow from region ito region jat time step k, Mf ij(k) Transfer flow from region ito region jwith final destination to region jat time step k, Mihj(k) Transfer flow from region ito region hwith final destination to region jat time step k, Mii(k) The internal flow from region iwith destination in itself at time step k, Gi(ni(k)) Trip completion flow for region iat time step k, uij(k) Perimeter control ratio from region ito region jat time step k, bihj(k) The ratio of vehicles in region ichoosing to go through the next immediate region hto reach their destination region jat time step k, T The sampling and the control cycle length. Remark 1: It is noteworthy that the transfer flow Mij(k) and Mf ij(k)are only for j∈Ni.Mij(k)and Mf ij(k)are both equal to 0 for j/∈Ni. Under the effect of perimeter control,

<!-- page 4 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2897 uij(k) * Mij(k),uij(k) * Mf ij(k),a n d uij(k) * Mijh(k)are the actual transfer flows. The perimeter control uij(k)is defined as the ratio of vehicles that can actually transfer from region ito region j, which is relative to the transfer flow under the case of original fixed timing control (i.e., no control, NC) [24]. When the traffic is sufficient, the transfer flow is proportional to the green time ratio of boundary intersections. For simplicity, it isassumed that all the boundary intersections have the same signal period and timing plan [25]. Denote the initial fixed green time ratio of boundary intersections is ω f,a n dt h a t under perimeter control is ωp. Then the physical meaning of

$$
perimeter control input is approximated as uij=ωp/ω f.
$$

It is noticeable that ther e is a boundary capacity between every two neighboring regions. The boundary capacity Cij((nj(k))is considered as below: Cij(nj(k)) =⎧ ⎪⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎪⎩C max ij

$$
if 0\le nj(k)\le α * njam
$$

j Cmin ij-Cmax ij (1-α) * njam j * nj(k)+Cmax ij-α * Cmin ij 1-α, ifα * njam

$$
j\le nj(k)\le njam
$$

j(13) where Cmax ijand Cmin ijrepresent the maximum and the minimum value of the boundary capacity, respectively, and 0 < α< 1.Cmin ijis equal to 0 in [13], [30] for simplification. In reality, however, there is still a very small amount of trip completion flow (i.e., Gj(njam j), such as MFD in the downtown of Yokohama) under this circumstance. Therefore, in this work, Cmin ijis modified to a portion of Gj(njam j),w h i c h is more realistic.

$$
In consideration of the boundary capacity, one has uij(k)\le
$$

Cij((nj(k))/Mij(k). In addition, uij(k)is also limited by the green time ratio. Denote the maximum and minimum green time ratios as ωmax andωmin, respectively. Thus, ug ij,max= ωmax/ω fand ug

$$
ij,min=ωmin/ω fare the theoretical approx-
$$

imation of maximum and minimum perimeter control ratio, respectively. Therefore, the range of perimeter control input is presented below: ug

$$
ij,min\le uij(k)\le min{ug
$$

ij,max,Cij((nj(k))/Mij(k)}(14) B. Route Choice (RC) In the urban traffic system, RC is often used to describe the actual traffic situation [13]. Therefore, the traffic simulation system with route choice can be more closely related to the actual traffic flow status. The RC strategy is shown as follows.

$$
For region j∈Ni, one has bijj(k)=1a n d bihj(k)=0,
$$

which means that vehicles are suggested to enter region jdirectly. Hence, vehicles with destinations in neighboring regions no longer need to go the long way around. For region j/∈Ni, a logit model [53] integrating with Dijkstra’s algorithm [54] for K-shortest paths strategy (similar to [13], [30]) is utilized to calculate the route choice ratioas below: blog it

$$
ihj(k)=eτ/tihj(k)/\sum
$$

h∈Vijeτ/tihj(k)(15)

$$
bihj(k)=β * binit
$$

ihj+(1-β) * blog it ihj(k), j/∈Ni,h∈Vij (16) where the definition of the above variables are listed below: blogit ihj(k)The logit ratio of vehicles from region i with destination to region jchoosing to go through the next immediate region hat time step k, binit ihjThe initial ratio of vehicles from region iwith destination to region jchoosing to go through the nextimmediate region h, t ihj(k) The shortest average travel time for the route from region ito region jvia the next immediate region hat time step k, τ A positive scale parameter, β The rate of drivers who persist in their initial

$$
choices, 0 \le β\le 1.
$$

In fact, the routes those take a lot of time and need to go too far away (for example, region hlocates at the upstream of region iin the direction to region j) are always not chosen by drivers. Therefore, the first Kshortest routes are generally provided for drivers to choose from via (15).

## III. M ETHODOLOGY FRAMEWORK

As shown in the above dynamics (1)-(16), the multi-region urban road network system is a complex interconnected strongcoupled MIMO nonlinear system. The control methods for MIMO nonlinear systems can be utilized for the system, but it will definitely lead to too complex control systemif the model based control methods are used to design the controller, in a sequel, it is difficult to implement. In the next, the MIMO MRUTS is first decomposed into some multiple-input and single-output (MISO) subsystems, then the DEDMFAC for the complex interconnected system is proposed to the perimeter control for the MIMO nonlinear multi-region urban traffic system. A. System Decomposition In this section, the MRUTS is decomposed into NMISO subsystems through the urban road network is divided into N regions, shown in Fig. 1. The whole urban traffic system has Noutputs, that is, the accumulation of each region, and there are two perimeter contro l inputs in each boundary between every two adjacent regions. For subsystem j, the controllable perimeter control inputs are u ij,i∈Nj, and the output is nj. Besides, uji,i∈Nj, are uncontrollable for subsystem j.I tm e a n st h a tt h ei n fl o wo fr e g i o n jis controllable for subsystem j, while the outflow of region jis uncontrollable. Instead, it is controlled by other subsystems.

<!-- page 5 -->

## 2898 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

For the j-th subsystem, when one perimeter control input uijis regarded as the controllable control input, the other perimeter control inputs related to subsystem jare considered as the interconnected influences. The interconnected influence of subsystem hon subsystem j(h∈Nj)consists of two parts. On one hand, ujhleads to the reduction of the output of subsystem j. On the other hand, uhjresults in the increase of it. The interaction of other subsystems acting on subsystem 1 is shown in Fig. 1 as an example. In this example, u21is considered as the controllable perimeter control input of subsystem 1, and other related perimeter control inputs are the interconnected effects of othersubsystems acting on subsystem 1. The same is true for other subsystems. For all the regions h∈N j, the subsystem hhas the interconnected influence on subsystem j, denoted by zhj.F o r

$$
h/∈Nj, one has zhj=0. The physical meaning of zhjis the
$$

increment of vehicles contributed by region hto region j,i . e .

$$
zhj(k)=T * (uhj(k-1) * Mhj(k-1)-ujh(k-1) * Mjh(k-1))
$$

(17)

$$
zij(k)=- T * uji(k-1) * Mji(k-1) (18)
$$

The reason why there is a minus sign “ -” in (18) is that zij means the number of vehicles flowing out of region jto region i, leading to the reduction of nj.S i n c e uijis the controllable perimeter control input of subsystem j, the interconnected influence of subsystem ion subsystem jis only composed ofuji, see (18) and Fig. 1. For subsystem j, the interactions (17)-(18) are uncontrollable but can be measured by traffic detectors. B. Dynamic Linearization for Subsystems After decomposition, each subsystem is still a nonlinear system. Fortunately, an equivalent description of the unknown nonlinear system can be provided by dynamic linearizationdata modeling technique. The dynamic linearization data modeling method is to describe the dynamic data relationship between the changes of all factors affecting the system outputat the current time and the changes of the system output at the next time. It differs from the state space model, but it can replace the functions of the latter. The dynamic linearization data model has three forms [49], [55]: the compact form dynamic linearization (CFDL), the partial form dynamiclinearization (PFDL), and the full form dynamic linearization (FFDL) data model. The time-varying dynamical relationship between the increments of the system output at the nexttime step and that of the control input at the current time step is considered in CFDL data modeling scheme. In PFDL data modeling method, the impacts on the increments of systemoutput at the next time step imposed by the change of control input within a fixed length moving time window at the current time are all taken into consideration. In FFDL data modeling approach, all the effects on the system output increments at the next time step imposed by both the control input incrementsand the system output increments within input-related and output-related fixed length moving time windows at the current time step are fully taken into account. The above three formsof data model are all applicable for the MRUTS. Without loss of generality, CFDL data model is utilized in this paper. Assume that a complex interconnected MIMO nonlinear system consists of Nsubsystems, and the j-th subsystem is described as below: y

$$
j(k+1)=fj(yj(k) , ..., yj(k-nyj),uij(k) ,... , uij(k-nuij),
$$

z1j(k) ,..., z1j(k-nz1j) ,..., zhj(k) ,..., zhj(k-nzhj) ,..., zNj(k) ,..., zNj(k-nzNj)),

$$
i,j,h=1,2,..., N,i,h∈Nj (19)
$$

where uij(k)∈Rand yj(k)∈Rrepresent the controllable control input and the output of subsystem j, respectively.

$$
zhj(k)∈R,h\ne =j, is the measurable interactions of subsystem
$$

hacting on subsystem j.nyj,nuijand nzhjare unknown integers, and fj( ... ) is an unknown nonlinear function, which describes the dynamics of subsystem j. For the multi-region perimeter control problem (1)-(18), writing them with another compact form, it can be rewritten in following equation (20).

$$
nj(k+1)=fj(nj(k),uij(k),zhj(k),), i,h,j=1,..., N
$$

(20) Comparing (19) and (20), we can see that they have the same descriptions, and nyj,nuij,a n d nzhjare all equal to

## 0 in the given multi-region perimeter control problem of this

paper. In order to make the symbol notation simplification, and without loss the rigor, we still use yj(k)to represent nj(k). Define the augmented control input vector of

$$
subsystem jwith respect to uij as uij(k)=
$$

$$
[uij(k),z1j(k) ,..., zhj(k) ,..., zNj(k)]T, h \ne = j,
$$

$$
i,j,h=1,..., N,zhj(k)=0i f h/∈Nj.T h e j-th
$$

subsystem (19) can be rewritten as

$$
yj(k+1)=fj(yj(k) ,..., yj(k-nyj),uij(k) , ..., uij(k-nuij))
$$

(21)

$$
where nuij=max{nuij,nz1j,..., nzhj,..., nzNj},h\ne =j,
$$

$$
i,j,h=1,..., N.
$$

The augmented control input vector of each subsystem j is composed of the controllable perimeter control uijand the measurable interactions from other subsystems. It is noted that the following two assumptions are satisfied for the considered complex interconnected MRUTS. Assumption 1: The partial derivatives of fj( ... ) with respect to each component of the control vector uij(k)are continuous. Assumption 2: Each subsystem (21) is generalized Lipschitz,

$$
i.e.,/vextenddouble/vextenddoubleyj(k1+1)-yj(k2+1)/vextenddouble/vextenddouble\le b/vextenddouble/vextenddoubleuij(k1)-uij(k2)/vextenddouble/vextenddoublefor
$$

$$
allk1\ne =k2,k1,k2>0a n d uij(k1)\ne =uij(k2),w h e r e yj(kp+
$$

1)=f(yj(kp) ,..., yj(kp-nyj),uij(kp) ,..., uij(kp-nuij)),

$$
p=1,2, and bis a positive constant.
$$

Remark 2: For the urban traffic system, assumption 1 is easy to be verified from the dynamics of the MRUTS (1)-(20), and meanwhile it is also a typical assumption for controller design for nonlinear systems. Assumption 2 is a physical constraint by the inherent nature of urban traffic system, i.e., finite change ofvehicle flow does not lead to infinite change of the number of vehicles in a region. Meanwhile, it is also a physical constraint of the real system from the energy point of view.

<!-- page 6 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2899 Theorem 1 [49]: Consider the nonlinear subsystem j,s a t -

$$
isfying the assumptions 1 and 2 and/vextenddouble/vextenddouble/Delta1uij(k)/vextenddouble/vextenddouble\ne =0, there
$$

must exist a pseudo gradient (PG) denoted by φij(k),s u c h that the subsystem (21) can be transformed into the followingequivalent CFDL data model: /Delta1y j(k+1)=φT ij(k)/Delta1uij(k) (22)

$$
where φij(k)=[φij(k),ϕ 1j(k) ,...,ϕ hj(k) ,...,ϕ Nj(k)]T,
$$

$$
h\ne =j,i,j,h=1,..., N, is the PG of the subsystem j
$$

$$
with respect to uij,/Delta1yj(k+1)=yj(k+1)-yj(k),a n d
$$

$$
/Delta1uij(k)=uij(k)-uij(k-1).
$$

Remark 3: It can be seen from (22) that the change of the j-th subsystem’s output /Delta1yj(k+1)is not only related to the change of the controllable control input of subsystem j(i.e., uij(k)), but also influenced by the change of the interactions from other subsystems, which are depicted by

$$
φij(k)/Delta1uij(k)andN\sum
$$

$$
h=1,h\ne =jϕhj(k) * /Delta1zhj(k), respectively. The
$$

latter item fully illustrates the impact of other subsystems acting on subsystem j. In the MRUTS, the physical meaning of the above discussion is that the change of the accumulations in region jis not only related to the change of the controllable perimeter control ratio uij(k), which controls the inflow from the corresponding region i, but also associated with the change of the inflow from and the outflow to other regions, which aremeasurable. C. DED-MF AC Perimeter Controller Design For the convenience of reading, a brief description for DEDMFAC is introduced here. After CFDL for the MISO nonlinear subsystem j, the perimeter control of DED-MFAC scheme is designed as follows. The objective function for estimating PG is as follows: J

$$
j(φij(k))=/vextendsingle/vextendsingle/vextendsingleyj(k)-yj(k-1)-φT
$$

ij(k)/Delta1uij(k-1)/vextendsingle/vextendsingle/vextendsingle2 +μ/vextenddouble/vextenddouble/vextenddoubleφ ij(k)-ˆφij(k-1)/vextenddouble/vextenddouble/vextenddouble2 (23) where μ> 0 is a weighting factor to penalize excessive change of the estimation of the PG. PG updating algorithm is then designed by minimizing (23) via some modifications with consideration of practical applications:

$$
ˆφij(k)=ˆφij(1),if/vextendsingle/vextendsingle/vextendsingleˆφij(k)/vextendsingle/vextendsingle/vextendsingle<εorsign(ˆφij(k))\ne =sign(ˆφij(1))
$$

(25)

$$
ˆϕhj(k)=ˆϕhj(1),if/vextendsingle/vextendsingleˆϕhj(k)/vextendsingle/vextendsingle<εorsign(ˆϕhj(k))\ne =sign(ˆϕhj(1))
$$

(26) where ˆφij(1)andˆϕhj(1)are the initial values of ˆφij(k)and

$$
ˆϕhj(k),h\ne =j,i,j,h=1,..., N, respectively, and ˆφij(k)is
$$

the estimation of φij(k). The objective function for perimeter control input design is as follows:

$$
Jj(uij(k))=/vextendsingle/vextendsingle/vextendsingley∗
$$

j(k+1)-yj(k+1)/vextendsingle/vextendsingle/vextendsingle2 +ζλj/vextendsingle/vextendsingleuij(k)-uij(k-1)/vextendsingle/vextendsingle2(27)where y∗ j(k+1)(i.e., n∗ j(k+1))is the desired output signal of subsystem j, which represents the expected number of vehicles in region j.λj>0 is a weighting constant to penalize excessive changes of the control i nput signal, i.e., the perimeter control ratios should not change too fast. This is the practical consideration for traffic control. If the green light time of the two consecutive cycles changes too fast, it will result in somerisk of safety. ζis a factor that makes the order of magnitude of the two items in (27) are in the same level. Substituting (22) into (27), then differentiating it with respect to u ij(k), and letting it zero, gives the perimeter control ratio as below: where η∈(0,2]andρ∈(0,1]are step-size constants, andεis a positive constant. (29) is extra added in the control input algorithm for practical consideration of traffic controlapplication, which has the same functions as (14) to deal with the actual traffic situation. The DED-MFAC scheme consists of (24)-(26) and (28)-(29), shown at the top of the next page, where the reset mechanism (25)-(26) are designed to make the parameterestimation algorithm (24), shown at the top of the next page, have stronger ability for trackin g time-varying parameters of the traffic system. For other discussions on the DED-MFACscheme, please refer to [49] for details. The outstanding features of the proposed DED-MFAC scheme are as follows: 1) Since that the MIMO nonlinear urban traffic system is decomposed to Nsubsystems, and each subsystem is a MISO nonlinear system with only one controllable input and N-1 uncontrollable inputs, in which the latter is regarded as the interconnected actions from other subsystems. Fortunately,it has no difficulty for traffic practice since these influences are easily measured using geomagnetic coil or video detector. The interactions among the subsystems are compensated via the last item in the numerator of the second item on the right side of the equal sign in (28), so that the internal couplingof the MIMO nonlinear systems can be addressed by the DED-MFAC approach. By establishing CFDL data model with measurable interactions and designing MFAC scheme foreach subsystem, the decentralized estimation and decentralized control for the whole MRUTS is realized. 2) The proposed DED-MFAC perimeter control strategy is independent of the mathematical model of the urban traffic system. Instead, only the input and output data of the urbantraffic system (i.e., the perimeter control ratios at the last time and the accumulations at the current time) are needed in the process of perimeter controller design. Besides, thereis no unmodeled traffic system dynamics in the proposed DED-MFAC scheme, and the structure and the orders of the mathematical model of the urban traffic system are both nolonger required to be known. Furthermore, the DED-MFAC method does not need any training process or satisfy the persistence excitation conditions, which are usually necessary for other adaptive control methods [26], [27] for urban traffic control. 3) There are different limitations in other typical linearization methods for perimeter control. For instance, the highorder terms are ignored for the Taylor’s linearization [25],

<!-- page 7 -->

## 2900 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

$$
ˆφij(k)= ˆφij(k-1)+η/Delta1uij(k-1)(yj(k)-yj(k-1)-ˆφT
$$

ij(k-1)/Delta1uij(k-1)) μ+/vextenddouble/vextenddouble/Delta1uij(k-1)/vextenddouble/vextenddouble2(24)

$$
uij(k)=uij(k-1)+ρˆφij(k)(y∗
$$

$$
j(k+1)-yj(k)-N\sum
$$

$$
h=1,h\ne =jˆϕhj(k)/Delta1zhj(k))
$$

ζλj+ˆφ2 ij(k)(28)

$$
uij(k)=⎧
$$

⎪⎪⎪⎪⎪⎪⎪⎪⎨ ⎪⎪⎪⎪⎪⎪⎪⎪⎩u g ij,min, ifuij(k)< ug ij,min uij(k), ifug

$$
ij,min\le uij(k)\le min{ug
$$

ij,max,Cij((nj(k))/Mij(k)} min{ug ij,max,Cij((nj(k))/Mij(k)}, ifuij(k)>min{ug ij,max,Cij((nj(k))/Mij(k)}(29) more model information of the urban traffic system is required for the piecewise linearization [22], such as the switching and residence time of the piecewise linearized dynamics of the urban traffic system. Further, they are both difficult to handle the parameter uncertainties o r disturbances in MFD, demand, and accumulation meas urement, etc. Different from the above existing linearization methods, an equivalent description of the original MIMO urban traffic system is provided by CFDL data model, in which only the input and output data of the MRUTSis needed, and the system dynamics is no longer required. 4) The existence of the PG is guaranteed by rigorous mathematical analysis [49]. Meanwhile, the CFDL data model is very simple since the PG is easily estimated by using the urban traffic system measurement data, without heavy computationalburden. Finally, since the PG is a differential signal in some sense, and is a slowly time-vary ing parameter for the practical traffic system, thus it is insensitive to the time-varying factorsof the urban traffic system, such as accumulations, demands, etc. These features will make the DED-MFAC method have strong robustness. However, if the MIMO system cannot be decomposed into subsystems with measurable interactions, or the system is toocomplex that it cannot be separated into Nsubsystems, then the proposed control method will no longer work well. This is the main limitation of the proposed method. IV . S IMULATION RESULTS Two cases are simulated to te st the performance of the proposed DED-MFAC strategy for the multi-region perime-ter control problem. In case I, the measurement noises in demands, accumulations, and MF Ds are integrated to test the effectiveness of the proposed perimeter control strategy withuncertainties in the traffic model. In addition, no control (NC) [24] and model predictive control (MPC) [22], [30] are also applied to the MRUTS under the same condition with the same route choice strategy to verify the superiority of DEDMFAC perimeter control strategy. In case II, the measurementnoises are also added to the measurable interactions under DED-MFAC strategy to further study the robustness of it.In the simulation, the following MFD-based urban traffic model is only used to produce the traffic data, rather than in the process of perimeter controller design. A. The Setting of Parameters and Traffic Demands The urban traffic network is partitioned into five regions

$$
(i.e., N=5) in the simulation. Region 1 is at the center of
$$

the city, while region 2-5 are on the periphery. In order to make the simulation simple and time-saving, it is assumed that the structure of MFD in each region is the same, while the parameters are different. Region 2-5 have the same MFD as the one in the downtown of Yokohama [11], [22], while theMFD of region 1 is 1.2 times as the ones in other regions. The trip completion flow G i(ni(k))is approximately formulated as a third-order polynomial function of ni(k),i . e . Gi(ni(k)) =⎧ ⎪⎪⎪⎨ ⎪⎪⎪⎩(1.7852 * 10 -7 * ni(k)3-3.5022 * 10-3 * ni(k)2

$$
+18.1094 * ni(k))/3600,i=1.
$$

(1.4877 * 10-7 * ni(k)3-2.9185 * 10-3 * ni(k)2

$$
+15.0912 * ni(k))/3600,i=2,3,4,5.(30)
$$

where ncr

$$
i=3400(veh),Gi(ncr
$$

i)=6.3(veh/s),njam i=

## 10000 (veh),a n d Gi(njam

$$
i)=0.43(veh/s),i=2,3,4,5,
$$

while for region 1, one has G1(ncr 1)=7.56(veh/s)and G1(njam 1)=0.52(veh/s), and the other MFD parameters are the same as the ones in the MFD of region 2-5. The parametersof boundary capacity are α=0.64, C max

$$
ij=3.2(veh/s)
$$

[30], and Cmin

$$
ij=0.15(veh/s)for j=2,3,4,5a n d
$$

i∈Nj, while for region 1, the corresponding parameters are Cmax

$$
i1=3.84(veh/s)and Cmin
$$

$$
i1=0.18(veh/s),i\ne =1,
$$

respectively. The initial number of vehicles are: n1(0)=5000, n2(0)= 4000, n3(0)=4000, n4(0)=4000, and n5(0)=4000, respectively. All the regions are initially congested according to the definition of MFD, since region iis congested when the accumulation is greater than ncr i. The initial conditions are set up to simulate the actual situation of morning peak. The initial

<!-- page 8 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2901

#### Fig. 2. Traffic demands for each pair of regions during the whole simulation period.

$$
green time ratio is ωf=0.5, while the maximum and the
$$

$$
minimum green time ratios are ωmax=0.9a n d ωmin=0.1,
$$

respectively. According to the definition of perimeter control ratio, one has ug

$$
ij,max=1.8a n d ug
$$

$$
ij,min=0.2.
$$

The initial route choice ratios are binit

$$
i1j=0.8a n d binit
$$

ihj=0.1

$$
respectively, i,j,h=2,3,4,5,h∈Vij. Other parameters of
$$

$$
route choice are τ=50000, β=0.3, and K=3, respectively.
$$

The measurement noises in the accumulations, demands, MFDs, and measurable interactions obey normal and uniform distribution, respectively, which are presented as follows:

$$
˜ni(k)=ni(k) * (1+N(0,σ2
$$

ni)) (31)

$$
˜qij(k)=qij(k) * (1+N(0,σ2
$$

qij)) (32)

$$
˜Gi(ni(k))=Gi(ni(k)) * (1+U(-αGi,α Gi)) (33)
$$

$$
˜zij(k)=zij(k) * (1+N(0,σ2
$$

zij)) (34) where the error parameters are chosen as σ2

$$
ni=0.1,σ2
$$

$$
qij=0.1,
$$

$$
andαGi=0.35 in both cases, respectively. In the second case,
$$

the additional noise parameter of the measurable interactions is selected as σ2

$$
zij=0.1.
$$

The simulation duration is set as 4 hours including the morning peak hour, and the signal cycle length of the boundaryintersections is set as 120s, while the control cycle length is

$$
T=240s, which is the common multiple of the signal cycle
$$

length for control convenience. Then the 4 hours of simulationduration is divided into 60 time steps (i.e., k

$$
end=60).
$$

The time-varying traffic demands are shown in Fig. 2 to simulate the real traffic situation in the morning peak hour. Thesimulation is based on MATLAB, and the CPU configuration is Intel(R) Core(TM) i7-6700HQ, 2.60GHz. The following four evaluation indicators, i.e., the total network throughput (TNT) for the entire urban road network, the total time spent (TTS) and the average traveltime (ATT) for all vehicles, and the total CPU time (TCT), are utilized to evaluate the effectiveness of the perimeter

$$
control methods. The first three indicators are defined asfollows: TNT =T *
$$

$$
kend\sum
$$

$$
k=1N\sum
$$

$$
i=1Mii(k),TTS=T * kend\sum
$$

$$
k=1N\sum
$$

$$
i=1ni(k),
$$

$$
and AT T=TTS
$$

TN T, respectively, and TCT means the total time for calculating the perimeter control inputs during the simu-lation. Under the same initial condition and traffic demands, the more TTP, and the less TTS, ATT, and TCT, the better performance the perimeter control strategy has. B. Perimeter Control Methods 1) DED-MF AC: In the proposed DED-MFAC strategy, the estimated value of the PGs and the perimeter control ratios are obtained via (24)-(26) and (28)-(29), respectively. The urban traffic model (1)-(16) are utilized to generate the urban traffic data, instead of controller design. The desired output of each subsystem iis chosen as 0 .98 * n cr iin order to make the trip completion flow near the maximum value without

$$
congestion. Other parameters are: ζ=1000, λi=10,η=1,
$$

ρ=1, and μ=1, respectively. 2) No Control (NC): In the case of NC, the perimeter control ratio uijis constant to 1 [24]. NC is served as a benchmark for comparing the perimeter control effects. 3) Model Predictive Control (MPC): MPC [22], [30] is a frequently used perimeter control method benefiting from its excellent control performance in the case of models are precisely known. In this paper, MPC serves as a model based traffic control method for the performance comparison. Theurban traffic model proposed in Section II is utilized to design the MPC perimeter controller. The objective functions and the constraints of the MPC strategy are the same as the ones in[22]. The predictive horizon and the control horizon are chosen asN

$$
p=3a n d Nc=2, respectively.
$$

C. Simulation Results 1) Case I: The simulation results under case I are presented in Fig. 3-5 and the first three lines of Table I respectively.

<!-- page 9 -->

## 2902 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

#### TABLE I

EVA L UAT I O N RESULTS OF DIFFERENT STRATEGIES UNDER DIFFERENT CASES

#### Fig. 3. Result of NC strategy under case I: (a) evolution of accumulation in each region; (b) perimeter control input of NC; (c) trip completion flow for

each region; (d) ratio of route choice.

#### Fig. 4. Result of MPC strategy under case I: (a) evolution of accumulation i n each region; (b) perimeter control i nput of MPC; (c) trip completion flow fo r

each region; (d) ratio of route choice. The evolution of accumulations in the five regions under different perimeter control strategies are depicted inFig. 3 (a) -Fig. 5 (a), respectively. It can be seen from

#### Fig. 3 (a) that there was a long period of jam phenomenonin 3 of the 5 regions under NC strategy. MPC worked better

than NC, since that there was only one region congested atthe end of the morning peak, while the other 4 regions were well operated since the accumulations of them were changing

<!-- page 10 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2903

#### Fig. 5. Result of DED-MFAC strategy under case I: (a) evolution of accumu lation in each region; (b) perimeter control input of DED-MFAC; (c) trip

completion flow for each region; (d) ratio of route choice.

#### Fig. 6. Result of DED-MFAC strategy under case II: (a) evolution of accumu lation in each region; (b) perimeter control input of DED-MFAC; (c) trip

completion flow for each region; (d) ratio of route choice. around the critical values, see Fig. 4 (a). On the contrary, it can be seen from Fig. 5 (a) that all the five regions were nolonger congested all the way under DED-MFAC approach, and the accumulations in each region kept near the desired values during the peak hour. The time-varying perimeter control ratiosand route choice ratios of the above strategies are displayed in Fig. 3 (b) -Fig. 5 (b) and Fig. 3 (d) -Fig. 5 (d), respectively. The trip completion flows for the regions under each perimeter control strategy are shown in Fig. 3 (c) -Fig. 5 (c), respectively. As depicted in the figures, the trip completionflows maintained at a relatively high level under DED-MFACstrategy during the morning peak since the accumulations in each region were near the expected values, while fewervehicles in the congested regions could finish their trips under the other strategies because of th e fact that the trip completion flow will decrease when the accumu lation is greater than the critical value. The first three lines of Table I indicate that DED-MFAC is superior to other strategies for the multi-region perimeter control problem, as the TNT is greater than others, while the TTS, ATT, and TCT are less than other perimeter controlstrategies.

<!-- page 11 -->

## 2904 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 21, NO. 7, JULY 2020

2) Case II: The simulation results of case II are presented in Fig. 6 and the last line of Table I, respectively. It can be seen from Fig. 6 (a) that although the noises were added into the measurable interactions, the number of vehicles ineach region were still operated near the expected values, and the trip completion flows of the five regions still remained near their maximum values, see Fig. 6 (c). The perimetercontrol inputs and the route choice ratios under this case are depicted in Fig. 6 (b) and (d ), respectively. The last line of Table I reveals that the proposed DED-MFAC perimeter control method is also superior to other strategies in spite of the uncertainties in the measurable interactions. Meanwhile,it is noteworthy that the total CPU time 0.48s of DED-MFAC for calculating the control inputs is much smaller than the signal cycle 120s, which implies that it can be implementedin real time. V. C ONCLUSION A novel data driven approach called DED-MFAC is first applied to deal with the problem of perimeter control for multi-region urban traffic network systems in this paper. The DED-MFAC scheme includes the following three parts: Firstly,the MIMO nonlinear multi-region urban traffic system is decomposed into NMISO subsystems. Secondly, CFDL data model for each subsystem is established. Finally, the PG estimation and perimeter controller design for each subsystem are proposed respectively. A remarkable advantage of theproposed method is that only the input and output data of the urban traffic system is n eeded to design the perimeter controller, and the urban tra ffic model is no longer required. The superiority and effectiveness of the proposed method are verified by comparison with MPC method via simulation. The results revealed that the performance of DED-MFAC strategy is superior to other methods with measurement noises in demands, accumulations, and MFDs, even when measurementnoises appear in the interactions. In the future work, we will focus on how to determine the desired number of vehicles in each region or in eachlink or even for an intersection via urban traffic big data directly. Meanwhile, we will try to make it implemented in some regions in Beijing. R EFERENCES [1] D. I. Robertson and R. D. Brethert on, “Optimizing networks of traffic signals in real time-the SCOOT method,” IEEE Trans. Veh. Technol. , vol. 40, no. 1, pp. 11-15, Feb. 1991. [2] P. Lowrie, “The Sydney coordinated a daptive traffic system: Principles, methodology, algorithms,” in Proc. Int. Conf. Road Traffic Signalling , Mar. 1982, pp. 67-70. [3] H. Chen, S. L. Cohen, and N. H. Gartner, “Simulation study of OPAC: A demand-responsive strategy for traffic signal control,” in Transportation and Traffic Theory . New York, NY , USA: Elsevier, 1987, pp. 233-249. [4] C. Diakaki, M. Papageorgiou, and K. Aboudolas, “A multivariable regulator approach to traffic-respons ive network-wide signal control,” Control Eng. Pract. , vol. 10, no. 2, pp. 183-195, Feb. 2002. [5] K. Aboudolas, M. Papageorgiou, and E. Kosmatopoulos, “Store-andforward based methods for the signal control problem in large-scale congested urban road networks,” Transp. Res. C, Emerg. Technol. , vol. 17, no. 2, pp. 163-174, Apr. 2009. [6] S. Lin, B. De Schutter, Y . Xi, and H. Hellendoorn, “Fast model predictive control for urban road networks via MILP,” IEEE Trans. Intell. Transp. Syst. , vol. 12, no. 3, pp. 846-856, Sep. 2011.[7] M. Hajiahmadi et al. , “Integrated predictive control of freeway networks using the extended link transmission model,” IEEE Trans. Intell. Transp. Syst. , vol. 17, no. 1, pp. 65-78, Jan. 2016. [8] J. W. Godfrey, “The mechanism of a road network,” Traffic Eng. Control , vol. 11, no. 7, pp. 323-327, 1969. [9] R. Herman and I. Prigogine, “A two-fluid approach to town traffic,” Science , vol. 204, no. 4389, pp. 148-151, 1979. [10] C. F. Daganzo, “Urban gridlock: Macroscopic modeling and mitigation approaches,” Transp. Res. B, Methodol. , vol. 41, no. 1, pp. 49-62, 2007. [11] N. Geroliminis and C. F. Daganzo, “Existence of urban-scale macroscopic fundamental diagrams: S ome experimental findings,” Transp. Res. B, Methodol. , vol. 42, no. 9, pp. 759-770, Nov. 2008. [12] D. Helbing, “Derivation of a funda mental diagram for urban traffic flow,” Eur. Phys. J. B , vol. 70, no. 2, pp. 229-241, Jul. 2009. [13] M. Ramezani, J. Haddad, and N. Geroliminis, “Dynamics of heterogeneity in urban networks: Aggregat ed traffic modeling and hierarchical control,” Transp. Res. B, Methodol. , vol. 74, pp. 1-19, Apr. 2015. [14] L. Zhang, T. M. Garoni, and J. de Gier, “A comparative study of macroscopic fundamental diagrams of arterial road networks governed by adaptive traffic signal systems,” Transp. Res. B, Methodol. , vol. 49, no. 1, pp. 1-23, 2013. [15] M. Keyvan-Ekbatani, A. Kouvelas, I. Papamichail, and M. Papageorgiou, “Exploiting the fundamental diagram of urban networks for feedbackbased gating,” Transp. Res. B, Methodol. , vol. 46, no. 10, pp. 1393-1403, Dec. 2012. [16] M. Keyvan-Ekbatani, R. C. Carlson, V . L. Knoop, S. P. Hoogendoorn, and M. Papageorgiou, “Queuing under perimeter control: Analysisand control strategy,” in Proc. IEEE 19th Int. Conf. Intell. Transp. Syst. (ITSC) Board Annu. Meeting , Rio de Janeiro, Brazil, Nov. 2016, pp. 1502-1507. [17] M. Keyvan-Ekbatani, M. Papageorgiou, and V . L. Knoop, “Controller design for gating traffic control in presence of time-delay in urban road networks,” Transp. Res. C, Emerg. Technol. , vol. 59, pp. 308-322, Oct. 2015. [18] J. Haddad, “Optimal coupled and d ecoupled perimeter control in oneregion cities,” Control Eng. Pract. , vol. 61, pp. 134-148, Apr. 2017. [19] J. Haddad and A. Shraiber, “Ro bust perimeter control design for an urban region,” Transp. Res. B, Methodol. , vol. 68, pp. 315-332, Oct. 2014. [20] J. Haddad and N. Gerolimins, “On the stability of traffic perimeter control in two-region urban cities,” Transp. Res. B, Methodol. , vol. 46, no. 1, pp. 1159-1176, 2012. [21] V . V . Gayah, X. S. Gao, and A. S. Nagle, “On the impacts of locally adaptive signal control on urban network stability and the macroscopic fundamental diagram,” Transp. Res. B, Methodol. , vol. 70, pp. 255-268, Dec. 2014. [22] N. Geroliminis, J. Haddad, and M. Ramezani, “Optimal perimeter control for two urban regions with m acroscopic fundamental diagrams: A model predictive approach,” IEEE Trans. Intell. Transp. Syst. , vol. 14, no. 1, pp. 348-359, Mar. 2013. [23] J. Haddad, “Optimal perimeter c ontrol synthesis for two urban regions with aggregate boundary queue dynamics,” Transp. Res. B, Methodol. , vol. 96, pp. 1-25, Feb. 2017. [24] A. Kouvelas, M. Saeedmanesh, and N. Geroliminis, “Enhancing model-based feedback perimeter cont rol with data-driven online adaptive optimization,” Transp. Res. B, Methodol. , vol. 96, pp. 26-45, Feb. 2017. [25] K. Aboudolas and N. Geroliminis , “Perimeter and boundary flow control in multi-reservoir heterogeneous networks,” Transp. Res. B, Methodol. , vol. 55, pp. 265-281, Sep. 2013. [26] J. Haddad and B. Mirkin, “Adap tive perimeter traffic control of urban road networks based on MFD model with time delays,”Int. J. Robust Nonlinear Control , vol. 26, no. 6, pp. 1267-1285, Apr. 2016. [27] J. Haddad and B. Mirkin, “Coordina ted distributed adaptive perimeter control for large-scale urban road networks,” Transp. Res. C, Emerg. Technol. , vol. 77, pp. 495-515, Apr. 2017. [28] M. Hajiahmadi, J. Haddad, B. De Schutter, and N. Geroliminis, “Optimal hybrid perimeter and switching plans c ontrol for urban traffic networks,” IEEE Trans. Control Syst. Technol. , vol. 23, no. 2, pp. 464-478, Mar. 2015. [29] M. Keyvan-Ekbatani, M. Yildirimoglu, N. Geroliminis, and M. Papageorgiou, “Multiple concentric gating traffic control in largescale urban networks,” IEEE Trans. Intell. Transp. Syst. , vol. 16, no. 4, pp. 2141-2154, Aug. 2015.

<!-- page 12 -->

LEI et al. : DATA DRIVEN MODEL FREE ADAPTIVE PERIMETER CONTROL FOR MULTI-REGION URBAN TRAFFIC NETWORKS 2905 [30] I. I. Sirmatel and N. Geroliminis, “Economic model predictive control of large-scale urban road networks via perimeter control and regional route guidance,” IEEE Trans. Intell. Transp. Syst. , vol. 19, no. 4, pp. 1112-1121, Apr. 2016. [31] M. Yildirimoglu and N. Geroliminis, “Approximating dynamic equilibrium conditions with macros copic fundamental diagrams,” Transp. Res. B, Methodol. , vol. 70, pp. 186-200, Dec. 2014. [32] M. Yildirimoglu, M. Ramezani, and N. Geroliminis, “Equilibrium analysis and route guidance in large-scale networks with MFD dynamics,” Transp. Res. C, Emerg. Technol. , vol. 59, pp. 404-420, Oct. 2015. [33] C. Buisson and C. Ladier, “Exploring the impact of homogeneity of traffic measurements on the existence of macroscopic fundamental diagrams,” Transp. Res. Rec., J. Transp. Res. Board , vol. 137, no. 2124, pp. 127-136, 2009. [34] A. Mazloumian, N. Geroliminis, and D. Helbing, “The spatial variability of vehicle densities as determinant of urban network capacity,” Philos. Trans. Roy. Soc. A, Math., Phys., Eng. Sci. , vol. 368, no. 1928, pp. 4627-4647, Oct. 2010. [35] V . V . Gayah and C. F. Daganzo, “Clockwise hysteresis loops in the macroscopic fundamental diagram: An effect of network instability,”Transp. Res. B, Methodol. , vol. 45, no. 4, pp. 643-655, 2011. [36] N. Gerolimins and J. Sun, “Hyste resis phenomena of a macroscopic fundamental diagram in freeway networks,” Transp. Res. A, Policy Pract. , vol. 45, no. 9, pp. 966-979, 2011. [37] Y . Ji and N. Geroliminis, “On the spatial partitioning of urban transportation networks,” Transp. Res. B, Methodol. , vol. 46, no. 10, pp. 1639-1656, Dec. 2012. [38] M. Saeedmanesh and N. Geroliminis, “Clustering of heterogeneous networks with directional flows based on ‘Snake’ similarities,” Transp. Res. B, Methodol. , vol. 91, pp. 250-269, Sep. 2016. [39] K. An, Y .-C. Chiu, X. Hu, and X. Chen, “A network partitioning algorithmic approach for macroscopic fundame ntal diagram-based hierarchical traffic network management,” IEEE Trans. Intell. Transp. Syst. , vol. 19, no. 4, pp. 1130-1139, Apr. 2018. [40] C. Lopez, P. Krishnakumari, L. Leclercq, N. Chiabaut, and H. van Lint, “Spatiotemporal partitioning of transportation network using travel time data,” Transp. Res. Rec. J. Transp. Res. Board , vol. 2623, pp. 98-107, Jan. 2017. [41] M. Saeedmanesh and N. Geroliminis, “Dynamic clustering and propagation of congestion in heterogeneously c ongested urban traffic networks,” Transp. Res. B, Methodol. , vol. 105, pp. 193-211, Nov. 2017. [42] A. Abadi, T. Rajabioun, and P. A. Ioannou, “Traffic flow prediction for road transportation networks with limited traffic data,” IEEE Trans. Intell. Transp. Syst. , vol. 16, no. 2, pp. 653-662, Apr. 2015. [43] Y . Lv, Y . Duan, W. Kang, Z. Li, and F.-Y . Wang, “Traffic flow prediction with big data: A deep learning approach,” IEEE Trans. Intell. Transp. Syst. , vol. 16, no. 2, pp. 865-873, Apr. 2015. [44] Z. S. Hou and X. Y . Li, “Repeatability and similarity of freeway traffic flow and long-term prediction under big data,” IEEE Trans. Intell. Transp. Syst. , vol. 17, no. 6, pp. 1786-1796, Jun. 2016. [45] R.-H. Chi and Z.-S. Hou, “A model-free periodic adaptive control for freeway traffic density via ramp metering,” ACTA Automat. Sinica , vol. 36, pp. 1029-1033, Jul. 2010. [46] F.-Y . Wang, “Parallel control and ma nagement for intelligent transportation systems: Concepts, architectures, and applications,” IEEE Trans. Intell. Transp. Syst. , vol. 11, no. 3, pp. 630-638, Sep. 2010. [47] Z. S. Hou, “The parameter identifi cation, adaptive control and model free learning adaptive control for nonlinear systems,” (in Chinese), Ph.D. dissertation, Northeas tern Univ., Shenyang, China, 1994. [48] Z. Hou and S. Jin, “Data-driven model-free adaptive control for a class of MIMO nonlinear discrete-time systems,” IEEE Trans. Neural Netw. , vol. 22, no. 12, pp. 2173-2188, Dec. 2011. [49] Z. Hou and S. Jin, Model Free Adaptive Control: Theory and Applications . Boca Raton, FL, USA: CRC Press, 2013. [50] H. Zhang, J. Zhou, Q. Sun, J. M. Guerrero, and D. Ma, “Datadriven control for interlinked AC/DC microgrids via model-free adaptivecontrol and dual-droop control,” IEEE Trans. Smart Grid , vol. 8, no. 2, pp. 557-571, Dec. 2015. [51] Z.-H. Pang, G.-P. Liu, D. Zhou, an d D. Sun, “Data-based predictive control for networked nonlinear systems with network-induced delay and packet dropout,” IEEE Trans. Ind. Electron. , vol. 63, no. 2, pp. 1249-1257, Feb. 2016. [52] W. Chu, X. Guan, Z. Cai, and L. Gao, “Real-time volume control for interactive network traffic replay,” Comput. Netw. , vol. 57, no. 17, pp. 1611-1629, May 2013.[53] M. Ben-Akiva and M. Bierlaire, “Discrete choice methods and their applications to short term travel decisions,” in Handbook of Transportation Science . New York, NY , USA: Springer, 1999, pp. 5-33. [54] E. W. Dijkstra, “A note on two problems in connexion with graphs,” Numer. Math. , vol. 1, no. 1, pp. 269-271, Dec. 1959. [55] Z. Hou and S. Xiong, “On model free adaptive control and its stability analysis,” IEEE Trans. Auto. Control , to be published. [Online]. Available: https://ieeexplore.ieee.org/document/8621060 Ting Lei received the bachelor’s degree from Zhengzhou University, Zhengzhou, China, in 2012. He is currently pursuing the Ph.D. degree withthe Advanced Control Systems Laboratory, Beijing Jiaotong University, Beijing, China. His current research intere sts include urban transportation systems, data-driven control, and optimiza-tion and control of large scale networks. Zhongsheng Hou (SM’13) received the B.S. and M.S. degrees from the Jilin University of Technol-ogy, Jilin, China, in 1983 and 1988, respectively, and the Ph.D. degree from Northeastern University, Shenyang, China, in 1994. From 1995 to 1997, he was a Post-Doctoral Fellow with the Harbin Institute of Technology, Harbin, China. From 2002 to 2003, he was a Visiting Scholar with Yale University, New Haven, CT, USA. From1997 to 2018, he was with Beijing Jiaotong University, Beijing, China, where he was a Distinguished Professor and the Founding Director of the Advanced Control Systems Lab,and the Head of the Department of Automatic Control. He is currently aChair Professor with the School of Auto mation, Qingdao University, Qingdao, China. His research interests are in the fields of data-driven control, model-free adaptive control, learning control, and intelligent transportation systems. Untilnow, he has authored or coauthored over 180 peer-reviewed journal papers and over 140 papers in prestigious conference proceedings. He has authored two monographs, Nonparametric Model and Its Adaptive Control Theory (Science Press) (in Chinese) in 1999, and the Model Free Adaptive Control: Theory and Applications (CRC Press, 2013). His pioneerin g work on model-free adaptive control has been verified in over 160 diff erent field applications, laboratory equipments and simulations with prac tical background, including wide-area power systems, lateral control of a utonomous vehicles, and temperature control of silicon rod. His works on data-driven learning and control have been supported by multiple projects supported by the National Natural Science Foundation of China (NSFC), including three Key Projects in 2009, 2015, and 2019, respectively, and a Major Inter national Cooperation Project in 2012. Dr. Hou is the Founding Director of the Technical Committee on Data Driven Control, Learning and Optimization (DDCLO), and the ChineseAssociation of Automation (CAA). He is a fellow of the CAA. He is also anInternational Federation of Automatic Control Technical Committee Member of both “Adaptive and Learning Systems” and “Transportation Systems.” He was the Guest Editor for two Special Sections on the topic of data-driven control of the IEEE T RANSACTIONS ON NEURAL NETWORKS (2011), and the IEEE T RANSACTIONS ON INDUSTRIAL ELECTRONICS (2017). Ye Ren received the bachelor’s degree from Beijing Jiaotong University, Beijing, China, in 2013, wherehe is currently pursuing the Ph.D. degree with the Advanced Control Systems Laboratory. His current research interests include optimization and control of large scale networks, data-drivencontrol, and multi-agent systems control.
