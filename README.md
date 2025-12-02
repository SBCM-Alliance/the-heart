# 🫀 The Heart
**Global Liquidity Protocol based on SBCM Economics.**

[![Status](https://img.shields.io/website?url=https%3A%2F%2Fsbcm-alliance.github.io%2F&label=System%20Status)](https://sbcm-alliance.github.io/)
[![Tech](https://img.shields.io/badge/Built_with-PyScript-yellow)](https://pyscript.net/)
[![License](https://img.shields.io/badge/License-MIT-blue)](LICENSE)

> **"From Logic to the Heart."**
> 
**[Launch Dashboard (Live Demo)](https://sbcm-alliance.github.io/the-heart/)**

---

## 📖 Overview

**The Heart** は、SBCM経済学（Meso-Economics）を具現化した、地球規模の富の循環シミュレーターです。
国家（Leviathan）における富の偏在（ストロー効果）をリアルタイムで監視し、**「G-Cart」**によって是正された余剰資金を、瀕死の地域ブロックへ**「仕事（Special Quests）」**として輸血する自律分散プロトコルです。

### The Problem: The Straw Effect (ストロー効果)
放置された資本主義社会では、富は「重力」に従って地方（Prey）から中央（Predator/Tokyo）へと吸い上げられます。
このシステムでは、その不可逆な流れを**アルゴリズムによって逆流（還流）**させます。

---

## ⚙️ System Architecture

このプロトコルは、ブラウザ上の **PyScript (WebAssembly)** で動作するサーバーレス・アプリケーションです。中央サーバーに依存せず、各クライアント（市民）のデバイス上で自律的に計算が行われます。

```mermaid
graph TD
    Leviathan["<b>Leviathan</b><br>(国家・行政)"] -->|予算執行| Valve{"<b>G-Cart Valve</b><br>(歪み検知)"}
    
    Valve -- "歪み > 10.0" -->|遮断 & 徴収| Heart(("<b>The Heart</b><br>Liquidity Pool"))
    Valve -- 正常 -->|承認| Tokyo["<b>Tokyo</b><br>(Predator Block)"]
    
    Heart -->|"Systole (収縮)"| Target{"<b>Triage Logic</b><br>(生存判定)"}
    
    Target -- "瀕死 (HP < 30%)" -->|"輸血 (Special Quest)"| Yubari["<b>Yubari</b><br>(Dying Block)"]
    Target -- 瀕死 -->|輸血| Akita["<b>Akita</b><br>(Dying Block)"]
    
    style Heart fill:#ff4b4b,stroke:#333,stroke-width:4px,color:white
    style Leviathan fill:#333,stroke:#fff,color:white
```

### Core Modules (`heart.py`)

1.  **`Leviathan`**:
    金銭感覚の欠如した巨大行政主体。ランダムに過剰な予算（歪み）を執行しようとします。
2.  **`GCartValve`**:
    ゲートキーパー。予算歪み指数 ($D_{index}$) が閾値（9.9）を超えた場合、執行をブロックし、適正価格との差額を「余剰（Surplus）」として回収します。
3.  **`TheHeart`**:
    循環ポンプ。回収された余剰をプールし、バイタル（HP）が最も低いブロックへ優先的に再分配します。ただし現金給付ではなく、**「インフラ修復クエスト」**として発注されるため、地域の $R_{block}$（残留率）は100%となります。

---

## 🎮 How to Monitor

[ダッシュボード](https://sbcm-alliance.github.io/) にアクセスすると、シミュレーションが開始されます。

### 1. The Reality (放置)
何も操作しない場合、**「ストロー効果」**が観測されます。
*   地方（右側のブロック）から、富を表す **紫色の粒子** が吸い出されます。
*   Tokyo（左端）のゲージだけが肥大化し、地方は赤字（Critical）に転落します。

### 2. The Intervention (介入)
**`⚡ Run G-Cart`** ボタンをクリックしてください。
*   **G-Cart発動:** Tokyoの超過利潤が強制的に徴収され、Heart（上部）にプールされます（**金色の粒子**）。
*   **Systole (収縮):** プールされた資金が、瀕死のブロックへ **赤色の粒子** として輸血されます。
*   **Result:** 地方のインフラ（HP）が劇的に回復します。

---

## 🛠️ Development

### Prerequisites
*   No Server required.
*   Just a modern web browser.

### Run Locally
```bash
# Clone the repository
git clone https://github.com/SBCM-Alliance/the-heart.git

# Serve with Python (or any static server)
cd the-heart
python3 -m http.server
# -> Open http://localhost:8000
```

### Configuration
`heart.py` 内の定数を変更することで、経済パラメータを調整可能です。

```python
THRESHOLD_DISTORTION = 9.9  # 歪み許容値
PROTOCOL_FEE_RATE = 0.3     # プール率 (30%)
```

---

## 📜 License

[MIT License](LICENSE)

**Author:** SBCM Alliance (Hokuto Koyama)  
*"Logic is the Brain. But this Protocol is the Heart."*
```
