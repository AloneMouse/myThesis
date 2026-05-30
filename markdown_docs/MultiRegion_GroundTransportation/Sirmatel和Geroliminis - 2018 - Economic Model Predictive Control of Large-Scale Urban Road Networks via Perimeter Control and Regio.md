---
source_pdf: Sirmatel和Geroliminis - 2018 - Economic Model Predictive Control of Large-Scale Urban Road Networks via Perimeter Control and Regio.pdf
pages: 10
---

# Sirmatel和Geroliminis - 2018 - Economic Model Predictive Control of Large-Scale Urban Road Networks via Perimeter Control and Regio

<!-- page 1 -->

## 1112 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 19, NO. 4, APRIL 2018

Economic Model Predictive Control of Large-Scale Urban Road Networks via Perimeter Control and Regional Route Guidance Isik Ilber Sirmatel and Nikolas Geroliminis Abstract Local traffic control schemes fall short of achieving coordination with other parts of the urban road network, whereasa centralized controller based on the detailed traffic modelswould suffer from excessive computational burden. State esti-mation for detailed traffic models with limited observations andunpredictability of individual driver behavior create additionalcomplications in the applicability of these models for large-scale traffic control. This point toward the need for designingnetwork-level controllers building on aggregated traffic models,which have recently attracted attention through the macroscopicfundamental diagram (MFD) of urban traffic. Under some con-ditions, the MFD provides a unimodal, low-scatter, and demand-insensitive relationship between vehicle accumulation and travelproduction inside an urban region. In this paper, we proposeMFD-based economic model predictive control (MPC) schemesto improve mobility in heterogeneously congested large-scaleurban road networks. For more realistic simulations of urbannetworks with route guidance actuation-based control, a newmodel with cyclic behavior prohibition is developed. This paperextends upon earlier works on perimeter control-based MPCschemes with MFD modeling by integrating route guidance type actuation, which distributes flows exiting a region over its neighboring regions. Performance of the proposed schemesis evaluated via simulations of congested scenarios with noisein demand estimation and measurement errors. Results showthe possibility of substantial improvements in urban networkperformance, in terms of network delays and traveled distance,even for low levels of driver compliance to route guidance. Index Terms Model predictive control (MPC), urban traffic control, perimeter control, route guidance, macroscopic funda-mental diagram (MFD).

## I. I NTRODUCTION

URBAN traffic congestion continues to trouble the cities of modern society and remains a challenging problem. Application of automatic control methods to traffic problems gained increasing interest for ensuring efficient and reliable operation of urban networks (for reviews refer to [1] and [2]). Coupling advanced control techniques with complex trafficmodels requires challenging improvements on both fields. There is considerable literatu re on methods for controlling a Manuscript received November 16, 2016; revised March 25, 2017 and May 31, 2017; accepted June 11, 2017. Date of publication June 30, 2017;date of current version March 28, 2018. The Associate Editor for this paper was A. Hegyi. (Corresponding author: Nikolas Geroliminis.) The authors are with the School of Architecture, Civil and Environmental Engineering, École Polytechnique Fé dérale de Lausanne, 1015 Lausanne, Switzerland (e-mail: isik.sirmatel@epfl.ch; nikolas.geroliminis@epfl.ch). Color versions of one or more of the figures in this paper are available online at http://ieeexplore.ieee.org. Digital Object Identifier 10.1109/TITS.2017.2716541limited area of the urban network, which are usually based on detailed microor mesoscopic models and involve control schemes that consider only a small part of the whole urban network, such as a set of signalized intersections. Intheir locale of operation, these methods provide good performance for undersatured traffic conditions, but they also have important shortcomings: (a) They are inadequate in dealing with congested conditi ons and heterogeneous distribution/spatiotemporal propagation of congestion (especiallywhen spillbacks occur), (b) there is no coordination between controllers operating in different parts of the network, leading to uncoordinated decisions and potentially conflicts, andultimately to suffering network performance, (c) they require information on highly detailed traffic states, which might be difficult to measure/estimate. Thus, the need for developing control schemes that can achieve coordination between regions of the network, can handle severely and heterogeneouslycongested conditions, and rely only on aggregated traffic information that is relatively easy to measure, points to the direction of exploring network-level controllers for large-scaleurban road networks. The main idea of network-level aggregated control is to create an additional layer in a hierarchical structure before the local controllers are implemented (see [3]). Improving the overall condition in critical areas of a city can help the aforementioned local schemes to improve the localobjectives as disturbances under mild conditions will have less negative effect. Since the beginning of 1980s many works have focused on modeling and control of urban traffic, which usually consider mesoscopic models with link-level dynamics and controllers using local information. As one of the relatively recent studies, based on the linear -quadratic regulator problem, traffic-responsive urban control (TUC) [4] represents a multi-variable feedback regulator a pproach for network-wide urban traffic control, which has been tested both via simulations and field implementations (see [5]). Although TUC can dealwith oversaturated conditions via minimizing and balancing the relative occupancies of network links, it may not be optimal for heterogeneous networks with multiple pockets of congestion. Based on the max-pressure approach, many local control schemes have been proposed for networks of signalizedintersections (see [6]-[8]), wh ich involve evaluations at each intersection requiring inform ation exclusively from adjacent links. Although the high level of detail in mesoscopic modelsis desirable for simulation purposes, the increased complexity 1524-9050 © 2017 I EEE. Personal u se is perm itted, but republication/redistri bution requires IEEE permission. See http://www.ieee.org/publications_standards/publications/rights/index.html for more information.

<!-- page 2 -->

