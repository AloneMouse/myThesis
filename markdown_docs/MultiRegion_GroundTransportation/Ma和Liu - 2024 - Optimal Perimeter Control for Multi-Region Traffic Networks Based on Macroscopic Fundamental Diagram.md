---
source_pdf: Ma和Liu - 2024 - Optimal Perimeter Control for Multi-Region Traffic Networks Based on Macroscopic Fundamental Diagram.pdf
pages: 12
---

# Ma和Liu - 2024 - Optimal Perimeter Control for Multi-Region Traffic Networks Based on Macroscopic Fundamental Diagram

<!-- page 1 -->

Received 7 April 2024, accepted 25 April 2024, date of publication 29 April 2024, date of current version 7 May 2024. Digital Object Identifier 10.1 109/ACCESS.2024.3394717 Optimal Perimeter Control for Multi-Region Traffic Networks Based on Macroscopic Fundamental Diagram YAFENG MA 1,2AND ZUOMAN LIU1 1School of Transportation Engineering, East China Jiaotong University, Nanchang 330013, China 2Postdoctoral Research Center of Transportation Engineering, East China Jiaotong University, Nanchang 330013, China Corresponding author: Yafeng Ma (3028@ecjtu.edu.cn) This work was supported in part by the National Natural Science Foundation of China under Grant 52002127 and Grant 52262048, in part by Jiangxi Provincial Youth Project for Humanities and Social Sciences Research in Universities under Grant GL21201, in part by the Education of Humanities and Social Science Research on Youth Fund Project under Grant 19YJC630121, and in part by the Science and Technology Research Project of Department of Education in Jiangxi Province under Grant GJJ200669. ABSTRACT In order to improve the urban traffic operational state of traffic networks, this paper proposed a new optimal perimeter control strategy based on macroscopic fundamental diagram (MFD). Firstly, the traffic flow equilibrium model for monocentric region networks was established by analyzing the matching in-flow and out-flow relationship of adjacent regions, as well as the traffic flow equilibrium model for multi-region networks. Secondly, an optimal perimeter control model was built, based on the traffic network state equation and perimeter control condition, to optimize the overall operation benefit of the macroscopic networks. According to the optimal control condition, the critical in-flow and out-flow rates on the boundary of the sub-regions could be calculated. And then the optimization method of signal timing for the boundary intersections was presented with the aim of reducing their saturation degree rapidly. Lastly, the local network at 1st Ring Road, Chengdu was chosen as the test object to compare the effect of no perimeter control (NPC), Bang-Bang perimeter control (PC) and optimal perimeter control (OPC) proposed in this paper by simulation. The result showed that compare with NPC, PC could improve the overall operation benefit of the macroscopic networks with 33.73%, while OPC is 57.09%. In the meantime, compare with PC, the accumulating volume of every sub-region was reduced even bigger under OPC, which meant that OPC could improve road network operation efficiency and alleviate regional traffic congestion more effectively. INDEX TERMS Urban traffic, perimeter control, macroscopic fundamental diagram, traffic sub-region, feedback control.

## I. INTRODUCTION

Urban motorization greatly improved the velocity and intensity of people and freight circulating within and between cities, which is one of the important driving forces for rapid development of economic and living standard. At the same time, urban traffic congestion, especially regional traffic congestion, often occurs and gradually becomes one of the obstacles that hinders and limits the sustainable development of cities. Fortunately, regional control systems such as TRANSYT, SCATS, and SCOOT was developed, which give us a solution for urban road network traffic control, but their The associate editor coordinating the review of this manuscript and approving it for publication was Jianxiang Xi .control effectiveness is poor in saturated environments [1]. Control systems based on advanced complex algorithms such as OPAC [2], RHODES [3], SPOT/UTOPIA [4], etc., are difficult to apply in real-time traffic congestion control due to their large computational requirements. In the practice of regional traffic congestion control, researchers found that the control strategy should not only focus on the congested intersections and road segments in the region, but also the uncongested neighboring regions, exploring the variation of traffic flow between different regions, avoid the congestion drifting from one place to another, and achieve effective regional traffic congestion control. Thanks to the Macroscopic Fundamental Diagram (MFD) [5], which established a unimodal and low-dispersion relationship model between VOLUME 12, 2024

## 2024 The Authors. This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 License.

For more information, see https://creativecommons.org/licenses/by-nc-nd/4.0/ 61937

<!-- page 2 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD the accumulative volume (A V) and flowing-out rate of the regional road network, providing a theoretical basis and support for effective regional traffic congestion control. The physical model of MFD was first proposed by Godfrey in 1969 [5]. Daganzo theoretically proved its existence and subsequently confirmed the existence of MFD in real traffic networks based on traffic detection data in Yokohama in

## 2007 [6], [7], [8]. With more than ten years’ research,

