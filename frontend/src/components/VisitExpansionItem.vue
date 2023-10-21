<template>
  <q-expansion-item class="bordered">
    <!-- Label -->
    <template v-slot:header>
      <q-item class="column text-center">
        <q-item-label class="text-bold">{{ visit.place_name }}</q-item-label>
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
      <slot> </slot>
    </div>
  </q-expansion-item>
</template>

<script setup lang="ts">
import { Visit } from '../stores/types'
defineProps<{
  visit: Visit
}>()
</script>
