from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

plt.switch_backend("Agg")


BASE_DIR = Path(__file__).resolve().parent


def create_autocorrelation_plot(input_path: Path, output_path: Path) -> None:
    data = np.loadtxt(input_path, delimiter=",")
    signal = data[:, 1] - np.mean(data[:, 1])
    variance = np.var(signal)
    lags = np.arange(len(signal))
    autocorrelation = np.array([
        np.sum(signal[:len(signal) - lag] * signal[lag:])
        / (len(signal) - lag)
        / variance
        for lag in lags
    ])

    plt.figure(figsize=(8, 5))
    plt.plot(lags, autocorrelation, linewidth=2)
    plt.axhline(0, linewidth=1, color="black")
    plt.xlabel("Lag [frame]")
    plt.ylabel("Autocorrelation")
    plt.title(f"Autocorrelation of {input_path.name}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=200)
    plt.close()


if __name__ == "__main__":
    input_path = BASE_DIR / "data.csv"
    output_path = BASE_DIR / "data_acf.png"
    create_autocorrelation_plot(input_path, output_path)
    print(f"saved: {output_path}")