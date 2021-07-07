<template>
  <div id="web-page">
    <dropzone
      ref="myDropzone"
      id="myDropzone"
      class="myDropzone"
      @vdropzone-success="onUploadComplete"
      @vdropzone-removed-file="onFileRemove"
      :options="dropzoneOptions"
      :useCustomSlot="true"
    >
      <div class="dropzone-custom-content">
        <h3 class="dropzone-custom-title">Drag and drop to upload an ATSPM CSV file!</h3>
        <div class="subtitle">...or click to select a file from your computer</div>
      </div>
    </dropzone>
    <h3 class="instructions">
      Click <a href="/analysis">here</a> to analyze your files!
    </h3>
  </div>
</template>

<script>
// import axios from 'axios';
import vue2Dropzone from 'vue2-dropzone';
import 'vue2-dropzone/dist/vue2Dropzone.min.css';

// Change to 'http://localhost:5000/' if endpoint doesn't work.
const API_URL = 'https://s0g8xuigid.execute-api.us-east-1.amazonaws.com/dev/';

export default {
  name: 'FileUpload',
  components: {
    dropzone: vue2Dropzone,
  },
  methods: {
    onUploadComplete(file) {
      console.log(`Uploaded ${file.name}`);
    },
    async onFileRemove(file) {
      let output = await this.$http.delete(
          `${API_URL}files/${file['name']}`,
      ).then(() => {
        console.log(output);
      }).catch((error) => {
        console.error(error);
      });
    },
  },
  data() {
    return {
      // dropzone settings
      dropzoneOptions: {
        url: `${API_URL}files`,
        addRemoveLinks: true,
        thumbnailWidth: 250,
        maxFilesize: 25,
        maxFiles: 4,
        acceptedFiles: ".csv", //This allows only CSV files
        dictDefaultMessage: "<i class='fa fa-cloud-upload'></i>UPLOAD ME",
      },
    };
  },
};
</script>

<style scoped>
.file-upload {
  margin: 0px 10px 0px 10px;
  color: azure;
}

#myDropzone >>> .dz-message {
  font-weight: 700;
  color: #ec7424;
}
#myDropzone >>> .fa-cloud-upload {
  margin-right: 10px;
}
.myDropzone {
  position: relative;
  margin: 20px 10px 10px 10px;
  height: 300px;
  background-color: dimgray;
}
.myDropzone:hover {
  background-color: slategray;
}
.dropzone-custom-content {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  text-align: center;
}
.dropzone-custom-title {
  margin-top: 0;
  color: #ec7424; /*Secondary in bootstrap*/
}
.subtitle {
  color: azure;
}
.instructions {
  margin-top: 20px;
  text-align: center;
}
</style>
