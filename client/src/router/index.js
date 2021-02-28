import Vue from 'vue';
import Router from 'vue-router';
import FileUpload from '@/components/FileUpload.vue';
import Home from '@/components/Home.vue';

Vue.use(Router);

export default new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
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
  ],
});
