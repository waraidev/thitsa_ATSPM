<template>
  <div id="home">
    <h1>Welcome the GDOT ATSPM Analysis Web Engine!</h1>
    <p>
      Click below or in the navigation bar to upload files and analyze them!
    </p>
    <router-link class="nav-item nav-link px-3" to="/upload">File Uploads</router-link>
    <router-link class="nav-item nav-link px-3" to="/analysis">File Analysis</router-link>
    <a href="https://traffic.dot.ga.gov/atspm">
      <img src="/images/atspm_logo.png" class="rounded mx-auto d-block img-fluid">
    </a>
    <a href="https://www.mercer.edu/">
      <img src="/images/mercer_logo.png" class="rounded mx-auto d-flex img-fluid">
    </a>
    <a href="https://www.gatech.edu/">
      <img src="/images/yellow_jacket.png" class="rounded mx-auto d-flex img-fluid">
    </a>
  </div>
</template>

<script>
export default {
  name: 'Home',
  components: {
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
  width: 20%;
  height: 20%;
  margin-top: 30px;
}
</style>
