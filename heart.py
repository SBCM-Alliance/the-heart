from dataclasses import dataclass
from typing import List, Tuple
import js
from pyscript import document

# --- System Constants ---
THRESHOLD_DISTORTION = 10.0
PROTOCOL_FEE_RATE = 0.1

# 出力用ヘルパー
def log(text):
    term = js.document.getElementById("terminal")
    if "System Ready" in term.innerText:
        term.innerText = text + "\n"
    else:
        term.innerText += text + "\n"
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
        return self.vitality < 0.3 or self.wealth < 10000

    def receive_transfusion(self, amount: float):
        log(f"  [💗 THE HEART] 輸血を実行 -> Target: {self.name}")
        log(f"    -> 特別クエスト発注: 予算 ¥{amount:,.0f}")
        
        healing = (amount / 100000000) * 0.1 
        old_vitality = self.vitality
        self.vitality = min(1.0, self.vitality + healing)
        self.wealth += amount
        
        log(f"    -> バイタル回復: {old_vitality:.2f} => {self.vitality:.2f}")
        log(f"    -> 地域富の増加: ¥{self.wealth:,.0f}")

class Leviathan:
    def attempt_spending(self, target_block: StandardBlock) -> Tuple[float, float]:
        fair_value = 100000000.0
        bloated_budget = 1000000000.0
        return bloated_budget, fair_value

class GCartValve:
    def check_and_regulate(self, budget: float, fair_value: float, block: StandardBlock) -> Tuple[float, float]:
        distortion = budget / fair_value
        if distortion > THRESHOLD_DISTORTION:
            log(f"  [🛡️ G-CART] 異常検知: 歪み指数 {distortion:.1f} (Block: {block.name})")
            log(f"    -> 遮断弁閉鎖。適正価格 ¥{fair_value:,.0f} に強制修正。")
            return fair_value, (budget - fair_value)
        return budget, 0.0

class TheHeart:
    def __init__(self):
        self.arterial_pool = 0.0

    def diastole(self, saved_wealth: float):
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
            log("  [🫀 SYSTOLE] 全ブロックの健常性を確認。エネルギーを温存します。")

# ボタンから呼ばれるメイン関数
def run_simulation(event):
    clear_log()
    log("==================================================")
    log("   SYSTEM BOOT: The Heart (Global Liquidity Protocol)")
    log("==================================================\n")
    
    world_blocks = [
        StandardBlock("A", "Tokyo-Minato", 200000, 999999999, 0.95),
        StandardBlock("B", "Osaka-Kita",   150000, 50000000, 0.70),
        StandardBlock("C", "Yubari-Like",  6000,   1000,     0.15)
    ]
    
    leviathan = Leviathan()
    valve = GCartValve()
    heart = TheHeart()
    
    log("--- Phase 1: Distortion & Regulation ---")
    target_block = world_blocks[0]
    
    budget, fair = leviathan.attempt_spending(target_block)
    log(f"Target: {target_block.name} | 行政提示額: ¥{budget:,.0f}")
    
    paid, saved = valve.check_and_regulate(budget, fair, target_block)
    log(f"-> 執行額: ¥{paid:,.0f} | 浮いた税金(Surplus): ¥{saved:,.0f}")
    
    log("\n--- Phase 2: The Heartbeat ---")
    heart.diastole(saved)
    heart.systole(world_blocks)
    
    log("\n==================================================")
    log("   SYSTEM STATUS: Stable. Circulation Optimized.")
    log("==================================================")
