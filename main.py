"""
System Name: The Heart
Subtitle: Algorithmic Pump for Global Wealth Circulation
-------------------------------------------------------
"Logic is the Brain. But this Protocol is the Heart."

[Theory of Operation]
1. Leviathan (The State) attempts to execute a distorted budget.
2. G-Cart (The Valve) detects the Distortion ($D_index > 10$) and blocks it.
3. The Heart (The Pump) collects the saved wealth (Surplus).
4. The Protocol injects this liquidity into dying blocks not as charity,
   but as "Special Quests" (Infrastructure Repair & Skill Dev).

Author: SBCM Alliance (Hokuto Koyama)
Date: 2025-12-02
License: MIT
Status: Alive
"""

import random
from dataclasses import dataclass
from typing import List, Tuple

# --- System Constants ---
THRESHOLD_DISTORTION = 10.0  # 許容される歪み指数 ($D_index$) の限界値
PROTOCOL_FEE_RATE = 0.1      # プロトコル維持・再分配のためのプール率 (10%)

@dataclass
class StandardBlock:
    """
    基礎自治体 (Standard Block) の定義
    """
    id: str
    name: str
    population: int
    wealth: float          # 地域内の富の総量
    vitality: float        # 生命力/インフラ健全度 (0.0 - 1.0)
    
    @property
    def scale_factor(self) -> float:
        """SBCM規模係数 (人口 / 72,176)"""
        return self.population / 72176.0

    def is_critical(self) -> bool:
        """救命措置が必要な状態か判定"""
        return self.vitality < 0.3 or self.wealth < 10000

    def receive_transfusion(self, amount: float):
        """
        【輸血プロセス】
        現金のバラマキではなく、Yorbee経由の「特別クエスト」として発注される。
        これにより、インフラが修復され、かつ富が地元業者に定着($R_block=1.0$)する。
        """
        print(f"  [💗 THE HEART] 輸血を実行 -> Target: {self.name}")
        print(f"    -> 特別クエスト発注: 予算 ¥{amount:,.0f}")
        
        # 1. 治癒 (Vitality回復)
        # 金額に応じた物理的なインフラ修復効果
        healing = (amount / 100000000) * 0.1 
        old_vitality = self.vitality
        self.vitality = min(1.0, self.vitality + healing)
        
        # 2. 循環 (Wealth定着)
        self.wealth += amount
        
        print(f"    -> バイタル回復: {old_vitality:.2f} => {self.vitality:.2f}")
        print(f"    -> 地域富の増加: ¥{self.wealth:,.0f}")

class Leviathan:
    """
    リヴァイアサン: 金銭感覚と痛覚を持たない巨大行政機構
    """
    def attempt_spending(self, target_block: StandardBlock) -> Tuple[float, float]:
        """
        無駄なハコモノを作ろうとする (例: 適正1億円の案件に10億円つける)
        """
        fair_value = 100000000.0  # 実勢価格 1億円
        bloated_budget = 1000000000.0 # 提示額 10億円 (歪み10倍)
        
        return bloated_budget, fair_value

class GCartValve:
    """
    G-Cart: 歪みを検知し、適正圧に調整する弁
    """
    def check_and_regulate(self, budget: float, fair_value: float, block: StandardBlock) -> Tuple[float, float]:
        """
        戻り値: (執行される金額, カットされて浮いた金額)
        """
        # SBCM計算: 予算インパクト / 普及インパクト(ここでは1.0と仮定)
        # 簡易的に 金額倍率 で判定
        distortion = budget / fair_value
        
        if distortion > THRESHOLD_DISTORTION:
            print(f"  [🛡️ G-CART] 異常検知: 歪み指数 {distortion:.1f} (Block: {block.name})")
            print(f"    -> 遮断弁閉鎖。適正価格 ¥{fair_value:,.0f} に強制修正。")
            return fair_value, (budget - fair_value)
        
        return budget, 0.0

class TheHeart:
    """
    The Heart: 地球規模の循環ポンプ
    """
    def __init__(self):
        self.arterial_pool = 0.0 # 動脈プール (再分配用資金)

    def diastole(self, saved_wealth: float):
        """
        【拡張期】 余剰資源の吸い上げ
        G-Cartによって節約された税金の一部を、循環系に取り込む。
        """
        flow = saved_wealth * PROTOCOL_FEE_RATE
        self.arterial_pool += flow
        print(f"  [🫀 DIASTOLE] 循環プール還流: +¥{flow:,.0f} (Total: ¥{self.arterial_pool:,.0f})")

    def systole(self, blocks: List[StandardBlock]):
        """
        【収縮期】 瀕死のブロックへの圧送
        最もバイタルの低いブロックへ、プールされた全エネルギーを送り込む。
        """
        if self.arterial_pool <= 0:
            return

        # トリアージ: 最も危険な状態のブロックを探す
        critical_blocks = [b for b in blocks if b.is_critical()]
        
        if critical_blocks:
            # 最も弱っているブロックを特定
            target = min(critical_blocks, key=lambda b: b.vitality)
            
            # 全エネルギーを放出 (Quest Injection)
            injection_amount = self.arterial_pool
            target.receive_transfusion(injection_amount)
            
            self.arterial_pool = 0.0
        else:
            print("  [🫀 SYSTOLE] 全ブロックの健常性を確認。エネルギーを温存します。")

# --- Main Simulation Sequence ---

def main():
    print("==================================================")
    print("   SYSTEM BOOT: The Heart (Global Liquidity Protocol)")
    print("==================================================\n")
    
    # 世界 (Body) の生成
    world_blocks = [
        StandardBlock("A", "Tokyo-Minato", 200000, 999999999, 0.95), # 過剰に元気
        StandardBlock("B", "Osaka-Kita",   150000, 50000000, 0.70),  # 普通
        StandardBlock("C", "Yubari-Like",  6000,   1000,     0.15)   # 瀕死 (Critical)
    ]
    
    # モジュール初期化
    leviathan = Leviathan()
    valve = GCartValve()
    heart = TheHeart()
    
    # --- Step 1: 歪みの発生と検知 ---
    print("--- Phase 1: Distortion & Regulation ---")
    target_block = world_blocks[0] # 東京で無駄遣いが発生
    
    # リヴァイアサンが予算を提示
    budget, fair = leviathan.attempt_spending(target_block)
    print(f"Target: {target_block.name} | 行政提示額: ¥{budget:,.0f}")
    
    # G-Cartが介入・最適化
    paid, saved = valve.check_and_regulate(budget, fair, target_block)
    print(f"-> 執行額: ¥{paid:,.0f} | 浮いた税金(Surplus): ¥{saved:,.0f}")
    
    # --- Step 2: 循環 (The Heartbeat) ---
    print("\n--- Phase 2: The Heartbeat ---")
    
    # 拡張期: 余剰の一部を吸い上げる
    heart.diastole(saved)
    
    # 収縮期: 瀕死のブロックCへ輸血する
    heart.systole(world_blocks)
    
    print("\n==================================================")
    print("   SYSTEM STATUS: Stable. Circulation Optimized.")
    print("==================================================")

if __name__ == "__main__":
    main()
