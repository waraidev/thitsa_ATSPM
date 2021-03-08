<template>
  <div id="home">
    <div id="welcome">
      <h1 class="rounded" style="background-color: dimgray">Welcome the GDOT ATSPM Analysis Web Engine!</h1>
    </div>
    <div id="click-files">
      <h4 class="rounded">Click below or in the navigation bar to upload files and analyze them!</h4>
    </div>
    <b-button pill variant="primary" class="nav-link" to="/upload">File Uploads</b-button>
    <b-button pill variant="info" class="nav-link" to="/analysis">File Analysis</b-button>
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
#home {
  color: azure;
  text-align: center;
  background-color: black;
  background-position: bottom;
  border-radius: 25px 25px 25px 25px;
  margin: 2vh 2vw 2vh 2vw;
  padding: 5vh 0 10vh 0;
  background-image: url("../../public/images/pixel_city.png");
}
#welcome {
  margin: 0 24vw 0 24vw;
}
#welcome h1 {
  background-color: dimgray;
}
#click-files {
  margin: 2vh 28.5vw 2vh 28.5vw;
}
#click-files h4 {
  background-color: dimgray;
}
.nav-link {
  margin: 1vh 35vw 1vh 35vw;
}
.logo {
  width: 20%;
  height: auto;
  margin: 30px 20px 0px 20px;
}
</style>
