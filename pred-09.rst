=============
Predavanja 09
=============


Uvod u distribuirane proračune
==============================

Distribuirani proračuni u praksi, na primeru realnih R&D projekata [nastavak]
-----------------------------------------------------------------------------

- uradite code-review tvojih probranih OSS projekata koji koriste ``celery``
- nauči studente kako radi pravi production-ready distribuirani sistem i prokomentarišite na šta sve treba obratiti pažnju
- detaljna analiza https://github.com/petarmaric/export_beam_integrals/ OSS projekta kao primera distribuiranog sistema

Uvod u Celery
-------------

- upoznavanje sa Celery framework
- prednosti i mane
- grupisanje više nezavisnih Celery task-ova u ogromne distribuirane (i graf orijentisane) workflow-ove

Celery workflow, tj. taskovi višeg reda
---------------------------------------

- ``group``: distribuirana ``for``-petlja
- ``chain``: uvezivanje više taskova, tako da se distribuirano izvršavaju jedan za drugim
- ``chord``: ``group`` + "reduktor" task (nad rezultatima cele te grupe)

Use case: Matrica ko-faktora i njihovih prostih brojeva
-------------------------------------------------------

- prepravka naših postojećih rešenja ovog problema u distribuirano rešenje
