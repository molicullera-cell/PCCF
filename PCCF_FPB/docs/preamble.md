---
title: "[Programació d'Aula IMX  \\newline FPB Informàtica d'Oficina]"
subtitle: "FPB Informàtica i Comunicacions \\newline \\today"
author: "JB Talens"
titlepage: true
titlepage-rule-height: 0
titlepage-text-color: "F08A2A"
titlepage-background: "docs/img/portada-aula.png"
geometry: "left=2cm,right=2cm,top=3cm,bottom=3cm"
toc: true
toc-own-page: true
toc-title: "Índex"
numbersections: true
toc-depth: 3
lang: ca
listings: true

page-background: "docs/img/fondo.png"
header-left: \includegraphics[scale=0.5]{docs/img/logos/logoJust.png} \textcolor{morat}{| Programació d'Aula IMX}
header-right: \includegraphics[scale=0.5]{docs/img/logos/GvaNext.png}
footer-left:   \includegraphics[scale=0.3]{docs/img/logos/FonsVal.png}
footer-center: \thepage/\pageref{LastPage}
footer-right:  \includegraphics[scale=0.3]{docs/img/logos/miniPla.png}

bibliography: "bibliografia.bib"
csl: "apa.csl"
biblatexoptions: [language=spanish,backend=biber]

header-includes:
  - \usepackage{fontspec}
  - \usepackage{titling}
  - \usepackage{lastpage}
  - \usepackage{longtable}
  - \usepackage{booktabs}
  - \usepackage{xcolor,colortbl}
  - \usepackage{geometry}
  - \geometry{head=28pt}
  - \usepackage{csquotes}
  - \DeclareQuoteStyle{catalan}
  - \usepackage{xltxtra}
  - \usepackage{listings}
  - \usepackage{awesomebox, tcolorbox, xcolor}
  - "\definecolor{morat}{rgb}{0.396, 0.188, 0.592}"
  - "\definecolor{groc}{rgb}{0.984, 0.612, 0.031}"
  - "\definecolor{lightblue}{rgb}{0.68, 0.85, 0.9}"
  - "\definecolor{ballblue}{rgb}{0.13, 0.67, 0.8}"
  - "\definecolor{cerulean}{rgb}{0.0, 0.48, 0.65}"
  - "\definecolor{almond}{rgb}{0.94, 0.87, 0.8}"
  - "\definecolor{apricot}{rgb}{0.98, 0.81, 0.69}"
  - "\definecolor{cream}{rgb}{1.0, 0.99, 0.82}"
  - "\definecolor{coralred}{rgb}{1.0, 0.25, 0.25}"
  - "\definecolor{headerblue}{RGB}{26,72,110}"
  - "\definecolor{headergreen}{RGB}{3,75,33}"
  - "\definecolor{headerpurple}{RGB}{102,58,143}"
  - "\definecolor{rowgray}{RGB}{240,240,240}"
  - "\definecolor{bordergray}{RGB}{200,200,200}"
  - "\definecolor{cellgreen}{RGB}{226,239,218}"
  - "\definecolor{cellblue}{RGB}{198,217,241}"
  - \usepackage{sectsty}
  - "\sectionfont{\color{morat}}"
  - "\subsectionfont{\color{morat}}"
  - "\subsubsectionfont{\color{morat}}"
  - "\renewcommand{\arraystretch}{1.3}"
  - "\setlength{\arrayrulewidth}{1pt}"
  - "\arrayrulecolor{bordergray}"
  - "\setlength{\tabcolsep}{8pt}"
  - "\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}"
  - "\newcolumntype{C}[1]{>{\centering\arraybackslash}p{#1}}"
  - "\newcolumntype{R}[1]{>{\raggedleft\arraybackslash}p{#1}}"
  - "\AtBeginEnvironment{longtable}{\rowcolors{2}{rowgray}{white}}"
  - "\AtBeginEnvironment{tabular}{\rowcolors{2}{rowgray}{white}}"
  - "\newcommand{\tableheaderstyle}{\rowcolor{headerblue}\color{white}\bfseries}"
  - "\newcommand{\sectionheaderstyle}{\rowcolor{headergreen}\color{white}\bfseries}"
  - "\newcommand{\contentheaderstyle}{\rowcolor{headerpurple}\color{white}\bfseries}"
  - "\newcommand{\saberfer}{\cellcolor{cellgreen}}"
  - "\newcommand{\saberestar}{\cellcolor{cellblue}}"
---

# Introducció. Justificació i contextualització
