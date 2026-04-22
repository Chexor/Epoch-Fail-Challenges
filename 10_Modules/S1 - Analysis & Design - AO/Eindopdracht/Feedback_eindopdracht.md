**Score: 11/20**

Goede casus.

De lijst met usecases is vrij goed.

"Melding afsluiten" is geen zinvolle usecase. Een melding bekijken wel.

UC10 is te ruim van scope, en moet opgesplitst worden per doel van het rapport.

De lijst is beperkter dan wat je in de casus opgeeft. Daar is er ook sprake van "voertuigtypes" en "onderhoudsparameters".

UC5 lijkt me een onderdeel van UC4 te zijn.

Er ontbreekt een usecase voor aanmelden.

Het usecasediagram is goed.

De usecasebeschrijvingen zijn goed ingedeeld. Er is aandacht voor uitzonderingen, en voor wat het systeem doet.

Sommige zaken moeten nog verder gespecificeerd worden. Vb: "De opgegeven periode is ongeldig": wat zijn de criteria om te beslissen over geldigheid?

Soms kan het systeem meer helpen. De eerste stap van het normaal scenario bij Schade/Defect melden lijkt overkill. Het systeem weet toch welk voertuig de gebruiker heeft? Waarom moet de gebruiker dan nog eens dat voertuig invoeren?

De niet-functionele eisen zijn zinvol maar weinig meetbaar geformuleerd.

In het domeinmodel zitten de nodige domeinconcepten.

Enumeraties hebben geen associaties.

De multipliciteiten bij de associatie Reservering – Rit moeten andersom.

Id-attributen zijn enkel nodig in een domeinmodel als de gebruikers die id's ook daadwerkelijk zien en gebruiken.

Twee statussen voor klasse Reservering is weinig. Wat met reserveringen waarvan de rit lopende is, en reserveringen waarvan de rit afgelopen is?

De beschrijving van klassen en attributen is goed.

De lijst met events is goed. Maar voor klassen die een status-attribuut hebben is het beter om met meer dan 1 wijzigingsevent te werken. Dat wordt ook duidelijk bij de specificatie van MOD_Reservatie: daar blijkt dat niet 1 event te zijn, maar 2 verschillende.

De propagatie in de object event table is niet goed.

De eventspecifiicaties zijn goed ingedeeld, en ze houden rekening met bestaansafhankelijkheid.

Wat je doet met MOD_Reservatie is niet correct. Twee events met dezelfde naam, dat mag niet.

In CRE_Rit zijn de laatste twee regels van de postcondities niet nodig en niet gewenst.

In MOD_Rit moet de naam van het event overeenkomen met die in de OET. De tussentitel "Propagatie" is niet nodig en niet gewenst. Wat je daaronder schrijft hoort bij de postcondities van het event. De "conditionele propagatie" is niet correct. Maak geen functie van een event. Een event kan geen andere events triggeren.

In END_Rit ontbreekt de eis dat er geen Melding-objecten meer mogen bestaan die afhangen van Rit.

In CRE_Melding dan weer ontbreekt het ouderobject Rit. Houd je daar aan je domeinmodel. Volgens je domeinmodel is een Melding geassocieerd met een Rit, niet met een Voertuig.

De toestandsdiagrammen zijn correct, maar ook hier is er het probleem met de verwarrende naamgeving die je gebruikt voor events.

Je kunt de technieken uit de cursus toepassen, zij het met tekortkomingen. De vereistenanalyse en het domeinmodel zijn vrij goed, het eventmodel is echter niet bruikbaar in de huidige vorm. Voldoende.