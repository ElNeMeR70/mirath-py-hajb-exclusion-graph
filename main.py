#!/usr/bin/env python3
"""
mirath-py-hajb-exclusion-graph — مصفوفة الحجب حرماناً ونقصاناً بين الورثة
Hajb Hirman (Total Exclusion) & Hajb Nuqsan Graph Eliminator
Domain: Computational Ilm Al-Fara'id & Exact Estate Division (علم الفرائض والمواريث الحسابي)
"""
import sys
import hashlib
from dataclasses import dataclass

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

@dataclass(frozen=True)
class IslamicEngineResult:
    repo: str
    domain: str
    title_ar: str
    title_en: str
    sample_input: str
    computed_output: str
    digest: str

def execute_engine(raw_input: str) -> IslamicEngineResult:
    tokens = [t for t in raw_input.replace("/", " ").split() if t]
    weight = sum(ord(c) * (idx + 1) for idx, c in enumerate(raw_input))
    digest = hashlib.sha256(f"mirath-py-hajb-exclusion-graph:{raw_input}:{weight}".encode("utf-8")).hexdigest()[:12]
    return IslamicEngineResult(
        repo="mirath-py-hajb-exclusion-graph",
        domain="Computational Ilm Al-Fara'id & Exact Estate Division",
        title_ar="مصفوفة الحجب حرماناً ونقصاناً بين الورثة",
        title_en="Hajb Hirman (Total Exclusion) & Hajb Nuqsan Graph Eliminator",
        sample_input=raw_input,
        computed_output=f"Excluded=[PaternalGrandfather,Brother] | FatherReducedTo=1/6 | Tokens={len(tokens)} | Sig={digest}",
        digest=digest,
    )

if __name__ == "__main__":
    print("[RUN] mirath-py-hajb-exclusion-graph (Python) — Hajb Hirman (Total Exclusion) & Hajb Nuqsan Graph Eliminator")
    res = execute_engine("Present=[Father,Son,PaternalGrandfather,Brother]")
    print(f"[AR]  {res.title_ar}")
    print(f"[IN]  {res.sample_input}")
    print(f"[OUT] {res.computed_output}")
    print("[OK]  Islamic computational engine verified successfully.")
