import gmpy2
from gmpy2 import mpz
from tqdm import tqdm
import time

start = time.time()

p = mpz(13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171)
g = mpz(11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568)
h1 = mpz(14986535000696671050997440471631035328840329254126462257167343955669001657810533800007614863885805191397376011447213611683234390696415399104241078393997)
# x = log_g (h1) mod p


B = mpz(2 ** 20)
g_pow_B = gmpy2.powmod(g, B, p)
f = dict()

print("Filing x1 values...")
for x1 in tqdm(range(B)):
    f_value = gmpy2.divm(h1, gmpy2.powmod(g, x1, p), p)
    f[f_value] = x1

print("Finding x2...")
B_range = tqdm(range(B))
for x0 in B_range:
    h_value = gmpy2.powmod(g_pow_B, x0, p)
    if h_value in f:
        B_range.close()
        print("x0 = ", x0)
        print("x1 = ", f[h_value])
        x = x0 * B + f[h_value]
        print("x = ", x)
        break

end = time.time()

print(f"Total time: {(end - start) * 1000:.3f} ms")