the fundamental characteristics [9], [10], influencing factors [11], and practical applications [12], [13] of MFD were developed and numerous research achievements were obtained. The researches shown that MFD is an inherent attribute of urban road networks, only related to the road network itself, and not dependent on the OD distribution and its changes. The MFD model can intuitively describe the relationship between accumulative volume and flowing-out rate of regional road networks [14], [15]. At the same time, the lower the heterogeneity of the road network, the lower the degree of MFD dispersion [16]. This characteristic has led to rapid development and application of perimeter control strategies in urban traffic congestion control. The perimeter control, with the controlling of the traffic flow control facilities, such as the traffic signals, ramps at the boundaries of the regions, regulating the traffic flow between the different regions to make the accumulative volume in appropriate range, ensuring efficient operation of the controlled area. Daganzo first proposed a perimeter control method with the goal of maximizing the flowing-out rate of a single area in 2007 and proved that Bang-Bang control is the optimal control strategy [6]. Subsequent studies by Yang Xiaoguang and other researchers also proved its effectiveness [17]. Keyvan-Ekbatani et al. proposed a perimeter control model based on PI gate and verified its robustness [18]. Haddad and Geroliminis analyzed the stability of perimeter control in a twin-zone urban traffic system based on MFD [19]. Geroliminis et al. established a perimeter control model based on traffic flow prediction models, but it is difficult to apply it to engineering practice due to the limitations of actual prediction accuracy [20]. Ding et al. established boundary control models for congested areas in urban road networks with two sub-regions [21], [22] and multi-regions [23], respectively, with the objectives of maximizing the completion rate of vehicles in the road network and minimizing the number of blocked vehicles at the region boundaries, and provided corresponding signal timing optimization methods. Besides, for a typical urban traffic network composed of freeways and arterials, an integrated control method was proposed to effectively adjust and coordinate the traffic flow between the two subnetworks [24]. With the consideration of real-time traffic flows and queue dynamics, Guo et al. proposed a perimeter traffic control strategy for single urban congested region with MFD model and boundary conditions to improve the efficiency of the protected urban region and avoid the queue spillbacks at border links [25]. Considering the poor adaptive ability of traditional PID control, Yang et al. proposed a method combined MFD and fuzzyRBF neural network PID, reduced the congestion degree and improved the efficiency of urban networks [26]. Zheng and Wu proposed a new traffic control strategy based on multi-agent reinforcement learning (MARL), which solved the shortage of lacking feedback of traditional urban traffic control systems [27]. To adapt the spatial-temporal evolution of traffic congestion, percolation theory was introduced by Hamedmoghadam et al. and a traffic signal control method was proposed with time-varying geometry, which successfully balances the traffic flow capacity of the network and improves the performance [28]. To avoid possible long queues and delays at the perimeter of the controlled area, Fu et al. using colored Petri Nets established an enhanced MFD model, which integrated the gated intersections and segments as the boundary buffers, combined with route guidance, the integrated perimeter control strategy is effective in simulation [29]. As the traditional MFD model always restricted by the heterogeneity of road network, Gao et al. come up with the road network traffic carrying capacity model and a new perimeter coordination control framework, with the simulation based on SUMO software, the proposed perimeter control strategy is demonstrated to have impressive performance [30]. In order to cooperate the traffic signals in urban network, Li et al. developed a higher-order conflict graph approach to describe the connectivity and traffic flow movements of the upstream or downstream intersections, then cooperate multiple inter-sections and make the traffic flow operating in high efficiency [31]. Dantsuji et al. studied the travelers’ behavior changes in response to perimeter control with transit priority in a mixed bimodal transportation system, the result shows that transit priority may not be sufficient to promote the use of flexible route transit (FRT), and additional incentive may be required to encourage FRT use during perimeter control [32]. Under the disruption of extreme weather events, Zhu et al. proposed a network resilience curve based perimeter control strategy to facilitate the network equilibrium [33]. The current research based on MFD has obtained numerous achievements, nonetheless, the majority of studies are focuses on improving the operation efficiency of inner subregions, while neglecting the impact of perimeter control on the external sub-regions, which can easily drift the congestion from inner controlled sub-regions to the uncontrolled external sub-regions, preventing the whole network from reaching system optimization. Therefore, this paper proposed an optimal perimeter control method suitable for multiple sub-regions to regulates the traffic flow rates entering and exiting each sub-region to achieve the optimal operation efficiency of the road network. The rest of this paper is structured as follows: section II is the brief introduction to the characteristics of macroscopic fundamental diagram (MFD). Section IIIis the methodology, where subsection III.A is the notations explanations of symbols and abbreviations, subsection III.B is the traffic flow balance model for multi-region networks, subsection III.C is the optimal perimeter control model for multi-region traffic

## 61938 VOLUME 12, 2024

<!-- page 3 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD networks and subsection III.D is the signal control method of boundary intersections. Section IVis the experiment and section Vare the discussion and pointers for future research.

## II. MACROSCOPIC TRAFFIC CHARACTERISTICS OF

RGIONAL ROAD NETWORK According to the research results of Daganzo, Geroliminis, as shown in [6],[7], and [8], for a relatively homogeneous road network, there is a certain relationship between the accumulative volume, n(t), and the flowing-out rate, qout(t), which is called the Macroscopic Fundamental Diagram (MFD), as shown in Fig. 1.

#### FIGURE 1. Macroscopic fundamental diagram of traffic network.

The MFD has the following main characteristics: ①There is a basic trend between the flowing-out rate of the road network (including the flow arrive at the destination within the area and the flow out of the area) and its accumulative volume. When the accumulative volume, n(t) is small, the flowing-out rate, qout(t) will increase with the accumulative volume synchronously, and the two parameters roughly show a linear relationship. When n(t) increases to the critical accumulative volume, ˆn,qout(t) will show a certain degree of instability. As n(t) continues to increase, qout(t) will gradually decrease until the road network is completely congested, at which point the accumulative volume of the road network reaches the maximum value, nmax, and the flowing-out rate of the road network, qout(t), approaches 0. This relationship can be fitted with a cubic function. ②Hysteresis phenomenon. When the accumulative volume, n(t) approaches or reaches the critical accumulative volume, the flowing-out rate, qout(t) begins to be unstable. If the accumulative volume continues to increase, the flowing-out rate starts to decrease. Even if the accumulative volume decreases below the critical accumulative volume in a short time, it is difficult for the flowing-out rate of the road network to quickly recover to the original level, but there will be a certain degree of growth as the accumulative volume of the road network decreases. With regard to the shape of the MFD, early studies generally believed that it was triangular, while subsequent studies suggested that it is close to trapezoidal, and can

$$
be represented by a cubic equation qout(t)=a×n3(t)+
$$

b×n2(t)+c×n(t)+d. Based on the characteristics of the MFD, in perimeter control practice, the accumulative volumeTABLE 1. Symbols and abbreviations used in this paper. of the road network, ñ, should be controlled slightly below the critical accumulative volume, as shown in Fig. 1, to ensure the effectiveness of the perimeter control strategy.

## III. METHODOLOGY

A. NOTATIONS To improve the clarity of descriptions and explanations related to urban transportation network analysis and optimal perimeter control, we have compiled a detailed list of symbols and abbreviations used in this paper. For their comprehensive representation, please refer to Tab. 1. B. TRAFFIC FLOW BALANCE MODEL FOR MULTI-REGIONS NETWORK 1) TRAFFIC FLOW EQUILIBRIUM MODEL FOR MONOCENTRIC REGION NETWORK As shown in Fig. 2, the city’s traffic network is divided intoNsub-regions. Assuming that every sub-region has a VOLUME 12, 2024 61939

<!-- page 4 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD

#### FIGURE 2. Schematic of a multi-region network with macroscopic

fundamental diagram.

$$
well-defined macroscopic fundamental diagram (MFD i,i=
$$

1, 2, ..., N), where ni(t) represents the accumulative volume of sub-region iat time t. Correspondingly, nmax irepresents the maximum accumulative volume of sub-region i,qin(t) and qout(t) represent the traffic flow rates entering and leaving sub-region iat time t, respectively. According to the law of flow conservation, for any sub-region i, the accumulative volume at time tis:

$$
ni(t)=\intt
$$

t0[qiin(t)-qiout(t)]dt+ni(t0) (1) where ni(t0) is the initial accumulative volume of sub-region iat the initial time, t0. By differentiating both sides of equation (1), the traffic flow balance equation for sub-region iat time tis: dni(t)

$$
dt=qiin(t)-qiout(t) (2)
$$

Define piin(t) is the entering traffic flow rate through the boundary of sub-region i,diin(t) is the entering traffic flow rate originate from sub-region iitself, while piout(t) is the leaving traffic flow rate through the boundary of sub-region ianddiout(t) is the leaving traffic flow rate with sub-region i as the destination. It is obvious that:

$$
qiin(t)=piin(t)+diin(t) (3)
$$

$$
qiout(t)=piout(t)+diout(t) (4)
$$