SIRMATEL AND GEROLIMINIS: ECONOMIC MODEL PREDICTIVE CONTROL OF LARGE-SCALE URBAN ROAD NETWORKS 1113 results in complications for control. Furthermore, local controllers might not be able to operate properly under heavily congested conditions, as they do not protect the congested regions upstream. Another disadvantage of sophisticated localcontrollers is that they might require detailed information on traffic states, which are difficult to measure or estimate. The interaction between selfish route choices and the responsivepressure-driven traffic control policies are discussed in the P0 scheme and its extensions for simple networks (see [9], [10]). In the recent years, the two layer hierarchical control approach for urban networks appeared as an alternative to the local traffic control methods established in the litera-ture. At the upper layer a network-level controller optimizes network performance via manipulating macroscopic traffic flows through interregional actuation systems (e.g., perimetercontrol), whereas at the lower layer the local controllers regulate mesoscopic traffic flows through intraregional actuation systems (e.g., signalized intersections). The macroscopic fundamental diagram (MFD) of urban traffic garnered recent interest as a tool for developing aggregated models of urbannetworks, enabling low complexity modeling of whole cities and efficient network-level control design for the upper layer. First proposed by [11] and experimentally proven to exist for large-scale urban areas by [12], the MFD enables modeling of an urban region with roughly homogeneous accumulation (i.e., small spatial link density heterogeneity) by providing a unimodal, low-scatter, and demand-insensitive relationship between accumulation and trip completion flow [12]. Although a powerful modeling tool, the MFD has also its challenges, which might undermine its usefulness. Firstly, hysteresis phenomena, which can be observed on the onset or offsetof congestion, may adversely affect the shape of the MFD (see [3], [13] for details). Secondly, heterogeneous distribution of accumulation, especially in congested conditions, leads to the loss of a well-defined MFD for the urban region (see [14], [15]). Despite these shortcomings, the MFD sub-stantially reduces the complexity of traffic models, and is thus an efficient modeling tool for expressing aggregated dynamics of urban traffic networks, opening the way for the designof network-level control schemes for the upper layer of the hierarchical approach (integra tion of clustering techniques are shown to be beneficial with respect to the aforementioned shortcomings, see, e.g., [16], [17]). Thus, in the last decade the MFD attracted interest in the traffic control literature asan aggregated modeling tool for urban networks. MFD-based control schemes have been proposed by many researchers for single-region [18]-[22] and multi-region [3], [23]-[26] urbannetworks. More detailed literature reviews in MFD-based modeling and control can be found in [27] and [28]. The design of network-level controllers for urban networks with MFD-based modeling requires consideration of the following points: (a) Constraints on the traffic states and control inputs, (b) nonlinear dynamics of the MFD-based network model, (c) possibility of having access to future information (e.g., estimates of the trip demands based on historical data).These points strongly suggest th e suitability of model predictive control (MPC), which is an advanced control technique based on real-time repeated optimization, its most importantadvantage over other cont rol methods being its ability to handle constraints systematically. A computationally efficient method for tackling infinite horizon, constrained optimal control problems (OCPs), MPC provides approximate solutionsto such problems via solving a series of finite horizon openloop OCPs in receding horizon fashion. At each sampling instant, using the current state of the system as initial state,the finite horizon OCP is solved to obtain a sequence of optimal controls, the first of which is applied to the system and the whole procedure is repeated in the next sampling instant. Discussions on important issues of MPC can be found in [29] and an overview of theoretical aspects is given in [30]. Application of MPC to traffic control problems saw increased interest in the ITS literature in the last 15 years: Ramp metering for freeway networks [31]-[33], variable speedlimits [34], [35], integration of ramp metering with variable speed limits [36] and with route guidance [37] for freeway networks, signal control for urban networks [38], [39], signal control for mixed urban and freeway networks [40], and control of logistics systems and railways [41], [42]. MPC schemes with MFD-based prediction models for urban networks began to appear only recently in the literature. In the first work on this direction, a nonlinear MPC is proposedfor a two-region urban network equipped with perimeter control actuation [43]. For the cooperative control of a mixed transportation network consisting of a freeway and two urban regions, an MPC scheme is developed in [44]. A hybrid MPC is developed in [45] for an urban network equippedwith both perimeter control systems and switching signal timing plans. In [3], a model capturing the dynamics of heterogeneity is developed together with a hierarchical controlsystem with MPC on the upper level. The aforementioned works on MFD-based MPC for urban networks do not explore actuation via routing the the drivers. Although there are also some recent attempts on this direction [28], [46], enhancing perimeter control with route guidance actuation still remainsunexplored. In this paper network-level economic MPC schemes integrating perimeter control and regional route guidance areproposed to improve mobility in urban networks. In contrast to standard MPC where the objective function is related to a control goal such as regulation or setpoint tracking, economic MPC involves objective functions that express economically optimal plant operation (e.g., maximizing profitsor minimizing time spent). Firstly, a new MFD-based urban network model is developed with cyclic behavior avoidance, i.e., prohibiting vehicles from flowing back and forth betweenneighboring regions, which is important for simulating urban networks under closed-loop with route guidance based control schemes. Furthermore, the problem of finding the perimetercontrol and route guidance inputs for a m ulti-region urban network to minimize total time spent (TTS) is formulated as an economic MPC problem, along with various actuator configurations. The analysis in this work sheds some light to the demand conditions for which c oupling of perimeter control and route guidance can prove beneficial. Results indicate that the proposed MPC schemes can significantly decrease network delays and, when route guidance is coupled with perimeter

<!-- page 3 -->

## 1114 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 19, NO. 4, APRIL 2018

#### Fig. 1. Schematic of an urban network with 7 regions.

control, even low driver compliance levels are sufficient to improve network performance.

## II. M ODELING OF LARGE -SCALE URBAN NETWORKS

A. MFD-Based Modeling of a Multi-Region Urban Network We consider an urban network Rwith heterogeneous distribution of accumulation, consisting of Rhomogeneous

$$
regions, i.e., R={1,2,..., R}, each with a well-defined
$$

outflow MFD, defined via GI(NI(t))(veh/s) expressing the trip completion flow (i.e ., outflow) at accumulation NI(t). A network consisting of 7 regions is schematically shown infig. 1. The exogenous inflow demand generated in region I with destination JisQ IJ(t)(veh/s), whereas NIJ(t)(veh) is the accumulation in region Iwith destination J,a n d NI(t) (veh) the total accumulation in region I, at time t; I,J∈R;

$$
NI(t)/defines\sum
$$

J∈RNIJ(t). Between each pair of neighboring regions Iand H(I∈R,H∈NI,w h e r e NIis the set of regions neighboring region I) there exists perimeter controls UIH(t)and UHI(t)∈[0,1]that can manipulate the transfer flows. Furthermore, each region is equipped with regional route guidance controls θIHJ(t)(I∈R,H∈NI, J∈R\{I}), that can distribute the transfer flows exiting a region over its neighboring regions. Dynamics of an R-region MFDs network are [3], [28]:

$$
˙NII(t)=QII(t)-MII(t)+\sum
$$

H∈NIUHI(t)MHII(t)(1a)

$$
˙NIJ(t)=QIJ(t)-\sum
$$

H∈NIUIH(t)MIHJ(t) +\sum

$$
H∈NI;H\ne =JUHI(t)MHIJ(t), (1b)
$$

forI,J∈R,w h e r e MII(t)(veh/s) is the exit (i.e., internal trip completion) flow from region Ito destination I:

$$
MII(t)=NII(t)
$$

NI(t)GI(NI(t)) (2) and MIHJ(t)(veh/s) is the transfer flow from region Ito destination Jthrough the next immediate region H:

$$
MIHJ(t)=θIHJ(t)NIJ(t)
$$

NI(t)GI(NI(t)), (3) with MHII(t)and MHIJ(t)defined similarly, expressing the transfer flows from Hthrough Iwith destinations Iand J,respectively. It is assumed that trips inside a region have similar lengths (i.e., the distance traveled per vehicle inside a region does not depend on the origin and destination of the trip). Simulation and empirical results [12] suggest thatthe MFD can be approximated by an asymmetric unimodal curve skewed to the right (i.e., the critical accumulation N cr I, which maximizes GI(NI(t)),i sl e s st h a nh a l fo ft h ej a m accumulation Njam I, which puts the region in gridlock). Thus, GI(NI(t))can be expressed with a third-order polynomial in

$$
the variable NI(t), i.e., GI(NI(t))=AIN3
$$

I(t)+BIN2 I(t)+ CINI(t),w h e r e AI,BI,a n d CIare estimated parameters. Transfer flows are influenced by the boundary capacity between regions Iand H, as high accumulation in region Hmight restrict the reception of inflows from the boundary, which can be formalized through the following equation expressing capacity-restricted transfer flow ˆMIHJ(t)[3], [28]:

$$
ˆMIHJ(t)=min/parenleftbigg
$$

