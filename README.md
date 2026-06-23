# 🔍 OSINT Toolkit

> Automated OSINT reconnaissance toolkit — DNS enumeration, Shodan queries, Google Dorks, email harvesting.

![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=flat-square&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-blue?style=flat-square)
![Author](https://img.shields.io/badge/Author-ibramoha2-CC0000?style=flat-square)

> ⚠️ **Usage éthique uniquement.** Ces outils sont destinés à des audits légaux et autorisés.

---

## 🚀 Installation

```bash
git clone https://github.com/ibramoha2/osint-toolkit
cd osint-toolkit
pip install -r requirements.txt
```

## 📦 Modules

| Module | Description |
|--------|-------------|
| `dns_enum.py` | Énumération DNS complète |
| `email_harvest.py` | Collecte d'emails publics |
| `dork_gen.py` | Générateur de Google Dorks |
| `shodan_scan.py` | Recherche Shodan automatisée |

## ⚡ Usage rapide

```bash
# Énumération DNS
python dns_enum.py -d example.com

# Google Dorks
python dork_gen.py -t example.com -o dorks.txt

# Rapport complet
python osint_report.py -d example.com -o rapport.html
```

---

**Auteur :** [@ibramoha2](https://github.com/ibramoha2) | Niger 🇳🇪
