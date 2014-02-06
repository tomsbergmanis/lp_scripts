// OBJECTIVE FUNCTION

min:  xe1f1 + xe2f1 +xe3f1 +xe4f1 +xe5f1 +xe1f2+ xe2f2+ xe3f2+ xe4f2+ xe5f2 +xe1f3+ xe2f3+ xe3f3+ xe4f3+ xe5f3;

// CONSTRAINTS
// joint probabilities sum up to one
e1f1 + e2f1 +e3f1 +e4f1 +e5f1 +e1f2+ e2f2+ e3f2+ e4f2+ e5f2 e1f3+ e2f3+ e3f3+ e4f3+ e5f3 =1;
//probabilities must be > 0
e1f1	>= 0;
e1f2	>= 0;
e1f3	>= 0;
e2f1	>= 0;
e2f2	>= 0;
e2f3	>= 0;
e3f1	>= 0;
e3f2	>= 0;
e3f3	>= 0;
e4f1	>= 0;
e4f2	>= 0;
e4f3	>= 0;
e5f1	>= 0;
e5f2	>= 0;
e5f3	>= 0;
//defining olds
e1f1_OLD= 0.3  ;
e1f2_OLD=  0 ;
e1f3_OLD=  0 ;
e2f1_OLD=  0.4 ;
e2f2_OLD=  0 ;
e2f3_OLD=  0 ;
e3f1_OLD=  0.1 ;
e3f2_OLD=  0 ;
e3f3_OLD=  0 ;
e4f1_OLD=  0 ;
e4f2_OLD=  0.2 ;
e4f3_OLD=  0 ;
e5f1_OLD=  0 ;
e5f2_OLD=  0 ;
e5f3_OLD=  0 ;

//defining marginals
qf1=	0.6;
qf2=	0.2;
qf3=	0.2;
qe1=	0.12;
qe2=	0.08;
qe3=	0.4;
qe4=	0.2;
qe5=	0.2;
// matching marginals
e1f1+e1f2+e1f3 = qe1;
e2f1+e2f2+e2f3 = qe2;
e3f1+e3f2+e3f3 = qe3;
e4f1+e4f2+e4f3 = qe4;
e5f1+e5f2+e5f3 = qe5;

e1f1 + e2f1 +e3f1 +e4f1 +e5f1 = qf1;
e1f2 + e2f2 +e3f2 +e4f2 +e5f2 = qf2;
e1f3 + e2f3 +e3f3 +e4f3 +e5f3 = qf3;



// implementing abs | X |

e1f1-e1f1_OLD  <= xe1f1;
e1f2-e1f2_OLD  <=  xe1f2 ;
e1f3-e1f3_OLD  <=  xe1f3;
e2f1-e2f1_OLD  <= xe2f1 ;
e2f2-e2f2_OLD  <=  xe2f2 ;
e2f3-e2f3_OLD  <=  xe2f3  ;
e3f1-e3f1_OLD  <= xe3f1 ;
e3f2-e3f2_OLD  <=  xe3f2 ;
e3f3-e3f3_OLD  <=  xe3f3  ;
e4f1-e4f1_OLD  <= xe4f1 ;
e4f2-e4f2_OLD  <=  xe4f2 ;
e4f3-e4f3_OLD  <=   xe4f3  ;
e5f1-e5f1_OLD  <= xe5f1  ;
e5f2-e5f2_OLD  <=  xe5f2 ;
e5f3-e5f3_OLD  <=  xe5f3 ;

-e1f1+e1f1_OLD  <= xe1f1;
-e1f2+e1f2_OLD  <=  xe1f2 ;
-e1f3+e1f3_OLD  <=  xe1f3;
-e2f1+e2f1_OLD  <= xe2f1 ;
-e2f2+e2f2_OLD  <=  xe2f2 ;
-e2f3+e2f3_OLD  <=  xe2f3  ;
-e3f1+e3f1_OLD  <= xe3f1 ;
-e3f2+e3f2_OLD  <=  xe3f2 ;
-e3f3+e3f3_OLD  <=  xe3f3  ;
-e4f1+e4f1_OLD  <= xe4f1 ;
-e4f2+e4f2_OLD  <=  xe4f2 ;
-e4f3+e4f3_OLD  <=   xe4f3  ;
-e5f1+e5f1_OLD  <= xe5f1  ;
-e5f2+e5f2_OLD  <=  xe5f2 ;
-e5f3+e5f3_OLD  <=  xe5f3 ;


