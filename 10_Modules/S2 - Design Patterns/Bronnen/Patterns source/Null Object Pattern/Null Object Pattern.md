## Null Object Pattern

### Doel

Het Null Object Pattern heeft als doel om minder controles op het bestaan van objecten nodig te hebben. Dus: minder controles waar je nagaat of een referentie naar een object niet null is.

### Aanpak

Er is een klasse Foo met een bepaald gedrag.

```java
public class Foo {
    public void doSomething() { // implementatie }
}
```

Klasse Bar heeft dat gedrag van Foo nodig, maar het is niet altijd zeker dat er wel een object van Foo is. Daarom controleert klasse Bar eerst of het object wel bestaat.

```java
public class Bar {
    private Foo foo;
    public void useFoo() {
        if (foo != null) {
            foo.doSomething();
        }
    }
}
```
De controle of foo niet null is willen we weg, om de code overzichtelijker te maken.

Dat kan door een interface te definiëren voor Foo. Foo implementeert die interface, en klasse Bar gebruikt die interface. We maken dan een andere klasse die die interface implementeert, maar die eigenlijk niks doet: het null object. We zorgen er voor dat het veld foo in Bar default naar dat null object verwijst.

```java
interface IFoo {
    void doSomething();
}

public class Foo implements IFoo {
public void doSomething() { // implementatie }
}

public class NullFoo implements IFoo {
    public void doSomething() { // hier gebeurt niets! }
}

public class Bar {
    private IFoo foo = new NullFoo();
    public void useFoo() {
        foo.doSomething();
    }
}
```

In methode `useFoo()` is de controle of foo wel bestaat nu niet meer nodig.
### Voordeel
Implementaties van methodes worden overzichtelijker omdat er minder controles in staan.
### Nadeel
Meer klassen: codebasis als geheel wordt minder overzichtelijk.
### Gang of Four
Null object is geen Gang of Four-pattern.