MIHJ(t),CIH(NH(t))MIHJ(t) \sum K∈RMIHK(t)/parenrightbigg (4) where CIH(NH(t))(veh/s) is the boundary capacity between regions IandHthat depends on NHas follows [3]: CIH(NH)=⎧ ⎪⎨ ⎪⎩Cmax

$$
IHif 0\le NH<α * NH,jam
$$

Cmax IH 1-α(1-NH Njam H)ifα * Njam

$$
H\le NH\le Njam
$$

H, (5) where Cmax IH(veh/s) is the maximum boundary capacity, Njam H (veh) is the jam accumulation of the receiving region H, whereas α * Njam H(with 0 <α< 1) specifies the point where CIH(NH)starts decreasing with in creasing accumulation. The boundary capacity constraint can be omitted in the prediction model of MPC for computational advantage. The physical reasoning of this omission is that (i) the boundary capacity decreases for accumulations much larger than the criticalaccumulation, and (ii) the controller will not allow the regions to have accumulations close to gridlock [44]. The effect of tightening boundary capacity is studied in section IV-F. The assumption of a low-scatter regional outflow MFD is based on the equivalent assumption of a time-invariant regionaltrip length. While an adequate model for control design with simplified system dynamics without delays (i.e., it considers outflows equal to the ratio of production over constant triplength), and although there are empirical verifications about its validity via aggregated data (e.g., [12]), the MFD should not be considered as a universal law. For example, strongfluctuations in the demand that create fast evolving transients can influence the trip length distribution in a region at a specific time, potentially causing the ratio of production over trip length approximation of outflow to have inaccuracies. While we consider this a valid assumption for a range ofcases, further research would be useful to study under what conditions more complex dynamics (with delays) are required (see, e.g., some analysis in [47]), which is a research priority.

<!-- page 4 -->

SIRMATEL AND GEROLIMINIS: ECONOMIC MODEL PREDICTIVE CONTROL OF LARGE-SCALE URBAN ROAD NETWORKS 1115 B. Cyclic Behavior Prohibiting Urban Network Model The urban network model (1) has no memory of the region the vehicles were previously, thus does not prohibitvehicles from flowing back and forth between neighboring regions (i.e., it permits cyclic behavior). While this memoryless choice of routes is not crucial when only perimetercontrol actuation is applied, it is physically important for route guidance based schemes, where the controller may try to emulate perimeter control actuation via cyclic routes. We also need to be able to compare trave l times and trip lengths for inflow demands Q IJ(t)and for various control strategies and driver compliance levels. Thus, instead of NIJand MIHJ we have to introduce more detailed states. With NOGI J and MOGIHJ denoting the accumulation and flow, respectively, with origin O, previous region G, current region I, destination region J, and immediate next region H, the dynamics keeping memory of origin and previous regions can be written as:

$$
˙NIIII(t)=QII(t)-MIIIII(t),∀I∈R, (6a)
$$

$$
˙NIIIJ(t)=QIJ(t)-\sum
$$

H∈NIUIH(t)MIIIHJ(t),

$$
∀I,J∈R,J\ne =I, (6b)
$$

$$
˙NOGII(t)=\sum
$$

F∈N∗ G\{I}UGI(t)MOFGII (t)-MOGIII (t),

$$
∀O,G,I∈R,G∈NI,O\ne =I, (6c)
$$

$$
˙NOGI J(t)=\sum
$$

F∈N∗ G\{I,J}UGI(t)MOFGIJ (t) -\sum H∈NI\{O,G}UIH(t)MOGIHJ (t), ∀O,G,I,J∈R,G∈NI,

$$
O\ne =I,O\ne =J,G\ne =J,J\ne =I, (6d)
$$

whereN∗ Gis the set containing the neighboring regions of G and region Gitself. Note that if the last two indices of a flow term are identical, then this denotes an exit flow (as next and final region are the same); it denotes a transfer flow otherwise. Note that in (6a) there are no control inputs as flows are internal and uncontrolled. Note also that in (6c)-(6d) the positive terms of the right hand side are controlled transferflows from the neighboring regions to the current region. The exit and transfer flow terms can be calculated as follows: M

$$
OGIHJ (t)=θOGIHJ (t)NOGI J(t)
$$

NI(t)GI(NI(t)), (7) where θOGIHJ denotes the fraction of flows in an identical way with the flow terms, having the same 5 indices. Using (6) as the simulation model (i.e., the plant representing reality) with MPC controllers having (1) as the prediction model requires the transfer of variables between the two models as follows: \sum

$$
O∈R\{J}\sum
$$

$$
G∈R\{J}NOGI J(t)=NIJ(t),∀I,J∈R (8)for the accumulations states and
$$

$$
θOGIHJ (t)=/braceleftBigg
$$

$$
θIHJ(t)ifH\ne =G,
$$

0o t h e r w i s e ∀O,G,I,J∈R, G∈NI,H∈NI\{O}

$$
O\ne =I,O\ne =J,G\ne =J,J\ne =I (9)
$$

for the fraction of flows, where cycle-inducing θOGIHJ terms

$$
(i.e., those with H=G) are forced to be 0. Owing to this,
$$

the model (6) can prohibit cycles of length 2, and is thus a more realistic representation of urban network dynamics. Forprohibiting longer cycles, (6) s hould be extended with longer route memory, but this is not considered in this work since cycles longer than two are assumed to be negligible. III. O PTIMAL CONTROL OF URBAN NETWORKS VIA PERIMETER CONTROL AND REGIONAL ROUTE GUIDANCE A. Model Predictive Control Problem Formulation We formulate the problem of finding the UIHandθIHJ values that minimize TTS (for a finite horizon) as the following discrete time economic nonlinear MPC problem: minimize

$$
U,θTc * Np-1\sum
$$

$$
k=0/bardblN(k)/bardbl1
$$

subject to N(0)=ˆN(tc) |U(0)-ˆU(tc-1)|\le /Delta1U |θ(0)-ˆθ(tc-1)|\le /Delta1θ

$$
fork=0,..., Np-1:
$$

$$
N(k+1)=f(N(k),Q(k),U(k),θ(k))
$$

$$
0\le \sum
$$

$$
j∈RNIJ(k)\le Njam
$$

I,∀I∈R

$$
Umin\le UIH(k)\le Umax,∀I∈R,H∈NI
$$

$$
0\le θIHJ(k)\le 1,∀I,J∈R,I\ne =J,H∈NI\sum
$$

$$
H∈NIθIHJ(k)=1,∀I,J∈R,I\ne =J
$$

$$
ifk\ge Nc:
$$

$$
U(k)=U(k-1)
$$

$$
θ(k)=θ(k-1), (10)
$$

where Tcis the control sampling time, N(k),Q(k),U(k),a n d θ(k)are vectors containing all NIJ(k),QIJ(k),UIH(k),a n d θIHJ(k)terms, respectively, with kbeing the control interval counter, fis the time discretized version of eq. (1)-(3), tcis the current control time step and ˆN(tc)is the measurement taken at tc,ˆU(tc-1)andˆθ(tc-1)are the control inputs applied to the plant previously, NpandNcare the prediction and control horizons, whereas /Delta1Uand/Delta1θare the rate limits on perimeter control and route guidance inputs, respectively. The problem (10) is a nonconvex nonlinear program (NLP), which can be solved efficiently via, e.g., sequential quadratic programming (SQP) or interior point solvers. We propose three MPC schemes: (i) perimeter control MPC (PC) has UIHas control input, while drivers are free to choose their own routes (i.e., θIHJ) ,w h i c ha r ea s s u m e dfi x e dt ot h e i r

