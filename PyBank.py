def valid(password):
    """
    Überprüft, ob das Passwort die Anforderungen erfüllt:
    - Mindestens 8 Zeichen.
    - Mindestens ein Großbuchstabe.
    - Mindestens ein Kleinbuchstabe.
    - Mindestens eine Zahl.
    """
    if len(password) < 8:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    return True

def signup(user_accounts, log_in, username, password):
    """
    Ermöglicht es einem Benutzer, sich im System zu registrieren.
    Gibt True zurück, wenn die Registrierung erfolgreich ist, sonst False.
    """
    if username in user_accounts:
        return False
    if not valid(password):
        return False
    if username == password:
        return False
    
    user_accounts[username] = password
    log_in[username] = False
    return True

def login(user_accounts, log_in, username, password):
    """
    Ermöglicht es einem Benutzer, sich im System anzumelden.
    Gibt True zurück, wenn die Anmeldung erfolgreich ist, sonst False.
    """
    if username not in user_accounts or user_accounts[username] != password:
        return False
    log_in[username] = True
    return True

def update(bank, log_in, username, amount):
    """
    Aktualisiert den Kontostand des Benutzers.
    Gibt True zurück, wenn die Aktualisierung erfolgreich ist, sonst False.
    """
    if username not in log_in or not log_in[username]:
        return False
    if username not in bank:
        bank[username] = 0
    if bank[username] + amount < 0:
        return False
    bank[username] += amount
    return True

def transfer(bank, log_in, userA, userB, amount):
    """
    Überweist Geld von einem Konto auf ein anderes.
    Gibt True zurück, wenn die Überweisung erfolgreich ist, sonst False.
    """
    if userA not in log_in or not log_in[userA] or userB not in log_in:
        return False
    if userA not in bank or bank[userA] < amount:
        return False
    if userB not in bank:
        bank[userB] = 0
    bank[userA] -= amount
    bank[userB] += amount
    return True

def change_password(user_accounts, log_in, username, old_password, new_password):
    """
    Ändert das Passwort des Benutzers.
    Gibt True zurück, wenn die Änderung erfolgreich ist, sonst False.
    """
    if username not in user_accounts or user_accounts[username] != old_password:
        return False
    if not log_in[username]:
        return False
    if not valid(new_password) or new_password == old_password:
        return False
    user_accounts[username] = new_password
    return True

def delete_account(user_accounts, log_in, bank, username, password):
    """
    Löscht das Benutzerkonto.
    Gibt True zurück, wenn die Löschung erfolgreich ist, sonst False.
    """
    if username not in user_accounts or user_accounts[username] != password:
        return False
    if not log_in[username]:
        return False
    del user_accounts[username]
    del log_in[username]
    if username in bank:
        del bank[username]
    return True

def main():
    """
    Hauptfunktion des Online-Banking-Systems.
    """
    bank = {}
    user_accounts = {}
    log_in = {}

    print("Willkommen beim Py Bank!")
    while True:
        print("\nWählen Sie die gewünschte Option:")
        print("1. Konto erstellen")
        print("2. Auf Ihr Konto zugreifen")
        print("3. Einzahlung vornehmen")
        print("4. Konto löschen")
        print("5. Beenden")

        option = input("Ihre Wahl: ")

        if option == "1":
            username = input("Geben Sie Ihren Benutzernamen ein: ")
            password = input("Geben Sie Ihr Passwort ein: ")
            if signup(user_accounts, log_in, username, password):
                print("Konto erfolgreich erstellt!")
            else:
                print("Fehler: Benutzername bereits vergeben oder Passwort erfüllt nicht die Anforderungen.")

        elif option == "2":
            username = input("Geben Sie Ihren Benutzernamen ein: ")
            password = input("Geben Sie Ihr Passwort ein: ")
            if login(user_accounts, log_in, username, password):
                print("Anmeldung erfolgreich!")
                while True:
                    print("\nWählen Sie eine Option:")
                    print("1. Kontostand anzeigen")
                    print("2. Geld abheben")
                    print("3. Geld überweisen")
                    print("4. Geld einzahlen")
                    print("5. Konto löschen")
                    print("6. Abmelden")

                    sub_option = input("Ihre Wahl: ")

                    if sub_option == "1":
                        if username in bank:
                            print(f"Ihr Kontostand beträgt: {bank[username]} €")
                        else:
                            print("Kein Kontostand verfügbar.")

                    elif sub_option == "2":
                        amount = float(input("Geben Sie den Betrag ein, den Sie abheben möchten: "))
                        if update(bank, log_in, username, -amount):
                            print(f"{amount} € erfolgreich abgehoben.")
                        else:
                            print("Fehler: Ungültiger Betrag oder unzureichender Kontostand.")

                    elif sub_option == "3":
                        userB = input("Geben Sie den Benutzernamen des Empfängers ein: ")
                        amount = float(input("Geben Sie den Betrag ein, den Sie überweisen möchten: "))
                        if transfer(bank, log_in, username, userB, amount):
                            print(f"{amount} € erfolgreich an {userB} überwiesen.")
                        else:
                            print("Fehler: Überweisung fehlgeschlagen.")

                    elif sub_option == "4":
                        amount = float(input("Geben Sie den Betrag ein, den Sie einzahlen möchten: "))
                        if update(bank, log_in, username, amount):
                            print(f"{amount} € erfolgreich eingezahlt.")
                        else:
                            print("Fehler: Ungültiger Betrag.")

                    elif sub_option == "5":
                        password = input("Geben Sie Ihr Passwort zur Bestätigung ein: ")
                        if delete_account(user_accounts, log_in, bank, username, password):
                            print("Konto erfolgreich gelöscht.")
                            break
                        else:
                            print("Fehler: Falsches Passwort oder Benutzer nicht angemeldet.")

                    elif sub_option == "6":
                        log_in[username] = False
                        print("Sie wurden abgemeldet.")
                        break

                    else:
                        print("Ungültige Option. Bitte versuchen Sie es erneut.")

            else:
                print("Fehler: Falscher Benutzername oder Passwort.")
                print("1. Erneut versuchen")
                print("2. Passwort zurücksetzen")
                retry_option = input("Ihre Wahl: ")
                if retry_option == "1":
                    continue
                elif retry_option == "2":
                    # Hier könnte eine Passwort-Zurücksetzungsfunktion implementiert werden.
                    print("Passwort-Zurücksetzung noch nicht implementiert.")
                else:
                    print("Ungültige Option.")

        elif option == "3":
            username = input("Geben Sie Ihren Benutzernamen ein: ")
            amount = float(input("Geben Sie den Einzahlungsbetrag ein: "))
            if update(bank, log_in, username, amount):
                print(f"{amount} € erfolgreich eingezahlt.")
            else:
                print("Fehler: Ungültiger Betrag oder Benutzer nicht angemeldet.")

        elif option == "4":
            username = input("Geben Sie Ihren Benutzernamen ein: ")
            password = input("Geben Sie Ihr Passwort ein: ")
            if delete_account(user_accounts, log_in, bank, username, password):
                print("Konto erfolgreich gelöscht.")
            else:
                print("Fehler: Falsches Passwort oder Benutzer nicht angemeldet.")

        elif option == "5":
            print("Vielen Dank für die Nutzung von Py Bank. Auf Wiedersehen!")
            break

        else:
            print("Ungültige Option. Bitte versuchen Sie es erneut.")

if __name__ == '__main__':
    main()