from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend("Agg")


BASE_DIR = Path(__file__).resolve().parent


def create_fft_plot(input_path: Path, output_path: Path) -> None:
    data = np.loadtxt(input_path, delimiter=",")

    time = data[:, 0]
    signal = data[:, 1]

    signal = signal - np.mean(signal)
    dt = np.mean(np.diff(time))
    sample_count = len(signal)

    fft_result = np.fft.rfft(signal)
    freq = np.fft.rfftfreq(sample_count, d=dt)
    amplitude = 2.0 / sample_count * np.abs(fft_result)
    amplitude[0] /= 2

    plt.figure(figsize=(8, 5))
    plt.plot(freq, amplitude, linewidth=2)
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Amplitude")
    plt.title("FFT Spectrum")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


if __name__ == "__main__":
    input_path = BASE_DIR / "data2.csv"
    output_path = BASE_DIR / "data2_fft.png"
    create_fft_plot(input_path, output_path)
    print(f"saved: {output_path}")
