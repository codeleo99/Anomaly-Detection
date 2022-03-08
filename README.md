# Anomaly Detection
Dieses Projekt beschäftigt sich mit der Entwicklung einer Analyseanwendung zur Erkennung von Anomalien in der Speicherauslastung.
## Funktion
- Datenabfrage über die Elasticseach API
- Datenfilterung
- Datenbereinigung
- Analyse durch BIRCH-Algorithmus
- Visuelle Darstellung

## Beispielausgabe
![Beispielausgabe](https://user-images.githubusercontent.com/79086895/157311434-aa95ffcf-44ba-4be4-b2b7-52cef4d1e925.png)
## Installation
**Getestet auf Python 3.7.8**

Die zur Ausführung benötigten Module können über folgendes Kommando installiert werden.

```pip install -r requirements.txt```

## Ausführung
```python -m birchAnalysis.py```

## esData
Dieses Modul greift unter Verwendung des [Elasticseach Python Client](https://www.elastic.co/guide/en/elasticsearch/client/python-api/current/index.html) auf die im ELK-Stack hinterlegten Daten zu. Die für den API-Call nötige Nutzlast wird in Form einer JSON-Query aufgestellt. Die ursprüngliche Query wurde durch Inspektion eines Elastic-Dashboards erzeugt. ![Inspektion-Button](https://user-images.githubusercontent.com/79086895/157314060-88cac56b-661d-467a-a55b-e554e1c9d8cf.png)
![Requests](https://user-images.githubusercontent.com/79086895/157314527-33d8f6e3-8051-483f-af8b-505d333aa077.png)
![Teil der JSON-Query](https://user-images.githubusercontent.com/79086895/157314337-cdcf07bd-8630-4a50-8bcd-7d883750b1bf.png)

## birchAnalysis
Dieses Modul verwendet den [Birch-Clustering Algorithmus](https://scikit-learn.org/stable/modules/clustering.html#birch) zur Erkennung von Anomalien innerhalb der virtuellen Umgebung. Die Ausgabe wird regelmäßig nach 15 Sekunden aktualisiert.
### Keine Anomalie
![Keine Anomalie](https://user-images.githubusercontent.com/79086895/157316249-31a6da94-9940-4d82-bb31-d65791bcf644.png)
### Anomalie durch einmalige Störung
![Anomalie durch einmalige Störung](https://user-images.githubusercontent.com/79086895/157316834-c38c1879-6856-41cc-a53d-5c7bbb6252be.png)
### Anomalie durch "Auto"-Modus der UnknownApp
![Anomalie durch "Auto"-Modus der UnknownApp](https://user-images.githubusercontent.com/79086895/157319432-987408d7-74d6-44b3-9013-c679e77004f4.png)


