<template>
  <div id="app">

    <div>
      <img alt="Vue logo" src="./assets/logo.png">
      <HelloWorld msg="Learn how to upload photos with Cloudinary"/>
    </div>

    <div v-if="!$auth.loading">
        <!-- show login when not authenticated -->
        <button v-if="!$auth.isAuthenticated" @click="login">Log in</button>
        <!-- show logout when authenticated -->
        <button v-if="$auth.isAuthenticated" @click="logout">Log out</button>
    </div>

    <div>
        <button @click="openUploadModel">Add Photo</button>
    </div>
  <div>
    <cld-context cloudName="diiayntjq">
      <div style="display: flex; justify-content: center;">
        <cld-image :publicId="publicId" width="250">
          <cld-transformation width="600" height="600" gravity="face" crop="thumb" />
         </cld-image>
         
      </div>
    </cld-context>
  </div>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import { CldContext, CldImage, CldTransformation } from 'cloudinary-vue'

export default {
  name: 'App',
  components: {
    HelloWorld,
    CldContext,
    CldImage,
    CldTransformation
  },
  data() {
    return {
      url: '',
      publicId: ''
    }
  },
  methods: {
    // Log the user in
    login() {
      this.$auth.loginWithRedirect();
    },
    // Log the user out
    logout() {
      this.$auth.logout({
        returnTo: window.location.origin
      });
    },
    openUploadModel() {
      window.cloudinary.openUploadWidget(
        { cloud_name: 'diiayntjq',
          upload_preset: 'bi7uln2q'
        },
        (error, result) => {
          if (!error && result && result.event === "success") {
            console.log('Image uploaded..: ', result.info);  

            this.url = result.info.url;
            this.publicId = result.info.public_id;
          }
        }).open();
    }
  }    
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
