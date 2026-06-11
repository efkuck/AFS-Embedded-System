# Richtlinien für Beiträge (Contributing Guidelines)

Wir freuen uns über Beiträge zu diesem Open-Source-Projekt! Da es sich um ein eingebettetes System handelt, beachten Sie bitte folgende Schritte:

1. **Fork** das Repository.
2. Erstellen Sie einen neuen **Branch** für Ihre Funktion (`git checkout -b feature/NeueFunktion`).
3. **Commit** Ihrer Änderungen (`git commit -m 'Neue Sensor-Logik hinzugefügt'`).
4. **Push** auf den Branch (`git push origin feature/NeueFunktion`).
5. Öffnen Sie einen **Pull Request**.

### Wichtige Hinweise:
* Bitte stellen Sie sicher, dass neue Code-Blöcke die harte Deadline (WCET) der Hauptschleife nicht überschreiten.
* Wenn Sie neue GPIO-Pins verwenden, dokumentieren Sie diese bitte in der README.