<!-- page 5 -->

## 1116 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 19, NO. 4, APRIL 2018

measured value, at tc, for the prediction horizon. (ii) For route guidance MPC (RG) θIHJ is the control input, while UIH is fixed to Umax. (iii) Perimeter control and route guidance MPC (PCRG) has access to both actuators. While θIHJ(tc)is difficult to estimate with fixed location sensors, use of mobile sensors with advanced estimation techniques provide strong potential in this direction (see, e.g., [48]). Performance metrics for evaluating the MPC schemes are TTS and total traveled distance (TTD):

$$
TTS=Ts * Texp\sum
$$

t=1\sum I∈RNI(t),

$$
TTD=Ts * Texp\sum
$$

t=1\sum I∈RLI * /parenleftbigg

$$
MII(t)+\sum
$$

$$
H∈NI\sum
$$

J∈R\I¯MIHJ(t)/parenrightbigg ,

$$
where the flow ¯MIHJ(t)(veh/s) is defined as ¯MIHJ(t)=
$$

UIH(t)θIHJ(t)MIJ(t). It is important to look at both performance metrics, as route guidance might enforce some drivers to take significantly longer routes for the system benefit. Such a result would be difficult to be acceptable in practice as drivers would follow the proposed routes only if their individual travel time is not significantly worse. For a single-region city governed by an outflow MFD, minimizing TTS will result in maximizing outflow (which is equivalent to maximizing TTD), as the objective is to letvehicles finish their trips as soon as possible. Thus, as proven in [18], the best strategy is to keep the region at its critical accumulation if the delays of vehicles waiting outside the network (i.e., the virtual queues) are considered. For a multi-region city (as is the case in the paper), however, it might be impossible to keep all regions under or at critical accumulation. Then, c ontrol via tracking regional accumulation setpoints is difficu lt, as it is not straightforward to find those setpoints that minimize TTS (since these might be time-varying and depend on the demand pattern). Maximizing TTD, on the other hand, might create very long routes for some vehicles especially unde r uncongested conditions due to detouring, which would decrease network outflow. B. Controller Tuning and Computational Efficiency MPC performance is strongly influenced by the prediction horizon N p. Computational effort is affected also by the chosen direct method and NLP solver (see [49] for details).To study the relations between all of the above, a series of simulation experiments (based on the congested scenario in section IV-B) is conducted with varying values of N p(with

$$
Ncfixed to 2 and a control sampling time of Tc=240 s) and
$$

various direct methods (see [50] for details). Direct multiple shooting (DMS, [51]) and direct collocation (DC) (solved with the solver IPOPT [52]) results for all three MPC schemes1are included together with direct single shooting (DSS) (solvedwith an SQP solver) for PC. Using SQP for DMS and DC is computationally disadvantageous, since SQP favors small and 1Implementation is done via the CasADi toolbox [53] in MATLAB 8.5.0 (R2015a), on a 64-bit Windows PC with 3.6-GHz Intel Core i7 processor and 16-GB RAM.Fig. 2. (a) Percent improvement in TTS over NC and (b) average CPU timesfor the MPC schemes with various direct methods as a function of N p. dense NLPs (such as those arising from DSS), while DMS and DC yield large and sparse NLPs (which are amenable to efficient solutions via e.g. IPOPT). The results, given in

#### fig. 2, show the TTS performance and the average CPU times,

which indicate that: (a) TTS performance is fairly insensitive

$$
to the choice of NpforNp\ge 7, (b) DSS is favorable for PC,
$$

whereas DC is favorable for RG and PCRG, (c) even for short horizons PCRG is able to yield high improvements. IV . C ASE STUDIES A. Network Description and Simulation Setup All simulations are conducted on a 7 region urban network (see fig. 1), with the simulation model given in (6) for representing the reality. A unit MFD is considered with the

$$
parameters ¯A=4.133 * 10-11,¯B=-8.282 * 10-7,¯C=0.0042,
$$

$$
jam accumulation ¯Njam=104(veh), critical accumulation
$$

$$
¯Ncr=3.4 * 103(veh), maximum outflow G(¯Ncr)=6.3( v e h / s ) ,
$$

$$
with an average trip length of ¯L=3600 m, which are
$$

consistent with the MFD observed in a part of downtown Yokohama (see [12]). Each region is assumed to have adifferent MFD that is a (within ±10%) scaled version of the unit MFD. Boundary capacity effect is included, with values ¯C max

$$
IH=3.2 veh/s and ¯α=0.64 for the unit MFD.
$$

Based on the results in section III-B, the prediction and

$$
control horizons are chosen as Np=7a n d Nc=2f o rt h e
$$

MPC schemes. Simulation sampling time is 30 s while the

$$
length of the simulation experiment is Texp=240 (in number
$$

of simulation steps), giving an effective length of 120 minutes.Bounds of U

$$
IHareUmin=0.1a n d Umax=0.9, whereas the
$$

$$
rate limits are /Delta1U=0.2a n d /Delta1θ=0.1, to reflect the fact that
$$

it is more difficult to cause abrupt changes in routing. For capturing the effect of m easurement noise in accumulation states (as accumulations have to be measured from fixedand mobile sensors, which invariably have noise), we add random noise terms with normal distribution: ˜N

$$
IJ(t)=NIJ(t)+NIJ(t) * N(0,σ2
$$

NIJ),∀I,J∈R,(11) where the noise has zero mean and its variance is chosen as σ2

$$
NIJ=0.25 in the simulations. Demand uncertainty is also
$$

considered, with the MPC having access to average demand profiles, while the actual inflow demands have random noise:

$$
˜QIJ(t)=QIJ(t)+QIJ(t) * N(0,σ2
$$

QIJ),∀I,J∈R,(12) with the variance chosen as σ2

$$
QIJ=0.25 in the simulations,
$$

representing presence of large noise.

<!-- page 6 -->

SIRMATEL AND GEROLIMINIS: ECONOMIC MODEL PREDICTIVE CONTROL OF LARGE-SCALE URBAN ROAD NETWORKS 1117 The MPC controllers are compared with a no control (NC) case, in which UIHare fixed to Umax, while drivers are free to choose their routes. In simulations this is captured by calculating θIHJ by a logit model (see [54]) using the current travel times from Ito destination Jthrough a predefined finite number of shortest sequences of regions connecting the two, calculated with Dijkstra’s algorithm for K-shortest

$$
paths ( K=3 for this paper). As drivers adapt to traffic
$$

