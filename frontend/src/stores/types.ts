export type Visit = {
  queue_id: string
  place_name: string
  location: {
    city: string
    street: string
    aprt_num: string
    post_code: string
  }
  visit_date: Date
  visit_name: string
  phone: string
}

export type UserRaport = {
  specialist: string
  province: string
  forChildren?: boolean
  provider?: string
  place?: string
  street?: string
  locality?: string
  disabled?: boolean
  elevator?: boolean
}
