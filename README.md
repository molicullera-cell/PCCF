# PCCF. Projectes Curriculars dels Cicles Formatius

Aquest repositori conté les versions en desenvolupament dels Projectes Curriculars dels Cicles Formatius dde la familia professional d'informàtica e l'IES Jaume II El Just.

Els fonts es troben en format Markdown, com a projectes amb mkdocs, i en un full de càlcul amb les taules, i permeten la seua exportació a PDF a través de Pandoc i Weasyprint, fent ús d'una adaptació de la plantilla [craigbass76
pandoc-css-weasyprint-template](https://github.com/craigbass76/pandoc-css-weasyprint-template).

Els diferents apartats del document són els indicats a la [Guía pràctica per al Docent del Projecte Curricular del Cicle Formatiu](https://ceice.gva.es/documents/388109149/390831792/PCCF_Guia_Practica_Docent_VAL.pdf) de la GVA.

## Continguts de cada carpeta PCCF

* **Carpeta `docs`**: Contle els diferents fitxers fonts en format markdown, i la carpeta `styles` amb els estils.
* **Fitxer `mkdocs.yml`**: Fitxer de configuració d'mkdocs, on definim bàsicament el tema, els plugins i l'estructura del document. 
* **Fitxer `PCCF_DAM.ods`**: Conté les taules que s'han d'incorporar al PCCF: Percentatges de les competències al títol, contribució de cada mòdul a les competències professionals i a les personals, i la taula d'organització del mòdul.
* **Carpeta `my_plugins`**: Conté el plugin personalitzat `add_tables`, amb el qual, cada vegada que servim o generem el lloc web, incorpora el contingut de les taules dels ods als documents originals.
* **Fitxer `ods2html.xslt`**: Conté el fitxer XSLT per fer la transformació de l'XML amb el contingut del fitxer ods a HTML, i és utilitzat pel plugin.
* **Script `genera_pdf.py`**: Script en python que genera el pdf a parrtir de tota la documentació, fent ús de la plantilla *pandoc-css-weasyprint-template*.
* **Carpeta `templates`**: Conté les plantilles, la configuració, les tipografies i els estils que necessita Weasyprint per generar el PDF.

## Requisits

Per tal de treballar amb mkdocs, caldrà generar un entorn virtual Python, activar-lo i instal·lar algunes llibreries. Per a això:

1. Creem un nou entorn virtual a l'arrel del projecte

```
python3 -m venv venv
```
Això ens generarà una carpeta `venv` al directori arrel, la qual no es puja al repositori, ja que és ignorada pel `.gitignore`.

2. Activem l'entorn virtual amb:

```
. venv/bin/activate
```

3. Dins l'entorn (Veurem que ens diu (venv) davant el prompt, instal·lem `mkdocs`, la plantilla *material* i les llibreries de python `lxml` i `weasyprint`.

```
pip install mkdocs mkdocs-material lxml weasyprint
```

4. Instal·lem el plugin local `add_tables`. Per a això, ens ubiquem en la carpeta `my_plugin` de cada projecte (per exemple `cd PCCF_DAM/my_plugins`), i llancem:

```
pip install -e .
```

5. **Instal·lació de pandoc**. Per a la conversió a html/pdf fem ús de pandoc, pel que aquest ha d'estar instal·lat al sistema:

```
sudo apt install pandoc
```

Amb això ja podem accedir a la carpeta de cada projecte i generar el lloc o el pdf corresponent.

Recordeu que per desactivar l'entorn virtual de python, haurem de fer-ho amb :

```
deactivate
```

## Visualització en HTML

Per tal de servir el lloc en local, ho farem amb:

```
mkdocs serve
```

Generalment, el tindrem disponible en l'adreça: http://127.0.0.1:8000.

Per altra banda, si volem generar el lloc per publicar-lo, farem:

```
mkdocs build
```

Que ens generarà la carpeta `site` amb el lloc en HTML.


## Generació del pdf

Per tal de generar el pdf, farem ús de l'script `genera_pdf.py`. El procés per a la generació consisteix en:

* **Pas 1**. Concatena un fitxer de capçalera (`templates/front-matter.md`) i tots els fitxers font markdown, prèviament processats per incorporar les taules del fitxer ODS.
* **Pas 2**. Converteix amb pandoc el markdown generat a HTML.
* **Pas 3**. Aplica weasyprint per convertir l'HTML a PDF.

Durant el procés es generen fitxers temporals amb el Markdown i l'HTML intermedi, que són esborrats en finalitzar la conversió.

L'ús de l'script pot ser de diverses formes:


```
python3 genera_pdf.py
```

* Genera el pdf amb el contingut del projecte, amb el nom `output.pdf`.


```
python3 genera_pdf.py nom.pdf
```

* Genera el pdf amb el contingut del projecte, amb el nom indicat `nom.pdf`.

```
python3 genera_pdf.py eixida.pdf --keep-html
```

```
python3 genera_pdf.py --keep-html
```

Amb l'opció `--keep-html` indiquem que no volem que esborre el md i l'html intermedi. Pot ser útil per a tasques de depuració d'errors en la generació.

## Configuració de cada PCCF

Per tal de generar cada PCCF caldrà realitzar alguns ajustos, tant al fitxer de configuració com a les plantilles.

### Modificació de l'mkdocs.yml

Al fitxer `mkdocs.yml` haurem d'ajustar la configuració del plugin personalitzat, concretament, al plugin `add_tables` l'opció `ods_path`:

```yaml
plugins:
  - search
  - add_tables:
      ods_path: 'PCCF_DAM.ods'
      xslt_path: 'ods2html.xslt'
```

Com veiem, aci es fa referència al fitxer `PCCF_DAM.ods`. Per als altres cicles caldrà tindre un fitxer `PCCF_Cicle.ods` (**Important: Amb la mateixa extructur de pestanyes que aquest**), amb el contingut de cada cicle.

Per tal d'incorporar una taula al markdown des de l'ods, el que haurem de fer és afegir la marca `{nom_del_full}` dins el markdown, per afegir el contingut del full. Per exemple, en `docs/3.adequacio_competencies.md`, afegim la marca:

```
{taula_percentatges_competencies}
```

Això el que fa és buscar el full `taula_percentatges_competencies` al full de càlcul `PCCF_DAM.ods` i incorporar-la en HTML on es troba la marca.

### Modificacions de la plantilla 

Quan generem el pdf d'altre cicle, cal ajustar alguns paràmetres, concretament al fitxer `templates/front-matter.md`, podrem inidcar:

* El títol i subtítol del document a la portada,
* Capçalera i peus,
* ...

**Nota**: Tot i que veureu aci les imatges de fons, s'especifiquen al CSS, pel que aquests camps són ignorats.


```yaml
---
title: Projecte Curricular del Cicle Formatiu \newline Desenvolupament d'Aplicacions Multiplataforma
titlepage: true
subtitle: PCCF DAM
...
titlepage-background: "templates/img/portada.png"
page-background: "templates/img/fondo.png"
header-left: Departament d'Informàtica. Curs 2025-2026
footer-left: IES Jaume II el Just. PCCF
---
```