conditions in real time, the θIHJ values are updated at each control time step. The logit model relaxes the assumption that drivers always choose the physical shortest path. Simulations using logit model thus tend to be more realistic as driversrarely have perfect information and do not always behave as rational actors. Parameters of the logit model can be adjusted to reflect the amount of information available to drivers ortheir sensitivity to travel time differences between routes. An interesting point to investigate is about deciding what the preferred actuation scheme is (i.e., PC, RG, or PCRG) under different demand conditions, given that there is a nonnegligible installation cost. While in principle the regions of the citythat attract most of the trips should operate at the critical accumulation that maximizes flo w (e.g., [18] proves this for single region systems), this might not be the case for multipleregions with competing objectives. Our objective is also to investigate the attractivity of the regions of a city with respect to (i) destinations and (ii) crossing zones. While point (i) is clear, with respect to point (ii) a region might attract a lot of trips simply because many shortest paths are passingfrom this region (even if destinations are elsewhere). Thus, two simulation parameters are defined to construct various scenarios: (a) The ratio of demands with destination region4 (i.e., city center) to demands from periphery to periphery, denoted by ρand (b) driver compliance level, denoted by γ. The ratio ρ, expressing the relative intensity of the inflow demands towards city center, is defined as follows: ρ=\sum Texp t=1\sum I∈RQI4(t)

$$
\sumTexp
$$

t=1\sum

$$
I∈R\{4}\sum
$$

J∈R\{4}QIJ(t), (13) whereas the driver compliance level γ( a l s od e fi n e da sa constant for a single simulation experiment) indicates the percentage of drivers following the route guidance recommendations of the traffic control scheme (i.e., either RG and PCRG), which is used in obtaining the route guidancecommand θ IHJ value for the control step tcas follows: θreal IHJ(tc)=γθMPC IHJ(tc)+(1-γ)θlogit IHJ(tc), (14) where θreal IHJ(tc)is the realized route guidance command (i.e., the value used in simulation), whereas θMPC IHJ(tc)andθlogit IHJ(tc) are the outputs of the MPC and the logit model, respectively. B. Control Performance Under Congested Conditions Let us describe the base case scenario: The network is uncongested at the beginning, but faces increased inflowdemands as time progresses. The driver compliance level γ is 100% and ratio of demands ρis equal to 0, meaning no trips have city center as destination-nevertheless this is anTABLE I PERFORMANCE EVA L UAT I O N F O R CONGESTED SCENARIO important region of attraction as many trips prefer to cross the center due to short distance. The results are given in

#### fig. 3, where the evolution of regional accumulations (fig. 3ato 3d) are shown alongside graphs of time spent in network

(fig. 3e), cumulative traveled distance (fig. 3f), outflow of city center (i.e., region 4) (fig. 3g), and the noisy inflow demands ˜Q IJ(t)(fig. 3h), all as a function of simulation time, for the no control (NC) case and the three MPC schemes (pleaserefer to the legends in fig. 3 for descriptions of each figure). A summary of the results is given in table I, which shows the two performance metrics about time and distance (i.e.,TTS and TTD), improvement over the NC case for TTS, increase in TTD over the theoretically possible minimum TTD (which is calculated by considering that all vehicles are able to take the physical shortest path to their destinations under free flow conditions, and is equal to 3 .87 * 10 8veh * m), and the CPU times for the MPC schemes. The results indicate that all MPC schemes are capable of improving mobility in the urban network, as they have decreased values of both theTTS and TTD metrics, in comparison to the NC case. Noting that control sampling time T cis chosen as 240 s, the CPU time results given in table I suggest that the schemes are computationally tractable, as their CPU times are negligible in comparison to Tc. PCRG is superior in distributing the vehicle flows efficiently over the whole network, which translates to efficient usage of the network capacity, leading to less congestion and alsodecreased values of TTS. This is clearly seen in the regional accumulation plots (b )-(d) in fig. 3, where PCRG can suppress congestion evenly in all regions. Note also that for all three strategies not all regions are able to operate below the critical value of accumulation, so even the best control scheme stillexperiences some congestion for some regions, notably for smaller durations. This highlights the importance of using prediction and aggregated future O-D information via MPC.For example, PI type controllers without demand information (see [19], [24], [55]) are successful when all regions can operate close to their critical accumulations. But if this is notpossible due to high demand, aggregated O-D information is expected to further improve network performance. The NC case cannot avoid severe congestion close to gridlock, leading to drastic decrease in outflow for the city center (as seen in fig. 3g) and thus inefficient use of thecity center capacity for transferring flows from periphery to periphery. This is crucial for both TTS and TTD metrics, since routes through the city center are generally the physical

<!-- page 7 -->

## 1118 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 19, NO. 4, APRIL 2018

#### Fig. 3. Results of the congested scenario for the no control (NC) case and th e three MPC schemes. Regional accumulations for (a) NC, (b) PC, (c) RG,

(d) PCRG. Comparison of the four cases for (e) time spent in network, (f) sta ndard deviation of regional accumulations, (g) outflow of city center. (h) N oisy inflow demand profiles, expressing demands for tri ps between 5 origin-destination region pairs.

#### Fig. 4. Usage of physical shortest path for the congested scenario.

shortest paths connecting two opposing peripheral regions. The MPC schemes, on the other hand, make efficient use of thecity center as seen in the city center outflow (i.e., G 4(N4(t))) plot in fig. 3g, which shows their success in keeping the city center close to cr itical accumulation Ncr 4until network starts to unload. It is interesting that city center remains severely congested even if drivers are adaptive and update their routesbased on travel time information (i.e., the NC case), which is not the case when control is applied. Route guidance based schemes can improve both TTS and TTD metrics compared to the PC scheme due to their authority over routing, increasing the percentage of drivers using the physical shortest path. Thus, vehicles spend less time andtravel for shorter distances before exiting the network. The percentage of drivers that are momentarily using the physical shortest path to their destinations is given in fig. 4 for NC and the three MPC schemes. This result shows that route guidance based schemes succeed in making more drivers usethe physical shortest path, explaining the improvement in TTD. The fact that regional route guidance (which tries to develop conditions close to system optimum) might create worse traveltimes for some users is analyzed later in the paper. C. Effect of Cyclic Behavior Prohibition To examine the effect of absence of cyclic behavior prohibition in the proposed model, given in section II-B, a series of simulation experiments are conducted based on the scenario inFig. 5. Ratio of cyclic to total flows for NC and the three MPC schemes. section IV-B. The model formulation is changed via relaxing

$$
the condition H\ne =Gin section II-B so as to allow cyclic
$$

flows. To summarize the presence of cyclic behavior, thepercentage of vehicle flows that are returning to the region they came from among the total vehicle flows is considered: \sum O∈R\sum

$$
K∈R\G\sum
$$

$$
G∈R\K\sum
$$

$$
K∈R\G\sum
$$

J∈R¯MOKGKJ (t) \sum O∈R\sum G∈R\sum

$$
IinR\sum
$$

H∈R\sum J∈R¯MOGIHJ (t), where the vehicle flow ¯MOGIHJ (t)is defined as follows

$$
¯MOGIHJ (t)=UIH(t)θOGIHJ (t)MOGI J(t).
$$

The results are given in fig. 5, showing this percentage as a function of simulation time. There are substantial cyclic flows occurring in the simulation, which can be avoided with the use of the proposed model, supporting the use of such a modelwith more detailed states to represent the plant. D. Driver Compliance and Demand Ratio ρAnalysis In an ideal case with route guidance actuation, all drivers would follow θ IHJ exactly, but this may not be the case in reality as some drivers might prefer choosing their own routes. To analyze how driver compliance affects route guidanceperformance, a series of simulati ons with four different values ofρare conducted by varying compliance level γfrom 0% to 100%, which are summarized in fig. 6. Interestingly, the results

