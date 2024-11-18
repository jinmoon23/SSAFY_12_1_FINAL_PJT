import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import UserSelectView from '@/views/UserSelectView.vue'
import LoadingView from '@/views/LoadingView.vue'
import ThemeListView from '@/views/ThemeListView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView,
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView,
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView,
    },
    {
      path: '/userselect',
      name: 'UserSelectView',
      component: UserSelectView,
    },
    {
      path: '/loading',
      name: 'LoadingView',
      component: LoadingView,
    },
    {
      path: '/themelist',
      name: 'ThemeListView',
      component: ThemeListView,
    }
  ],
})

export default router
