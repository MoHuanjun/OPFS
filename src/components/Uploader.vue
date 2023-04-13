<template>
  <div>
    <input type="file" ref="fileInput" @change="handleFileUpload">
    <button @click="uploadFile">Upload</button>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      file: null,
    };
  },
  methods: {
    handleFileUpload() {
      this.file = this.$refs.fileInput.files[0];
    },
    uploadFile() {
      let formData = new FormData();
      formData.append('file', this.file);

      axios.post('/uploader', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      }).then(response => {
        console.log(response.data);
      }).catch(error => {
        console.log(error);
      });
    },
  },
};
</script>
