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
        <visit-expansion-item
          v-for="visit in visits"
          :visit="visit"
          v-bind:key="visit.queue_id"
          :show-register-date="false"
        >
          <q-btn
            class="q-my-sm"
            label="Zarezerwuj"
            @click="() => (showDialog = true)"
            color="positive"
            outline
            no-caps
            style="font-size: small; width: 50vw"
          />
          <q-dialog v-model="showDialog" class="app-font text-center" no-focus>
            <q-card style="width: 100vw">
              <q-card-section class="bg-primary text-white text-bold">
                <h6 class="q-ma-none">Wybierz datę rezerwacji</h6>
              </q-card-section>
              <q-card-section class="flex flex-center">
                <div class="q-mt-md" style="max-width: 300px">
                  <q-input filled v-model="visit.registration_date">
                    <template v-slot:prepend>
                      <q-icon name="event" class="cursor-pointer">
                        <q-popup-proxy
                          cover
                          transition-show="scale"
                          transition-hide="scale"
                        >
                          <q-date
                            v-model="visit.registration_date"
                            mask="YYYY-MM-DD HH:mm"
                            :options="
                              (date) =>
                                new Date(date) >= new Date(visit.visit_date)
                            "
                          >
                            <div class="row items-center justify-end">
                              <q-btn
                                v-close-popup
                                label="Close"
                                color="primary"
                                flat
                              />
                            </div>
                          </q-date>
                        </q-popup-proxy>
                      </q-icon>
                    </template>

                    <template v-slot:append>
                      <q-icon name="access_time" class="cursor-pointer">
                        <q-popup-proxy
                          cover
                          transition-show="scale"
                          transition-hide="scale"
                        >
                          <q-time
                            v-model="visit.registration_date"
                            mask="YYYY-MM-DD HH:mm"
                            format24h
                            :options="(hr) => hr >= 6 && hr < 22"
                          >
                            <div class="row items-center justify-end">
                              <q-btn
                                v-close-popup
                                label="Close"
                                color="primary"
                                flat
                              />
                            </div>
                          </q-time>
                        </q-popup-proxy>
                      </q-icon>
                    </template>
                  </q-input>
                </div>
              </q-card-section>
              <q-card-section class="flex justify-between no-wrap">
                <q-btn
                  label="Potwierdź"
                  @click="
                    () => {
                      ;(showDialog = false), Register(visit)
                    }
                  "
                  color="positive"
                  outline
                  no-caps
                  style="font-size: small; width: 30vw"
                  :disable="
                    visit.registration_date === undefined ||
                    visit.registration_date.length === 0
                  "
                />
                <q-btn
                  label="Anuluj"
                  color="negative"
                  outline
                  no-caps
                  style="font-size: small; width: 30vw"
                  v-close-popup
                />
              </q-card-section>
            </q-card>
          </q-dialog>
        </visit-expansion-item>
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
import VisitExpansionItem from 'src/components/VisitExpansionItem.vue'

const $q = useQuasar()
const router = useRouter()
const loading = ref<boolean>(false)
const showDialog = ref<boolean>(false)

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
  if (userRaport.value.specialist === '') {
    $q.notify('Pozycja specjalisty nie może być pusta')
    return
  }
  if (userRaport.value.province === '') {
    $q.notify('Województwo nie może być puste')
  }

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
  'Stomatolog',
  'Urolog',
  'Wenerolog',
]
</script>
