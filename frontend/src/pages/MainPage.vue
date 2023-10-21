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
          inset
          style="width: 90%"
        />
        <h6 class="q-ma-none">Zarejestrowane wizyty</h6>
        <q-list v-if="visitStore.getQueues.length > 0">
          <q-item
            v-for="(visit, index) in visitStore.getQueues"
            v-bind:key="index"
            class="text-center q-mt-sm"
            style="
              border: 1px grey;
              border-style: solid;
              border-radius: 5px 5px 5px 5px;
            "
          ></q-item>
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
import { useRouter } from 'vue-router';
import { VisitStore } from 'src/stores/visitStore';

const visitStore = VisitStore();
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
