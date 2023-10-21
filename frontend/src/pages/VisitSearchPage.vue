<template>
  <q-page class="column q-gutter-y-xs items-center">
    <div class="text-center" style="min-width: 80%">
      <q-select
        v-model="userRaport.specialist"
        label="Wybierz specjalistę"
        :options="specialists"
      />
    </div>

    <div style="width: 80%">
      <q-select
        v-model="userRaport.province"
        label="Wybierz województwo"
        :options="voivodeship"
        option-label="label"
        option-value="value"
        emit-value
        map-options
      />
    </div>
    <div style="width: 80%">
      <q-expansion-item label="Dodatkowe filtry" class="full-width">
        <q-separator />
        <div class="column q-gutter-y-xs">
          <q-input v-model="userRaport.locality" label="Wpisz miasto" />
          <q-input v-model="userRaport.street" label="Ulica jednostki" />
          <q-input v-model="userRaport.place" label="Nazwa przychodzni" />
          <q-separator class="q-my-md" />
          <div class="flex no-wrap">
            <q-toggle
              v-model="userRaport.disabled"
              label="Przychodznia przyjazna niepełnosprawnym"
            />
            <q-toggle v-model="userRaport.elevator" label="Posiada windę" />
          </div>
          <q-separator class="q-my-md" />
          <q-toggle
            class="self-center"
            v-model="userRaport.forChildren"
            label="Szukaj wizyty dla dziecka"
          />
        </div>
      </q-expansion-item>
    </div>
    <q-btn
      class="q-mt-sm"
      label="Szukaj wizyt"
      @click="Search()"
      color="positive"
      outline
      no-caps
      style="font-size: medium; width: 50vw"
    />
  </q-page>
</template>

<script setup lang="ts">
import { Visit } from 'src/stores/types'
import { UserRaport } from 'src/stores/types'
import { ref } from 'vue'

const userRaport = ref<UserRaport>({
  specialist: '',
  province: '',
  elevator: false,
  forChildren: false,
  disabled: false,
})

const visits = ref<Visit[]>([])

function Search() {
  // TODO: Implement
}

const voivodeship: { label: string; value: string }[] = [
  { label: 'dolnośląskie', value: '01' },
  { label: 'kujawsko-pomorskie', value: '02' },
  { label: 'lubelskie', value: '03' },
  { label: 'lubuskie', value: '04' },
  { label: 'łódzkie', value: '05' },
  { label: 'małopolskie', value: '06' },
  { label: 'mazowieckie', value: '07' },
  { label: 'opolskie', value: '08' },
  { label: 'podkarpackie', value: '09' },
  { label: 'podlaskie', value: '10' },
  { label: 'pomorskie', value: '11' },
  { label: 'śląskie', value: '12' },
  { label: 'świętokrzyskie', value: '13' },
  { label: 'warmińsko-mazurskie', value: '14' },
  { label: 'wielkopolskie', value: '15' },
  { label: 'zachodniopomorskie', value: '16' },
]

const specialists: string[] = [
  'Chirurg',
  'Dermatolog',
  'Ginekolog',
  'Immunolog',
  'Kardiolog',
  'Nefrolog',
  'Neonatolog',
  'Neurolog',
  'Onkolog',
  'Patolog',
  'Pulmonolog',
  'Reumatolog',
  'Urolog',
  'Wenerolog',
]
</script>
