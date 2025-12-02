import random
import time
from dataclasses import dataclass
from typing import List, Tuple
import js
from pyscript import document

# --- System Constants ---
THRESHOLD_DISTORTION = 9.9  # 10倍でも確実に引っかかるように修正
PROTOCOL_FEE_RATE = 0.3     # 変化を分かりやすくするため30%に増量

# 出力用ヘルパー
def log(text):
    term = js.document.getElementById("terminal")
    # HTMLタグを使えるようにinnerHTMLに変更
    msg = f"<div>{text}</div>"
    if "System Ready" in term.innerHTML:
        term.innerHTML = msg
    else:
        term.innerHTML += msg
    term.scrollTop = term.scrollHeight

def clear_log():
    js.document.getElementById("terminal").innerText = ""

@dataclass
class StandardBlock:
    id: str
    name: str
    population: int
    wealth: float
    vitality: float
    
    def is_critical(self) -> bool:
        return self.vitality < 0.4

    def receive_transfusion(self, amount: float):
        log(f"<span style='color: #ff4b4b;'>  [💗 THE HEART] 輸血を実行 -> Target: {self.name}</span>")
        log(f"    -> 特別クエスト発注: 予算 ¥{amount:,.0f}")
        
        healing = 0.2
        old_vitality = self.vitality
        self.vitality = min(1.0, self.vitality + healing)
        self.wealth += amount
        
        log(f"    -> バイタル回復: {old_vitality:.2f} => {self.vitality:.2f}")

class Leviathan:
    def attempt_spending(self, target_block: StandardBlock) -> Tuple[float, float]:
        # ランダムに無駄遣いを画策する
        fair_value = 100000000.0  # 適正1億円
        
        # 50%の確率で「異常な歪み（15倍〜30倍）」を発生させる
        if random.random() > 0.5:
            scale = random.uniform(15.0, 30.0)
            return fair_value * scale, fair_value
        else:
            # まともな予算
            return fair_value, fair_value

class GCartValve:
    def check_and_regulate(self, budget: float, fair_value: float, block: StandardBlock) -> Tuple[float, float]:
        distortion = budget / fair_value
        
        if distortion > THRESHOLD_DISTORTION:
            log(f"<span style='color: #ffd700;'>  [🛡️ G-CART] 異常検知: 歪み指数 {distortion:.1f} (Block: {block.name})</span>")
            log(f"    -> 遮断弁閉鎖。適正価格 ¥{fair_value:,.0f} に強制修正。")
            return fair_value, (budget - fair_value)
        
        log(f"  [✅ G-CART] 正常承認: 歪み指数 {distortion:.1f}")
        return budget, 0.0

class TheHeart:
    def __init__(self):
        self.arterial_pool = 0.0

    def diastole(self, saved_wealth: float):
        if saved_wealth > 0:
            flow = saved_wealth * PROTOCOL_FEE_RATE
            self.arterial_pool += flow
            log(f"  [🫀 DIASTOLE] 循環プール還流: +¥{flow:,.0f} (Total: ¥{self.arterial_pool:,.0f})")

    def systole(self, blocks: List[StandardBlock]):
        if self.arterial_pool <= 0:
            return
        
        critical_blocks = [b for b in blocks if b.is_critical()]
        
        if critical_blocks:
            target = min(critical_blocks, key=lambda b: b.vitality)
            injection_amount = self.arterial_pool
            target.receive_transfusion(injection_amount)
            self.arterial_pool = 0.0
        else:
            log("  [💤 SYSTOLE] 全ブロック健常。エネルギー温存。")

# メイン関数
def run_simulation(event):
    clear_log()
    log("==================================================")
    log("   SYSTEM BOOT: The Heart (Global Liquidity Protocol)")
    log("==================================================")
    
    world_blocks = [
        StandardBlock("A", "Tokyo-Minato", 200000, 900000000, 0.95),
        StandardBlock("B", "Osaka-Kita",   150000, 50000000, 0.70),
        StandardBlock("C", "Yubari-Like",  6000,   1000,     0.10),
        StandardBlock("D", "Rural-Village", 3000,  500,      0.20)
    ]
    
    leviathan = Leviathan()
    valve = GCartValve()
    heart = TheHeart()
    
    # 5ターン回してみる
    for turn in range(1, 6):
        log(f"<br>--- Turn {turn}: Monitoring ---")
        
        # ランダムな都市で予算執行
        target = random.choice(world_blocks)
        
        # 1. 予算発生
        budget, fair = leviathan.attempt_spending(target)
        
        # 2. 監査と是正
        paid, saved = valve.check_and_regulate(budget, fair, target)
        
        # 3. 循環
        heart.diastole(saved)
        heart.systole(world_blocks)

    log("<br>==================================================")
    log("   SIMULATION COMPLETE.")
    log("==================================================")
