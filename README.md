# TrainingMate 
TrainingMate je web aplikacija namijenjena evidentiranju vježbi i obroka uz razne funkcionalnosti koje korisnicima omogućuju lakše praćanje informacija vezanih uz vježbe i obroke. 
## Funkcionalnosti
### Osnovne funkcionalnosti
1. Create exercise
2. Read exercise
3. Update exercise
4. Delete exercise
5. Create meal
6. Read meal
7. Update meal
8. Delete meal
### Dodatne funkcionalnosti
1. Calculate exercise duration
2. Calculate exercise calories
3. Calculate meal calories
4. Sort meals by calories
5. Sort exercises by duration
6. Calculate caloric balance
7. Show graph with exercise calories
8. Show graph with meal calories
9. Show graph with exercises and their intensities
10. Show graph with meals and their categories

----
## Struktura
Web aplikacija sastoji se dva povezana servisa, od kojih jedan omogućuje evidentiranje vježbi, a drugi evidentiranje obroka.
Omogućeno je dodavanje, pregledavanje, izmjenjivanje te brisanje vježbi i obroka, praćanje unosa, potrošnje kalorija, sortiranje vježbi i obroka te vizualiziranje pojedinih podataka pomoću grafova. 

----
## Pokretanje
- Preuzeti sve datoteke s Githuba i spremiti ih u mapu
- Putem naredbenog retka pozicionirati se u mapu iz prethodnog koraka
- Pomoću naredbe: _docker build -t trainingmate ._ izraditi docker image
- Pomoću naredbe: _docker run -p 5000:8080 trainingmate_ pokrenuti konteiner pomoću stvorenog image-a
- Otvoriti preglednik: _localhost:5000_
