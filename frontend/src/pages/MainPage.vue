<template>
  <q-page>
    <div class="column items-center q-gutter-y-sm">
      <!-- Registered queues -->
      <div class="full-width column items-center">
        <h6 class="q-ma-none">Zarejestrowane wizyty</h6>
        <q-separator
          class="shadow-3"
          color="primary"
          inset
          style="width: 90%"
        />
      </div>

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
    </div>
  </q-page>
</template>

<script setup lang="ts">
import { useRouter } from 'vue-router';

const router = useRouter();

const buttons: {
  label: string;
  onClick: () => void;
  color?: string;
}[] = [
  {
    label: 'Wyszukaj wizytę',
    onClick: () => {
      router.push('/visit_search');
    },
  },
  {
    label: 'Archiwum wizyt',
    onClick: () => {
      router.push('/arhive');
    },
    color: 'grey-7',
  },
];
</script>
