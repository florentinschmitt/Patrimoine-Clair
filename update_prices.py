#!/usr/bin/env python3
"""Met à jour prices.json à partir de tickers.json.
Source : API non officielle de Yahoo Finance (peut changer ou se bloquer sans préavis)."""
import json
import urllib.request
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).parent
URL = "https://query1.finance.yahoo.com/v8/finance/chart/{}?interval=1d&range=5d"


def fetch(symbol):
    req = urllib.request.Request(URL.format(symbol), headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        meta = json.load(r)["chart"]["result"][0]["meta"]
    price = meta.get("regularMarketPrice")
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("cours absent")
    if meta.get("currency") not in ("EUR", None):
        raise ValueError(f"devise {meta.get('currency')} (EUR attendu)")
    return round(float(price), 4)


def main():
    tickers = {k.upper(): v for k, v in json.loads((ROOT / "tickers.json").read_text(encoding="utf-8")).items()}
    out = ROOT / "prices.json"
    try:
        prices = json.loads(out.read_text(encoding="utf-8")).get("prices", {})
    except (FileNotFoundError, json.JSONDecodeError):
        prices = {}
    prices = {k: v for k, v in prices.items() if k in tickers}
    ok = 0
    for code, symbol in tickers.items():
        try:
            prices[code] = fetch(symbol)
            ok += 1
            print(f"OK {code} ({symbol}) : {prices[code]}")
        except Exception as e:
            print(f"KO {code} ({symbol}) : {e}")
    if ok == 0:
        raise SystemExit("Aucun cours récupéré : prices.json non modifié.")
    now = datetime.now(ZoneInfo("Europe/Paris")).strftime("%d/%m/%Y")
    out.write_text(json.dumps({"updated": now, "prices": prices}, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
