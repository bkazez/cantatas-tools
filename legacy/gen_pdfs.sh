#!/usr/bin/env sh

# --debug to generate smaller test PDF
# source lib/assets/gen_pdfs.sh
# aws s3 presign s3://cantatas-scores/[PATH-TO-PDF] --expires-in 604800

./cleanup_scans.rb 10,50% "../scans/2022-03-17 Couperin - Sept Versets 1704"/*
./cleanup_scans.rb 10,50% "../scans/2022-03-17 Couperin - Sept Versets 1705"/*
./cleanup_scans.rb 10,50% "../scans/2022-03-18 Stucke - Cantates Livre IV"/* # done
./cleanup_scans.rb 10,50% "../scans/2022-03-18b Stuck - Cantates Livre III"/*
./cleanup_scans.rb 10,50% "../scans/2022-03-18c Nivers - Motets 1689"/*
./cleanup_scans.rb 10,50% "../scans/2022-03-18d Stuck - Cantates Livre II"/* # FAILED
./cleanup_scans.rb 10,50% "../scans/2022-03-18e Stuck - Cantates Livre I"/* # FAILED
./cleanup_scans.rb 10,50% "../scans/2022-03-18f Haendel - Cantates Vol 1"/*
./cleanup_scans.rb 10,50% "../scans/2022-03-18g Jacquet - Livre I"/* # FAILED
./cleanup_scans.rb  5,40% "../scans/2022-03-19a Purcell - Vol 30 = XXX"/*
./cleanup_scans.rb  5,40% "../scans/2022-03-19b Purcell - Vol 29 = XXIX"/*
./cleanup_scans.rb  3,40% "../scans/2022-03-19c Rameau - Vol unknown - Zaïs - extraites de la partition d'orchestre"/*
./cleanup_scans.rb  3,40% "../scans/2022-03-19d Rameau - Vol 2"/*
./cleanup_scans.rb  3,40% "../scans/2022-03-19e Rameau - Vol 1"/*
./cleanup_scans.rb  3,40% "../scans/2022-03-19e Rameau - Vol 1"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-19g Purcell - Vol 16 part 1"/*
./cleanup_scans.rb 10,20% "../scans/2022-03-19h Bruhns Kirchenkantaten Nr 1-7"/*
./cleanup_scans.rb  8,10% "../scans/2022-03-19i Purcell - Vol 18"/*
./cleanup_scans.rb  8,35% "../scans/2022-03-20h Purcell - Vol 11-2"/*
./cleanup_scans.rb  6,50% "../scans/2022-03-20i Purcell - Vol 13"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-20j Telemann - Band 5 = V"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-20k Telemann - Band 46"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-22 Telemann - Band 48"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-23 Bach Compendium Vol 3 = III"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-23b Telemann - Band 49"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-23c Telemann - Band 50"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-24a Telemann - Band 51"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-24b Telemann - Band 52"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-24c Telemann - Band 39"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-24d Telemann - Band 40"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-24e Bach Compendium Vol 4 = IV"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-25a Telemann - Band 41"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-25b Telemann - Band 42"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-26a Telemann - Band 43"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-26b Telemann - Band 44"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-27a Telemann - Band 33"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-27b Telemann - Band 45"/*
./cleanup_scans.rb  6,40% "../scans/2022-03-27c Telemann - Band 53"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-27d Boismortier - Les Quatre Saisons 1724"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-28a Telemann - Band 55"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-28b Telemann - Band 56"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-28c Telemann - Band 57"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29a Telemann - Band 59"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29b Telemann - Band 64"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29c Telemann - Band 60"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29d Telemann - Band 62"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29e Telemann - Band 63"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29f Telemann - Band 66"/*
./cleanup_scans.rb  7,40% "../scans/2022-03-29g Telemann - Band 65"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30b Clerambault - Cantates 1716"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30c Brossard - Prodromus"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30d Bourgeois - Cantates 1708"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30e Bernier - 9 lecons"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30f Bourgeois - Cantates 1718"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-30g Campra - Motets - Livre Second"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31a Clerambault - Motets"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31b Boismortier - Motests 1728"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31c Bernier - Motets - prem oeuvre"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31d Bernier - Motets 1713"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31e Lully - Motet Dies Irae"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31f Lully - Motets a deux choeurs pour la Chapelle du Roy - Full Score"/*
./cleanup_scans.rb  8,40% "../scans/2022-03-31g Lully - Motets a deux choeurs pour la Chapelle du Roy - Parts"/*
./cleanup_scans.rb  8,40% "../scans/2022-04-29 Haydn ser 22 band 1 - Stabat Mater"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-02b Haydn ser 23 band 5 - Messe Nr 12"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-02c Haydn ser 24 band 1 - Philemon und Baucis"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-02d Haydn ser 25 band 4 - Le Pescatrici"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-03a Haydn ser 25 band 5 - L'Infedelta Delusa"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-03b Haydn ser 25 band 6 part 1 L'Incontro Improvviso"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-03c Haydn ser 25 band 6 part 2 L'Incontro Improvviso"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-04b Haydn ser 25 band 10 part 2 - La Fedelta Premiata"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-04c Haydn ser 25 band 9 - L'Isola Disabitata"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-04d Haydn ser 25 band 7 - Il Mondo Della Luna"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-04e Haydn ser 25 band 8 La Vera Costanza"
./cleanup_scans.rb  8,40% "../scans/2022-05-05a Haydn ser 25 band 3 - Lo Speziale"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-05b Haydn ser 24 band 2 - Textbucher verschollener Singspiel"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-05c Haydn ser 24 band 3 - Die Feuersbrunst"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-05d Haydn ser 25 band 1 - Acide"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-07a Haydn ser 26 band 1 - Arien und Szenen mit Orchester, 1 Folge"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-07b Haydn ser 25 band 13 - L'Anima del Filosofo"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-07c Haydn ser 25 band 12 - Armida"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-07d Haydn ser 25 band 11 part 2- Orlando Paladino"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-07e Haydn ser 26 band 2 - Arien, Szenen... 2 Folge"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08a Haydn ser 28 band 1 part 1 - Il Ritorno di Tobia"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08b Haydn ser 32 band 3 - Volksliedbearbeitungen No 151-268"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08c Haydn ser 27 band 3 - Chöre..."/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08d Haydn ser 28 band 1 part 2 - Il Ritorno di Tobia"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08e Haydn ser 36 band 4 - Volksliedbearbeitungen No 269-364"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08f Haydn ser 32 band 5 - Volksliedbearbeitungen No 365-429"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08g Haydn ser 21 band 1 - Volksliedbearbeitungen No 1-100"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08h Haydn ser 30 - Mehrstimmige Gesänge"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08i Haydn ser 31 - Kanons"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08j Haydn ser 29 band 1 - Lieder"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08k Haydn ser 26 band 3 - Bearbeitungen... 2 Folge"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08l Haydn ser 29 band 2 - Verschiedene Gesänge"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08m Haydn ser 28 band 3 part 2 - Die Schöpfung"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-08n Haydn ser 32 band 2 - Volksliedbearbeitungen No 101-150"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09a Haydn ser 27 band 1 - Kantaten"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09b Haydn ser 28 band 2 - Die Sieben letzetn Worte"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09c Haydn ser 28 band 4 - Die Jahreszeiten"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09d Haydn ser 27 band 2 - Applausus"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09e Haydn ser 28 band 3 part 1 - Die Schöpfung"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09f Haydn ser 29 band 4 part 2 - Die Jahreszeiten"/*
./cleanup_scans.rb  8,40% "../scans/2022-05-09g Haydn ser 28 band 3 part 3 - Die Schöpfung - [1] Vorwort und..."/* --nosplit --rotate=90
./cleanup_scans.rb  8,40% "../scans/2022-05-09g Haydn ser 28 band 3 part 3 - Die Schöpfung - [2] Übertragungen Querformat"/* --nosplit --rotate=180
./cleanup_scans.rb  8,40% "../scans/2022-05-09g Haydn ser 28 band 3 part 3 - Die Schöpfung - [3] Übertragungen Hochformat"/* --nosplit --rotate=90
./cleanup_scans.rb  8,40% "../scans/2022-05-09g Haydn ser 28 band 3 part 3 - Die Schöpfung - [4] Abbildungen Querformat"/* --nosplit --rotate=180
./cleanup_scans.rb  8,40% "../scans/2022-05-09g Haydn ser 28 band 3 part 3 - Die Schöpfung - [5] Abbildungen Hochformat"/* --nosplit --rotate=-90
./cleanup_scans.rb  9,50% "../scans/2022-07-27 Purcell - Works vol 21 - Dramatic Music Part III pages 178 - end"/*
./cleanup_scans.rb 10,60% "../scans/2022-07-28 Haydn ser 22 band 22 - Verschiedene... 1. Folge"/*
./cleanup_scans.rb 10,45% "../scans/2022-07-29 Haydn ser 25 band 11 part 1 - Orlando Paladino"/*
./cleanup_scans.rb 10,50% "../scans/2022-07-29b Haydn ser 23 band 4 Messe Nr. 11 Schöpfungsmesse 1801"/*
./cleanup_scans.rb 10,55% "../scans/2022-07-30a Haydn ser 25 band 2 La Canterina"/*
./cleanup_scans.rb 10,55% "../scans/2022-07-30b Haydn ser 25 band 7 part 1 Il Mondo Della Luna"/*
./cleanup_scans.rb 10,55% "../scans/2022-08-01a Haydn ser 25 band 7 part 2 Il Mondo Della Luna"/*
./cleanup_scans.rb 10,55% "../scans/2022-08-01b Haydn ser 25 band 10 part 1 - La Fedelta Premiata"/*
./cleanup_scans.rb 10,65% "../scans/2022-08-01c Haydn ser 25 band 14 Libretti"/*
./cleanup_scans.rb 10,60% "../scans/2022-08-02a Haydn ser 25 band 8 La Vera Costanza ACCIDENTAL DUPLICATE? PLEASE CHECK"/*
./cleanup_scans.rb 10,60% "../scans/2022-08-02b Haydn ser 22 band 3 Verschiedene... 2. Folge"/*
./cleanup_scans.rb 10,65% "../scans/2022-08-02c Haydn ser 23 band 1b Messen Nr 3-4"/*
./cleanup_scans.rb  9,65% "../scans/2022-08-03a Haydn ser 23 band 1a Messen Nr 1-2"/*
./cleanup_scans.rb 10,65% "../scans/2022-08-03b Haydn ser 23 band 2 Messen Nr 5-8"/*
./cleanup_scans.rb 10,65% "../scans/2022-08-03c Haydn ser 23 band 3 Messen Nr 9-10"/*
./cleanup_scans.rb  9,62% "../scans/2022-08-04a Haydn ser 23 band 2 Messen 5-8 Revidierte Neuausgabe"/*
./cleanup_scans.rb 10,70% "../scans/2022-08-10 Haydn ser 26 band 4 - Bearbeitungen... 1 Folge"/*
./cleanup_scans.rb 10,70% "../scans/2022-09-18 Telemann band 3 fix"/*
./cleanup_scans.rb 10,70% "../scans/2022-09-21 Rameau - OOR IV.25 - Anacréon"/*
./cleanup_scans.rb 10,65% "../scans/2022-10-07 Rameau - OOR IV.8 - Dardanus 1744, 1760, 1763"/*
./cleanup_scans.rb 10,65% "../scans/2022-11-11 Charpentier - Hitchcock"/*
./cleanup_scans.rb 10,60% "../scans/2022-11-23 Handel - Serie 1, Band 14.1 - Israel in Egypt pp 20-117"/*
./cleanup_scans.rb 10,60% "../scans/2022-12-02a Schütz, band 2"/*
./cleanup_scans.rb 10,60% "../scans/2022-12-02b Schütz, band 3"/*
./cleanup_scans.rb 10,60% "../scans/2022-12-09 Gluck - Abteilung I, Band 2 - Telemaco"/*
./cleanup_scans.rb 10,60% "../scans/2022-12-15 Schütz, band 1 (2017)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-10a Schütz, band 4 (1956)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-10b Schütz, band 6 (1957)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-10c Schütz, band 7 (1988)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-10d Schütz, band 8 and 9 (2004)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-11a Telemann, band 3, pages 200-201"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-11b Telemann, band 55, pages 152-153"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18a Schütz, band 5 pt 1 (2003)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18b Schütz, band 5 pt 2 (2006)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18c Schütz, band 23 (1971)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18d Schütz, band 26 (1974)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18e Schütz, band 29 (2016)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18f Schütz, band 34-35 (2015)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18g Schütz, band 36 (2017)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-18h Schütz, band 37 (1970)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-28a Schütz, band 39 (1984)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-28b Gluck, Abteilung I, Band 9 - Iphigénie en Tauride (1973)"/*
./cleanup_scans.rb 10,60% "../scans/2023-01-31 Schein, band 8 (1969)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06a Schütz, band 14 (1965)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06b Schütz, band 15 (1964)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06c Schütz, band 16 (1965)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06d Schütz, band 17 (1968)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06e Schütz, band 18 (1989)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06f Schütz, band 19 (1990)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06g Schütz, band 20 (1996)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-06h Schütz, band 21 (2002)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-11a Schütz, band 22 (1962)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-11b Schütz, band 24 (1979)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-11c Schütz, band 25 (1981)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18a Schütz band 10 (1963)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18b Schütz band 12 (1963)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18c Schütz band 13 (1957)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18d Schütz band 27 (1970)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18e Schütz band 28 (1971)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18f Schütz band 31 (1970)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18g Schütz band 32 (1971)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18h Schütz band 33 (2008)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18i Schütz band 38 (1971)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18j Schütz band 40 (1988)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18k Gluck band 26 (1974)"/*
./cleanup_scans.rb 10,60% "../scans/2023-02-18l Gluck band 27 (2006)"/*

./cleanup_scans.rb 10,60% "../scans/2023-02-20 Handel - Serie I, Band 18.2 - Samson (2011)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-17 Gluck - abt I, band 3, teilb a - Alceste (1988)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-18 Gluck - abt I, band 2 - Telemaco (1972) - PERHAPS NOT NEEDED"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-19a Gluck - abt I, band 1 - Orfeo ed Euridice (1963)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-19b Gluck - abt I, band 5, teilb a - Iphigénie en Aulide (1987)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-20a Gluck - abt I, band 5, teilb b - Iphigénie en Audilide (1989)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-20b Gluck - abt I, band 6 - Orfée et Euridice (1967)"/*
./cleanup_scans.rb 10,50% "../scans/2023-03-21 Gluck - abt I, band 7 - Alceste (1957)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-09a Gluck - abt I, band 8, teilb a - Armide (1987)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-09b Gluck - abt I, band 8, teilb b - Armide (1991)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-09c Gluck - abt I, band 10 - Echo et Narcisse (1953)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-10a Gluck - abt I, band 11 - Iphigenie auf Tauris (1965)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-10b Gluck - abt II, band 1 - Don Juan, Semiramis (1961)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-10c Gluck - abt II, band 6 - Ipermestra (1997)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-11a Gluck - abt III, band 8 - Il Re Pastore (1968)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-11b Gluck - abt III, band 11 - Le nozze d'Ercole e d'Ebe (2009)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-12a Gluck - abt III, band 12 - La Semiramide riconosciuta (1994)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-12b Gluck - abt III, band 13 - La contesa dei Numi (2004)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-12c Gluck - abt III, band 14 - Ezio (1990)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-14a Gluck - abt III, band 16 - La clemenza di Tito (1995)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-14b Gluck - abt III, band 17 - Le Cinesi (1958)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-14c Gluck - abt III, band 18 - La Danza (1969)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-15a Gluck - abt III, band 19 - L'innocenza giustificata (1999)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-15b Gluck - abt III, band 20 - Antigono (2007)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-15c Gluck - abt III, band 22 - Tetide (1978)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16a Gluck - abt III, band 24 - Ezio (1992)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16b Gluck - abt III, band 23 - Il trionfo di Clelia (2008)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16c Gluck - abt III, band 25 - Il Parnaso confuso (1970)"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16d Telemann, band 3, pages 200-201 TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16e Telemann, band 55, pages 152-153 TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16f Telemann, band 55 scores pages 152-153 TO ADD - PERHAPS NOT NEEDED"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16g Purcell - Works vol 21 - Dramatic Music Part III pages 180-181 TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-16h Purcell - Works vol 19 - The Indian Queen pages 130-131 TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-21a Purcell - Works vol 9 - Dioclesian - pages 10-11 TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-21B Gluck - abt I, band 4 - Paride ed Elena (1954) several pages TO ADD"/*
./cleanup_scans.rb 10,50% "../scans/2023-04-21c Gluck - abt IV, band 5 - L'Ivrogne corrige (1951) title page TO ADD"/*
