import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from "@/components/Home.vue"
import FileUpload from "@/components/FileUpload";

Vue.use(VueRouter)

const routes = [
    {
      path: '/upload',
      name: 'FileUpload',
      component: FileUpload,
    },
    {
      path: '/analysis',
      name: 'FileUpload',
      component: FileUpload,
    },
    {
      path: '/',
      name: 'Home',
      component: Home,
    },
  ]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes: routes,
})

export default router
