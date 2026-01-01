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