<!-- page 8 -->

SIRMATEL AND GEROLIMINIS: ECONOMIC MODEL PREDICTIVE CONTROL OF LARGE-SCALE URBAN ROAD NETWORKS 1119

#### Fig. 6. Performance comparison of the NC case and the three MPC

schemes, for different values of ρ, as a function of driver compliance levelγ: (a)-(d) normalized TTS, (e)-(h) normalized TTD. differ with varying ratio of demand that has the city center as a destination: For low values of ρ, i.e., for the case with most of the trips from periphery to periphery, these results show that: (a) PC is not very successful in decreasing TTS, whileRG performs well for high compliance; thus, PC is not very appropriate when destinations are distributed all over the city and the city center is used mainly for crossing trips, (b) there is no difference between RG and PCRG schemes. For high ρ values, on the other hand, the results indicate: (a) Increasing γ, especially for RG, yields in larg er performance improvements, (b) there are substantial differences between RG and PCRG. Specifically, for the case with ρ=0.35, RG cannot prevent gridlock for γlower than 0 .8, whereas PCRG is able to prevent it for γhigher than 0 .5, showcasing the superiority of PCRG over RG in improving network performance even in difficult demand conditions (i.e., high ρ) and low compliance. Besides the performance improvement aspect of these results,an intuition with respect to field implementations can be developed: When a small number of destinations is within the city center, a route guidance system would be sufficientand perimeter control is not necessary. This might happen if the city center has high quality public transport and expensive parking, discouraging people to travel by car in the center.If the number of destinations in the center is higher, then perimeter control is beneficial as it can prevent the center from overcrowding even for low levels of compliance. Furthermore, while RG and PCRG have similar performance for high compliance (with the exception of many city center trips, i.e.,forρ=0.35), the difference is highly pronounced for lower compliance levels. This highlights the importance of coupling PC with RG for realistic implementations, as γmight not beFig. 7. Departure curve (d.c.) and arrival curves (a.c.) for the three MPC schemes, for the O-D pair 1-7.

#### Fig. 8. Travel time benefit of drivers in RG and PCRG schemes with respectto PC scheme, for ρvalues of 0.05, 0.15, 0.25, and 0.35, for a constant γ

separately for each ρvalue. very high due to issues of accepta nce by the whole population of drivers and lack of smart technologies in some cars. E. A More Detailed Consideration of Travel Time Benefits Control via route guidance may cause some drivers to experience longer travel times compared to cases with no route guidance, leading to lower compliance and finally in less efficient schemes due to low user acceptance. To examine thetravel time benefit of drivers under the RG and PCRG schemes, compared to the PC scheme, a ser ies of simulation experiments are conducted with four different values of ρandγ. For each MPC scheme, the travel times of each group of users with a certain regional O-D are estimated as a function of time based on the horizontal distance between the cumulative departure-arrival curves. Figure 7 provides the cumulative curves for the three schemes (departure curve is the same, as each scheme is tested with the same demand) for O-D pair 1-7. While for smallρand in the beginning of each case the three schemes are very similar, when a higher number of trips has the center asdestination (i.e., for high values of ρ), PCRG performs better than PC and RG. Based on these estimations the distribution of travel time benefits of RG and PCRG are compared to PC,

<!-- page 9 -->

## 1120 IEEE TRANSACTIONS ON INTELLIGENT TRANSPORTATION SYS TEMS, VOL. 19, NO. 4, APRIL 2018

#### Fig. 9. Sensitivity of TTS performance to changes in boundary capacity.

which does not have any ability to control individual O-D movements. The distributions, given in fig. 8, consist of all O-D pairs and times, and are for 4 different values of ρ, each case having a constant value of γ(for each case separately, this corresponds to the γvalue for which PC and RG have the same TTS performance). The distributions are skewed and containboth positive and negative values indicating the influence of the schemes for different users. These results indicate the superiority of PCRG over RG, as it keeps almost all drivers better off in terms of experienced travel times: In all cases, roughly 90% of drivers benefit from PCRG, and in generalonly 2-3% experience travel times extended longer than 5 minutes, suggesting substantial potential for practice. F . Sensitivity to Changes in Boundary Capacity To study the effect of the boundary capacity, a series of simulation experiments are conducte d via scaling the parameters C max IH(maximum capacity) and α(specifies the accumulation for which the capacity starts decreasing) used for the congested scenario in IV-B by factors varying from 0.3 to 1.1 (capacitiesare non-binding above 1.1). The results, given in fig. 9, show that the MPC schemes are fairly insensitive to changes in boundary capacity for factors larger than 0.6, supporting theinitial conjecture that boundary capacity can be ignored in the MPC prediction model. Interestingly, boundary capacity seems to provide benefits similar to perimeter control for those cases without actual perimeter control, as seen from the decreased TTS for factors around 0.5 for NC and 0.6 for RG. V. C ONCLUSION The paper contributes in two aspects: (a) In the traffic modeling side a novel cyclic behavior prohibiting dynamic urbannetwork model is proposed, with the potential of yielding more realistic simulation results compared to current MFD-based urban network models in the literature, (b) in the controldesign aspect, integrating perimeter control and route guidance type actuators, economic nonlinear MPC schemes are developed for improving mobility in urban networks. Simulationstudies show the potential for substantial improvement in mobility through the u se of route guidance, in comparison to control via perimeter control only. A further observation is that since route guidance actuation cannot restrict flows, unlike perimeter control, it is unable to protect urban regions fromsevere congestion especially for cases with imperfect driver compliance. Highest performance is obtained by using both types of actuators.Future research could include (a) comparison of the proposed schemes with other approaches (e.g., feedback perimeter control [24], [25]), (b) more detailed simulation experiments with microor mesoscopic methods, (c) design of routeguidance based control schemes for mixed urban-freeway networks, (d) field implementation. A field test is under preparation for estimation of θ IHJ values through cellphone data in a Swiss city and integration of this information in a PC scheme (with possibility of extension to PCRG cases).

## REFERENCES

