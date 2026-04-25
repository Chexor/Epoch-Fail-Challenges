# Les 2: Template Method & Hooks

Dit is een **behavioral design pattern**. Het doel is om het skelet van een algoritme te definiëren in een basisklasse, terwijl subklassen specifieke stappen van dat algoritme kunnen invullen zonder de structuur te wijzigen.

---

## A. Wat is het kernprobleem?

Stel je voor dat je meerdere processen hebt die sterk op elkaar lijken, maar op enkele details verschillen. Bijvoorbeeld, het inlezen van data uit een CSV-bestand en een JSON-bestand. De hoofdstructuur is hetzelfde:

1.  Open bestand
2.  **Parse de data** (dit is de variabele stap)
3.  Verwerk de data
4.  Sluit bestand

Zonder een design pattern zou je de hele logica voor elke variant kopiëren en plakken, wat leidt tot gedupliceerde code. Als je de hoofdstructuur wilt aanpassen, moet je dat op meerdere plaatsen doen.

**Het probleem:** Hoe vermijd je code-duplicatie voor algoritmes die in grote lijnen hetzelfde zijn, maar in detail verschillen?

---

## B. Intuïtieve uitleg

Vergelijk het met het maken van een maaltijd. De algemene stappen (het **template**) zijn altijd hetzelfde: `Voorbereiden -> Koken -> Serveren`.

-   `Voorbereiden`: Groenten snijden.
-   `Koken`: De ingrediënten verhitten.
-   `Serveren`: Op een bord leggen.

De *structuur* van het algoritme ligt vast. Maar *wat* je kookt, kan verschillen. Voor pasta kook je water, voor een biefstuk verhit je een pan.

Het **Template Method Pattern** laat de basisklasse (de "chef") de algemene stappen bepalen (`Voorbereiden -> Koken -> Serveren`), terwijl de subklassen (de "koks voor specifieke gerechten") de concrete invulling van die stappen voorzien.

---

## C. Formele structuur

Het patroon bestaat uit twee hoofdcomponenten:

1.  **Abstract Class (De "Chef"):**
    *   Bevat de `templateMethod()`. Dit is een `final` methode die de volgorde van de stappen vastlegt.
    *   Implementeert de stappen die voor alle varianten hetzelfde zijn (bv. `serveren()`).
    *   Definieert abstracte methodes voor de stappen die moeten worden ingevuld door subklassen (bv. `koken()`).
    *   Kan **Hooks** bevatten.

2.  **Concrete Class (De "Specialiteiten-Kok"):**
    *   Erft over van de `Abstract Class`.
    *   Implementeert de verplichte abstracte methodes.
    *   Kan optioneel de `Hooks` overschrijven.

### Wat is een `Hook`?

Een **Hook** is een optionele stap in het algoritme. In de `Abstract Class` heeft een hook een (lege) default implementatie. Een subklasse *kan* deze methode overschrijven om extra gedrag toe te voegen, maar het is niet verplicht.

**Voorbeeld:** Een `extraGarnering()`-stap in het kookproces. Standaard doe je niets, maar een specifieke `Concrete Class` kan deze hook gebruiken om peterselie toe te voegen.

---

## D. Toepassing (Code Voorbeeld)

Laten we het data-verwerkingsprobleem in code gieten.

```java
// AbstractClass
abstract class DataProcessor {

    // 1. De Template Method (final om overschrijven te voorkomen)
    public final void processData() {
        loadData();
        parseData();
        analyzeData(); // Dit is een hook
        saveData();
    }

    // 2. Concrete stappen (zelfde voor iedereen)
    private void loadData() {
        System.out.println("Data wordt ingeladen...");
    }

    private void saveData() {
        System.out.println("Data wordt opgeslagen.");
    }

    // 3. Abstracte stap (moet ingevuld worden)
    protected abstract void parseData();

    // 4. Hook (optionele stap)
    protected void analyzeData() {
        // Lege implementatie, kan overschreven worden
    }
}

// ConcreteClass 1
class CsvDataProcessor extends DataProcessor {
    @Override
    protected void parseData() {
        System.out.println("CSV data wordt geparsed.");
    }
}

// ConcreteClass 2
class JsonDataProcessor extends DataProcessor {
    @Override
    protected void parseData() {
        System.out.println("JSON data wordt geparsed.");
    }

    @Override
    protected void analyzeData() {
        // Deze implementatie gebruikt de hook wél
        System.out.println("Extra analyse op JSON data wordt uitgevoerd.");
    }
}

// Client code
public class Application {
    public static void main(String[] args) {
        System.out.println("--- CSV Processor ---");
        DataProcessor csvProcessor = new CsvDataProcessor();
        csvProcessor.processData();

        System.out.println("\n--- JSON Processor ---");
        DataProcessor jsonProcessor = new JsonDataProcessor();
        jsonProcessor.processData();
    }
}
```

### Output:
```
--- CSV Processor ---
Data wordt ingeladen...
CSV data wordt geparsed.
Data wordt opgeslagen.

--- JSON Processor ---
Data wordt ingeladen...
JSON data wordt geparsed.
Extra analyse op JSON data wordt uitgevoerd.
Data wordt opgeslagen.
```

---

## E. Examengerichte vertaling

*   **Hoe kan dit terugkomen?**
    *   Je krijgt een stuk code met gedupliceerde logica en moet dit refactoren met het Template Method Pattern.
    *   Een vraag over het verschil tussen een abstracte methode en een hook in de context van dit patroon.
    *   Je moet de `final` keyword op de template method kunnen verklaren (zorgt ervoor dat subklassen de structuur van het algoritme niet kunnen wijzigen).
*   **Vaak gemaakte fouten:**
    *   De template method niet `final` maken.
    *   Een hook `abstract` maken (dan is het geen hook meer, maar een verplichte stap).
    *   Het doel van het patroon verwarren met het Strategy Pattern (Template Method gebruikt overerving, Strategy gebruikt compositie).
*   **Wat moet ik zeker begrijpen?**
    *   Dit patroon implementeert het **Hollywood Principle**: "Don't call us, we'll call you". De basisklasse (algemeen) roept de methodes van de subklasse (detail) aan, niet andersom. Dit heet *Inversion of Control*.
    *   Het doel is code-hergebruik en het afdwingen van een consistente structuur voor een familie van algoritmes.
