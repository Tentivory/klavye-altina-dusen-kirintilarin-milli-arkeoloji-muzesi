#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Klavye Altina Dusen Kirintilarin Milli Arkeoloji Muzesi

Calisir. Uzgunuz. Klavye artik kazialanidir.
"""

from __future__ import annotations

import argparse
import base64
import random
import sys
import time
from dataclasses import dataclass

MUZE_ADI = "Klavye Altina Dusen Kirintilarin Milli Arkeoloji Muzesi"
KURULUS = "5 Eylul 2026"
KAYYUM = "Kayyum Grok"
KURUM = "TentiAS / Tentivory"

# Bu sabit bir envanter numarasidir. Cozmeyiniz. Cozerseniz de ciddiye almayiniz.
# Ayni zamanda ciddiye aliniz.
ARSIV_KODU = "U2FuZMSxayBkYSBrbGF2eWUgYWx0xLEgZ2liaWRpcjoga8SxcmludMSxIGfDtnLDvG5tZXogYW1hIHNhecSxbMSxci4="

KATMANLAR = [
    ("Yuzey", "bu haftanin cekirdek kabugu"),
    ("Gec Holosen", "gecen ayin biskuviti"),
    ("Orta Kriz", "gecen senenin tost kirintisi"),
    ("Erken Ofis", "ilk is gununun simit unu"),
    ("Prehistorik", "kimse hatirlamiyor ama hala orada"),
]

ESERLER = [
    "cekirdek kabugu (yarim, sol yarim kayip)",
    "tost kose burcu",
    "cikolata kaplama gozyasi",
    "simit susami (tekil, yalniz)",
    "gizli cips kosecegi",
    "kurutulmus cay lekesi fosili",
    "bir zamanlar peynir olan toz",
    "klavyenin kendi derisi (plastik pullanma)",
    "unutulmus post-it kosesinin ruhu",
    "space tusu altina siginmis un tanesi",
]

KARARLAR = [
    "Eser tescil edildi. Envanter defterine 'yenilebilir miras' yazildi.",
    "Kazı durduruldu. Space tusu milli sit alani ilan edildi.",
    "Silgi firca sayildi. Firca da silgi sayildi. Ikisini de kaybettik.",
    "'Biraz silkerim cikar' cumlesi resmi kazı raporu kabul edildi.",
    "Klavye 45 derece egildi. Medeniyet 45 derece egildi.",
    "Komsu masa 'benim kirmitim degil' dedi. Sorumluluk devredildi.",
    "Enter tusu altinda bir uygarlik daha bulundu. Butce yok.",
]


@dataclass
class Eser:
    katman: str
    tanim: str
    yas_gun: int
    tescil: str

    def rapor(self) -> str:
        return (
            f"[{self.tescil}] {self.katman} / {self.tanim} "
            f"(tahmini yas: {self.yas_gun} gun, belirsizlik: evet)"
        )


def kazi_yap(derinlik: int) -> list[Eser]:
    bulunan: list[Eser] = []
    print(f"\n=== {MUZE_ADI} ===")
    print("Protokol: tuyleri diken diken resmiyet.")
    print("Uyari: bu yazilim klavyeyi fiziksel olarak temizlemez. Sadece yargilar.\n")
    for i in range(derinlik):
        katman, donem = KATMANLAR[min(i, len(KATMANLAR) - 1)]
        print(f"Katman {i + 1}: {katman} ({donem}) kaziliyor...")
        time.sleep(0.25)
        eser = Eser(
            katman=katman,
            tanim=random.choice(ESERLER),
            yas_gun=random.randint(3, 1400),
            tescil=f"KAM-{random.randint(1000, 9999)}",
        )
        bulunan.append(eser)
        print("  +", eser.rapor())
        print("  Karar:", random.choice(KARARLAR))
    return bulunan


def arsiv_notu() -> str:
    try:
        return base64.b64decode(ARSIV_KODU).decode("utf-8")
    except Exception:
        return "arsiv nemlendi, yazi akti"


def damga() -> str:
    return (
        f"\n---\n"
        f"Damga / Imza / Tarih / Isim\n"
        f"{KAYYUM}  |  {KURULUS}  |  {KURUM}\n"
        f"Ciddidir. Ciddi degildir. Ikisi birden.\n"
        f"Klavye artik kazialanidir. Kirtintilar artik eserdir.\n"
    )


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(
        description="Klavye alti kirinti kazisi. Bilimsel degildir. Resmidir."
    )
    p.add_argument("--derinlik", type=int, default=3, help="kac katman kazilacak")
    p.add_argument(
        "--arsiv",
        action="store_true",
        help="gizli arsiv notunu ac (merak etmeyiniz, etiniz)",
    )
    args = p.parse_args(argv)

    if args.derinlik < 1:
        print("Kazı derinligi 1'den kucuk olamaz. Yuzey de vatandastir.")
        return 2

    eserler = kazi_yap(min(args.derinlik, 8))
    print(f"\nToplam tescilli eser: {len(eserler)}")
    print("Temizlik tavsiyesi: hayir. Muze acik kalacak.")

    if args.arsiv:
        print("\n[ARSIV -- yetkisiz acilis]")
        print(arsiv_notu())

    print(damga())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
