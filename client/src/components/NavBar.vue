<template>
  <div id="nav">
    <b-navbar toggleable="lg" type="dark">
      <b-navbar-brand href="/">GDOT ATSPM Analysis</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/upload">File Upload</b-nav-item>
          <b-nav-item href="/analysis">Analysis</b-nav-item>
          <b-nav-item href="/past-analysis">Past Analysis</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  name: 'NavBar',
};
</script>

<style scoped>
#nav {
  background-image: url("../../public/images/ML.jpg");
}
</style>
