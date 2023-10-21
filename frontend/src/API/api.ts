import axios from 'axios'
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
      ...userVisit,
      user_id: localStorage.getItem('user_token'),
    }),
  })
    .then((response) => {
      if (response.status === 200) result = 'OK'
      else result = '500'
    })
    .catch(() => {
      result = '500'
    })

  return result
}

// POST /user/registered
export async function POST_GET_VISITS() {
  await axios({})
}