Based on the position and physical meaning of the boundary, the traffic flow, piin(t) and piout(t), which entering and leaving sub-region ithrough the boundary, are controlled by the boundary signals, while diin(t) and diout(t), as subregion iis the origin and destination, cannot be controlled by the boundary signal. Assume that the traffic flow rate entering the sub-region through its boundary, piin(t), is distributed in a stable proportion to the total flowing-in rate, qiin(t), as well as the relationship between piout(t) and qiout(t). Define the proportion as αiinandαiout, then we can obtain: /braceleftigg

$$
αiin=piin(t)/slashbig
$$

qiin(t)

$$
αiout=piout(t)/slashbig
$$

qiout(t)(5)Combine equation (3),(4)and(5), the relationship between diin(t) and qiin(t),diout(t) and qiout(t) can be deduced as follows:/braceleftigg

$$
diin(t)=qiin(t) (1-αiin)
$$

$$
diout(t)=qiout(t) (1-αiout)(6)
$$

According to the 1stcharacteristic of the macroscopic fundamental diagram of the regional network: the outflow of sub-region iis a function of its accumulative volume, i.e.:

$$
qiout(t)=Oi(ni(t)) (7)
$$

where Oirefers to the relationship between qiout(t) and ni(t). At the same time, based on the matching relationship between sub-region iand other sub-regions in Fig. 2, the boundary flowing-in rate of sub-region ican be expressed as:

$$
piin(t)=N\sum
$$

$$
j=1βji(t)pjout(t)
$$

=N\sum

$$
j=1βji(t)αjoutOj/parenleftbig
$$

nj(t)/parenrightbig (8) where βjiis the ratio of the traffic flow rate entering subregion ifrom sub-region jto the total boundary outflow rate of

$$
sub-region j,\sumN
$$

$$
i=1βji=1, and when sub-regions iandjare
$$

$$
not adjacent, βji=0. Furthermore, when j=i,βji=0, as the
$$

traffic flow with the origin and destination in the sub-region itself cannot be controlled by the boundary signals. αjoutis the proportion of the boundary outflow of sub-region jto its total outflow.

#### FIGURE 3. Diagram of monocentric region network with macroscopic

fundamental diagram. For example, a typical monocentric traffic network, as show in Fig. 3, sub-region 1 is the central region and surrounded by sub-region 2 and sub-region 3, then the boundary flowing-in rate of sub-region 1 is:

$$
p1in(t)=3\sum
$$

$$
j=1βj1(t)pjout(t)
$$

$$
=β21(t)p2out(t)+β31(t)p3out(t)
$$

$$
=β21(t)α2outO2(n2(t))+β31(t)α3outO3(n3(t))
$$

(9)

## 61940 VOLUME 12, 2024

<!-- page 5 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD Similarly, the boundary flowing-in rate of sub-region 2 and sub-region 3 can be obtained as follows:

$$
p2in(t)=3\sum
$$

$$
j=1βj2(t)pjout(t)
$$

$$
=β12(t)p1out(t)+β32(t)p3out(t)
$$

$$
=β12(t)α1outO1(n1(t))+β32(t)α3outO3(n3(t))
$$

(10)

$$
p3in(t)=3\sum
$$

$$
j=1βj3(t)pjout(t)
$$

$$
=β13(t)p1out(t)+β23(t)p2out(t)
$$

$$
=β13(t)α1outO1(n1(t))+β23(t)α2outO2(n2(t))
$$

(11) Combined with equation (2)-(5), the traffic flow balance equations of the three sub-regions in Fig. 3can be derived as: dn1(t)/slashbig

$$
dt=q1in(t)-q1out(t)
$$

=/parenleftbig 1/slashbig α1in/parenrightbig p1in-q1out(t) =/parenleftbig 1/slashbig α1in/parenrightbig [β21(t)α2outO2(n2(t)) +β31(t)α3outO3(n3(t))]-O1(n1(t))(12) dn2(t)/slashbig

$$
dt=q2in(t)-q2out(t)
$$

=/parenleftbig 1/slashbig α2in/parenrightbig p2in-q2out(t) =/parenleftbig 1/slashbig α2in/parenrightbig [β12(t)α1outO1(n1(t)) +β32(t)α3outO3(n3(t))]-O2(n2(t))(13) dn3(t)/slashbig

$$
dt=q3in(t)-q3out(t)
$$

=/parenleftbig 1/slashbig α3in/parenrightbig p3in-q3out(t) =/parenleftbig 1/slashbig α3in/parenrightbig [β13(t)α1outO1(n1(t)) +β23(t)α2outO2(n2(t))]-O3(n3(t))(14) Based on the above analysis, the traffic flow balance equation for sub-region iwith multi-adjacent regions can be derived as follows: dni(t)

$$
dt=qiin(t)-qiout(t)
$$

=/parenleftbig 1/slashbig αiin/parenrightbig piin(t)-qiout(t) =/parenleftbig 1/slashbig

$$
αiin/parenrightbigN\sum
$$

$$
j=1βji(t)αjoutOj/parenleftbig
$$

nj(t)/parenrightbig -Oi(ni(t)) (15) 2) TRAFFIC FLOW EQUILIBRIUM MODEL FOR MULTI-REGION NETWORKS For convenience of calculation, introduce the Hadamard Product matrix operator ‘‘◦’’ and define the element-division operator ‘‘•/’’: for any two matrices with same size, X,Y∈

$$
RM×N, the matrix Z=X◦Y=[(xij)×(yij)],K=X•/Y=
$$

[(xij)÷(yij)]. Extend the monocentric region traffic flow equilibrium model, as shown in equation (15), to a multi-region network,we can obtain the multi-region network traffic flow equilibrium model as follows: dn(t)

$$
dt=A◦{B(t)[αout◦O(n(t))]}-O(n(t)) (16)
$$

where n(t)∈RNrepresents the accumulative volumes of

$$
the sub-regions, A=[1/α iin]∈RNrepresents the proportion
$$

vector of the total flowing-in rates and the entering traffic

$$
flow rate through the boundary for every sub-region, B(t)=
$$

[βji(t)]∈RN×Nrepresents the proportional distribution matrix of the outflow through the boundary from every sub-region to its adjacent sub-regions. Since the internal flowing-in and flowing-out flow within every sub-region is

$$
not considered, βii=0.αout∈RNrepresents the proportion
$$

of boundary outflow and total outflow of every sub-region, O(n(t ))∈RNrepresents the outflow of the sub-regions, which is a function of the accumulative volume of every sub-region.

## C. OPTIMAL PERIMETER CONTROL MODEL FOR

MULTI-REGION NETWORK 1) NETWORK TRAFFIC STATE EQUATION According to the 1stcharacteristic of macroscopic fundamental diagram of the regional network, it can be known that for any sub-region i, there exists a critical accumulative

$$
volume (i =1, 2, ..., N), under which the outflow rate of
$$

sub-region iwill reach its maximum value. At this point, the nonlinear model in equation (15) will satisfy the following equation at a set of stationary points,/parenleftig ˆni,ˆβji/parenrightig of the MFD of sub-region i: dni(t)

$$
dt=/parenleftbig
$$

1/slashbig

$$
αiin/parenrightbigN\sum
$$

$$
j=1ˆβji(t)αjoutOj/parenleftbig
$$

