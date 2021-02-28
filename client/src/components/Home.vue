<template>
  <div id="home">
    <NavBar />
    <h1>Welcome the GDOT ATSPM Analysis Web Engine!</h1>
    <p>
      Click below or in the navigation bar to upload files and analyze them!
    </p>
    <router-link class="nav-item nav-link px-3" to="/upload">File Uploads</router-link>
    <router-link class="nav-item nav-link px-3" to="/analysis">File Analysis</router-link>
    <img src="/images/atspm_logo.png" class="rounded mx-auto d-block img-fluid">
  </div>
</template>

<script>
import NavBar from '@/components/NavBar.vue';

export default {
  name: 'Home',
  components: {
    NavBar,
  },
};
</script>

<style scoped>
h1 {
  margin: 15px 0px 10px 0px;
  text-align: center;
}
p {
  text-align: center;
  padding-top: 20px;
}
.nav-link {
  text-align: center;
}
.img-fluid {
  width: 80%;
  height: 80%;
  margin-top: 30px;
}
</style>
