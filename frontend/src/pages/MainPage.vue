<template>
  <q-page>
    <div class="column items-center q-gutter-y-sm">
      <!-- Buttons -->
      <div v-for="(btn, index) in buttons" v-bind:key="index">
        <q-btn
          :label="btn.label"
          @click="btn.onClick()"
          :color="btn.color ? btn.color : 'primary'"
          outline
          no-caps
          style="font-size: large; width: 50vw"
        />
      </div>
      <!-- Registered queues -->
      <div class="full-width column items-center">
        <q-separator
          class="shadow-3 q-my-md"
          color="primary"
          style="width: 90%"
        />
        <h6 class="q-ma-none">Zarejestrowane wizyty</h6>
        <q-list
          v-if="
            visitStore.getQueues.filter(
              (v) => new Date(v.registration_date) >= new Date()
            ).length > 0
          "
          style="width: 80%"
          class="q-gutter-y-sm"
        >
          <visit-expansion-item
            v-for="(visit, index) in visitStore.getQueues.filter(
              (v) => new Date(v.registration_date) >= new Date()
            )"
            v-bind:key="index"
            :visit="visit"
            :show-register-date="true"
          >
            <div class="flex flex-center q-gutter-x-sm">
              <p class="q-ma-none">Przed wizytą:</p>
              <q-icon name="help_outline" size="lg" color="amber-6">
                <q-popup-proxy
                  transition-show="flip-up"
                  transition-hide="flip-down"
                >
                  <q-banner class="bg-white text-black">
                    {{ beforeVisit[visit.specialist] }}
                  </q-banner>
                </q-popup-proxy></q-icon
              >
            </div>
            <q-separator style="width: 90%" />
            <q-btn
              class="q-my-sm"
              label="Zrezygnuj"
              @click="visitStore.DeleteQueue(visit.queue_id)"
              color="negative"
              outline
              no-caps
              style="font-size: small; width: 50vw"
            />
          </visit-expansion-item>
        </q-list>
        <q-item
          class="text-center q-mt-sm"
          style="
            border: 1px grey;
            border-style: solid;
            border-radius: 5px 5px 5px 5px;
          "
          v-else
        >
          <q-item-label class="flex flex-center"
            >Nie masz żadnych zarejestrowanych wizyt</q-item-label
          >
        </q-item>
      </div>
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router'
import { VisitStore } from 'src/stores/visitStore'
import VisitExpansionItem from 'src/components/VisitExpansionItem.vue'
import { beforeVisit } from 'src/stores/beforeVisit'

const visitStore = VisitStore()
const router = useRouter()

visitStore.setup()

const buttons: {
  label: string
  onClick: () => void
  color?: string
}[] = [
  {
    label: 'Wyszukaj wizytę',
    onClick: () => {
      router.push('/visit_search')
    },
  },
  {
    label: 'Archiwum wizyt',
    onClick: () => {
      router.push('/archive')
    },
    color: 'grey-7',
  },
]
</script>