ˆnj(t)/parenrightbig -Oi/parenleftbig ˆni(t)/parenrightbig =0 (17)

$$
Let1x=x- ˆxand apply it to all variables, then unfold
$$

equation (17) at the stationary point,/parenleftig ˆni,ˆβji/parenrightig , using the first-order Taylor series: d(1ni(t)) dt=1n• i(t) =1

$$
αiinN\sum
$$

$$
j=11βji(t)αjoutOj/parenleftbig
$$

ˆnj(t)/parenrightbig +1

$$
αiinN\sum
$$

$$
j=1ˆβji(t)αjoutO′j/parenleftbig
$$

ˆnj(t)/parenrightbig/parenleftbig 1nj(t)/parenrightbig -O′i/parenleftbig ˆni(t)/parenrightbig (1ni(t)) (18) By extending equation (18) to a multi-region network as shown in Fig. 2, the network traffic state equation (in vector form) can be obtained as follows:

$$
1•n(t)=C1n(t )+D1β (t) (19)
$$

$$
where 1n(t )∈RNis the state difference vector, 1ni=
$$

ni-ˆni, which represents the difference between the VOLUME 12, 2024 61941

<!-- page 6 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD accumulative volume vector and the critical accumulative volume vector of every sub-region. 1β(t)∈RMis the

$$
control difference variable, 1βji=βji-ˆβji, which represents
$$

the difference between the proportional outflow distribution vector and its critical distribution vector of every sub-region, distributed by column. CandDare the state matrix and control matrix, C∈RN×Nis a square matrix with its

$$
diagonal elements can be expressed as Cii= -O′
$$

i/parenleftbig ˆni(t)/parenrightbig ,

$$
and if sub-region jis adjacent to sub-region i,Cji=/parenleftbig
$$

αjout/slashbig αiin/parenrightbigˆβjiO′ j/parenleftbig ˆnj(t)/parenrightbig

$$
; otherwise, Cji=0.D∈RN×M
$$

is a matrix based on the number of sub-region divisions

$$
and their adjacency, M\le N2, if sub-region jis adjacent
$$

$$
to sub-region i,Dji=/parenleftbig
$$

αjout/slashbig αiin/parenrightbig Oj/parenleftbig ˆnj(t)/parenrightbig ; otherwise, Dji=0. 2) CONTROL AT THE SUB-REGION BOUNDARIES In order to achieve the optimal operating state of the road network, it is necessary to adjust and control the flowing-in rates of the sub-regions from their adjacent sub-regions based on the MFD theory, that is, adjust the adjacent sub-regions’ boundary outflow distribution matrix B(t). When the macroscopic fundamental diagram of every sub-region in the network are determined, the critical accumulative volume and outflow rate are also determined. The operating state of every sub-region can be optimized dynamically by adjusting the flowing-in rates. In perimeter control practice, due to the restrictions of the minimum green time and the maximum cycle time, the proportion distribution of boundary flows of all sub-regions needs to satisfy:

$$
βji,min\le βji(t)\le βji,max (20)
$$

where βji,min andβji,max are the minimum and maximum outflow proportions, respectively, under the conditions of the minimum green time and the maximum cycle time, and βji,min >0, which is the guarantee to avoid overflow in the target region. At the same time, in order to reduce the impact of overflow on the overall performance of the network, at any time during the control process, the accumulative volume ni(t) of every sub-region should satisfy the following constraint:

$$
0\le ni(t)\le ni,max (21)
$$

3) CONTROL SYSTEM OBJECTIVES AND CONTROLLER DESIGN For a monocentric road network, the control objective is to minimize the travel time, including the waiting time at the boundaries and the travel time in the network. In order to achieve this objective, the common control strategy is the Bang-Bang control, which means that if the accumulative volume in the road network not exceeding the critical accumulative volume, vehicles enter the controlled roadnetwork at the maximum flowing-in rate; once the accumulative volume exceeds the critical accumulative volume, the flowing-in rate is quickly reduced to the minimum. The control strategy can be expressed as:

$$
qin(t)=/braceleftigg
$$

qmax ifn(t)<ˆn qmin else(22) where qmaxand qminare the maximum and minimum flowing-in rates, respectively. It has been proven that Bang-Bang control has good control effects on relatively slow dynamic systems, but the switching between maximum and minimum flowing-in rates can cause system oscillations. For a macroscopic traffic network with multiple subregions, the control objective should be maximizing the total outflow of the network as a whole. However, if every subregion adopts the Bang-Bang control strategy separately, it will cause uneven distribution of the accumulative volumes, enhance heterogeneity among controlled sub-regions, and reduce the total outflow of the network, thereby reducing the operational efficiency of the network. In order to maximize the total outflow of the network with multiple sub-regions, it is necessary to not only consider the accumulative volumes of every sub-region, but also consider the distribution of interchange volumes at the boundaries of every subregion. By adjusting the green signal ratio distribution matrix of boundary intersections to control the flowing-out rates distribution proportion, βji, make it near the critical distribution proportion, so as the accumulative volumes of every sub-region close to their critical accumulative volumes, ensuring the maximization of the outflow rates of every sub-region. Therefore, the objective of maximizing the total outflow can be decomposed into: ①minimize the difference between the accumulative volumes of every sub-region and their critical accumulative volumes, ②minimize the difference between the proportional outflow rates from adjacent sub-regions and their critical outflow rates, that is:

$$
8(n, β)=min\inttf
$$

t0/parenleftbigg/vextenddouble/vextenddouble1n(t )•/ˆn/vextenddouble/vextenddouble2+/vextenddouble/vextenddouble/vextenddouble1β(t)•/ˆβ/vextenddouble/vextenddouble/vextenddouble2/parenrightbigg dt (23) where 8(n, β) is the performance index of the controlled network’s operational efficiency, t0andtfare the starting

$$
and ending time of the control strategy, 1n(t)=n(t)-ˆn
$$

and1β(t)=β(t)-ˆβare the state difference variables and control difference variables of the multi-region network, respectively. The element-division operation is proposed for non-dimensional standardization of the state difference variables and control difference variables. Since traffic control system is a discrete in time and has a certain periodicity, equation (23)can be simplified as: 8(n, β)

$$
=min\intt0+k1t
$$

t0+(k-1)1t/parenleftbigg/vextenddouble/vextenddouble1n(t )•/ˆn/vextenddouble/vextenddouble2+/vextenddouble/vextenddouble/vextenddouble1β(t)•/ˆβ/vextenddouble/vextenddouble/vextenddouble2/parenrightbigg dt (24)

## 61942 VOLUME 12, 2024

<!-- page 7 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD In order to minimize the state and control differences of every sub-region under the constraint of the macroscopic traffic network state equation (19), the designed multi-variable feedback control is as follows: β(t)=ˆβ-K/parenleftbig n(t)-ˆn/parenrightbig (25) where Kis the steady-state solution of the Riccati equation corresponding to the network traffic state equation at time t, as shown in [34], which only depends on the state matrix C and control matrix D.

