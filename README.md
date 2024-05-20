# Projekt pro detekci švů a vyhodnocení anotací

Tento projekt obsahuje několik Jupyter notebooků zaměřených na detekci švů na obrázcích a vyhodnocení přesnosti těchto detekcí. Níže jsou uvedeny jednotlivé skripty a jejich stručný popis.

## Soubory

### 1. `Detekce_svu.ipynb`

**Popis:**
Tento notebook je zaměřen na detekci švů pomocí různých metod zpracování obrazu a morfologických operací. Obsahuje kroky jako předzpracování obrazů, aplikaci hranového detektoru a morfologické operace pro zvýraznění švů.

**Hlavní kroky:**
- Načtení a předzpracování obrazových dat.
- Aplikace hranového detektoru.
- Morfologické operace pro zvýraznění švů.
- Detekce a počítání objektů.
- Vyhodnocení přesnosti detekce.

### 2. `SVM.ipynb`

**Popis:**
Tento notebook využívá algoritmus Support Vector Machine (SVM) pro klasifikaci švů na obrázcích. Notebook obsahuje kroky jako načtení dat, předzpracování, trénink SVM modelu a vyhodnocení jeho přesnosti.

**Hlavní kroky:**
- Načtení a předzpracování dat.
- Rozdělení dat na trénovací a testovací sady.
- Trénink SVM modelu.
- Vyhodnocení modelu na testovacích datech.

### 3. `evaluationOfAnotation.ipynb`

**Popis:**
Tento notebook se zaměřuje na vyhodnocení přesnosti anotací provedených na obrázcích. Porovnává výsledky ručně anotovaných švů s výsledky automatické detekce a počítá metriky přesnosti.

**Hlavní kroky:**
- Načtení anotovaných dat.
- Porovnání ručních a automatických anotací.
- Výpočet metrik přesnosti, jako je přesnost a F1 skóre.

## Požadavky

Pro spuštění těchto notebooků je potřeba mít nainstalované následující knihovny:
- numpy
- pandas
- matplotlib
- scikit-learn
- opencv-python
- scikit-image
- jupyter

## Jak začít

1. Klonujte tento repozitář:
   ```sh
   git clone https://github.com/kmuller00/ZDO_sem2024.git
   cd projekt
2. pip install -r requirements.txt
3. jupyter notebook
