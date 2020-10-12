import Vue from 'vue'
import VueRouter from 'vue-router'
import MainPage from '@/views/MainPage.vue'
import CategoryPage from '@/views/CategoryPage.vue'
import PictogramPage from '@/views/PictogramPage.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'MainPage',
    component: MainPage
  },
  {
    path: '/category/:categoryId/pictogram/:iconId',
    name: 'PictogramPage',
    component: PictogramPage
  },
  {
    path: '/category/:id',
    name: 'CategoryPage',
    component: CategoryPage
  }
]

const router = new VueRouter({
  routes
})

export default router
