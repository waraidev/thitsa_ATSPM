<template>
    <div id="analysis">
      <h1>Choose a file to analyze below!</h1>
      <div id="button-list">
        <div id="button" v-for="file in fileList" :key="file">
          <b-button class="px-3" variant="info">
            {{ file }}
          </b-button>
        </div>
      </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'Analysis',
    data() {
        return {
            fileList: [],
        };
    },
    methods: {
        getFiles() {
            const path = 'http://localhost:5000/files';
            axios.get(path)
                .then((res) => {
                    this.fileList = res.data;
                })
                .catch((error) => {
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
</style>