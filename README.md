alitropy

ml aims to extract signals from data and make critical predictions ,on the other hand it studies encoding,decoding,transmitting and manipuliting information,as a result ,it provides language to studies information processing in ml systems

an information can be encoded in anything with a sequence of some format

Self Information:
now suppose we have an event of sequence of n bits ,then each 0 and 1 occurs with proba 1/2 **n ,mathematicly shannon descripved as:
I(x) = -log(p)

I("0101") = -log(p("0101")) = -log(1/2 **4) = 4 bits

self-information is only for discrete event
Entropy:
axioms of shannon entropy:
1. The information we gain by observing a random variable does not depend on what we call
the elements, or the presence of additional elements which have probability zero.
2. The information we gain by observing two random variables is no more than the sum of the
information we gain by observing them separately. If they are independent, then it is exactly
the sum.
3. The information gained when observing (nearly) certain events is (nearly) zero.


definition:
for any random variable X that follows distribution P with pdf or pmf p(x),we measure the expected information by entropy:
H(x) = -Ex~P[log(p(x))]
in discrete it is a sum and in continous it is an integral

why log we have p(x)=f1 .... fn this means fn contribute independently in information,and in axioms we need this to be additive and luckily log is perfect for this job 
and why negative because of more frequent event should contain less information

Mutual information:
joint entropy
H(X,Y)=-Ex,y~P[log(pX,Y(x,y))]

H(X), H(Y ) ≤ H(X, Y ) ≤ H(X) + H(Y )


conditional entropy:

H(Y | X) = −E(x,y)∼P [log p(y | x)]

H(Y | X) = H(X, Y ) − H(X)

mutual information:

I(X, Y ) = H(X, Y ) − H(Y | X)−H(X | Y )

I(X,Y) = ExEy{pX,Y(x,y) * log(pX,Y(x,y)/pX(x)*pY(y))}

pointwise mutual information:

pmi(x,y) = log(pX,Y(x,y)/pX(x)*pY(y))

This allows us to interpret the mutual information as the average amount that we were
surprised to see two outcomes occurring together compared to what we would expect if they were
independent

this concept help us in many fields like nlp:
when we say amazon is on fire ,it can be an missunderstood but if we find the mutual information with group of words such amazon , tech..., then it will make the context clear

cross entropy:
we try to maximaze the log likelihood ,and we conclude the -log loss
and that signify minimize the logloss

CE(P, Q) = −Ex∼P [log(q(x))]

CE(P, Q) = H(P) + DKL (P∥Q)

minimazing ce is equivalant to minimazing ce


