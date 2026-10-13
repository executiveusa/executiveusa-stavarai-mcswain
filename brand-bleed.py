#!/usr/bin/env python3
"""Fails if store-only content appears on the personal site outside the Postatees row.
Usage: python3 brand-bleed.py design.html"""
import re,sys
html=open(sys.argv[1],encoding='utf-8').read()
# regions where store content is allowed: the Postatees work row, the 'Inside Postatees' strip, the brand links in Contact
allowed=[r'<li><a href="https://www\.postatees\.com".*?</li>', r'<div class="inside".*?</div>', r'<div class="brandlinks">.*?</div>']
for pat in allowed:
    html=re.sub(pat,'',html,flags=re.S)
banned=["No Idol","Premium streetwear","love for the game","Exchange or store credit","Support replies","VIP","Seattle Edition","Signature Athletes","Beanie","Custom Merch","Limited Edition Green","Hoodies &amp; Zippers","30 days","10% off","Shop the store","serious collector"]
hits=[b for b in banned if b.lower() in html.lower()]
print("BRAND BLEED:",hits if hits else "none")
sys.exit(1 if hits else 0)
