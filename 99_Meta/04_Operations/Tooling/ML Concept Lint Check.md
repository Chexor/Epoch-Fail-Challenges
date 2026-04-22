# ML Concept Lint Check

Gebruik deze check om structuurproblemen snel te vinden in `20_Domains/Machine Learning`.

## Script

- `99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py`

## Wat wordt gecontroleerd?

- H1-titel aanwezig (`# ...`)
- Korte uitleg direct onder titel/tag-regel (voor hover pop-up)
- Optioneel (strict voor `02_Theory/`): vaste sectiestructuur

## Gebruik

```bash
python3 "99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py"
```

Met extra structuurcontrole voor theory-notes:

```bash
python3 "99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py" --strict-theory
```

Met auto-fix (intro-zin en ontbrekende theory-secties):

```bash
python3 "99_Meta/04_Operations/Tooling/lint_ml_concept_notes.py" --strict-theory --fix
```

## Exit codes

- `0`: alles OK
- `1`: minstens 1 lint-issue gevonden
- `2`: map niet gevonden / fout pad

## Aanbevolen routine

Bij wijzigingen in `20_Domains/Machine Learning`:

1. run `--strict-theory --fix`
2. run daarna nog eens zonder `--fix` als verificatie
