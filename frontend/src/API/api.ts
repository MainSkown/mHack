import axios from 'axios'
import { LocalStorage } from 'quasar'
import { UserRaport, Visit } from 'src/stores/types'

const port = 5000
const url = `http://localhost:${port}/`

// POST /search
export async function POST_QUEUES(
  userRaport: UserRaport
): Promise<Visit[] | '504' | '500'> {
  let result: Visit[] = []

  await axios({
    method: 'POST',
    url: url + 'search',
    data: JSON.stringify(userRaport),
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
  })
    .then((response) => {
      result = response.data as Visit[]
      console.log('result', result)
    })
    .catch((error) => {
      console.log(error)
      if (error.status === 504) return '504'
      else return '500'
    })
  return result
}

// POST /user/register
export async function POST_VISIT(userVisit: Visit): Promise<'OK' | '500'> {
  let result: 'OK' | '500' = '500'
  await axios({
    method: 'POST',
    url: url + 'user/register',
    data: JSON.stringify({
      user_id: localStorage.getItem('user_token'),
      ...userVisit,
    }),
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
  })
    .then((response) => {
      if (response.status >= 200 && response.status < 300) result = 'OK'
      else result = '500'
    })
    .catch(() => {
      result = '500'
    })

  return result
}

// POST /user/registered
export async function POST_GET_VISITS(): Promise<Visit[] | '500'> {
  let result: Visit[] | '500' = []
  await axios({
    method: 'POST',
    url: url + 'user/registered',
    data: JSON.stringify({ user_id: LocalStorage.getItem('user_token') }),
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
  })
    .then((response) => {
      result = response.data.queues
    })
    .catch(() => {
      result = '500'
    })

  return result
}

// PUT /user/delete
export async function PUT_DELETE(queue_id: string): Promise<'OK' | '500'> {
  let result: 'OK' | '500' = '500'
  await axios({
    method: 'PUT',
    url: url + 'user/delete',
    data: JSON.stringify({
      user_id: LocalStorage.getItem('user_token'),
      queue_id: queue_id,
    }),
    headers: { Accept: 'application/json', 'Content-Type': 'application/json' },
  })
    .then((response) => {
      if (response.status >= 200 && response.status < 300) result = 'OK'
      else result = '500'
    })
    .catch(() => {
      result = '500'
    })

  return result
}
