<template>
  <div id="app">
    <NavBar />
    <router-view />
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'App',
  components: {
    NavBar
  },
};
</script>

<style>
#app {
  margin-top: 0;
  min-height: 100vh;
  min-width: 100vw;
  background-color: darkgray;
  background-image: url("../public/images/background.jpg");
  background-position: center;
}
#web-page { /*Each page uses this style*/
  color: azure;
  text-align: center;
  background-color: black;
  background-image: url("../public/images/hex.png");
  background-position: bottom;
  border-radius: 25px 25px 25px 25px;
  margin: 2vh 2vw 2vh 2vw;
  padding: 1vh 0 1vh 0;
}
</style>