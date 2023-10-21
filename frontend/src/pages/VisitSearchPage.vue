<template>
  <q-page class="q-my-md column q-gutter-y-xs items-center">
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
          <q-input v-model="userRaport.place" label="Nazwa przychodni" />
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
      label="Szukaj wizyty"
      @click="Search()"
      color="positive"
      outline
      no-caps
      style="font-size: medium; width: 50vw"
      :disable="loading"
    />
    <q-spinner class="q-mt-md" color="primary" size="3em" v-if="loading" />
    <!--Show visit cards-->
    <div v-if="visits.length > 0" style="width: 80%">
      <q-separator class="q-mt-sm q-mb-md" color="primary" />
      <q-list class="q-gutter-y-xs">
        <q-expansion-item
          class="bordered"
          v-for="visit in visits"
          v-bind:key="visit.queue_id"
        >
          <!-- Label -->
          <template v-slot:header>
            <q-item class="column text-center">
              <q-item-label class="text-bold">{{
                visit.place_name
              }}</q-item-label>
              <q-separator />
              <q-item-section>{{ visit.visit_name }} </q-item-section>
            </q-item>
          </template>
          <q-separator />
          <div class="column items-center text-center">
            <p class="q-mt-xs q-mb-none">
              {{ visit.location.city }}
            </p>
            <p class="q-mb-xs">
              {{ visit.location.street }}
            </p>
            <q-separator style="width: 90%" />
            <p class="q-my-xs">Numer telefonu: {{ visit.phone }}</p>
            <q-separator style="width: 90%" />
            <p class="q-my-xs">
              Wizyta wolna od:
              {{ new Date(visit.visit_date).toLocaleDateString('pl') }}
            </p>
            <q-separator style="width: 90%" />
            <q-btn
              class="q-my-sm"
              label="Zarezerwuj"
              @click="Register(visit)"
              color="positive"
              outline
              no-caps
              style="font-size: small; width: 50vw"
            />
          </div>
        </q-expansion-item>
      </q-list>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { Visit } from 'src/stores/types'
import { UserRaport } from 'src/stores/types'
import { ref } from 'vue'
import { POST_QUEUES, POST_VISIT } from 'src/API/api'
import { useQuasar } from 'quasar'
import { useRouter } from 'vue-router'

const $q = useQuasar()
const router = useRouter()
const loading = ref<boolean>(false)

const userRaport = ref<UserRaport>({
  specialist: '',
  province: '',
  place: '',
  street: '',
  elevator: false,
  forChildren: false,
  disabled: false,
  provider: '',
  locality: '',
})

const visits = ref<Visit[]>([])

async function Search() {
  visits.value = []
  loading.value = true
  await POST_QUEUES(userRaport.value).then((result) => {
    console.log(result)

    if (result === '500') {
      $q.notify({
        message:
          'Wystąpił błąd po stronie serwera. Proszę spróbować jeszcze raz.',
        color: 'negative',
      })
    } else if (result === '504' || result.length === 0) {
      $q.notify({
        message:
          'Wystąpił błąd podczas próby wyszukania wizyt. Proszę spróbować ponownie później.',
        color: 'negative',
      })
    } else {
      visits.value = result
    }
  })
  loading.value = false
}

async function Register(userVisit: Visit) {
  await POST_VISIT(userVisit).then((message) => {
    switch (message) {
      case 'OK':
        router.push('/')
        $q.notify({
          message: 'Pomyślnie zarezerwowano wizytę',
          color: 'positive',
        })
        break
      case '500':
        $q.notify({
          message:
            'Wystąpił problem po stronie serwera. Proszę spróbować jeszcze raz',
          color: 'negative',
        })
        break
    }
  })
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
