import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from "@/views/Home.vue"
import FileUpload from "@/views/FileUpload.vue"
import Analysis from "@/views/Analysis";
import PastAnalysis from "@/views/PastAnalysis";

Vue.use(VueRouter)

const routes = [
    {
      path: '/upload',
      name: 'FileUpload',
      component: FileUpload,
    },
    {
      path: '/analysis',
      name: 'Analysis',
      component: Analysis,
    },
    {
      path: '/past-analysis',
      name: 'PastAnalysis',
      component: PastAnalysis,
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
