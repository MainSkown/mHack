<template>
  <q-page class="column items-center q-mt-md">
    <h6 class="q-ma-none">Zarchiwizowane wizyty</h6>
    <q-separator class="shadow-3 q-my-md" color="primary" style="width: 90%" />
    <div
      v-if="
        visitStore.getQueues.filter(
          (v) => new Date(v.registration_date) < new Date()
        ).length > 0
      "
      class="column items-center q-mt-sm q-gutter-y-sm"
    >
      <VisitExpansionItem
        style="width: 80%"
        v-for="visit in visitStore.getQueues.filter(
          (v) => new Date(v.registration_date) < new Date()
        )"
        v-bind:key="visit.queue_id"
        :visit="visit"
        :show-register-date="true"
      >
        <q-btn
          class="q-my-sm"
          label="Usuń"
          @click="visitStore.DeleteQueue(visit.queue_id)"
          color="negative"
          outline
          no-caps
          style="font-size: small; width: 50vw"
        />
      </VisitExpansionItem>
    </div>
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
        >Nie masz żadnych zarchiwizowanych wizyt</q-item-label
      >
    </q-item>
  </q-page>
</template>

<script setup lang="ts">
import { VisitStore } from 'src/stores/visitStore'
import VisitExpansionItem from 'src/components/VisitExpansionItem.vue'

const visitStore = VisitStore()
</script>
