# Dokumentacja Projektu

## Pomysł

### Głowne założenie projektu

Projekt ma służyć obywatelom, pomagając im znaleźć specjalistę, zarejestrować wizytę, oraz dostać opowiednie informacje, by mogli się odpowiednio przygotować.

### Cele szczegółowe

- Zaimplementowanie wyszukiwarki najbliższych terminów w okolicy, odpowiednio dla:

  - Specjalista
  - **?** Choroba
  - Lokalizacja
  - **?** Opinie ~ baza danych

- Utworzyć kategorie możliwych badań / wizyt zależnych od specjalisty.

  - Wysyłanie odpowiedniej informacji jak pacjent powinien się przygotować do badania / wizyty.

- Rejestrowanie się pacjenta, wyświetlanie wizyty

- **?** Podłączyć możliwość używania skierowań do lekarzy

- **?** Email - Przypomnienie o wizycie

- **?** Powiadomienia o szybszym terminie

## API

### GET /search

#### Request:

```js
specialist: string;
?province: int;
?forChildren: boolean;
?provider: string;
?place: string
?street: string
?locality: string
?disabled: boolean
?elevator: boolean
```

### Response:

```js
queue_id: string;
place_name: string;
location: {
  city: string;
  street: string;
  local_number: string;
  post_code: string;
}
visit_date: Date;
visit_name: string;
phone: string;
```

### POST /register

#### Request:

```js
user_id: string;
queue_id: string;
```

#### Response:

OK

### GET /benefits

#### Response:

```js
benefits: string[]
```

### GET /user/registered

#### Request:

```js
user_id: string;
```

#### Response:

```js
queues: {
  queue_id: string;
  location: {
    place_name: string;
    city: string;
    street: string;
  }
  visit_date: Date;
  visit_name: string;
  phone: string;
}
[];
```
