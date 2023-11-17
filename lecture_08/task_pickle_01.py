import os
import pickle

res = pickle.loads(b"cos\nsystem\n(S'echo Hello world!'\ntR.")
print(f"{res = }")

os.system('echo Hello World!')