## D. PERIMETER SIGNAL CONTROL METHOD

The optimal perimeter control model of the multi-region network mentioned above can effectively determine the outflow and their proportional distribution of every sub-region to its adjacent sub-regions. However, the traffic flow exchange between adjacent sub-regions is completed through boundary intersections, so corresponding boundary intersection control methods need to be designed.

#### FIGURE 4. Diagram of perimeter control for two adjacent sub-regions.

Taking Fig. 4 as an example, iand jare adjacent sub-regions, intersection groups 2, 3, 4, and 5, 6, 7 are signal-controlled intersections at the boundaries of the two sub-regions, relatively. As the sub-region boundary is an artificial virtual boundary, the transformation of the traffic flow between adjacent sub-regions are all completed through boundary intersections. Adjusting the signal timing parameters of intersections 2, 3, 4 can dynamically adjust the traffic flow from sub-region ito sub-region j. Correspondingly, adjusting the signal control parameters of intersections 5, 6, 7 can regulate the traffic flow from sub-region jto subregion i. ensure the smooth transportation channel between adjacent sub-regions, avoiding traffic congestion and overflow between adjacent sub-regions due to the lack of coordination of signal timing parameters at adjacent intersections, which would affect the effectiveness of boundary control. In order to control the traffic flow rate from sub-region ito sub-region j, assuming that there are mchannels connecting the two sub-regions, and the lth channel connects nflow directions from sub-region ito sub-region j, the minimum traffic volume from sub-region ito sub-region jin period tis:

$$
qij,min(t)=m\sum
$$

$$
l=1n\sum
$$

$$
h=1qlh,min(t) (26)
$$

where qlh,min (t) is the minimum traffic volume entering the

$$
channel from phase hof the intersection on the boundary ofsub-region iof the lth channel in time period t;l=1, 2, ...,
$$

$$
m;h=1, 2, ..., n.
$$

Similarly, in period t, under the constraints of the maximum green time and maximum cycle length for each phase, the maximum traffic volume from sub-region ito subregion jis:

$$
qij,max(t)=m\sum
$$

$$
l=1n\sum
$$

$$
h=1qlh,max (t) (27)
$$

where qlh,max (t) is the maximum traffic volume entering the channel from phase hof the intersection on the boundary of

$$
sub-region iof the lth channel in time period t;l=1, 2, ...,
$$

$$
m;h=1, 2, ..., n.
$$

As mentioned earlier, the proportion of traffic flow from sub-region ito sub-region jin time period t, is a proportion of the total outflow from the boundary of sub-region i, is denoted asβij(t). The traffic flow from sub-region ito sub-region jin time period t can be calculated as:

$$
qij(t)=βij(t)αi,outOi(t) (28)
$$

$$
①When qij(t)\le qij,min(t), then the actual traffic flow from
$$

sub-region ito sub-region jis itself, and the green signal ratio for each intersection phase can be set to λlh,min(t).

$$
②When qij(t)\ge qij,max(t), then the actual traffic flow from
$$

sub-region ito sub-region jis the maximum traffic volume qij,max(t), and the green signal ratio for each intersection phase should be set to λlh,max(t). ③When qij,min(t)<qij(t)<qij,max(t), then there can be multiple assignment schemes for the traffic flow from sub-region ito sub-region j, such as equal distribution. However, considering that the capacity of each intersection on the boundary may be different due to the location, traffic conditions, geometric parameters, etc., equal distribution may result in significant differences in saturation levels at different intersections. It is preferable to prioritize reducing the saturation of the intersections with higher saturation levels to improve the overall traffic efficiency of the intersections at the sub-region boundary. In the perimeter control, assuming that the saturation flow at the intersection on the lthchannel of the boundary of sub-region iisSi l, then the green signal ratio of phase h, λlh(t) is approximately equal to its saturation level, i.e., under the conditions of the minimum traffic volume qlh,min (t) and maximum traffic volume qlh,max (t), the green signal ratio are:  

$$
λlh,min(t)=qlh,min(t)/slashig
$$

Si l

$$
λlh,max (t)=qlh,max (t)/slashig
$$

Si l(29) Assume λlh,ini(t) is the initial green signal ratio of phase h on the lth channel, and qlh,ini(t) is the initial traffic volume for the corresponding phase. The remaining saturation level (green signal ratio) for this phase is:

$$
λlh,sur(t)=λlh,max (t)-λlh,ini(t) (30)
$$

VOLUME 12, 2024 61943

<!-- page 8 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD

#### FIGURE 5. Experimental network (a) satellite map and (b)sub-region division result.

After the initial assignment, the remaining undistributed traffic flow from sub-region ito sub-region j,qij,sur(t), is:

$$
qij,sur(t)=qij(t)-m\sum
$$

$$
l=1n\sum
$$

$$
h=1qlh.ini(t) (31)
$$

In order to achieve the goal of quickly reducing the saturation level at intersections with high saturation levels during the distribution of remaining boundary traffic flow, the remaining saturation levels of each phase are used to proportionally distribute the traffic flow. The adjusted traffic flow for each phase at the boundary is:

$$
1qlh(t)=qij,sur(t)λlh,max-λlh,ini(t)
$$

m\sum

$$
l=1n\sum
$$

$$
h=1/bracketleftbig
$$

λlh,max-λlh,ini(t)/bracketrightbig(32) The corresponding adjustment amount for the green signal ratio of the phase is:

$$
1λlh(t)=1qlh(t)
$$

Slh(33) The parameter allocation steps for multi-sub-region boundary control are as follows: Step 1: Set the initial green signal ratio for each phase of the boundary intersection from sub-region ito sub-region jas

$$
the minimum green signal ratio, i.e., λlh,ini(t)=λlh,min (t).
$$

Step 2: Solve for the green signal ratio increment 1λlh for every phase of the boundary intersections through equations (30) to (33). Step 3: Determine the adjusted initial green signal ratio as

$$
λlh,ini(t+1t)=λlh,ini(t)+1λlh.
$$

Step 4: Check all phases for the presence of λlh,ini(t+1t) >λlh,max (t), if not, go to Step 7; Otherwise, go to Step 5. Step 5: Forλlh,ini(t+1t)>λlh,max (t), which means the phase has overflowed, then set the green signal ratio to the maximum value λlh,max (t), and convert the excess ratio into new undistributed traffic flow qij,sur(t). Step 6: Remove the phases with their green signal ratio has reached the maximum value, update the other phases’ initialgreen signal ratio to λlh,ini(t+1t), then return to Step 2 to redistribute the remaining traffic flow qij,sur(t). Step 7: Distribution is completed, monitor the accumulative volume of the sub-region and move on to the next cycle. The obtained green signal ratios for the phase can be used as the signal timing parameters for the boundary intersections. As the traffic flow is bidirectional between the adjacent sub-region iand sub-region jwith different flow rates, the signal timing parameters of the different traffic flow directions should be different, the asymmetric phases can be used for control parameter design.

## IV. EXPERIMENTAL ANALYSIS

