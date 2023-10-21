import { RouteRecordRaw } from 'vue-router'
import MainLayout from 'src/layouts/MainLayout.vue'
import MainPage from 'src/pages/MainPage.vue'
import VisitSearchPage from 'src/pages/VisitSearchPage.vue'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: MainLayout,
    children: [
      { path: '', component: MainPage },
      { path: '/visit_search', component: VisitSearchPage },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
