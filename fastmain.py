from tqdm import tqdm
import time

start = time.time()
p = 13407807929942597099574024998205846127479365820592393377723561443721764030073546976801874298166903427690031858186486050853753882811946569946433649006084171
g = 11717829880366207009516117596335367088558084999998952205599979459063929499736583746670572176471460312928594829675428279466566527115212748467589894601965568
h1 = 14986535000696671050997440471631035328840329254126462257167343955669001657810533800007614863885805191397376011447213611683234390696415399104241078393997
# x = log_g (h1) mod p


B = 2 ** 20

# calulate g inverse
g_inv = pow(g, -1, p)
f = dict()
f[h1] = 0
prev = h1
# filling x1
print("Filing x1 values...")
for x1 in tqdm(range(1, B)):
    new = (prev * g_inv) % p
    f[new] = x1
    prev = new


print("Finding x2...")
B_range = tqdm(range(1, B))
prev = 1
g_pow_B = pow(g, B, p)

if prev in f:
    print("x0 = ", 0)
    print("x1 =", f[prev])
    x = f[prev]
    print("x = ", x)
else:
    for x0 in B_range:
        new = (prev * g_pow_B) % p
        if new in f:
            B_range.close()
            print("x0 = ", x0)
            print("x1 = ", f[new])
            x = x0 * B + f[new]
            print("x = ", x)
            break
        prev = new

end = time.time()

print(f"Total time: {(end - start) * 1000:.3f} ms")
