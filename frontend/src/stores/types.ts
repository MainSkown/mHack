export type Visit = {
  queue_id: string;
  place_name: string;
  location: {
    city: string;
    street: string;
    local_number: string;
    post_code: string;
  };
  visit_date: Date;
  visit_name: string;
  phone: string;
};
