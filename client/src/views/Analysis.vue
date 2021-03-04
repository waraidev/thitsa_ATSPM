<template>
    <div id="analysis">
      <h1>Choose a file to analyze below!</h1>
      <div id="button-list">
        <b-button v-for="file in fileList" :key="file"
            id="button" class="px-3" variant="info" v-on:click="showChart(file)">
          {{ file }}
        </b-button>
      </div>
      <div id="chart">
        <h3 class="chart-item">{{completion_time}}</h3>
        <b-spinner class="chart-item" variant="info" v-if="loading" />
        <b-img fluid :src="image" />
        <h3>{{error}}</h3>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

const path = 'http://localhost:5000/'

export default {
  name: 'Analysis',
  data() {
    return {
      fileList: [],
      image: '',
      loading: false,
      error: '',
      completion_time: ''
    };
  },
  methods: {
    getFiles() {
      axios.get(`${path}files`)
        .then((res) => {
          this.fileList = res.data;
        })
        .catch((error) => {
            console.error(error);
        });
    },
    showChart(filename) {
      this.loading = true;
      let start = performance.now();
      axios.get(`${path}plot/${filename}`)
        .then((res) => {
          this.loading = false;
          this.image = res.data;

          let end = performance.now();
          let calc_time = ((end - start) * 0.001).toPrecision(5);
          this.completion_time = `It took ${calc_time} seconds to complete SIMPLS!`;

          console.log("SIMPLS Finished!")
        }).catch((error) => {
          this.error = error;
          console.error(error);
      });
    },
  },
  created() {
    this.getFiles();
  },
    
}
</script>

<style scoped>
h1 {
  margin: 15px 0px 10px 0px;
  text-align: center;
}
#button-list {
  text-align: center;
  margin-top: 30px;
}
#button {
  margin: 10px;
}
.px-3 {
  padding: 10px;
}
#chart {
  margin-top: 30px;
  text-align: center;
}
</style>