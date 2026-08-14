(*
  Quadratic-core mean source versus second-chaos zero-set certificate
  Date: 2026-08-14

  Exact rational computation.
  Goal under c = Curl[A.z] = e3:
    P = (A z . Grad) Q - A Q == 0  ==>  A c == 0.
*)

ClearAll[xx, z1, z2, z3];

vars = Array[xx, 15];

(* Symmetry T_{i,j,k}=T_{i,k,j}.  Three divergence constraints are
   solved in the entries T3[1,3], T3[2,3], T3[3,3]. *)

t1 = {
  {vars[[1]], vars[[2]], vars[[3]]},
  {vars[[2]], vars[[4]], vars[[5]]},
  {vars[[3]], vars[[5]], vars[[6]]}
};

t2 = {
  {vars[[7]], vars[[8]], vars[[9]]},
  {vars[[8]], vars[[10]], vars[[11]]},
  {vars[[9]], vars[[11]], vars[[12]]}
};

t3 = {
  {vars[[13]], vars[[14]], -(vars[[1]] + vars[[8]])},
  {vars[[14]], vars[[15]], -(vars[[2]] + vars[[10]])},
  {-(vars[[1]] + vars[[8]]),
   -(vars[[2]] + vars[[10]]),
   -(vars[[3]] + vars[[11]])}
};

(* Normalize c = Curl[A.z] to e3.  For this parameterization,
   c = {-x1-x4-x6, -x7-x10-x12, x3+x11-x13-x15}. *)

normalizationRules = {
  vars[[6]]  -> -vars[[1]] - vars[[4]],
  vars[[12]] -> -vars[[7]] - vars[[10]],
  vars[[15]] ->  vars[[3]] + vars[[11]] - vars[[13]] - 1
};

tt = {t1, t2, t3} /. normalizationRules;

ee = Normal[LeviCivitaTensor[3]];

(* A_{a,k} = eps_{a,b,c} T_{c,b,k}. *)

aa = Expand@Table[
  Sum[ee[[a, b, c]] tt[[c, b, k]], {b, 3}, {c, 3}],
  {a, 3}, {k, 3}
];

zz = {z1, z2, z3};

qq = Table[
  Expand[1/2 zz . tt[[i]] . zz],
  {i, 3}
];

(* Homogeneous degree-two bracket P=(Az.grad)Q-AQ. *)

pp = Expand@Table[
  Sum[(aa . zz)[[l]] D[qq[[i]], zz[[l]]], {l, 3}]
    - Sum[aa[[i, l]] qq[[l]], {l, 3}],
  {i, 3}
];

pCoefficients = DeleteCases[
  Flatten@Table[
    Coefficient[pp[[i]], zz[[j]] zz[[k]]],
    {i, 3}, {j, 3}, {k, j, 3}
  ],
  0
];

remainingVariables = DeleteCases[
  vars,
  Alternatives[vars[[6]], vars[[12]], vars[[15]]]
];

gb = GroebnerBasis[
  pCoefficients,
  remainingVariables,
  MonomialOrder -> DegreeReverseLexicographic
];

cNormalized = {0, 0, 1};
ac = Expand[aa . cNormalized];

acRemainder =
  PolynomialReduce[#, gb, remainingVariables][[2]] & /@ ac;

specialBasisElements = Select[
  gb,
  ! FreeQ[#, xx[8]] || ! FreeQ[#, xx[10]] &
] // Factor;

Print["Number of P coefficients: ", Length[pCoefficients]];
Print["Number of normalized variables: ", Length[remainingVariables]];
Print["Groebner basis length: ", Length[gb]];
Print["A c modulo the Groebner basis: ", acRemainder];
Print["Basis elements involving x8 or x10: ", specialBasisElements];

(* Expected exact output includes
     acRemainder = {-2 xx[10], 2 xx[8], 0}
   and basis elements
     xx[10]^2, xx[8] xx[10], xx[8]^2.
   Therefore on the real zero set x8=x10=0 and A c=0.
*)
