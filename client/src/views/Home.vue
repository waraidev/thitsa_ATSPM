<template>
  <div id="home">
    <h1>Welcome the GDOT ATSPM Analysis Web Engine!</h1>
    <p>
      Click below or in the navigation bar to upload files and analyze them!
    </p>
    <router-link class="nav-item nav-link px-3" to="/upload">File Uploads</router-link>
    <router-link class="nav-item nav-link px-3" to="/analysis">File Analysis</router-link>
    <div style="text-align: center;">
      <a href="https://www.mercer.edu/">
        <b-img fluid class="logo" src="/images/mercer_logo.png" />
      </a>
      <a href="https://traffic.dot.ga.gov/atspm">
        <b-img fluid class="logo" src="/images/atspm_logo.png" />
      </a>
      <a href="https://www.gatech.edu/">
        <b-img fluid class="logo" src="/images/yellow_jacket.png" />
      </a>
    </div>

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
.logo {
  width: 20%;
  height: auto;
  margin: 30px 20px 0px 20px;
}
</style>