[1] M. Papageorgiou, C. Diakaki, V . Dinopoulou, A. Kotsialos, and Y . Wang, “Review of road traffic control strategies,” Proc. IEEE , vol. 91, no. 12, pp. 2043-2067, Dec. 2003. [2] F.-Y . Wang, “Parallel control and management for intelligent transportation systems: Concepts, architectures, and applications,” IEEE Trans. Intell. Transp. Syst. , vol. 11, no. 3, pp. 630-638, Sep. 2010. [3] M. Ramezani, J. Haddad, and N. Geroliminis, “Dynamics of heterogeneity in urban networks: Aggregat ed traffic modeling and hierarchical control,” Transp. Res. B, Methodol. , vol. 74, pp. 1-19, Apr. 2015. [4] C. Diakaki, M. Papageorgiou, and K. Aboudolas, “A multivariable regulator approach to traffic-respons ive network-wide signal control,” Control Eng. Pract. , vol. 10, no. 2, pp. 183-195, Feb. 2002. [5] A. Kouvelas, K. Aboudolas, M. Papageorgiou, and E. B. Kosmatopoulos, “A hybrid strategy for real-time traffic signal control of urbanroad networks,” IEEE Trans. Intell. Transp. Syst. , vol. 12, no. 3, pp. 884-894, Sep. 2011. [6] P. Varaiya, “Max pressure control o f a network of signalized intersections,” Transp. Res. C, Emerg. Technol. , vol. 36, pp. 177-195, Nov. 2013. [7] A. Kouvelas, J. Lioris, S. Fayazi, and P. Varaiya, “Maximum pressure controller for stabilizing queues in signalized arterial networks,” Transp. Res. Rec. J. Transp. Res. Board , vol. 2421, pp. 133-141, Oct. 2014. [8] A. A. Zaidi, B. Kulcsár, and H. Wymeersch, “Traffic-adaptive signal control and vehicle routing using a decentralized back-pressure method,”inProc. Eur. Control Conf. , Jul. 2015, pp. 3029-3034. [9] M. Smith and R. Mounce, “A splitting rate model of traffic rerouteing and traffic control,” Transp. Res. B, Methodol. , vol. 45, no. 9, pp. 1389-1409, 2011. [10] M. Smith, “Traffic signal control and route choice: A new assignment and control model which designs signal timings,” Transp. Res. C, Emerg. Technol. , vol. 58, pp. 451-473, Sep. 2015. [11] J. Godfrey, “The mechanism of a road network,” Traffic Eng. Control , vol. 11, no. 7, pp. 323-327, 1969. [12] N. Geroliminis and C. F. Daganzo, “Existence of urban-scale macroscopic fundamental diagrams: S ome experimental findings,” Transp. Res. B, Methodol. , vol. 42, no. 9, pp. 759-770, Nov. 2008. [13] V . V . Gayah and C. F. Daganzo, “Clockwise hysteresis loops in the macroscopic fundamental diagram: An effect of network instability,” Transp. Res. B, Methodol. , vol. 45, no. 4, pp. 643-655, 2011. [14] N. Geroliminis and J. Sun, “Prope rties of a well-defined macroscopic fundamental diagram for urban traffic,” Transp. Res. B, Methodol. , vol. 45, no. 3, pp. 605-617, Mar. 2011. [15] V . Knoop, S. Hoogendoorn, and J. Van Lint, “Routing strategies based on macroscopic fundamental diagram,” Transp. Res. Rec. J. Transp. Res. Board , vol. 2315, pp. 1-10, Dec. 2012. [16] Y . Ji, J. Luo, and N. Geroliminis, “Empirical observations of congestion propagation and dynamic partitioning with probe data for large-scale systems,” Transp. Res. Rec. J. Transp. Res. Board , vol. 2422, pp. 1-11, Oct. 2014. [17] M. Saeedmanesh and N. Geroliminis, “Clustering of heterogeneous networks with directional flows based on ‘Snake’ similarities,” Transp. Res. B, Methodol. , vol. 91, pp. 250-269, Sep. 2016. [18] C. F. Daganzo, “Urban gridlock: Macroscopic modeling and mitigation approaches,” Transp. Res. B, Methodol. , vol. 41, no. 1, pp. 49-62, 2007. [19] M. Keyvan-Ekbatani, A. Kouvelas, I. Papamichail, and M. Papageorgiou, “Exploiting the fundamental diagram of urban networks for feedback-based gating,” Transp. Res. B, Methodol. , vol. 46, no. 10, pp. 1393-1403, Dec. 2012. [20] V . V . Gayah, X. Gao, and A. S. Nagle, “On the impacts of locally adaptive signal control on urban network stability and the macroscopic fundamental diagram,” Transp. Res. B, Methodol. , vol. 70, pp. 255-268, Dec. 2014.

<!-- page 10 -->

