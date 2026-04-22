---
type: topic-samenvatting
vak: Introduction to AI
topic: 2 - Machine Learning & Deep Learning
status: afgerond
---

# Samenvatting Topic 2: Machine Learning & Deep Learning

Up: [[10_Modules/S2 - IoT1/00_Module_Overzicht]]

Deze samenvatting behandelt de fundamenten van Machine Learning en Deep Learning, gebaseerd op de slides van Topic 2a en 2b.

---

## Deel 1: Machine Learning (Topic 2a)

### 1. Wat is Machine Learning?
Machine Learning (ML) stelt systemen in staat om te **leren van data** zonder expliciet geprogrammeerd te zijn.

- **Klassieke Definitie (Arthur Samuel, 1959):** "Het vakgebied dat computers de mogelijkheid geeft te leren zonder expliciet geprogrammeerd te zijn."
- **Moderne Definitie (Tom Mitchell, 1997):** Een computerprogramma leert van **Ervaring (E)** met betrekking tot een **Taak (T)** en een **Prestatiemaatstaf (P)**, als de prestatie op T verbetert met ervaring E.

### 2. De Drie Hoofdtypes van ML
1. **[[Supervised Learning]] (Begeleid Leren):** Leren van gelabelde data (input + correct antwoord).
   - *Classificatie:* Voorspellen van categorieën (bv. Spam/Geen Spam).
   - *Regressie:* Voorspellen van continue waarden (bv. Huizenprijs).
1. **[[Unsupervised Learning]] (Onbegeleid Leren):** Zoeken naar patronen in unlabeled data.
   - *Clustering:* Groeperen van vergelijkbare data (bv. Klantsegmentatie).
   - *Dimensionality Reduction:* Vereenvoudigen van complexe data.
3. **[[Reinforcement Learning]] (Bekrachtigend Leren):** Leren door interactie met een omgeving via beloningen en straffen (bv. Spellen, Robotica).

### 3. Belangrijke Terminologie
- **Model:** De wiskundige representatie van patronen in de data.
- **Features:** Inputvariabelen (kenmerken).
- **Label / Target:** De te voorspellen output (bij Supervised Learning).
- **Training vs. Test Data:** Data om te leren vs. data om de prestaties te meten.

---

## Deel 2: Deep Learning (Topic 2b)

### 1. Wat is Deep Learning?
Deep Learning is een subveld van ML dat gebruikmaakt van **Artificiële Neurale Netwerken (ANNs)** met vele lagen (**"Deep"**). Het is geïnspireerd op de werking van het menselijk brein.

### 2. De Bouwsteen: De Neuron (Perceptron)
Een artificiële neuron:
1. Ontvangt **Inputs**.
2. Vermenigvuldigt deze met **Gewichten (Weights)**.
3. Telt alles op en stuurt het door een **[[Activation Function]]** (bepaalt of het neuron "vuurt").

### 3. Structuur van een Neuraal Netwerk
- **Input Layer:** Ontvangt ruwe data.
- **Hidden Layers:** Hier vindt de extractie van kenmerken plaats.
- **Output Layer:** Geeft het uiteindelijke resultaat.

**[[Hierarchical Feature Learning]]:**
- Vroege lagen: Simpele patronen (randen, lijnen).
- Diepere lagen: Complexere concepten (ogen, gezichten, objecten).

### 4. Waarom nu?
De doorbraak van (Deep) Learning komt door:
- **Big Data:** Enorme hoeveelheden trainingsdata.
- **GPU's:** Krachtige hardware voor parallelle berekeningen.
- **Betere Algoritmes:** Innovaties in optimalisatie en architectuur.

### 5. Uitdagingen
- **Data-hongerig:** Vereist enorme datasets.
- **Black Box:** Moeilijk te begrijpen *waarom* een model een beslissing neemt.
- **Overfitting:** Het model leert de trainingsdata te goed "uit het hoofd" en faalt op nieuwe data.

---

## Actiepunten
- [ ] Bekijk de conceptnotities voor [[Supervised Learning]] en [[Deep Learning]].
- [ ] Oefen met het onderscheiden van Classificatie vs. Regressie.
