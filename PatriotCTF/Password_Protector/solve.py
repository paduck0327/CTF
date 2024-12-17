import base64
bittysEnc = base64.b64decode("Zfo5ibyl6t7WYtr2voUEZ0nSAJeWMcN3Qe3/+MLXoKL/p59K3jgV")

fourth = 'Ocmu{9gtuf'
fourth += 'MmQg8G0eCXWi3MY9QfZ0NjCrXhzJEj50fumttU0ymp'
fourth = list(fourth)

for i in range(len(fourth)):
	fourth[i] = ord(fourth[i]) - 1

fourth = base64.b64decode(''.join(map(chr, fourth)))
print(bytes.fromhex(hex(int.from_bytes(bytes(fourth)) ^ int.from_bytes(bittysEnc))[2:]))