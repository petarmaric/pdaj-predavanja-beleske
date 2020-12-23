=============
Predavanja 07
=============


Uvod u vizuelizaciju sekvencijalno/paralelno sračunatih podataka
================================================================

- diskusija o različim Python rešenjima za vizuelizaciju podataka:

  - ``PIL``, tj. ``Pillow``
  - ``seaborn``
  - ``matplotlib``

Use case: Matrica ko-faktora i njihovih prostih brojeva
-------------------------------------------------------

- mali POC rešenja za vizuelizaciju podataka sračunatih na prethodnim predavanjima


Alternativni pristupi u paralelizaciji proračuna
================================================

- ``concurrent.futures`` biblioteka, tj. futures/promises execution pattern

  - prednosti i mane u odnosu na ``multiprocessing.Pool.imap`` i ``multiprocessing.Pool.imap_unordered``


Paralelizacija proračuna u praksi, na primeru realnih R&D projekata
===================================================================

- uradite code-review tvojih probranih OSS projekata koji koriste ``multiprocessing`` i/ili ``concurrent.futures``
- nauči studente kako radi pravi production-ready paralelizovani sistem i prokomentarišite na šta sve treba obratiti pažnju
- detaljna analiza https://github.com/petarmaric/fsm_eigenvalue/ OSS projekta kao primera različitih pristupa optimizacije vremena izvršavanja proračuna