SIRMATEL AND GEROLIMINIS: ECONOMIC MODEL PREDICTIVE CONTROL OF LARGE-SCALE URBAN ROAD NETWORKS 1121 [21] J. Haddad and A. Shraiber, “Ro bust perimeter control design for an urban region,” Transp. Res. B, Methodol. , vol. 68, pp. 315-332, Oct. 2014. [22] J. Haddad, “Optimal coupled and d ecoupled perimeter control in oneregion cities,” Control Eng. Pract. , vol. 61, pp. 134-148, Apr. 2017. [23] J. Haddad and N. Geroliminis, “On the stability of traffic perimeter control in two-region urban cities,” Transp. Res. B, Methodol. , vol. 46, no. 9, pp. 1159-1176, 2012. [24] K. Aboudolas and N. Geroliminis , “Perimeter and boundary flow control in multi-reservoir heterogeneous networks,” Transp. Res. B, Methodol. , vol. 55, pp. 265-281, Sep. 2013. [25] A. Kouvelas, M. Saeedmanesh, and N. Geroliminis, “Enhancing modelbased feedback perimeter control with data-driven online adaptive optimization,” Transp. Res. B, Methodol. , vol. 96, pp. 26-45, Feb. 2017. [26] J. Haddad, “Optimal perimeter c ontrol synthesis for two urban regions with aggregate boundary queue dynamics,” Transp. Res. B, Methodol. , vol. 96, pp. 1-25, Feb. 2017. [27] M. Saberi and H. Mahmassani, “E xploring properties of networkwide flow-density relations in a freeway network,” Transp. Res. Rec. J. Transp. Res. Board , vol. 2315, pp. 153-163, Dec. 2012. [28] M. Yildirimoglu, M. Ramezani, and N. Geroliminis, “Equilibrium analysis and route guidance in large-scale networks with MFD dynamics,”Transp. Res. C, Emerg. Technol. , vol. 59, pp. 404-420, Oct. 2015. [29] C. E. Garcia, D. M. Prett, and M . Morari, “Model predictive control: Theory and practice-A survey,” Automatica , vol. 25, no. 3, pp. 335-348, 1989. [30] D. Q. Mayne, J. B. Rawlings, C. V . Rao, and P. O. M. Scokaert, “Constrained model predictive control: Stability and optimality,” Automatica , vol. 36, no. 6, pp. 789-814, 2000. [31] G. Gomes and R. Horowitz, “Optimal freeway ramp metering using the asymmetric cell transmission model,” Transp. Res. C, Emerg. Technol. , vol. 14, no. 4, pp. 244-262, 2006. [32] I. Papamichail, A. Kotsialos, I. Margonis, and M. Papageorgiou, “Coordinated ramp metering for freew ay networks-A model-predictive hierarchical control approach,” Transp. Res. C, Emerg. Technol. , vol. 18, no. 3, pp. 311-331, 2010. [33] M. Hajiahmadi et al. , “Integrated predictive control of freeway networks using the extended link transmission model,” IEEE Trans. Intell. Transp. Syst., vol. 17, no. 1, pp. 65-78, Jan. 2016. [34] A. Hegyi, B. De Schutter, and J. H ellendoorn, “Optimal coordination of variable speed limits to suppress shock waves,” IEEE Trans. Intell. Transp. Syst. , vol. 6, no. 1, pp. 102-112, Mar. 2005. [35] J. R. D. Frejo, A. Núñez, B. De Schutter, and E. F. Camacho, “Hybrid model predictive control for freeway traffic using discrete speed limit signals,” Transp. Res. C, Emerg. Technol. , vol. 46, pp. 309-325, Sep. 2014. [36] A. Hegyi, B. De Schutter, and J . Hellendoorn, “Model predictive control for optimal coordination of ramp metering and variable speedlimits,” Transp. Res. C, Emerg. Technol. , vol. 13, no. 3, pp. 185-209, Jun. 2005. [37] A. Karimi, A. Hegyi, B. De Schu tter, H. Hellendoorn, and F. Middelham, “Integration of dynamic route gui dance and freeway ramp metering using model predictive control,” in Proc. Amer. Control Conf. ,v o l .6 . Jul. 2004, pp. 5533-5538. [38] S. Lin, B. De Schutter, Y . Xi, and H. Hellendoorn, “Fast model predictive control for urban road networks via MILP,” IEEE Trans. Intell. Transp. Syst., vol. 12, no. 3, pp. 846-856, Sep. 2011. [39] Z. Zhou, B. De Schutter, S. Lin, and Y . Xi, “Multi-agent modelbased predictive control for large-scale urban traffic networks using aserial scheme,” IET Control Theory Appl. , vol. 9, no. 3, pp. 475-484, 2015. [40] M. Van den Berg, A. Hegyi, B. De Schutter, and H. Hellendoorn, “Integrated traffic control for mixed urban and freeway networks: A model predictive control approach,” Eur. J. Transp. Infrastruct. Res. , vol. 7, no. 3, pp. 223-250, 2007. [41] L. Li, R. R. Negenborn, and B. De Schutter, “Distributed model predictive control for c ooperative synchromodal freight transport,” Transport. Res. Part E , 2016. [Online]. Available: http://dx.doi.org/10.1016/j.tre.2016.08.006 [42] B. Kersbergen, T. van den Boom, and B. De Schutter, “Distributed model predictive control for railway traffic management,” Transp. Res. C, Emerg. Technol. , vol. 68, pp. 462-489, Jul. 2016. [43] N. Geroliminis, J. Haddad, and M. Ramezani, “Optimal perimeter control for two urban regions with m acroscopic fundamental diagrams: A model predictive approach,” IEEE Trans. Intell. Transp. Syst. , vol. 14, no. 1, pp. 348-359, Mar. 2013.[44] J. Haddad, M. Ramezani, and N. Geroliminis, “Cooperative traffic control of a mixed network with two urban regions and a freeway,”Transp. Res. B, Methodol. , vol. 54, no. 8, pp. 17-36, Aug. 2013. [45] M. Hajiahmadi, J. Haddad, B. De Schutter, and N. Geroliminis, “Optimal hybrid perimeter and switching plans c ontrol for urban traffic networks,” IEEE Trans. Control Syst. Technol. , vol. 23, no. 2, pp. 464-478, Mar. 2015. [46] M. Hajiahmadi, V . L. Knoop, B. De Schutter, and H. Hellendoorn, “Optimal dynamic route guidance: A model predictive approach usingthe macroscopic fundamental diagram,” in Proc. 16th Int. IEEE Conf. Intell. Transp. Syst. , Oct. 2013, pp. 1022-1028. [47] R. Lamotte and N. Geroliminis, “The morning commute in urban areas: Insights from theory and simulation,” in Proc. 95th Annu. Meet. Transp. Res. Board , 2016, paper 16-2003, p. 20. [Online]. Available:

$$
https://trid.trb.org/view.aspx?id=1392730
$$

[48] L. Ambühl and M. Menendez, “Data fusion algorithm for macroscopic fundamental diagram estimation,” Transp. Res. C, Emerg. Technol. , vol. 71, pp. 184-197, Oct. 2016. [49] M. Diehl, H. J. Ferreau, and N. Haverbeke, “Efficient numerical methods for nonlinear MPC and moving horizon estimation,” in Nonlinear Model Predictive Control . Berlin, Germany: Springer, 2009, pp. 391-417. [50] M. Diehl, H. G. Bock, H. Diedam, and P.-B. Wieber, “Fast direct multiple shooting algorithms for optimal robot control,” in Fast Motions in Biomechanics and Robotics . Berlin, Germany: Springer, 2006, pp. 65-93. [51] H. G. Bock and K. J. Plitt, “A multip le shooting algorithm for direct solution of optimal control problems,” in Proc. 9th IFAC World Congr. , Budapest, Hungary, 1984, pp. 242-247. [52] A. Wächter and L. T. Biegler, “On the implementation of an interiorpoint filter line-search algorithm for large-scale nonlinear programming,” Math. Programm. , vol. 106, no. 1, pp. 25-57, 2006. [53] J. Andersson, “A general-purpose s oftware framework for dynamic optimization,” Arenberg Doctoral Sc hool, Dept. Elect. Eng. (ESAT/SCD) Optim. Eng. Center, KU Leuven, Heverlee, Belgium, Oct. 2013. [54] M. Ben-Akiva and M. Bierlaire, “Discrete choice methods and their applications to short term travel decisions,” in Handbook of Transportation Science . New York, NY , USA: Springer, 1999, pp. 5-33. [55] M. Keyvan-Ekbatani, M. Yildirimoglu, N. Geroliminis, and M. Papageorgiou, “Multiple concentric gating traffic control in largescale urban networks,” IEEE Trans. Intell. Transp. Syst. , vol. 16, no. 4, pp. 2141-2154, Aug. 2015. Isik Ilber Sirmatel received the B.Sc. degree in mechanical and control engineering from IstanbulTechnical University, Turkey, in 2010, and the M.Sc. degree in mechanical engineering from the Swiss Federal Institute of Technology, Zurich, Switzerland,in 2012 and 2014, respectively. He is currently pur-suing the Ph.D. degree in electrical engineering with the Urban Transport Systems Laboratory, School of Architecture, Civil and Environmental Engineering,École Polytechnique Fédé rale de Lausanne, Lausanne, Switzerland. His current research interests include automatic control, optimization, and model predictive control, withapplications to control of transportation systems. Nikolas Geroliminis received the Diploma in civil engineering from the National Technical Universityof Athens, and the M.Sc. and Ph.D. degrees in civil engineering from the University of California at Berkeley, Berkeley, CA, USA. He is an AssociateProfessor with the École Polytechnique Fédérale de Lausanne (EPFL), Lausanne, and the Head of the Urban Transport Systems Laboratory. Before joiningEPFL, he was an Assistant Professor with the facultyof the Department of Civil Engineering, University of Minnesota. His research interests focus primarily on urban transportation systems, traffic flow theory and control, publictransportation and logistics, on-demand transportation, optimization and largescale networks. He is a member of the Transportation Research Board’s Traffic Flow Theory Committee. He is a recent recipient of the ERC starting grant METAFERW: Modeling and Controlling Traffic Congestion and Propagationin Large-Scale Urban Multimodal Networks. He also serves as an Associate Editor in Transportation Research, Part C, Transportation Science and the IEEE T RANSACTIONS ON INTELLIGENT TRANSPORTA TION SYSTEMS and in the Editorial Board of Transportation Research, Part B, Journal of Intelligent Transportation Systems and of many international conferences.
