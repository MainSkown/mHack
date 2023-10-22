import { defineStore } from 'pinia'
import { Visit } from './types'
import { POST_GET_VISITS, PUT_DELETE } from 'src/API/api'
import { Notify } from 'quasar'

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
    async DeleteQueue(queue_id: string) {
      await PUT_DELETE(queue_id).then((message) => {
        if (message === 'OK') {
          this.queues = this.queues.filter((q) => q.queue_id !== queue_id)
        } else {
          Notify.create({
            message: 'Nie udało się usunąć wizyty',
            color: 'negative',
          })
        }
      })
    },
  },

  getters: {
    getQueues(): Visit[] {
      return this.queues
    },
  },
})
