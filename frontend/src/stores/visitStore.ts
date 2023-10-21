import { defineStore } from 'pinia'
import { Visit } from './types'
import { POST_GET_VISITS } from 'src/API/api'

type VisitStoreState = {
  queues: Visit[]
}

export const VisitStore = defineStore('VisitStore', {
  state: (): VisitStoreState => ({
    queues: [],
  }),

  actions: {
    async setup() {
      const res = await POST_GET_VISITS()
      if (res !== '500') {
        this.queues = res
      }
    },
  },

  getters: {
    getQueues(): Visit[] {
      return this.queues
    },
  },
})
