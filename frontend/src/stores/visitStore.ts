import { defineStore } from 'pinia';
import { Visit } from './types';

type VisitStoreState = {
  queues: Visit[];
};

export const VisitStore = defineStore('VisitStore', {
  state: (): VisitStoreState => ({
    queues: [],
  }),

  actions: {
    setup() {
      // TODO: Implement axios getter
    },
  },

  getters: {
    getQueues(): Visit[] {
      return this.queues;
    },
  },
});
