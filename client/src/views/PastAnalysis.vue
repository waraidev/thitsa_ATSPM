<template>
  <div id="web-page">
    <h1>Choose a past prediction analysis!</h1>
    <div id="button-list">
      <b-button
          v-for="image_name in imageList"
          :key="image_name"
          id="button"
          class="px-3"
          variant="outline-primary"
          v-b-modal.image-modal
          v-on:click="showImage(image_name)"
      >
        {{ imageName(image_name) }}
      </b-button>
    </div>
    <div id="button-output">
      <b-modal
          id="image-modal"
          :title="title"
          hide-backdrop ok-only size="xl"
          header-bg-variant="primary"
          header-text-variant="light"
          ok-title="Close"
      >
        <b-spinner variant="primary" v-if="loading" />
        <b-img :src="image" class="col-lg-12"/>
        <h3 v-if="!(error === '')">{{error}}</h3>
      </b-modal>
    </div>
  </div>
</template>

<script>
import axios from "axios";

// Change to 'http://localhost:5000/' if endpoint doesn't work.
const path = 'https://s0g8xuigid.execute-api.us-east-1.amazonaws.com/dev/';

export default {
name: "PastAnalysis",
  data() {
    return {
      imageList: [],
      image: '',
      loading: false,
      error: '',
      title: '',
    };
  },
  methods: {
    getImages() {
      axios.get(`${path}images`)
        .then((res) => {
          this.imageList = res.data;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    imageName(image_name) {
      let i = image_name.indexOf('signal') + 6;
      image_name = image_name[0].toUpperCase()
          + image_name.substring(1, i) + ' '
          + image_name.substring(i, image_name.length - 4);
      return image_name;
    },
    showImage(image_name) {
      this.error = '';
      this.loading = true;
      this.title = this.imageName(image_name);
      axios.get(`${path}images/${image_name}`)
        .then((res) => {
          this.loading = false;
          this.image = res.data;

          console.log("Image loaded.");
        }).catch((error) => {
          this.error = error;
          this.loading = false;
          console.error(error);
      });
    }
  },
  created() {
    this.getImages();
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
.modal-title {
  color: azure;
}
#button-output {
  margin: 10px 10vw 10vh 10vw;
  text-align: center;
}
</style>