A. EXPERIMENTAL NETWORK AND ITS MFD As show in Fig. 5(a), there is a partial road network of the Chengdu city’s First Ring Road. Due to differences in road grades, this road network exhibits significant heterogeneity in different areas. To model the macroscopic road network, detectors are set on each road segment, and based on the distribution characteristics of traffic flow density in the network, it is divided into four sub-regions as shown in

#### Fig. 5(b). Sub-region 1 is the central area of the road

network, which is easily occur traffic congestion. During peak periods, it is necessary to quickly evacuate traffic flow from sub-region 1 to its circumjacent sub-regions to alleviate congestion. The parameters for the entire road network and the four sub-regions, such as area, number of road segments, length of road segments, number of intersections, and signal timing, are shown in Tab. 2. The experiment road network consists of 311 intersections and 303 road segments with lengths ranging from 200 meters to 1600 meters. The free-flow speed is 60 km/h on the First Ring Road, Renmin South Road, Xinhua Avenue, and Shudu Avenue, and 40 km/h on the other roads. The intersections on the boundary of the current road network are all controlled by multi-phase fixed-time signals. The signal cycle of the boundary intersections on the First Ring Road is 148s, and the signal cycle of other boundary intersections ranges from 74s to 148s.

## 61944 VOLUME 12, 2024

<!-- page 9 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD

#### TABLE 2. Road network basic parameters.

#### FIGURE 6. Macroscopic fundamental diagrams (a) Entire traffic network; (b) Sub-region 1; (c) Sub-region 2; (d) Sub-region 3;

(e) Sub-region 4. Based on the traffic data during morning and evening peak periods on August 12, 2019, and through simulation testing, the MFDs of the entire traffic network and the four sub-regions are obtained as shown in Fig. 6(a) to Fig.6(e). The macroscopic fundamental diagram parameters, critical accumulative volume and maximum accumulative volume for the entire network and the four sub-regions are obtained based on parameter calibration, as shown in Tab.3.B. PERIMETER CONTROL SETUP For comparison, three control schemes are studied in this study: no perimeter control (NPC), perimeter control (PC) with Bang-Bang control at the boundary of the central subregion, and the optimal perimeter control (OPC) proposed in this paper. In the implementation of each control scheme, considering the pedestrian crossing time, signal split and maximum green period, the signal cycle range of the boundary intersections is set to [60s, 240s], and the green VOLUME 12, 2024 61945

<!-- page 10 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD

#### TABLE 3. Calibration and characteristic parameters of MFDs for each road network.

light time range for every phase is [15s, 60s]. The saturation

$$
flow rate for every approach is Sh=1400pcu/h/ln. Based
$$

on the critical accumulative volume, maximum outflow, and adjacency conditions of every sub-region, the critical proportion distribution vector of the boundary outflow is calculated

