import Vue from 'vue'
import VueRouter from 'vue-router'
import MovieView from '../views/MovieView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'movies',
    component: MovieView
  },
  {
    path: '/random',
    name: 'random',
    component: () => import('../views/RandomView.vue')
  },
  {
    path: '/watch-list',
    name: 'watch-list',
    component: () => import('../views/WatchListView.vue')
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
