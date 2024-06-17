import numpy as np
import matplotlib.pyplot as plt

# giriş sinyali
x = [1, 2, 3, 4]

# Ayrık Fourier Dönüşümü (DFT)
N = len(x)
X = np.fft.fft(x)

print("Frequency domain representation (real and imaginary parts):")
for k in range(N):
    print(f"X[{k}] = {X[k].real} + {X[k].imag}j")
    

# genlik spektrumunu hesapla ve çiz
amplitude_spectrum = np.abs(X)

print("Amplitude spectrum:")
for k in range(N):
    print(f"A[{k}] = {amplitude_spectrum[k]}")


plt.figure(figsize=(10, 6))
plt.stem(np.arange(N), amplitude_spectrum)
plt.xlabel("Frequency index (k)")
plt.ylabel("Amplitude")
plt.title("Amplitude Spectrum")
plt.show()    
    

# faz spektrumunu hesapla ve çiz
phase_spectrum = np.angle(X)


print("Phase spectrum:")
for k in range(N):
    print(f"φ[{k}] = {phase_spectrum[k]:.4f}")

# Plot the phase spectrum
plt.figure(figsize=(10, 6))
plt.stem(np.arange(N), phase_spectrum)
plt.xlabel("Frequency index (k)")
plt.ylabel("Phase (radians)")
plt.title("Phase Spectrum")
plt.show()