$$
asˆβji=[β11β21β31β41β12β22β32β42β13β23β33β43β14
$$

$$
β24β34β44]T=[0 0.25 0.35 0.30 0.40 0 0.35 0.30 0.30 0.40 0
$$

### 0.40 0.30 0.35 0.30 0]T. Then, take the minimum green light

time and the longest cycle time as constraints, the minimum and maximum proportion distribution vectors of the boundary

$$
outflow are set as βji,min=0.2T(j̸=i) and βji,max=[0 0.60
$$

### 0.55 0.5 0.50 0 0.40 0.30 0.45 0.35 0 0.35 0.45 0.35 0.40

0]T. The proportion of the entering traffic flow through the boundary to the total entering traffic flow in every sub-region

$$
isαiin=0.50T, and the proportion of leaving traffic flow
$$

through the boundary to the total leaving traffic flow in every

$$
sub-region is αiout=0.50T.
$$

## C. SIMULATION ANALYSIS

At the initial time of the simulation, the accumulative volume in sub-region 1, 2, 3, and 4 are 1500pcu, 2000 pcu, 2000 pcu, and 2000 pcu respectively. The initial proportion distribution vector of the boundary outflow is [0 0.25 0.35 0.30 0.40 0 0.35

### 0.30 0.30 0.40 0 0.40 0.30 0.35 0.30 0]T. The accumulative

volume in every sub-region is collected every 5 minutes, and then the signal control parameters at the sub-region boundary are calculated based on the Bang-Bang control scheme at the boundary of the central sub-region and the optimal perimeter control scheme proposed in this study to adjust the boundary outflow in every sub-region. The Bang-Bang control scheme at the boundary of the central sub-region uses Equation (22) to calculate the signal control parameters, while the optimal perimeter control scheme uses Equation (19)as the network traffic state equation. Under the constraints of Equation (20) ∼(21), the goal is to minimize the difference between the accumulative volume and the critical accumulative volume in the road network, as given by Equation (24), to determine the adjustment of the proportion distribution vector among the sub-regions in next 5 minutes. During the simulation process, the accumulative volume in the road network is as shown in Fig.7and Tab. 4. As show in Fig. 7, it can be observed clearly that without boundary control, sub-region 1 is congested for most of the simulation time, especially from 80 minutes and 220 minutes,it is almost gridlocked. Sub-region 2 and 3 are congested either, only while sub-region 4 operate in a stable state. Under the central sub-region perimeter control scheme, sub-region 1 always maintains good operation state, but this control scheme traps vehicles outside the central subregion, resulting in severe congestion in sub-regions 2 and

## 4 after 200 minutes, and sub-region 3 is congested between

## 150 minutes and 210 minutes. Under the optimal perimeter

control scheme, except for sub-region 3, which is mildly congested between 110 minutes and 155 minutes, the other sub-regions are always in good operation state. Tab.4shows the comparison of the three control strategies. In contrast with the NPC scheme, the PC scheme increases the average accumulative volume of the entire road network by 2.23%, and the average accumulative volume change rates for the sub-region 1, 2, 3 and 4 are -45.75%, 10.48%, -6.51%, and 55.61% respectively. This indicates that the PC scheme can effectively improve the operational efficiency of the central sub-region, but the efficiency of the adjacent external sub-regions cannot simultaneously improve. On the other hand, compare to NPC scheme, the OPC scheme reduces the average accumulative volume of the entire road network by 37.24%, with corresponding changes rates for the four sub-regions are -46.54%, -52.42%, -22.75%, and -11.95% respectively, indicating that the OPC scheme can not only effectively improve the operation of the central sub-region, but also improve the traffic conditions of adjacent external sub-regions. During the simulation period, the overall average operational benefits of the controlled road network under the three control schemes are as follows: NPC 326.28, PC 216.22, OPC 140.00. Compared to the NPC scheme, the benefits of the PC scheme change by -33.73%, and the OPC scheme is -57.09%. According to the definition of operational benefits in Equation (23), it can be concluded that the traffic operation of the entire road network is best under the OPC scheme, followed by the PC scheme, and the NPC is the worst.

## V. DISCUSSION AND FUTRUE RESEARCH

In this work, we first established a multi-region network traffic flow equilibrium model based on the macroscopic fundamental diagram theory urban transportation networks, then, a multi-region network optimal perimeter control

## 61946 VOLUME 12, 2024

<!-- page 11 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD

#### FIGURE 7. Accumulative volume(a) sub-region 1; (b) sub-region 2; (c) sub-region 3; (d) sub-region 4.

#### TABLE 4. The average accumulative volume and change rate.

model was proposed and the corresponding signal control algorithm for boundary intersections was developed either. Through simulation analysis and experimental comparison, the accumulative volume and operational benefits of every sub-region and the entire road network under three control schemes, namely, no boundary control (NPC), perimeter control (PC) and optimal perimeter control (OPC), have been

    analyzed.    The results shown that under the proposed optimal

perimeter control scheme (OPC), the operational benefits of the road network are improved by 57.09%, compared to no boundary control (NPC), as well as the improvement of perimeter control (PC) scheme is 33.73%, indicates that both PC and OPC scheme can effectively improve the operational efficiency of the regional road network and alleviate traffic congestion, with the OPC scheme showing better results. The OPC scheme can make the accumulative volume of vehicles in every sub-region closer to their critical accumulative volume, consequently, the spatial-temporal distribution of vehicles will more reasonable and the traffic operation efficiency will be improved and the global optimum can be approached. However, the actual traffic environment is quite complex, as the multi-entrances and exits on the road segments cannot be effectively controlled, and the mix of variousvehicle types and non-motorized vehicles also increases the complexity of management. The application of the OPC strategy in actual traffic networks also requires permission and coordination of the traffic management department, as well as the multi-category traffic information collection and signal control facilities, is also a great challenge. The research results of this study provide a new approach and method for perimeter control of heterogeneous multi-region traffic networks. However, the study ignores the influence of perimeter control strategy on the MFD curve of every sub-region and the spatial-temporal shift of traffic congestion. Further research and exploration are needed to quantitatively analyze and describe these factors. In the meantime, there are various new methods, such as deep learning and reinforcement learning, can be utilized for making optimal perimeter control in the future work.

## REFERENCES

[1] R. M. Li, ‘‘Study status and prospect of traffic signal control for oversaturated intersection,’’ J. Traffic Transp. Eng., vol. 13, no. 6, pp. 119-126, Jun. 2013, doi: 10.3969/j.issn.1671-1637.2013.06.017. [2] S. Nuli, and T. V. Mathew, ‘‘Online coordination of signals for heterogeneous traffic using stop line detection,’’ Proc. Soc. Behav. Sci., vol. 104, no. 1, pp. 765-774, Dec. 2013, doi: 10.1016/j.sbspro2013.11.171. VOLUME 12, 2024 61947

<!-- page 12 -->

Y. Ma, Z. Liu: OPC for Multi-Region Traffic Networks Based on MFD [3] P. Mirchandani and L. Head, ‘‘A real-time traffic signal control system: Architecture, algorithms, and analysis,’’ Transp. Res. C, Emerg. Technol., vol. 9, no. 6, pp. 415-432, Dec. 2001, doi: 10.1016/s0968-090x(00)000474. [4] C. Roncoli, M. Papageorgiou, and I. Papamichail, ‘‘Traffic flow optimisation in presence of vehicle automation and communication systems-Part II: Optimal control for multi-lane motorways,’’ Transp. Res. C, Emerg. Technol., vol. 57, pp. 260-275, Aug. 2015, doi: 10.1016/j.trc.2015.05.011. [5] J. W. Godfrey, ‘‘The mechanism of a road network,’’ Traffic Eng. Control, vol. 11, pp. 323-327, Nov. 1969. [6] C. F. Daganzo, ‘‘Urban gridlock: Macroscopic modeling and mitigation approaches,’’ Transp. Res. B, Methodol., vol. 41, no. 1, pp. 49-62, Jan. 2007, doi: 10.1016/j.trb.2006.03.001. [7] N. Geroliminis and C. F. Daganzo, ‘‘Existence of urban-scale macroscopic fundamental diagrams: Some experimental findings,’’ Transp. Res. B, Methodol., vol. 42, no. 9, pp. 759-770, Nov. 2008, doi: 10.1016/j.trb.2008.02.002. [8] C. F. Daganzo and N. Geroliminis, ‘‘An analytical approximation for the macroscopic fundamental diagram of urban traffic,’’ Transp. Res. B, Methodol., vol. 42, no. 9, pp. 771-781, Nov. 2008, doi: 10.1016/j.trb.2008.06.008. [9] Y. B. Ji, ‘‘Existence Verification of Macroscopic Fundamental Diagram (MFD) based on Simulation Method,’’ J. Wuhan Univ. Technol. Transp. Sci. Eng. Ed., vol. 37, no. 5, pp. 929-933, Oct. 2013, doi: 10.3963/j.issn.20953844.2013.05.008. [10] Z. B. He, W. Guan, and L. L. Fan, and J. Z. Guan, ‘‘Characteristics of macroscopic fundamental diagram for Beijing urban ring freeways,’’ J. Transp. Syst. Eng. Inf. Technol, vol. 14, no. 2, pp. 199-205, Apr. 2014, doi:10.3969/j.issn.1009-6744.201402.032. [11] Y. Y. Hui, J. Zhao, and S. C. Jiang, ‘‘Influence of artery coordinated control strategies on macroscopic fundamental diagram,’’ J. Transp. Inf. Saf., vol. 37, no. 4, pp. 74-81, Aug. 2019, doi: 10.3963/j.issn.16744861.2019.04.010. [12] F. F. Xu, Z. C. He, and Z. R. Sha, ‘‘Impacts of traffic management measures on urban network microscopic fundamental diagram,’’ J. Transp. Syst. Eng. Inf. Technol., vol. 13, no. 2, pp. 185-190, Apr. 2013, doi: 10.3969/j.issn.1009-6744.2013.02.028. [13] L. Zhu, L. Yu, and G. H. Song, ‘‘MFD-based investigation into macroscopic traffic status of urban networks and its influencing factors,’’ J. South China Univ. Technol., Nat. Sci., vol. 40, no. 11, pp. 138-146, Nov. 2012, doi: 10.3969/j.issn.1000-565X.2012.11.021. [14] C. F. Daganzo, V. V. Gayah, and E. J. Gonzales, ‘‘Macroscopic relations of urban traffic variables: Bifurcations, multivaluedness and instability,’’ Transp. Res B, Methodol., vol. 45, no. 1, pp. 278-288, Jan. 2011, doi: 10.1016/j.trb.2010.06.006. [15] N. Geroliminis and J. Sun, ‘‘Properties of a well-defined macroscopic fundamental diagram for urban traffic,’’ Transp. Res. B, Methodol., vol. 45, no. 3, pp. 605-617, Mar. 2011, doi: 10.1016/j.trb.2010.11.004. [16] W. J. Ma, and D. B. Liao, ‘‘Progress and prospects of macroscopic fundamental diagram,’’ J. Wuhan Univ. Technol. Transp. Sci. Eng. Ed., vol. 38, no. 6, pp. 1226-1233, Dec. 2014, doi: 10.3963/j.issn.20953844.2014.06.010. [17] Y. Zhang, Y. Bai, and X. G. Yang, ‘‘Strategy of traffic gridlock control for urban road network,’’ China J. Highway Transp., vol. 23, no. 6, pp. 96-102, Nov. 2010, doi: 10.19721/j.issn.1001-7372.2010.06.015. [18] M. Keyvan-Ekbatani, M. Papageorgiou, and I. Papamichail, ‘‘Urban congestion gating control based on reduced operational network fundamental diagrams,’’ Transp. Res. C, Emerg. Technol., vol. 33, pp. 74-87, Aug. 2013, doi:10.1016/j.trc.201304.010. [19] J. Haddad and N. Geroliminis, ‘‘On the stability of traffic perimeter control in two-region urban cities,’’ Transp. Res. B, Methodol., vol. 46, no. 9, pp. 1159-1176, Nov. 2012, doi: 10.1016/j.trb.2012.04.004. [20] N. Geroliminis, J. Haddad, and M. Ramezani, ‘‘Optimal perimeter control for two urban regions with macroscopic fundamental diagrams: A model predictive approach,’’ IEEE Trans. Intell. Transp. Syst., vol. 14, no. 1, pp. 348-359, Mar. 2013, doi: 10.1109/TITS.2012.2216877. [21] H. Ding, X. Y. Zheng, Y. Zhang, L. Y. Zhu, and W. H. Zhang, ‘‘Optimal control for traffic congested area boundary in macroscopic traffic networks,’’ China J. Highway Transp., vol. 30, no. 1, pp. 111-120, Jan. 2017, doi: 10.19721/j.cnki.1001-73722017.01.014. [22] H. Ding, T. Yang, X. Y. Zheng, W. H. Zhang, and Y. Zhang, ‘‘Extension lifting control for boundary entrance of traffic congested area,’’ J. Southeast Uni. Nat. Sci. Ed., vol. 49, no. 4, pp. 781-787, Jul. 2019, doi: 10.3969/j.issn.1001-0505.2019.04.02.[23] H. Ding, F. Guo, C. B. Jiang, Y. Zhang, and W. H. Zhang, ‘‘Coordinated method of perimeter control for multiple MFD regions,’’ Acta Autom. Sin., vol. 43, no. 4, pp. 548-559, Apr. 2017, doi: 10.16383/j.aas.2017.c160322. [24] H. Ding, H. Yuan, X. Zheng, H. Bai, W. Huang, and C. Jiang, ‘‘Integrated control for a large-scale mixed network of arterials and freeways,’’ IEEE Intell. Transp. Syst. Mag., vol. 13, no. 3, pp. 131-145, Fall. 2021, doi: 10.1109/MITS.2019.2907677. [25] Y. Guo, L. Yang, S. Hao, and X. Gu, ‘‘Perimeter traffic control for single urban congested region with macroscopic fundamental diagram and boundary conditions,’’ Phys. A, Stat. Mech. Appl., vol. 562, Jan. 2021, Art. no. 125401, doi: 10.1016/j.physa2020.125401. [26] X. Yang, J. Chen, M. Yan, Z. He, Z. Qin, and J. Zhao, ‘‘Regional boundary control of traffic network based on MFD and FR-PID,’’ J. Adv. Transp., vol. 2021, pp. 1-12, Sep. 2021, doi: 10.1155/2021/9730813. [27] L. Zheng and B. Wu, ‘‘A reinforcement learning based traffic control strategy in a macroscopic fundamental diagram region,’’ J. Adv. Transp., vol. 2022, pp. 1-12, Apr. 2022, doi: 10.1155/2022/5681234. [28] H. Hamedmoghadam, N. Zheng, D. Li, and H. L. Vu, ‘‘Percolation-based dynamic perimeter control for mitigating congestion propagation in urban road networks,’’ Transp. Res. C, Emerg. Technol., vol. 145, Dec. 2022, Art. no. 103922, doi: 10.1016/j.trc.2022.103922. [29] H. Fu, S. Chen, K. Chen, A. Kouvelas, and N. Geroliminis, ‘‘Perimeter control and route guidance of multi-region MFD systems with boundary queues using colored Petri nets,’’ IEEE Trans. Intell. Transp. Syst., vol. 23, no. 8, pp. 12977-12999, Aug. 2022, doi: 10.1109/TITS.2021.3119017. [30] Y. Gao, Z. Qu, X. Song, Z. Yun, and F. Zhu, ‘‘Coordinated perimeter control of urban road network based on traffic carrying capacity model,’’ Simul. Model. Pract. Theory, vol. 123, Feb. 2023, Art. no. 102680, doi: 10.1016/jsimpat.2022.102680. [31] W. Li, B. Wang, Z. H. Khattak, and X. Deng, ‘‘Network-level traffic signal cooperation: A higher-order conflict graph approach,’’ IEEE Trans. Intell. Transp. Syst., vol. 24, no. 1, pp. 990-999, Jan. 2023, doi: 10.1109/TITS.2022.3191290. [32] T. Dantsuji, Y. Takayama, and D. Fukuda, ‘‘Perimeter control in a mixed bimodal bathtub model,’’ Transp. Res. B, Methodol., vol. 173, pp. 267-291, Jul. 2023, doi: 10.1016/j.trb.2023.05.003. [33] C. Zhu, G. Wen, N. Li, L. Bian, J. Wu, and A. Kouvelas, ‘‘Resilience enhancement of urban roadway network during disruption via perimeter control,’’ IEEE Trans. Netw. Sci. Eng., vol. 11, no. 1, pp. 1227-1237, Feb. 2024, doi: 10.1109/TNSE.2023.3321678. [34] K. Aboudolas and N. Geroliminis, ‘‘Perimeter and boundary flow control in multi-reservoir heterogeneous networks,’’ Transp. Res. B, Methodol., vol. 55, pp. 265-281, Sep. 2013, doi: 10.1016/j.trb.201307.003. YAFENG MA was born in Yongshou, Shaanxi, China, in 1988. He received the B.S. degree in traffic engineering from Harbin Institute of Technology, Harbin, Heilongjiang, China, in 2011, and the Ph.D. degree in transportation planning and management from Southwest Jiaotong University, Sichuan, China, in 2018. He is currently an Associate Professor with the School of Transportation Engineering, East China Jiaotong University. He is the author of two books and more than

## 30 articles. His research interests include transportation planning, traffic

management and control, traffic design, and transportation system modeling, and optimization. ZUOMAN LIU was born in Jianli, Hubei, China, in 1988. She received the B.S. degree in traffic engineering from Shandong Jiaotong University, Jinan, Shandong, China, in 2010, and the M.S. degree in transportation planning and management from Southwest Jiaotong University, Chengdu, Sichuan, China, in 2013. She is currently pursuing the Ph.D. degree with East China Jiaotong University, with a focus on traffic system modeling and optimization. From 2013 to 2016, she was an Engineer at Chengdu Yida Transportation Technology Company Ltd.

## 61948 VOLUME 12, 2024
