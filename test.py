import gmpy2
from gmpy2 import mpz


p = mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g = mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
h1 = mpz(14986535000696671050997440471631035328840329254126462257167343955669001657810533800007614863885805191397376011447213611683234390696415399104241078393997)
# x = log_g (h1) mod p

# testing
x = mpz(368313625481)

print("Caclulated h1 =", gmpy2.powmod(g, x, p))
print("Real h1       =", h1)
print("Equals:", h1 == gmpy2.powmod(g, x, p))
