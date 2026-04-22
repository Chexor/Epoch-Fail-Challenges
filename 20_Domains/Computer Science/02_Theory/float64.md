---
type: theory
domain: "computer-science"
parent: "Data Representation"
related:
  - Data Representation
  - float32
  - uint8
  - float32 vs float64
theme: "data-representation-and-computation"
aliases:
  - float64
---

# float64
#concept #cs

## 1. Wat is het kernprobleem?
Je moet weten welk datatype gebruikt wordt om kommagetallen op te slaan, omdat dit invloed heeft op precisie en geheugen.

## 2. Intuitieve uitleg
`float64` is een datatype voor kommagetallen met hoge precisie. Het kan veel decimalen nauwkeurig voorstellen, maar gebruikt meer geheugen dan `float32`.

## 3. Formele structuur
- `float64` gebruikt 64 bits = 8 bytes
- Geschikt voor decimale berekeningen met hogere nauwkeurigheid
- Wordt vaak standaard gebruikt in NumPy en wetenschappelijke berekeningen

## 4. Toepassing
Bij numerieke berekeningen kan `float64` nuttig zijn als kleine afrondingsfouten een groot effect hebben.

## 5. Examengerichte vertaling
- **Typische vraag:** Wat is het verschil tussen `float64` en `float32`?
- **Vaak gemaakte fout:** Denken dat meer bits altijd beter is, zonder rekening te houden met geheugen en snelheid.
- **Link met andere concepten:** [[float32]], [[uint8]]

## Context in het domein
- Overzicht: [[00_Overzicht Computer Science]]
- Umbrella: [[Datatypes]]
- Vergelijking: [[float32 vs float64]]
- Uitwerking: [[Datatypekeuze Worked Example]]
