# Corel signal analysis

CSV データに対して FFT スペクトルと自己相関を計算し、PNG グラフとして保存するちっちゃな Python プロジェクトです。

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

## Usage

FFT スペクトルを作成します。

```bash
python FFT.py
```

`data2_fft.png` が作成されます。

自己相関グラフを作成します。

```bash
python test.py
```

`data_acf.png` と `data2_acf.png` が作成されます。生成された PNG は Git 管理対象外です。

## Input format

CSV はヘッダーなしの 2 列構成を想定しています。

- 1 列目: 時刻またはフレーム番号
- 2 列目: 信号値