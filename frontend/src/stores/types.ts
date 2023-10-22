export type Visit = {
  queue_id: string
  place_name: string
  location: {
    city: string
    street: string
  }
  visit_date: string
  registration_date: string
  visit_name: string
  phone: string
  specialist: string
}

export type UserRaport = {
  specialist: string
  province: string
  forChildren: boolean
  provider: string
  place: string
  street: string
  locality: string
  disabled: boolean
  elevator: boolean
  search_radius: number
}
