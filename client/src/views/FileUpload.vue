<template>
  <div class="file-upload">
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
        <h3 class="dropzone-custom-title">Drag and drop to upload ATSPM CSV file!</h3>
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
import axios from 'axios';

const API_URL = 'http://localhost:5000/';

export default {
  name: 'FileUpload',
  components: {
    dropzone: vue2Dropzone,
  },
  methods: {
    onUploadComplete(file) {
      console.log(`Uploaded ${file.name}`);
    },
    onFileRemove(file) {
      axios({
        url: `${API_URL}files/${file['name']}`,
        method: 'DELETE',
        data: {
          delete_file: file['name'],
        },
      })
      .then(res => {console.log(res)})
      .catch((error) => {
        console.error(error);
      });
      // axios.delete(`${API_URL}files`)
      //   .catch((error) => {
      //     console.error(error);
      //   });
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
}

#myDropzone >>> .dz-message {
  font-weight: 700;
  color: #acacac;
}
#myDropzone >>> .fa-cloud-upload {
  margin-right: 10px;
}
.myDropzone {
  position: relative;
  margin: 20px 10px 10px 10px;
  height: 300px;
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
  color: #00b782;
}
.subtitle {
  color: #314b5f;
}
.instructions {
  margin-top: 20px;
  text-align: center;
}
</style>
