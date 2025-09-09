# Lashgari_Mahdi_CarPro_GmbH
# CarPro — Kundendaten- und Fahrzeugverwaltung (Projektbeschreibung)

## Lernfeld
**Lernfeld 12 — Kundenspezifische Anwendungsentwicklung**

## Thema
**Ausgangssituation**

## Schulform
IT-Berufe

---

## Ausgangssituation
Die **CarPro GmbH** möchte eine Individualsoftware zur Verwaltung ihrer Kunden und ihrer Fahrzeuge entwickeln lassen.  
Die Software soll von den Mitarbeiterinnen und Mitarbeitern der Firma genutzt werden.

---

## Funktionale Anforderungen
- Kunden und Fahrzeuge (Gebrauchtwagen) müssen **eingeben, geändert und gelöscht** werden können.  
- Zu den Kunden werden **Adressen, Telefonnummern und Mailadresse** hinterlegt.  
- Zu den Fahrzeugen gehören **Marke, Typ, Erstzulassung und Farbe**. Wünschenswert ist das Hinterlegen einiger **Ausstattungsmerkmale** (z. B. „Anhängerkupplung“, „Panoramadach“).  
- Der **Status** eines Fahrzeugs muss hinterlegt werden können: **„Verkauft“, „Reserviert“, „Verfügbar“**.  
- Es muss eine **Exportfunktion (CSV)** geben, die Kundendaten exportiert. Die Daten sollen **gefiltet** werden können (z. B. E-Mail-Adressen aller Kunden, die sich für den Newsletter angemeldet haben).  
- Es muss eine **tabellarische Übersicht der Kunden** geben. Diese Übersicht soll nach **Kundennummer, Nachnamen** und zwei weiteren Kriterien filterbar sein. Entsprechende Funktionen müssen auch für Fahrzeuge vorhanden sein.  
- Zu einem Kunden können **beliebig viele Kaufverträge** gespeichert werden. Es muss möglich sein, zu einem Kunden eine Übersicht seiner Kaufverträge mit ausgewählten Daten der gekauften Fahrzeuge zu erhalten. *(Optional)*  
- Ein **Export der Fahrzeugdaten** in ein geeignetes Format (**CSV, XML oder JSON**) ist möglich.  
- Es gibt ein **Benutzerhandbuch**.  
- Das **Datenmodell** liegt als **ER-Diagramm** vor.

---

## Nicht-funktionale Anforderungen
- Die **Benutzeroberfläche** ist ergonomisch gestaltet.  
- Alle Eingabemöglichkeiten sind gegen **Fehleingaben abgesichert** (Validierung).  
- Die **Struktur der Software** ist dokumentiert; es wurde auf gute **Wartbarkeit** geachtet.  
- Die Software ist **leicht erweiterbar**.  
- Die Software ist auf **Windows 11** lauffähig.  
- Als Programmiersprache wird **C# (mit WPF)** oder **TypeScript (mit Angular-Framework)** verwendet.  
- Die Daten sind in einer **MySQL**- oder **MariaDB**-Datenbank gespeichert.

---

## Technologie-Stack (Vorschlag)
- Frontend: **Angular (TypeScript)** oder Desktop: **C# + WPF**  
- Backend: **Python (z. B. FastAPI / Flask / Django)** oder **.NET (C#)** (je nach Wahl)  
- Datenbank: **MySQL / MariaDB**  
- Deployment: **Docker / docker-compose**, Webserver/Reverse Proxy: **NGINX**

---

## Dateien / Artefakte (zu liefern)
- `ER-Diagramm` (z. B. `docs/er-diagram.png` oder `docs/er-diagram.drawio`)  
- `Benutzerhandbuch` (z. B. `docs/user-manual.md` oder `docs/user-manual.pdf`)  
- `API-Dokumentation` (z. B. OpenAPI/Swagger: `docs/openapi.yaml`)  
- Quellcode: `frontend/` und `backend/`  
- `.gitignore`  
- `docker-compose.yml`   
- `README.md`  — enthält Vorgehensweise und Instruktionen

---

## Vorgehensweise (Vorgehensweise / Dokumentation der Arbeitsschritte)
1. **Anforderungsanalyse**
   - Use Cases und User Stories aufnehmen (z. B. Kunde anlegen, Fahrzeug reservieren, Export CSV).
   - Nicht-funktionale Anforderungen klären (Performance, Sicherheit, OS-Support).

2. **Datenmodell entwerfen**
   - ER-Diagramm erstellen (Customer, Vehicle, PurchaseContract, User/Roles).
   - Constraints, Indizes und Beziehungen definieren.

3. **API-Design**
   - REST-Routen festlegen (z. B. `/api/customers`, `/api/vehicles`, `/api/contracts`, `/api/export`).
   - Request/Response-Schemas (JSON) spezifizieren.

4. **Projektstruktur & Basis-Setup**
   - Repositorien / Ordnerstruktur anlegen (`frontend/`, `backend/`, `docs/`).
   - Linter / Formatter konfigurieren (ESLint/Prettier für Angular, Black/isort/mypy für Python).

5. **Implementierung Backend**
   - Models/ORM definieren, Migrationsskripte (alembic oder Django-Migrations).
   - CRUD-Endpoints, Filterung, Paging, Sortierung implementieren.
   - Exportfunktionen (CSV/XML/JSON).
   - Authentifizierung/Autorisierung (z. B. JWT + Rollen).

6. **Implementierung Frontend**
   - Komponenten: Listen (MatTable), Formulare (Reactive Forms), Dialoge.
   - Services für API-Kommunikation (HttpClient).
   - Validierung, Benutzerfreundliche Fehlermeldungen.
   - Filter, Sortierung, Pagination, Export-Buttons.

7. **Testing**
   - Unit-Tests Backend (pytest) و Frontend (Jasmine/Karma).
   - Integration / E2E Tests (Cypress).
   - Validierung der Exporte, Datenintegrität.

8. **Dokumentation**
   - Benutzerhandbuch (Bedienung, Anleitungen für Exporte, Installation).
   - Entwicklerdokumentation (Architektur, Setup, Deploy).
   - API-Dokumentation (Swagger/OpenAPI).

9. **Deployment**
   - Docker Compose für Lokales Testing/Deployment.
   - Reverse Proxy (NGINX) für statische Dateien و API-Proxy.
   - Healthchecks و Logging konfigurieren.

10. **Abgabe**
    - Fertige Artefakte (Code, ER-Diagramm, Benutzerhandbuch, Installationsanleitung) bündeln.

---

## Hinweise zur Abgabe
- Achte auf **saubere Repository-Struktur**, aussagekräftige Commits و `.gitignore`.  
- Stelle sicher، dass sensible Dateien (z. B. `*.env`, Datenbankdumps) **nicht** ins Repo gelangen.  
- Lege Beispiel-Daten (Fixtures) für Tests und Demo an (`docs/sample-data.sql`).

---

## Kontakt / Autoren
- Projekt: CarPro GmbH (Auftraggeber)  
- Umsetzung: [Dein Name / Team]

---

