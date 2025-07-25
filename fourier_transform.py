import numpy as np
import matplotlib.pyplot as plt

# Create a sample signal: sine wave
t = np.linspace(0, 1, 500, endpoint=False)  # Time vector
freq = 5  # Frequency in Hz
signal = np.sin(2 * np.pi * freq * t)

# Compute the Fourier Transform
fft_result = np.fft.fft(signal)
frequencies = np.fft.fftfreq(len(t), d=(t[1] - t[0]))

# Plot the signal and its Fourier Transform
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(t, signal)
plt.title("Original Signal")
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")

plt.subplot(1, 2, 2)
plt.stem(frequencies[:len(frequencies)//2], np.abs(fft_result)[:len(frequencies)//2], use_line_collection=True)
plt.title("Fourier Transform")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Amplitude")

plt.tight_layout()
plt.show()
