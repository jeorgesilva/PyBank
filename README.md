# PyBank - Online-Banking-System

Dieses Projekt ist ein grundlegendes Online-Banking-System, das Benutzern folgende Funktionen bietet:

-   Registrierung im System
-   Anmeldung und Abmeldung
-   Änderung des Passworts
-   Anzeige und Aktualisierung des Kontostands
-   Überweisung von Geld zwischen Benutzern
-   Löschung des Benutzerkontos

## Funktionen

1.  **Benutzerregistrierung:**

    -   Benutzer können sich mit einem Benutzernamen und einem Passwort registrieren.
    -   Das Passwort muss folgende Kriterien erfüllen:
        -   Mindestens 8 Zeichen Länge
        -   Mindestens ein Großbuchstabe
        -   Mindestens ein Kleinbuchstabe
        -   Mindestens eine Ziffer
    -   (Hinweis: Aktuell werden Benutzernamen und Passwörter im Speicher gehalten und nicht persistent gespeichert.)

2.  **Anmeldung und Abmeldung:**

    -   Benutzer können sich mit ihren registrierten Anmeldedaten anmelden.
    -   Der Anmeldestatus wird temporär in einem Dictionary gespeichert.

3.  **Kontostandverwaltung:**

    -   Benutzer können Geld auf ihr Konto einzahlen und abheben.
    -   Der Kontostand darf nicht negativ werden.

4.  **Geldüberweisung:**

    -   Benutzer können Geld an andere registrierte Benutzer überweisen.
    -   Der Kontostand des Absenders muss die Überweisungssumme decken.

5.  **Passwortänderung:**

    -   Benutzer können ihr Passwort ändern, sofern das neue Passwort die definierten Kriterien erfüllt.

6.  **Kontolöschung:**

    -   Benutzer können ihr Konto löschen, wodurch die zugehörigen Daten entfernt werden.

## Technische Hinweise

-   Die Benutzerdaten und Kontostände werden aktuell nur im Speicher gehalten und gehen beim Beenden des Programms verloren. **Eine persistente Speicherung (z.B. in einer Datenbank) ist für eine reale Anwendung erforderlich, aber in dieser vereinfachten Version nicht implementiert.**
-   Die Passwortsicherheit ist grundlegend. **Für eine produktionsreife Anwendung wären deutlich sicherere Methoden (z.B. Hashing) notwendig.**
-   Es gibt keine Fehlerbehandlung für ungültige Benutzereingaben.

## Wie man das Projekt ausführt

1.  Klonen Sie das Repository:

    ```bash
    git clone [https://github.com/ihr-benutzername/PyBank.git](https://github.com/ihr-benutzername/PyBank.git)
    ```

2.  Navigieren Sie zum Projektverzeichnis:

    ```bash
    cd PyBank
    ```

3.  Führen Sie das Skript aus:

    ```bash
    python PyBank.py
    ```

## Geplante Erweiterungen (To-Do)

-   Persistente Speicherung der Daten in einer Datenbank (z.B. SQLite)
-   Implementierung sichererer Passwortspeicherung (z.B. Hashing mit Salt)
-   Verbesserte Fehlerbehandlung und Validierung der Benutzereingaben
-   Erweiterung der Funktionalitäten (z.B. Transaktionshistorie, verschiedene Kontotypen)
-   Erstellung von Unit-Tests zur Sicherstellung der Codequalität
