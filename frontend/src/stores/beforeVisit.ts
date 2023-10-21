export const beforeVisit: Record<string, string> = {
  Chirurg: `Przygotuj kopie dokumentów medycznych, takie jak wyniki badań i zdjęcia.
Przyjdź na wizytę punktualnie, z listą pytań i swoją historią zdrowia.

Omów swoje obawy, opcje leczenia i, jeśli to konieczne, planowane operacje.

Zapytaj o instrukcje przedoperacyjne, jeśli zabieg jest planowany.

Staraj się zapamiętywać lub notować ważne informacje od chirurga.

Jeśli jesteś niepewny, zawsze można rozważyć drugą opinię od innego specjalisty.`,
  Dermatolog: `Przygotuj kopie dokumentacji medycznej dotyczącej skóry.
Sporządź listę pytań i obaw.
Opowiedz o swojej historii skórnej i obecnych problemach.
Przyjdź na wizytę z odsłoniętą skórą lub w luźnych ubraniach.
Zapytaj o zalecenia dotyczące pielęgnacji skóry.
Współpracuj z dermatologiem i przestrzegaj jego zaleceń.`,
  Ginekolog: `Przyjdź na wizytę w dniu cyklu, kiedy nie ma miesiączki, chyba że masz specjalne potrzeby.
Przygotuj pytania lub obawy, które chciałabyś omówić.
Zadbaj o higienę intymną przed wizytą.
Współpracuj z lekarzem i przekaż mu wszelkie istotne informacje dotyczące zdrowia intymnego.
Stosuj się do zaleceń lekarza w zakresie badań profilaktycznych i opieki nad zdrowiem intymnym`,
  Immunolog: `Przygotuj dokumentację medyczną dotyczącą układu odpornościowego.
Przyjdź na wizytę z listą pytań lub obaw dotyczących swojego układu odpornościowego.
Opowiedz o swojej historii zdrowia, w tym o problemach związanych z odpornością.
Stosuj się do zaleceń lekarza w zakresie badań immunologicznych i opieki nad układem odpornościowym.`,
  Kardiolog: `Przygotuj wyniki badań krwi, EKG lub innych badań kardiologicznych, jeśli masz.
Sporządź listę pytań lub obaw dotyczących zdrowia serca.
Przedstaw swoją historię zdrowia, w tym czynniki ryzyka sercowego i wcześniejsze schorzenia serca.
Staraj się ściśle przestrzegać zaleceń lekarza dotyczących diety, aktywności fizycznej i leków.
Regularnie kontroluj swoje parametry sercowe i zdrowie serca zgodnie z zaleceniami kardiologa.`,
  Nefrolog: `Przygotuj wyniki badań krwi i moczu, jeśli masz.
Przygotuj listę pytań lub obaw dotyczących zdrowia nerek.
Przedstaw swoją historię zdrowia, w tym choroby nerek, schorzenia układu moczowego i ewentualne schorzenia współistniejące.
Stosuj się do zaleceń lekarza dotyczących diety, nawodnienia i leków.
Regularnie monitoruj swoje wyniki badań nerek i przestrzegaj zaleceń nefrologa w celu utrzymania zdrowia nerek.`,
  Neonatolog: `Przygotuj się na udzielenie lekarzowi dokładnych informacji dotyczących przebiegu ciąży, okoliczności porodu oraz wszelkich obserwacji dotyczących zdrowia noworodka.

Jeśli istnieją jakiekolwiek pytania lub obawy związane z opieką nad noworodkiem, zapisz je, aby upewnić się, że zostaną omówione podczas wizyty.

Bądź gotowy do dyskusji na temat opieki pielęgniarskiej nad noworodkiem, diety, ewentualnych badań i zaleceń medycznych, jeśli takie są potrzebne.

Współpracuj z neonatologiem i pielęgniarkami, aby zapewnić najlepszą opiekę i monitorowanie zdrowia noworodka.

Rozważ uczestnictwo w zajęciach edukacyjnych lub programach wsparcia dla rodziców noworodków, które mogą pomóc Ci lepiej zrozumieć potrzeby i opiekę nad swoim dzieckiem.`,
  Neurolog: `Przygotuj wyniki badań neurologicznych i listę pytań.
Przedstaw swoją historię zdrowia i objawy neurologiczne.
Bądź gotowy do badań neurologicznych, jeśli będą konieczne.
Przekaż informacje o lekach i innych schorzeniach.
Współpracuj z neurologiem i przestrzegaj jego zaleceń.`,
  Onkolog: `Przygotuj kopie wyników badań onkologicznych, tomografii, biopsji, czy innych badań związanych z nowotworem.
Przygotuj listę pytań lub obaw dotyczących leczenia i diagnozy.
Podziel się historią choroby, włączając informacje o diagnozie, etapie nowotworu i dotychczasowym leczeniu.
Współpracuj z lekarzem w zakresie planu leczenia i bądź gotów na dalsze badania i terapie.
Regularnie uczestnicz w kontrolach i przestrzegaj zaleceń onkologa w celu monitorowania i leczenia nowotworu.`,
  Patolog: `Przygotuj wyniki badań histopatologicznych, cytologicznych lub biopsji, które chcesz omówić.
Przygotuj listę pytań lub obaw dotyczących wyników badań i diagnozy.
Podziel się informacją na temat kontekstu klinicznego, który skierował Cię na badanie tkanek lub komórek.
Bądź gotów na wyjaśnienia dotyczące wyników i diagnozy ze strony patologa.
Współpracuj z lekarzem w zakresie dalszej opieki medycznej na podstawie wyników patologicznych.`,
  Pulmonolog: `Przygotuj wyniki badań spirometrycznych lub innych badań płucnych, jeśli masz.
Przygotuj listę pytań lub obaw dotyczących problemów oddechowych.
Podziel się historią zdrowia dotyczącą dolegliwości oddechowych, alergii, palenia tytoniu itp.
Współpracuj z lekarzem w zakresie diagnozy, leczenia i monitorowania problemów płucnych.
Przestrzegaj zaleceń dotyczących leczenia i zaplanowanych badań kontrolnych.`,
  Reumatolog: `Przygotuj wyniki badań laboratoryjnych lub obrazowych, jeśli masz.
Sporządź listę pytań lub obaw dotyczących problemów reumatycznych.
Przedstaw swoją historię zdrowia, włączając objawy bólu, obrzęku, sztywności i innych problemów.
Bądź gotów na badania dodatkowe i konsultacje w celu postawienia dokładnej diagnozy.
Przestrzegaj zaleceń lekarza w zakresie leczenia i dbaj o regularne badania kontrolne.`,
  Stomatolog: `Przygotuj informacje dotyczące ostatniej wizyty u stomatologa oraz danych dotyczących swojego stanu zdrowia ogólnego.
Podziel się z lekarzem informacją na temat objawów lub problemów stomatologicznych, takich jak ból zęba, krwawienie dziąseł itp.
Bądź gotów na badanie jamy ustnej, włączając w to przegląd zębów i dziąseł.
Rozważ plany leczenia lub procedury stomatologiczne, jeśli są zalecane przez stomatologa.
Przestrzegaj zaleceń stomatologa w zakresie higieny jamy ustnej i regularnych wizyt kontrolnych u dentysty.`,
  Urolog: `Przygotuj wyniki badań laboratoryjnych, jeśli masz.
Sporządź listę pytań lub obaw dotyczących problemów układu moczowego.
Podziel się swoją historią zdrowia, włączając objawy, takie jak trudności z oddawaniem moczu czy ból nerek.
Bądź gotów na badania fizyczne i ewentualnie badania dodatkowe.
Współpracuj z lekarzem w zakresie diagnozy i leczenia problemów z układem moczowym oraz przestrzegaj zaleceń dotyczących opieki zdrowotnej.`,
  Wenerolog: `Przygotuj informacje dotyczące swojej historii seksualnej, włączając w to dotychczasowe partnerstwa i wszelkie objawy lub problemy zdrowotne.
Bądź gotów na otwartą i szczegółową rozmowę z lekarzem na temat swojego stanu zdrowia seksualnego i wszelkich obaw.
Badania i testy: Wenerolog może zlecić badania i testy, aby ocenić stan zdrowia seksualnego i zdiagnozować ewentualne infekcje przenoszone drogą płciową.
Przestrzegaj zaleceń lekarza w zakresie leczenia i profilaktyki chorób przenoszonych drogą płciową oraz zaleceń dotyczących bezpiecznych praktyk seksualnych.`,
}
